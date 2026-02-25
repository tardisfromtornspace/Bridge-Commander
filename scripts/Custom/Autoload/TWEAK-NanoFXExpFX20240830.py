# VERSION 1.2.2
# 25th February 2026

import App
import string
import traceback

from bcdebug import debug

TRUE = 1
FALSE = 0

G_PATCHFIX = 3 # 0 Means we only apply the tweak, 1 that we also apply some extra fixes, 2 that we only apply a new death sequence alongside the tweak, 3 that we apply all the fixes and tweaks
versionPatch = 20260222 # Our version of the patch
# If disabled, replace TRUE with FALSE
bEnabled = FALSE

def ASequenceDummy(pAction):
	return 0

try:
	from Custom.NanoFXv2.ExplosionFX import ExpFX
	import Custom.NanoFXv2.ExplosionFX.ExpSfx
	import Custom.NanoFXv2.NanoFX_ScriptActions
	import Custom.NanoFXv2.NanoFX_Lib
	import Custom.NanoFXv2.NanoFX_Config
	import Multiplayer.MissionShared

	if not ExpFX:
		print "you don't have NanoFXv2 installed"
		bEnabled = FALSE
	else:
		if not hasattr(ExpFX, "version") or ExpFX.version < versionPatch:
			bEnabled = TRUE
except:
	print "NanoFX v2 beta is not installed, or an error happened:"
	bEnabled = FALSE
	traceback.print_exc()

if bEnabled:
	print "Tweaking NanoFX v2 explosions (version ", versionPatch, ")"
	#ExpFX.version = versionPatch

	oldCreateNanoWeaponExpSeq = ExpFX.CreateNanoWeaponExpSeq
	oldCreateNanoExpNovaSeq = ExpFX.CreateNanoExpNovaSeq
	oldCreateNanoExpLargeSeq = ExpFX.CreateNanoExpLargeSeq
	oldCreateNanoExpSmallSeq = ExpFX.CreateNanoExpSmallSeq
	oldNanoCollisionEffect = ExpFX.NanoCollisionEffect
	oldNanoDeathSeq = ExpFX.NanoDeathSeq

	####################################################################
	####################################################################
	# AUXILIAR STUFF:

	import Foundation
	import FoundationTech
	import FoundationTriggers
	import MissionLib

	g_Threshold = 0.9
	g_minThreshold = 0.87
	g_minShield = 1900

	def ShouldDoDebris(pShip, doShields=0.9, minThreshold = 0.87, fDmg=1000):
		debug(__name__ + ", ShouldDoDebris")
		shouldDo = 0
		try:
			if pShip:
				hullIgnore = 0
				if hasattr(pShip, "GetScript"):
					pShipModule = __import__(pShip.GetScript())
					if pShipModule != None and hasattr(pShipModule, "GetShipStats"):
						mDmgRadMod = 1.0
						mDmgStrMod = 1.0						
						try:
							kStats=pShipModule.GetShipStats()
							iskStatsD = (type(kStats) == type({}))
							if iskStatsD and (kStats.has_key('DamageRadMod')):
								mDmgRadMod=kStats['DamageRadMod']
							elif hasattr(pShipModule, "GetDamageRadMod"):
								mDmgRadMod=pShipModule.GetDamageRadMod()

							if iskStatsD and (kStats.has_key('DamageStrMod')):
								mDmgStrMod=kStats['DamageStrMod']
							elif hasattr(pShipModule, "GetDamageStrMod"):
								mDmgStrMod=pShipModule.GetDamageStrMod()
						except:
							mDmgRadMod = 1.0
							mDmgStrMod = 1.0
							traceback.print_exc()

						if mDmgRadMod == 0.0 or mDmgStrMod == 0.0:
							shouldDo = 0
						else:
							shouldDo = 1

				if shouldDo and doShields != 2 and hasattr(pShip, "GetShields"):
					pShd = pShip.GetShields()
					if pShd and pShd.IsOn() and not pShd.IsDisabled():
						breachedShields = 0
						for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
							fCurr = pShd.GetCurShields(shieldDir)
							fMax = pShd.GetMaxShields(shieldDir)
							if fMax < fDmg or (fMax > 0.0 and fCurr/fMax < minThreshold):
								breachedShields = breachedShields + 1
								break
						if not breachedShields and pShd.GetShieldPercentage() >= doShields:
							shouldDo = 0
		except:
			shouldDo = 0
			traceback.print_exc()

		return shouldDo

	def SafeShipFunc(function, checkDeadDying, iShipID, defaultReturn, *args, **kwargs): # TO-DO It is meant to wrap around the actions
		try:
			debug(__name__ + ", SafeShipFunc")
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				shouldPass = TRUE
				if checkDeadDying != None and checkDeadDying > 0:
					if pShip.IsDead():
						shouldPass = FALSE
					elif checkDeadDying > 1 and pShip.IsDying():
						shouldPass = FALSE
				if shouldPass:
					print "TO-DO function on SafeShipFunc is ", function, " *args are ", args, " **kwargs are ", kwargs
					return apply(function, args, kwargs)
		except:
			traceback.print_exc()
		return defaultReturn

	####################################################################
	####################################################################
	# A DOUBLE TEST, IF THIS WORKS, MAKE IT WORK BETTER:
	# It doesn't...
	"""
	from Custom.NanoFXv2.SpecialFX import PlasmaFX
	oldCreatePlasmaFX = PlasmaFX.CreatePlasmaFX
	def newCreatePlasmaFX(pShip, pEvent):
		debug(__name__ + ", newCreatePlasmaFX")
		pSequence = App.TGSequence_Create()
		pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5)
		if not pShip:
			return pSequence

		iShipID = pShip.GetObjID()
		return SafeShipFunc(oldCreatePlasmaFX, 2, iShipID, pSequence, pShip, pEvent)

	# ENABLE PATCH TO APPLY
	if G_PATCHFIX == 1 or G_PATCHFIX > 2:
		PlasmaFX.CreatePlasmaFX = newCreatePlasmaFX

	from Custom.QBautostart.TPSDATA import BCSTNGPlasmaFXoverride
	oldBCSTNGPlasmaFXoverride = BCSTNGPlasmaFXoverride.BCSTNGPlasmaFXoverride
	def newBCSTNGPlasmaFXoverride(pShip, pEvent):
		debug(__name__ + ", newBCSTNGPlasmaFXoverride")
		pSequence = App.TGSequence_Create()
		pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5)
		if not pShip:
			return pSequence

		iShipID = pShip.GetObjID()
		return SafeShipFunc(oldBCSTNGPlasmaFXoverride, 2, iShipID, pSequence, pShip, pEvent)

	# ENABLE PATCH TO APPLY
	if G_PATCHFIX == 1 or G_PATCHFIX > 2:
		BCSTNGPlasmaFXoverride.BCSTNGPlasmaFXoverride = newBCSTNGPlasmaFXoverride

	from Custom.NanoFXv2 import NanoFX_Lib
	oldCreateSpecialFXSeq = NanoFX_Lib.CreateSpecialFXSeq
	def NewCreateSpecialFXSeq(pShipA, pEvent, sFXType, bPlay = 0):
		debug(__name__ + ", NewCreateSpecialFXSeq")
		shouldPass = FALSE
		pSpecialFX = None
		checkDeadDying = 1 # TO-DO 2 or 1?
		pShip = None
		iShipID = pShipA.GetObjID()
		if (iShipID is not None) and iShipID != App.NULL_ID:
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if pShip:
			shouldPass = TRUE
			if checkDeadDying != None and checkDeadDying > 0:
				if pShip.IsDead():
						shouldPass = FALSE
				elif checkDeadDying > 1 and pShip.IsDying():
						shouldPass = FALSE
			if shouldPass:
				debug(__name__ + ", NewCreateSpecialFXSeq (actually doing it)")
				pSpecialFX = None
				if (sFXType == "PhalantiumFX"):
					try:
						import Custom.NanoFXv2.SpecialFX.PhalantiumFX
						pSpecialFX = Custom.NanoFXv2.SpecialFX.PhalantiumFX.CreatePhalantiumFX(pShip, pEvent)
					except:
						pSpecialFX = None
						traceback.print_exc()
	
				if (sFXType == "PlasmaFX"):
					try:
						import Custom.NanoFXv2.SpecialFX.PlasmaFX
						pSpecialFX = Custom.NanoFXv2.SpecialFX.PlasmaFX.CreatePlasmaFX(pShip, pEvent)
					except:
						pSpecialFX = None
						traceback.print_exc()
	
				if (sFXType == "Spatial"):
					try:
						import Custom.NanoFXv2.SpecialFX.SpatialFX
						pSpecialFX = Custom.NanoFXv2.SpecialFX.SpatialFX.CreateSpatialFX(pShip, pEvent)
					except:
						pSpecialFX = None
						traceback.print_exc()

				if (sFXType == "AtmosphereFX"):
					try:
						import Custom.NanoFXv2.SpecialFX.AtmosphereFX
						pSpecialFX = Custom.NanoFXv2.SpecialFX.SpatialFX.CreateAtmosphereFX(pSet, sName, sPlacement, fSize)
					except:
						pSpecialFX = None
						traceback.print_exc()

				noneSpecial = (pSpecialFX is not None)
				if noneSpecial:
					pSpecialFX = App.TGScriptAction_Create(__name__, "ASequenceDummy")
				if (bPlay == 1):
					pSequence = App.TGSequence_Create()
					pSequence.AddAction(pSpecialFX)
					pSequence.Play()
				else:
					return pSpecialFX

		if not shouldPass:
			pSpecialFX = App.TGScriptAction_Create(__name__, "ASequenceDummy")
			if (bPlay == 1):
				pSequence = App.TGSequence_Create()
				pSequence.AddAction(pSpecialFX)
				pSequence.Play()
			else:
				return pSpecialFX

		return pSpecialFX

	# ENABLE PATCH TO APPLY
	if G_PATCHFIX == 1 or G_PATCHFIX > 2:
		NanoFX_Lib.CreateSpecialFXSeq = NewCreateSpecialFXSeq

	DELETE_OBJECT_FROM_SET_MSG = 211
	def NewDeleteObjectFromSet(pSet, pShip):
		debug(__name__ + ", DeleteObjectFromSet")
		if not MissionLib.GetShip(pShip.GetName(), None, bAnySet = 1):
			return

		pSet.DeleteObjectFromSet(pShip.GetName())
		#pSet.RemoveObjectFromSet(pShip.GetName())
	
		if not App.g_kUtopiaModule.IsMultiplayer():
			return

		pNetwork = App.g_kUtopiaModule.GetNetwork()
	
	        # Now send a message to everybody else that the score was updated.
	        # allocate the message.
	        pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
	               
	        # Setup the stream.
	        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
	        kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
	        # Write relevant data to the stream.
	        # First write message type.
	        kStream.WriteChar(chr(DELETE_OBJECT_FROM_SET_MSG))
                                        
	        kStream.WriteInt(pShip.GetObjID())

	        # Okay, now set the data from the buffer stream to the message
	        pMessage.SetDataFromStream(kStream)

	        if not App.IsNull(pNetwork):
	                if App.g_kUtopiaModule.IsHost():
	                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
	                else:
	                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
	        # We're done.  Close the buffer.
	        kStream.CloseBuffer()

	# ENABLE PATCH TO APPLY
	if G_PATCHFIX == 1 or G_PATCHFIX > 2:
		ExpFX.DeleteObjectFromSet = NewDeleteObjectFromSet

	# leave no derelict for small ships
	def NewDoPostExplosionStuff(pAction, iShipID):	
		pShip = App.ShipClass_GetObjectByID(None, iShipID)
	
		if pShip:
			if pShip.GetRadius() < 0.5 and pShip.GetContainingSet():
				ExpFX.DeleteObjectFromSet(pShip.GetContainingSet(), pShip)
				pShip.SetDeleteMe(1)
		return 0

	# ENABLE PATCH TO APPLY
	if G_PATCHFIX == 1 or G_PATCHFIX > 2:
		ExpFX.DoPostExplosionStuff = NewDoPostExplosionStuff
	"""
	####################################################################
	####################################################################


	class NewNanoTimerDef(FoundationTech.TimerDef):
		def __init__(self, name, eventKey, tInterval, tDuration, dict, function, iShipID, *args, **kwargs):
			debug(__name__ + ", __init__")
			if eventKey != None:
				self.eventKey = eventKey
			else:
				self.eventKey = App.UtopiaModule_GetNextEventType()
			self.count = 0 # If set to -1 it will ignore the first event that happens

			self.idTimer = None
			self.tInterval = tInterval
			self.StartDelay = 0

			if dict != None and type(dict) == type({}):
				if dict.has_key("countStart"):
					self.count = dict["countStart"]
				else:
					self.count = 0

				if dict.has_key("countStart"):
					self.count = dict["countStart"]
				else:
					self.count = 0
				if dict.has_key("itsanEffect") and dict["itsanEffect"] == 1:
					self.itsanEffect = 1
				else:
					self.itsanEffect = 0

				if dict.has_key("defaultTimerDefBehaviour") and dict["defaultTimerDefBehaviour"] == 0:
					self.tInterval = tInterval
					self.StartDelay = 0
					self.tDuration = tDuration
					self.OneWonder = 0
				else:
					self.StartDelay = tInterval
					self.tInterval = 0
					self.tDuration = 0
					self.OneWonder = 1

				if dict.has_key("checkDead"):
					self.checkDead = dict["checkDead"]
				else:
					self.checkDead = 0

			key = name + str(eventKey)
			FoundationTriggers.__dict__[name + str(eventKey)] = self
			Foundation.MutatorElementDef.__init__(self, name, dict)
			# The line below because apparently the lines above did not cover dict on the level we want
			#self.__dict__.update(dict)
			self.function = function
			self.iShipID = iShipID
			self.myarguments = args
			self.numArguments = 0
			if args != None:
				 self.numArguments = len(self.myarguments)

			#self.mykeywordargs = kwargs #Theoretically, this should be the actual keyword argument values - in reality, for some reason, when it comes to call, that is not the case and they get on self.myarguments[1] as if they were introduced on a new tuple
			self.mykeywordargs = {}
			self.numKWArguments = 0
			for key in kwargs.keys():
				self.mykeywordargs[key] = kwargs[key]
				self.numKWArguments = self.numKWArguments + 1
			#print "function when __init__ is ", self.function, " *args are ", self.myarguments, " **kwargs are ", self.mykeywordargs
			#print "__init__ function ", self.function, " time ", App.g_kUtopiaModule.GetGameTime(), "next interval should be ", (App.g_kUtopiaModule.GetGameTime() + self.tInterval)

		def Start(self):
			#print 'Start:  self.__dict__', self.__dict__

			debug(__name__ + ", Start")
			if self.count == 0:
				#print 'Making a timer', self.__dict__

				sFunc = 'FoundationTriggers.' + self.name + str(self.eventKey)
				pTimer = MissionLib.CreateTimer(self.eventKey, sFunc, (App.g_kUtopiaModule.GetGameTime() + self.StartDelay), self.tInterval, self.tDuration)
				self.idTimer = pTimer.GetObjID()

			#print 'Start:  self.__dict__', self.__dict__

			self.count = self.count + 1

		def __call__(self, pObject, pEvent):
			debug(__name__ + ", __call__")
			if self.function != None:
				#print "__call__ function ", self.function, " time ", App.g_kUtopiaModule.GetGameTime(), "previus interval should have been ", (App.g_kUtopiaModule.GetGameTime() - self.tInterval)
				pShip = App.ShipClass_GetObjectByID(None, self.iShipID)
				if pShip:
					shouldPass = TRUE
					if self.checkDead != None and self.checkDead > 0:
						if pShip.IsDead():
							shouldPass = FALSE
						elif self.checkDead > 1 and pShip.IsDying():
							shouldPass = FALSE
					if shouldPass:
						if self.numArguments <= 0 and self.numKWArguments <= 0:
							try:
								myStuff = self.function()
							except:
								traceback.print_exc()
								myStuff = None
						else:
							myargs = None
							myargslen = len(self.myarguments)
							mykwargs = None
							funct = self.function
							if self.numKWArguments > 0 and not self.mykeywordargs and myargslen > 1: # For some reason, when switching from the init to call, self.myarguments sometimes transforms into a tuple of tuples and will now hold what self.mykeywordargs had, on the last position; while self.mykeywordargs just turns into an empty dictionary
								myargslen = len(self.myarguments[0])
								myargs = self.myarguments[0]
								mykwargs = self.myarguments[-1]
							else:
								myargs = self.myarguments
								mykwargs = self.mykeywordargs

							if type(mykwargs) != type({}):
								mykwargs = None
								mykwargs = {}

							#if myargs == None or len(myargs) <= 0:
							#	myargs = ()					
							try:
								myStuff = apply(self.function, myargs, mykwargs)
							except:
								print "ERROR on function when __call__ is ", self.function, " *args are ", self.myarguments, " **kwargs are ", self.mykeywordargs
								traceback.print_exc()
								myStuff = None
						try:
							if myStuff and self.itsanEffect:
								myStuff.Play()
						except:
							print "ERROR on function when calling Play for __call__ is ", self.function, " *args are ", self.myarguments, " **kwargs are ", self.mykeywordargs
							traceback.print_exc()
							myStuff = None
			if self.OneWonder == 1:
				self.Stop(1)
			return 0


	####################################################################
	####################################################################
	# TWEAK FOR: CreateNanoWeaponExpSeq
	def NewCreateNanoWeaponExpSeq(pEvent, sType):
		debug(__name__ + ", NewCreateNanoWeaponExpSeq")
		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoWeaponExpSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = App.TGSequence_Create()
		### Setup ###
		pShip = App.ShipClass_Cast(pEvent.GetTargetObject())
		if not pShip or not hasattr(pShip, "GetObjID"):
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 1.0)
			#pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if (not pShip) or pShip.IsDead() or pShip.IsDying():
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 1.0)
			#pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		# little Defiant fix:
		if pShip.GetRadius() < 0.1: # or else with small objects the game will crash without any warning
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 1.0)
			#pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		myHull = pShip.GetHull()
		if not myHull or myHull.GetCondition() < 100: # or else with small objects the game will crash without any warning
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 1.0)
			#pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence		

		pSet = pShip.GetContainingSet()
		if not pSet:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 1.0)
			#pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		### Create Nano's Small Explosion Sound ###
		if sType == "TorpShieldHit":
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpShieldSfx")
			if pSound:
				actionsAdded = actionsAdded + 1
				pSequence.AddAction(pSound)
		else:
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpSmallSfx")
			if pSound:
				actionsAdded = actionsAdded + 1
				pSequence.AddAction(pSound)
		###
			
		pAttachTo = pShip.GetNode()
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
		vEmitPos = pEvent.GetObjectHitPoint()
		vEmitDir = pEvent.GetObjectHitNormal()
		fSize  = pEvent.GetDamage() * (App.g_kSystemWrapper.GetRandomNumber(10) + 30) * 0.000035
		if fSize  > 9000000: # Something to prevent possible hyper-Damage crashes - it would be rare, but it could happen!
			fSize = 9000000
			
		# MLeo Flying debris Edit 2
		vSpeed = pShip.GetVelocityTG()
		vEmitDir.x = vSpeed.GetX() * vEmitDir.x
		vEmitDir.y = vSpeed.GetY() * vEmitDir.y
		vEmitDir.z = vSpeed.GetZ() * vEmitDir.z


		### TO-DO A TEST BELOW - doesn't seem to do the trick, but it might help ###
		if App.g_kLODModelManager.AreGlowMapsEnabled() == 1 and App.g_kLODModelManager.GetDropLODLevel() == 0:
			App.g_kLODModelManager.SetGlowMapsEnabled(0)
			App.g_kLODModelManager.SetGlowMapsEnabled(1)
		
		### TO-DO A TEST ABOVE ###
		shouldDoVisibleDmgStuff = 0
		if not (pShip.IsDead() or pShip.IsDying()):
			shouldDoVisibleDmgStuff = ShouldDoDebris(pShip, g_Threshold, g_minThreshold, g_minShield)

		if sType == "TorpShieldHit":
			# 0.13 is the stock photon torpedo damage radius
			auxRad = 1.0
			if pEvent.GetRadius() <= 0.0001: # Small-enough projectiles are not meant to deal knockback
				auxRad = pEvent.GetRadius() / 0.13
				fSize = (fSize / 2.0) * auxRad
				if fSize <= 0.1:
					if actionsAdded <= 0:
						pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 1.0)
						#pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
					return pSequence

				if fSize <= 1.0:
					fSize = 1.0
			elif pEvent.GetRadius() > 1.0:
				auxRad = 1.0
			else:
				fSize = (fSize / 2.0)

			if fSize < 0.00025:
				fSize = 0.00025

			pAttachTo = pSet.GetEffectRoot()

		if sType == "PhaserHullHit":
			fSize = fSize * 2.0
		###
		if sType == "TorpHullHit":
			knockback = pEvent.GetDamage()
				
			auxRad = 1.0
			if pEvent.GetRadius() <= 0.0001: # Small-enough projectiles are not meant to deal that much knockback
				auxRad = pEvent.GetRadius() / 0.13
				knockback = knockback * auxRad
				fSize = fSize * auxRad
				if fSize <= 1.0:
					fSize = 1.0

			if knockback <= 0.1:
				knockback = 0.1

			if (pEvent.GetDamage() >= 500 and sType == "TorpHullHit") and pAttachTo != None and vEmitPos != None and vEmitDir != None and pEmitFrom != None:
				if shouldDoVisibleDmgStuff:
					pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
					if pSparks:
						pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.4)
						actionsAdded = actionsAdded + 1
					pDebris = ExpFX.CreateNanoDebrisSeq(fSize * 1.25, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
					if pDebris:
						pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.4)
						actionsAdded = actionsAdded + 1
					if (App.g_kSystemWrapper.GetRandomNumber(100) < 25):
						pSparks = ExpFX.CreateDamageSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
						if pSparks:
							pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.4)
							actionsAdded = actionsAdded + 1

				pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpMedSfx")
				if pSound:
					pSequence.AddAction(pSound, App.TGAction_CreateNull(), 0.4)
					actionsAdded = actionsAdded + 1
	
			### Add Rotational Spin to Ship From Torp Explosion 25% Chance##
			if shouldDoVisibleDmgStuff and (App.g_kSystemWrapper.GetRandomNumber(100) < 25) and not (pShip.IsDead() or pShip.IsDying()):
				if (pEvent.GetDamage() >= 200):
					if (Custom.NanoFXv2.NanoFX_Config.eFX_RotationFX == "On") and (auxRad >= 1.0):
						anAction = Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq(pShip, knockback)
						if anAction:
							pSequence.AddAction(anAction, App.TGAction_CreateNull(), 0.4)
							actionsAdded = actionsAdded + 1
					if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
						anotherAction = Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 1.5)
						if anotherAction:
							pSequence.AddAction(anotherAction, App.TGAction_CreateNull(), 0.4)
							actionsAdded = actionsAdded + 1
				else:
					###
					if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
						if (App.g_kSystemWrapper.GetRandomNumber(100) < 10):
							anotherOtherAction = Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 0.6)
							if anotherOtherAction:
								pSequence.AddAction(anotherOtherAction)
								actionsAdded = actionsAdded + 1
					###
			if (Custom.NanoFXv2.NanoFX_Config.sFX_PlasmaFX == "On") and not (pShip.IsDead() or pShip.IsDying()):
				pPlasma = Custom.NanoFXv2.NanoFX_Lib.CreateSpecialFXSeq(pShip, pEvent, "PlasmaFX")
				if pPlasma != None:
					pSequence.AddAction(pPlasma)
					actionsAdded = actionsAdded + 1

		### Create Nano's Large Explosion ###
		debug(__name__ + ", CreateNanoWeaponExpSeq, the large explosion")
		if pAttachTo == None or vEmitPos == None or vEmitDir == None or pEmitFrom == None or fSize <= 0.000035:
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 1.0)
				#pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, fBrightness = 0.6)
		if pExplosion:
			pSequence.AddAction(pExplosion)
			actionsAdded = actionsAdded + 1

		sFile = ExpFX.GetNanoGfxFile("ExpFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
		pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 8.0, fBrightness = 0.6)
		if pFlash:
			pSequence.AddAction(pFlash)
			actionsAdded = actionsAdded + 1

		iNumPlume = 3
		for iPoint in range( iNumPlume ):
			debug(__name__ + ", CreateNanoWeaponExpSeq, the iPoint explosion")
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * 0.50, vEmitPos, vEmitDir, fVariance = 150.0, iTiming = 20, sType = "Plume")
			if pExplosion:
				pSequence.AddAction(pExplosion)
				actionsAdded = actionsAdded + 1
			sFile = ExpFX.GetNanoGfxFile("ExpFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/ExpFlash/")
			pFlash = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize, vEmitPos, vEmitDir, iTiming = 4.0, fBrightness = 0.6)
			if pFlash:
				pSequence.AddAction(pFlash)
				actionsAdded = actionsAdded + 1
		###
		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 1.0)
			#pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5)

		return pSequence

	################### ############# ############# ####################
	# THE TWEAK IS ALWAYS ENABLED
	ExpFX.CreateNanoWeaponExpSeq = NewCreateNanoWeaponExpSeq

	####################################################################
	####################################################################


	####################################################################
	####################################################################
	# PATCH FOR: CreateNanoExpNovaSeq
	# -- The following function is only for the Alternate Death "No sequence"
	def CreateNanoExpNovaNoSeq(pShip, fSize, forceStart=1, pSet=None, pAttachTo=None, pEmitFrom = None, pWarpcoreEmitPos = None, isPlayer=None, fFlashColor=None, sRace=None, iShow=None, iRadius=None):
		debug(__name__ + ", NewCreateNanoExpNovaSeq")

		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoExpNovaSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = [] # NOT an actual TGSequence!!!!

		#############################
		# something like:
		# for aTimerClass in pSequence:
		# 	aTimerClass.Start()
		##############################


		if not pShip or not hasattr(pShip, "GetObjID") or fSize <= 0.0:
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if (not pShip) or pShip.IsDead():
			return pSequence

		shipIsDead = pShip.IsDead()
		if pSet is None:
			pSet = pShip.GetContainingSet()
		if not pSet: 
			return pSequence

		###
		### Setup for Effect ###

		if pAttachTo is None:
			pAttachTo 	 = pSet.GetEffectRoot()

		if pEmitFrom is None:
			pEmitFrom 	 = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

		if pWarpcoreEmitPos is None:
			if not shipIsDead:
				pWarpcore 	 = pShip.GetPowerSubsystem() # WE DON'T CARE ABOUT THE WARP CORE, ONLY ITS POSITION!
				if pWarpcore and hasattr(pWarpcore, "GetPosition"):
					pWarpcoreEmitPos = pWarpcore.GetPosition()

		if pWarpcoreEmitPos is None:
			pWarpcoreEmitPos = App.NiPoint3(0, 0, 0)

		if isPlayer is None:
			if (not shipIsDead):
				try:
					pPlayer = MissionLib.GetPlayer()
					iPlayerID = None
					if pPlayer and hasattr(pPlayer, "GetObjID") and not pPlayer.IsDead():
						iPlayerID = pPlayer.GetObjID()
					if iPlayerID == iShipID:
						isPlayer = 1
				except:
					traceback.print_exc()
					myShpName = pShip.GetName()
					if myShpName is not None:
						sMyName = str(myShpName)
						if sMyName is not None and sMyName == "Player" or sMyName == "player":
							isPlayer = 1
		if iShow is None:
			if isPlayer:
				iShow = 2.0
			else:
				iShow = 0.0

		if fFlashColor is None:
			if (not shipIsDead):
				fFlashColor   = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, "ExpFX")
				if (fFlashColor == None):
					if sRace is None:
						sRace 			= Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
					if not (sRace is None):
						fFlashColor 	= Custom.NanoFXv2.NanoFX_Lib.GetRaceTextureColor(sRace)

		if fFlashColor is None:
			fFlashColor   = (255.0, 248.0, 220.0)

		vEmitDir = App.NiPoint3((App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01)

		###
		shouldDoVisibleDmgStuff = ShouldDoDebris(pShip, 2)
		if fSize != 1:

			sFile = ExpFX.GetNanoGfxFile("NovaRingGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/NovaRing/")
			if sFile != None:
				
				ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
				pExplosion = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.4, 0.4, {"itsanEffect": 1, "checkDead": 1}, Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX, iShipID, sFile, pEmitFrom, pAttachTo, fSize * (5.0 + iShow), pWarpcoreEmitPos, iTiming = 64, fRed = fFlashColor[0], fGreen = fFlashColor[1], fBlue = fFlashColor[2], fBrightness = 0.5)
				if pExplosion:
					pSequence.append(pExplosion)
					actionsAdded = actionsAdded + 1

			sFile = ExpFX.GetNanoGfxFile("NovaSphereGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/NovaSphere/")
			if sFile != None:
				ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
				pExplosion = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1, "checkDead": 1}, Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX, iShipID, sFile, pEmitFrom, pAttachTo, fSize * (3.0 + iShow), pWarpcoreEmitPos, iTiming = 28)
				if pExplosion:
					pSequence.append(pExplosion)
					actionsAdded = actionsAdded + 1

			sFile = ExpFX.GetNanoGfxFile("NovaFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/NovaFlash/")
			if sFile != None:
				ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
				pExplosion = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.01, 0.01, {"itsanEffect": 1, "checkDead": 1}, Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX, iShipID, sFile, pEmitFrom, pAttachTo, fSize * (3.0 + iShow), pWarpcoreEmitPos, iTiming = 20)
				if pExplosion:
					pSequence.append(pExplosion)
					actionsAdded = actionsAdded + 1

			### Create Nano's Nova Explosion Sound ###
			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			pSound = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.01, 0.01, {"itsanEffect": 1, "checkDead": 1}, ExpFX.CreateNanoSoundSeq, iShipID, pShip, "ExpNovaSfx")
			if pSound:
				pSequence.append(pSound)
				actionsAdded = actionsAdded + 1
			###
			### Damage the model with Warp Core Explosion ###
			if shouldDoVisibleDmgStuff:
				ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
				aDmgAction = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.7, 0.7, {"itsanEffect": 0, "checkDead": 1}, Custom.NanoFXv2.NanoFX_ScriptActions.NanoDamageShip, iShipID, None, pShip, pEmitFrom, pShip.GetRadius(), 600.0)
				if aDmgAction:
					pSequence.append(aDmgAction)
					actionsAdded = actionsAdded + 1
		else:
			try:
				if iRadius is None:
					if (not shipIsDead):
						iRadius = pShip.GetRadius()
			except:
				iRadius = 0
				traceback.print_exc()

			fSize = iRadius / 1.2

			### Create Nano's Nova Explosion Sound ###
			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			pSound = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.01, 0.01, {"itsanEffect": 1, "checkDead": 1}, ExpFX.CreateNanoSoundSeq, iShipID, pShip, "ExpLargeSfx")
			if pSound:
				pSequence.append(pSound)
				actionsAdded = actionsAdded + 1

			###

		if fSize > 0.0001:
			iNovaSparks = Custom.NanoFXv2.NanoFX_Config.eFX_ExpSparkFXLevel * 7.0
			if (not iNovaSparks is None) and iNovaSparks > 0:
				for iPoint in range( iNovaSparks ):
					fRand = App.g_kSystemWrapper.GetRandomNumber(100) *  0.01
					ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
					pSparks = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1, "checkDead": 1}, ExpFX.CreateExpSparkSeq, iShipID, fSize * (0.8 + fRand), pEmitFrom, pAttachTo, pWarpcoreEmitPos, vEmitDir)

					if pSparks:
						pSequence.append(pSparks)
						actionsAdded = actionsAdded + 1
		###

		#if actionsAdded == 0:
		#	ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		#	dummyF = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 0}, ASequenceDummy, iShipID)
		#	if dummyF:
		#		pSequence.append(dummyF)
		#		actionsAdded = actionsAdded + 1

		if forceStart:
			for aTimerClass in pSequence:
				aTimerClass.Start()

		return pSequence

	# -- The following function is the sequence-style patch
	def NewCreateNanoExpNovaSeq(pShip, fSize):
		debug(__name__ + ", NewCreateNanoExpNovaSeq")

		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoExpNovaSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = App.TGSequence_Create()

		if not pShip or not hasattr(pShip, "GetObjID") or fSize == 0.0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip or pShip.IsDead(): # Alex SL Gato tweak - apparently if the ship is dead some parameters will be broken and crash the game, so better not.
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		pSet = pShip.GetContainingSet()
		if not pSet:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		###
		### Setup for Effect ###
		pAttachTo 	 = pSet.GetEffectRoot()
		pEmitFrom 	 = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

		pWarpcore 	 = pShip.GetPowerSubsystem()
		pWarpcoreEmitPos = App.NiPoint3(0, 0, 0)
		if pWarpcore and hasattr(pWarpcore, "GetPosition"):
			pWarpcoreEmitPos = pWarpcore.GetPosition()
		else:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence
		
		vEmitDir = App.NiPoint3((App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01, (App.g_kSystemWrapper.GetRandomNumber(200) - 100) * 0.01)
		fFlashColor   = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, "ExpFX")
		iShow = 0.0
		if pShip.GetName() == "Player" or pShip.GetName() == "player":
			iShow = 2.0

		if (fFlashColor == None):
			sRace 			= Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
			fFlashColor 	= Custom.NanoFXv2.NanoFX_Lib.GetRaceTextureColor(sRace)

		shouldDoVisibleDmgStuff = ShouldDoDebris(pShip, 2)
		###
		if fSize != 1:
			sFile = ExpFX.GetNanoGfxFile("NovaRingGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/NovaRing/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * (5.0 + iShow), pWarpcoreEmitPos, iTiming = 64, fRed = fFlashColor[0], fGreen = fFlashColor[1], fBlue = fFlashColor[2], fBrightness = 0.5)
			if pExplosion:
				pSequence.AddAction(pExplosion, App.TGAction_CreateNull(), 0.4)
				actionsAdded = actionsAdded + 1
			sFile = ExpFX.GetNanoGfxFile("NovaSphereGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/NovaSphere/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * (3.0 + iShow), pWarpcoreEmitPos, iTiming = 28)
			if pExplosion:
				pSequence.AddAction(pExplosion, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
			sFile = ExpFX.GetNanoGfxFile("NovaFlashGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/NovaFlash/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize * (3.0 + iShow), pWarpcoreEmitPos, iTiming = 20)
			if pExplosion:
				pSequence.AddAction(pExplosion)
				actionsAdded = actionsAdded + 1
			### Create Nano's Nova Explosion Sound ###
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpNovaSfx")
			if pSound:
				pSequence.AddAction(pSound)
				actionsAdded = actionsAdded + 1
			###
			### Damage the model with Warp Core Explosion ###
			if shouldDoVisibleDmgStuff:
				aDmgAction = App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "NanoDamageShip", pShip, pEmitFrom, pShip.GetRadius(), 600.0)
				if aDmgAction:
					pSequence.AddAction(aDmgAction, App.TGAction_CreateNull(), 0.7)
					actionsAdded = actionsAdded + 1
		else:
			fSize = pShip.GetRadius() / 1.2
			### Create Nano's Nova Explosion Sound ###
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpLargeSfx")
			if pSound:
				pSequence.AddAction(pSound)
				actionsAdded = actionsAdded + 1
			###
		iNovaSparks = Custom.NanoFXv2.NanoFX_Config.eFX_ExpSparkFXLevel * 7.0
		for iPoint in range( iNovaSparks ):
			fRand = App.g_kSystemWrapper.GetRandomNumber(100) *  0.01
			pSparks = ExpFX.CreateExpSparkSeq(fSize * (0.8 + fRand), pEmitFrom, pAttachTo, pWarpcoreEmitPos, vEmitDir)
			if pSparks:
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.50)
				actionsAdded = actionsAdded + 1
		###

		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 

		return pSequence

	################### ############# ############# ####################
	# ENABLE PATCH TO APPLY
	if G_PATCHFIX == 1 or G_PATCHFIX > 2:
		ExpFX.CreateNanoExpNovaSeq = NewCreateNanoExpNovaSeq
	####################################################################
	####################################################################


	####################################################################
	####################################################################
	# PATCH FOR: CreateNanoExpLargeSeq
	# -- The following function is only for the Alternate Death "No sequence"
	def CreateNanoExpLargeNoSeq(pShip, iNumPlume, forceStart=1, shipRad=None, pEmitFrom=None):
		debug(__name__ + ", NewCreateNanoExpLargeSeq")
		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoExpLargeSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = []

		if not pShip or not hasattr(pShip, "GetObjID"):
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip:
			return pSequence

		# prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
		if pShip.IsDead() or pShip.IsDying():
			return pSequence

		pSet = pShip.GetContainingSet()
		if not pSet:
			return pSequence

		myHull = pShip.GetHull()
		if not myHull or myHull.GetConditionPercentage() <= 0: # or else with small objects the game will crash without any warning
			return pSequence

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		pSound = NewNanoTimerDef(str(actionsAdded) + "NanoExpLargeNoSeq" + str(iShipID), ET_NOVA_EVT, 0.01, 0.01, {"itsanEffect": 1}, ExpFX.CreateNanoSoundSeq, iShipID, pShip, "ExpMedSfx")
		if pSound:
			pSequence.append(pSound)
			actionsAdded = actionsAdded + 1

		# little Defiant fix: just don't crash with small objects, please.

		if shipRad is None:
			shipRad = pShip.GetRadius()

		if shipRad <= 0.1 or (myHull.GetCondition() < 100):
			return pSequence

		###
		### Setup for Effect ###
		if pEmitFrom is None:
			if not pShip.IsDead():
				pEmitFrom = pShip.GetRandomPointOnModel()
			else:
				pEmitFrom = App.NiPoint3(0, 0, 0)
		if not pEmitFrom:
			return pSequence

		pAttachTo = pShip.GetNode()
		vEmitPos = App.NiPoint3(0, 0, 0)
		vEmitDir = App.NiPoint3(1, 1, 1)
		fSize     = pShip.GetRadius() * 0.50
		sFile     = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		###

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		pExplosion = NewNanoTimerDef(str(actionsAdded) + "NanoExpLargeNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1}, Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX, iShipID, sFile, pEmitFrom, pAttachTo, fSize)
		if pExplosion:
			pSequence.append(pExplosion)
			actionsAdded = actionsAdded + 1

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		pSparks = NewNanoTimerDef(str(actionsAdded) + "NanoExpLargeNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1}, ExpFX.CreateExpSparkSeq, iShipID, fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)

		if pSparks:
			pSequence.append(pSparks)
			actionsAdded = actionsAdded + 1



		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		pDebris = NewNanoTimerDef(str(actionsAdded) + "NanoExpLargeNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1}, ExpFX.CreateNanoDebrisSeq, iShipID, fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)

		if pDebris:
			pSequence.append(pSparks)
			actionsAdded = actionsAdded + 1



		for iPoint in range( iNumPlume ):
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			if sFile:
				ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
				pExplosion = NewNanoTimerDef(str(actionsAdded) + "NanoExpLargeNoSeq" + str(iShipID), ET_NOVA_EVT, 0.01, 0.01, {"itsanEffect": 1}, Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX, iShipID, sFile, pEmitFrom, pAttachTo, fSize / 3.0,  fVariance = 120.0, iTiming = 20, sType = "Plume", fBrightness = 0.3)
				if pExplosion:
					pSequence.append(pExplosion)
					actionsAdded = actionsAdded + 1

			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			pSparks = NewNanoTimerDef(str(actionsAdded) + "NanoExpLargeNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1}, ExpFX.CreateExpSparkSeq, iShipID, fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			if pSparks:
				pSequence.append(pSparks)
				actionsAdded = actionsAdded + 1

			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			pDebris = NewNanoTimerDef(str(actionsAdded) + "NanoExpLargeNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1}, ExpFX.CreateNanoDebrisSeq, iShipID, fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			if pDebris:
				pSequence.append(pSparks)
				actionsAdded = actionsAdded + 1

		###
		#if actionsAdded == 0:
		#	ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		#	dummyF = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 0}, ASequenceDummy, iShipID)
		#	if dummyF:
		#		pSequence.append(dummyF)
		#		actionsAdded = actionsAdded + 1

		if forceStart:
			for aTimerClass in pSequence:
				aTimerClass.Start()

		return pSequence

	# -- The following function is the sequence-style patch
	def NewCreateNanoExpLargeSeq(pShip, iNumPlume):
		debug(__name__ + ", NewCreateNanoExpLargeSeq")
		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoExpLargeSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = App.TGSequence_Create()

		if not pShip or not hasattr(pShip, "GetObjID"):
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		# prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
		if pShip.IsDead() or pShip.IsDying():
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		pSet = pShip.GetContainingSet()
		if not pSet:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		###
		### Setup for Effect ###
		pEmitFrom = pShip.GetRandomPointOnModel()
		pAttachTo = pShip.GetNode()
		vEmitPos = App.NiPoint3(0, 0, 0)
		vEmitDir = App.NiPoint3(1, 1, 1)
		fSize     = pShip.GetRadius() * 0.50
		sFile     = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
		###
		pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpMedSfx")
		if pSound:
			actionsAdded = actionsAdded + 1
			pSequence.AddAction(pSound)

		# little Defiant fix: just don't crash with small objects, please.
		myHull = pShip.GetHull()
		if not myHull or myHull.GetCondition() <= 0: # or else with small objects the game will crash without any warning
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		if pShip.GetRadius() < 0.1 or (myHull.GetCondition() < 100):
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		if not pEmitFrom:
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize)
		if pExplosion:
			pSequence.AddAction(pExplosion)
			actionsAdded = actionsAdded + 1
		pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
		if pSparks:
			pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
			actionsAdded = actionsAdded + 1

		pDebris = ExpFX.CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
		if pDebris:
			pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
			actionsAdded = actionsAdded + 1

		for iPoint in range( iNumPlume ):
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize / 3.0,  fVariance = 120.0, iTiming = 20, sType = "Plume", fBrightness = 0.3)
			if pExplosion:
				pSequence.AddAction(pExplosion)
				actionsAdded = actionsAdded + 1
			pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			if pSparks:
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
			pDebris = ExpFX.CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			if pDebris:
				pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
		###
		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 

		return pSequence

	################### ############# ############# ####################
	# ENABLE PATCH TO APPLY
	if G_PATCHFIX == 1 or G_PATCHFIX > 2:
		ExpFX.CreateNanoExpLargeSeq = NewCreateNanoExpLargeSeq

	####################################################################
	####################################################################


	####################################################################
	####################################################################
	# PATCH FOR: CreateNanoExpSmallSeq
	# -- The following function is only for the Alternate Death "No sequence"
	def CreateNanoExpSmallNoSeq(pShip, fTime, forceStart=1):
		debug(__name__ + ", NewCreateNanoExpSmallSeq")
		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoExpSmallSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = []
		###
		### Setup for Effect ###

		if not pShip or not hasattr(pShip, "GetObjID"):
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip:
			return pSequence

		pSet = pShip.GetContainingSet()
		if not pSet:
			return pSequence

		iNumPlume = 1
		pAttachTo = pShip.GetNode()
		vEmitPos = App.NiPoint3(0, 0, 0)
		vEmitDir = App.NiPoint3(1, 1, 1)
		###
		### Create Nano's Explosion Sound ###

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		pSound = NewNanoTimerDef(str(actionsAdded) + "NanoExpSmallNoSeq" + str(iShipID), ET_NOVA_EVT, 0.01, 0.01, {"itsanEffect": 1}, ExpFX.CreateNanoSoundSeq, iShipID, pShip, "ExpLargeSfx")
		if pSound:
			pSequence.append(pSound)
			actionsAdded = actionsAdded + 1

		fExplosionTime = 0.0
		# little Defiant fix: just don't crash with small objects, please.
		# and prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
		# check: maybe the small object problem is linked to the randompoint one.
		#if pShip.GetRadius() < 0.1 or (pShip.GetHull() and pShip.GetHull().GetCondition() < 100) or pShip.IsDead() or pShip.IsDying():

		myHull = pShip.GetHull()
		if not myHull: # or else with small objects the game will crash without any warning
			return pSequence

		## prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
		if pShip.IsDead(): # or pShip.IsDying():
			return pSequence

		shipRadius = pShip.GetRadius()

		if not shipRadius or shipRadius < 0.1:
			return pSequence

		shouldDoVisibleDmgStuff = ShouldDoDebris(pShip, 2, fDmg=1200)

		while (fExplosionTime < fTime):
			###
			### Create Nano's Visual Smaller Explosions ###
			# prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
			#if pShip.IsDead() or pShip.IsDying() or not pShip.GetHull() or pShip.GetHull().GetConditionPercentage() == 0:
			if pShip.IsDead():
				return pSequence

			pEmitFrom = pShip.GetRandomPointOnModel()
			if not pEmitFrom:
				return pSequence

			fSize  = shipRadius * (App.g_kSystemWrapper.GetRandomNumber(40) + 20) * 0.01

			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")

			if sFile:
				ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
				pExplosion = NewNanoTimerDef(str(actionsAdded) + "NanoExpSmallNoSeq" + str(iShipID), ET_NOVA_EVT, 0.01, 0.01, {"itsanEffect": 1}, Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX, iShipID, sFile, pEmitFrom, pAttachTo, fSize)
				if pExplosion:
					pSequence.append(pExplosion)
					actionsAdded = actionsAdded + 1

			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			pSparks = NewNanoTimerDef(str(actionsAdded) + "NanoExpSmallNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1}, ExpFX.CreateExpSparkSeq, iShipID, fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
			if pSparks:
				pSequence.append(pSparks)
				actionsAdded = actionsAdded + 1

			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			pDebris = NewNanoTimerDef(str(actionsAdded) + "NanoExpSmallNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1}, ExpFX.CreateNanoDebrisSeq, iShipID, fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			if pDebris:
				pSequence.append(pSparks)
				actionsAdded = actionsAdded + 1

			for iPoint in range( iNumPlume ):
				sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
				if sFile:
					ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
					pExplosion = NewNanoTimerDef(str(actionsAdded) + "NanoExpSmallNoSeq" + str(iShipID), ET_NOVA_EVT, 0.01, 0.01, {"itsanEffect": 1}, Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX, iShipID, sFile, pEmitFrom, pAttachTo, fSize / 3.0,  fVariance = 120.0, iTiming = 20, sType = "Plume")
					if pExplosion:
						pSequence.append(pExplosion)
						actionsAdded = actionsAdded + 1

				ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
				pSparks = NewNanoTimerDef(str(actionsAdded) + "NanoExpSmallNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1}, ExpFX.CreateExpSparkSeq, iShipID, fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
				if pSparks:
					pSequence.append(pSparks)
					actionsAdded = actionsAdded + 1

				ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
				pDebris = NewNanoTimerDef(str(actionsAdded) + "NanoExpSmallNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 1}, ExpFX.CreateNanoDebrisSeq, iShipID, fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
				if pDebris:
					pSequence.append(pSparks)
					actionsAdded = actionsAdded + 1


			###
			### Damage the model with these explosions ###
			if shouldDoVisibleDmgStuff:
				ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
				dmgModelAction = NewNanoTimerDef(str(actionsAdded) + "NanoExpSmallNoSeq" + str(iShipID), ET_NOVA_EVT, 0.3, 0.3, {"itsanEffect": 0}, Custom.NanoFXv2.NanoFX_ScriptActions.NanoDamageShip, iShipID, None, pShip, pEmitFrom, shipRadius / 2.0, 1200.0)
				if dmgModelAction:
					pSequence.append(dmgModelAction)
					actionsAdded = actionsAdded + 1

				fExtraDamage = 0.1
				while (fExtraDamage < fTime):
					# prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
					#if pShip.IsDead() or pShip.IsDying() or not pShip.GetHull() or pShip.GetHull().GetConditionPercentage() == 0:
					if pShip.IsDead():
						return pSequence
					pEmitFrom = pShip.GetRandomPointOnModel()
					if not pEmitFrom:
						return pSequence
					ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
					anotherDmgAction = NewNanoTimerDef(str(actionsAdded) + "NanoExpSmallNoSeq" + str(iShipID), ET_NOVA_EVT, 0.3+fExtraDamage , 0.3 +fExtraDamage, {"itsanEffect": 0, "checkDead": 1}, Custom.NanoFXv2.NanoFX_ScriptActions.NanoDamageShip, iShipID, None,  pShip, pEmitFrom, shipRadius / 3.0, 1200.0)
					if anotherDmgAction:
						pSequence.append(anotherDmgAction)
						actionsAdded = actionsAdded + 1

					fExtraDamage = fExtraDamage + 0.04
			###
			fExplosionTime = fExplosionTime + 0.5

		#if actionsAdded == 0:
		#	ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		#	dummyF = NewNanoTimerDef(str(actionsAdded) + "NanoExpNovaNoSeq" + str(iShipID), ET_NOVA_EVT, 0.5, 0.5, {"itsanEffect": 0}, ASequenceDummy, iShipID)
		#	if dummyF:
		#		pSequence.append(dummyF)
		#		actionsAdded = actionsAdded + 1

		if forceStart:
			for aTimerClass in pSequence:
				aTimerClass.Start()

		return pSequence

	# -- The following function is the sequence-style patch
	def NewCreateNanoExpSmallSeq(pShip, fTime):
		debug(__name__ + ", NewCreateNanoExpSmallSeq")
		kTiming = App.TGProfilingInfo("ExpFX, CreateNanoExpSmallSeq")
		### Create Sequence Object ###
		actionsAdded = 0
		pSequence = App.TGSequence_Create()
		###
		### Setup for Effect ###

		if not pShip or not hasattr(pShip, "GetObjID"):
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iShipID = pShip.GetObjID()

		pShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		pSet = pShip.GetContainingSet()
		if not pSet:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		pAttachTo = pShip.GetNode()
		if not pAttachTo:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		iNumPlume = 1
		vEmitPos = App.NiPoint3(0, 0, 0)
		vEmitDir = App.NiPoint3(1, 1, 1)
		###
		### Create Nano's Explosion Sound ###
		pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpLargeSfx")
		if pSound:
			pSequence.AddAction(pSound)
			actionsAdded = actionsAdded + 1
		fExplosionTime = 0.0
		# little Defiant fix: just don't crash with small objects, please.
		# and prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
		# check: maybe the small object problem is linked to the randompoint one.
		#if pShip.GetRadius() < 0.1 or (pShip.GetHull() and pShip.GetHull().GetCondition() < 100) or pShip.IsDead() or pShip.IsDying():

		myHull = pShip.GetHull()
		if not myHull: # or else with small objects the game will crash without any warning
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		## prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
		if pShip.IsDead(): # or pShip.IsDying():
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		shipRadius = pShip.GetRadius()

		if not shipRadius or shipRadius < 0.1:
			if actionsAdded <= 0:
				pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			return pSequence

		shouldDoVisibleDmgStuff = ShouldDoDebris(pShip, 2, fDmg=1200)

		while (fExplosionTime < fTime):
			###
			### Create Nano's Visual Smaller Explosions ###
			# prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
			#if pShip.IsDead() or pShip.IsDying() or not pShip.GetHull() or pShip.GetHull().GetConditionPercentage() == 0:
			if pShip.IsDead():
				if actionsAdded <= 0:
					pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
				return pSequence

			pEmitFrom = pShip.GetRandomPointOnModel()
			if not pEmitFrom:
				if actionsAdded <= 0:
					pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
				return pSequence
			fSize  = shipRadius * (App.g_kSystemWrapper.GetRandomNumber(40) + 20) * 0.01
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize)
			if pExplosion:
				pSequence.AddAction(pExplosion)
				actionsAdded = actionsAdded + 1
			pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
			if pSparks:
				pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
			pDebris = ExpFX.CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
			if pDebris:
				pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
				actionsAdded = actionsAdded + 1
			for iPoint in range( iNumPlume ):
				sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
				pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize / 3.0,  fVariance = 120.0, iTiming = 20, sType = "Plume")
				if pExplosion:
					pSequence.AddAction(pExplosion)
					actionsAdded = actionsAdded + 1
				pSparks = ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pAttachTo, vEmitPos, vEmitDir)
				if pSparks:
					pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
					actionsAdded = actionsAdded + 1
				pDebris = ExpFX.CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
				if pDebris:
					pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
					actionsAdded = actionsAdded + 1
			###
			### Damage the model with these explosions ###
			if shouldDoVisibleDmgStuff:
				dmgModelAction = App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "NanoDamageShip", pShip, pEmitFrom, shipRadius / 2.0, 1200.0)
				if dmgModelAction:
					pSequence.AddAction(dmgModelAction, App.TGAction_CreateNull(), 0.3)
					actionsAdded = actionsAdded + 1

				fExtraDamage = 0.1
				while (fExtraDamage < fTime):
					# prevent GetRandomPointOnModel() from crashing the game on dying/dead ships
					#if pShip.IsDead() or pShip.IsDying() or not pShip.GetHull() or pShip.GetHull().GetConditionPercentage() == 0:
					if pShip.IsDead():
						if actionsAdded <= 0:
							pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
						return pSequence
					pEmitFrom = pShip.GetRandomPointOnModel()
					if not pEmitFrom:
						if actionsAdded <= 0:
							pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
						return pSequence
					anotherDmgAction = App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "NanoDamageShip", pShip, pEmitFrom, shipRadius / 3.0, 1200.0)
					if anotherDmgAction:
						pSequence.AddAction(anotherDmgAction, App.TGAction_CreateNull(), 0.3)
						actionsAdded = actionsAdded + 1
					fExtraDamage = fExtraDamage + 0.04
			###
			fExplosionTime = fExplosionTime + 0.5

		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 

		return pSequence

	################### ############# ############# ####################
	# ENABLE PATCH TO APPLY
	if G_PATCHFIX == 1 or G_PATCHFIX > 2:
		ExpFX.CreateNanoExpSmallSeq = NewCreateNanoExpSmallSeq

	####################################################################
	####################################################################


	####################################################################
	####################################################################
	# PATCH FOR: NanoCollisionEffect
	# -- The following function is the sequence-style patch
	def NewNanoCollisionEffect(pShip, pEvent):
		### Setup ###
		debug(__name__ + ", NanoCollisionEffect")

		if not pShip or not hasattr(pShip, "GetObjID"):
			return

		iShipID = pShip.GetObjID()

		pShip2 = App.ShipClass_GetObjectByID(None, iShipID)
		if not pShip2: # or pShip.IsDead():
			return

		pSet = pShip.GetContainingSet()
		if not pSet:
			return
		actionsAdded = 0
		fSize     = pShip.GetRadius()
		pAttachTo = pSet.GetEffectRoot()
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
		pSequence = App.TGSequence_Create()
		###
		### Get the collision points ###
		for iPoint in range( pEvent.GetNumPoints() ):
			vEmitPos = pEvent.GetPoint(iPoint)
			vEmitDir = App.TGPoint3_GetRandomUnitVector()

			### Add an explosion at this point ###
			sFile = ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
			pCollision = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, None, pAttachTo, fSize, vEmitPos, vEmitDir)
			if pCollision:
				pSequence.AddAction(pCollision)
				actionsAdded = actionsAdded + 1
			pSound = ExpFX.CreateNanoSoundSeq(pShip, "ExpCollisionSfx")
			if pSound:
				pSequence.AddAction(pSound)
				actionsAdded = actionsAdded + 1
		###

		if actionsAdded == 0:
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
		pSequence.Play()
		###
		pShip.CallNextHandler(pEvent)

	################### ############# ############# ####################
	# ENABLE PATCH TO APPLY
	if G_PATCHFIX == 1 or G_PATCHFIX > 2:
		ExpFX.NanoCollisionEffect = NewNanoCollisionEffect

	####################################################################
	####################################################################


	####################################################################
	####################################################################
	# PATCH FOR: NanoDeathSeq
	# -- The following function is the Alternate Death "No sequence"
	def NanoDeathNoSeq(pShip, forceStart=1):
		### Holds the Entire Death Sequence ###
		debug(__name__ + ", NewNanoDeathSeq")
		pFullSequence = []
		actionsAdded = 0
		###
		### Setup Sequence Timing ###
		fTotalSequenceTime = 14
		fExplosionShift = -8.0
		###
		### Set up Exploding Ship Properties ###
		pExplodingShipA = App.ShipClass_Cast(pShip)
		if not pExplodingShipA or not hasattr(pExplodingShipA, "GetObjID"):
			return

		iShipID = pExplodingShipA.GetObjID()

		pExplodingShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pExplodingShip:
			return

		pExplodingShip.SetMass(50000)
		pExplodingShip.SetRotationalInertia(11000)

		fRadius = 0.0
		shipName = pExplodingShip.GetName()
		fExplodingShipRadius = pExplodingShip.GetRadius()
		

		pLargeExpSeq1EmitFrom = None # ADDED LINEs, TEST if this functions is the cause of our suffering
		if (fExplodingShipRadius is not None) and fExplodingShipRadius > 0.1:
			pLargeExpSeq1EmitFrom = pExplodingShip.GetRandomPointOnModel() #ADDED LINEs, TEST if this functions is the cause of our suffering

		if fExplodingShipRadius <= (0.01 / 15.0): #ANOTHER ADDITION, MAYBE RADIUS TOO SMALL ARE NOT CONSIDERED?
			fExplodingShipRadius = 0.01/15.0 #ANOTHER ADDITION, MAYBE RADIUS TOO SMALL ARE NOT CONSIDERED?

		pWarpSubsys = pExplodingShip.GetPowerSubsystem()
		if (pExplodingShip.GetName() == "Player") or (pExplodingShip.GetName() == "player"):
			pExplodingShip.SetLifeTime (fTotalSequenceTime)
			pWarpPower = 15
			if pWarpSubsys and pWarpSubsys.GetPowerOutput() > 0 and fExplodingShipRadius > 0:
				pWarpPower = pWarpPower * fExplodingShipRadius
			fRadius = pWarpPower
		else:
			pExplodingShip.SetLifeTime (fTotalSequenceTime / 2 + 1)
			if pWarpSubsys:
				pWarpPower = (pWarpSubsys.GetAvailablePower() * 0.025) + (pWarpSubsys.GetPowerOutput() * 0.075)
				pWarpPower = pWarpPower * Custom.NanoFXv2.NanoFX_Config.eFX_SplashRadius
				fRadius = pWarpPower / 50.0
				if pWarpPower:
					pExplodingShip.SetSplashDamage(pWarpPower, fRadius)
					print("Setting splash damage for %s to (%f, %f)" % (pExplodingShip.GetName(), pExplodingShip.GetSplashDamage(), pExplodingShip.GetSplashDamageRadius()))
					debug(__name__ + ", NewNanoDeathSeq Setting splash damage for %s to (%f, %f)" % (pExplodingShip.GetName(), pExplodingShip.GetSplashDamage(), pExplodingShip.GetSplashDamageRadius()))

			pExplodingShip.UpdateNodeOnly() # ANOTHER ADDITION
		###
		### Begin Death Sequence ###
		############################
		###
		### Flicker some lights ###
		if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			myTime = 1.0
			pFlickerAction1 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, myTime, myTime, {"itsanEffect": 1}, Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq, iShipID, pExplodingShip, 3.0, sStatus = "Off")
			if pFlickerAction1:
				pFullSequence.append(pFlickerAction1)
				actionsAdded = actionsAdded + 1

		###
		### Create Nano's Initial Large explosions ###

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		myTime = 0.2
		pSmallExpSeq1 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, myTime, myTime, {"itsanEffect": 0}, CreateNanoExpSmallNoSeq, iShipID, pExplodingShip, 0.01)
		if pSmallExpSeq1:
			pFullSequence.append(pSmallExpSeq1)
			actionsAdded = actionsAdded + 1


		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		myTime = fTotalSequenceTime - 3.2 + fExplosionShift
		pLargeExpSeq1 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, myTime, myTime, {"itsanEffect": 0}, CreateNanoExpLargeNoSeq, iShipID, pExplodingShip, 2, pEmitFrom=pLargeExpSeq1EmitFrom)
		if pLargeExpSeq1: # CRASH CHECK PROGRESS: WITH THIS UNCOMMENTED, IT SOMETIMES CRASHES
			pFullSequence.append(pLargeExpSeq1)
			actionsAdded = actionsAdded + 1



		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		myTime = fTotalSequenceTime - 3.05 + fExplosionShift
		pLargeExpSeq2 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, myTime, myTime, {"itsanEffect": 0}, CreateNanoExpLargeNoSeq, iShipID, pExplodingShip, 2)
		if pLargeExpSeq2:
			pFullSequence.append(pLargeExpSeq2)
			actionsAdded = actionsAdded + 1

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		myTime = fTotalSequenceTime - 2.85 + fExplosionShift
		pLargeExpSeq3 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, myTime, myTime, {"itsanEffect": 0}, CreateNanoExpLargeNoSeq, iShipID, pExplodingShip, 2)
		if pLargeExpSeq3:
			pFullSequence.append(pLargeExpSeq3)
			actionsAdded = actionsAdded + 1

		###
		### Destroy Model into Debris Parts ###
		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		myTime = fTotalSequenceTime - 1.7 + fExplosionShift
		pSmallExpSeq2 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, myTime, myTime, {"itsanEffect": 0}, CreateNanoExpSmallNoSeq, iShipID, pExplodingShip, 2.0)
		if pSmallExpSeq2:
			pFullSequence.append(pSmallExpSeq2)
			actionsAdded = actionsAdded + 1


		###
		### Add Random Spin to Model ###
		if (Custom.NanoFXv2.NanoFX_Config.eFX_RotationFX == "On"):
			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			myTime = 0.3
			pRotAction1 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, myTime, myTime, {"itsanEffect": 1}, Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq, iShipID, pExplodingShip, fRotation = 700)
			if pRotAction1:
				pFullSequence.append(pRotAction1)
				actionsAdded = actionsAdded + 1
			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			myTime = fTotalSequenceTime - 1.6 + fExplosionShift
			pRotAction2 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, myTime, myTime, {"itsanEffect": 1}, Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq, iShipID, pExplodingShip, fRotation = 1000, fSpeed = 0.5)
			if pRotAction2:
				pFullSequence.append(pRotAction2)
				actionsAdded = actionsAdded + 1
		###
		### Create Nano's Warp Core Explosion ###
		if fRadius and fRadius > 0.0: 
			ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
			myTime = fTotalSequenceTime - 1.7 + fExplosionShift
			pNovaExpAction1 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, myTime, myTime, {"itsanEffect": 0}, CreateNanoExpNovaNoSeq, iShipID, pExplodingShip, fRadius / 15)
			if pNovaExpAction1:
				pFullSequence.append(pNovaExpAction1)
				actionsAdded = actionsAdded + 1

		###
		### Create Nano's Final Explosions ###

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		pFinalExpAction1 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, fTotalSequenceTime - 1.95 + fExplosionShift, fTotalSequenceTime - 1.95 + fExplosionShift, {"itsanEffect": 0}, CreateNanoExpLargeNoSeq, iShipID, pExplodingShip, 2)
		if pFinalExpAction1:
			pFullSequence.append(pFinalExpAction1)
			actionsAdded = actionsAdded + 1

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		pFinalExpAction2 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, fTotalSequenceTime - 1.85 + fExplosionShift, fTotalSequenceTime - 1.85 + fExplosionShift, {"itsanEffect": 0}, CreateNanoExpLargeNoSeq, iShipID, pExplodingShip, 2)
		if pFinalExpAction2:
			pFullSequence.append(pFinalExpAction2)
			actionsAdded = actionsAdded + 1

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		pFinalExpAction3 = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, fTotalSequenceTime - 1.65 + fExplosionShift, fTotalSequenceTime - 1.65 + fExplosionShift, {"itsanEffect": 0}, CreateNanoExpLargeNoSeq, iShipID, pExplodingShip, 2)
		if pFinalExpAction3:
			pFullSequence.append(pFinalExpAction3)
			actionsAdded = actionsAdded + 1
		###
		#pFullSequence.SetUseRealTime(1)

		ET_NOVA_EVT = App.UtopiaModule_GetNextEventType()
		pPostExplosionStuffAction = NewNanoTimerDef(str(actionsAdded) + "NanoDeathNoSeq" + str(iShipID), ET_NOVA_EVT, fTotalSequenceTime, fTotalSequenceTime, {"itsanEffect": 0}, Custom.NanoFXv2.ExplosionFX.ExpFX.DoPostExplosionStuff, iShipID, None, iShipID)
		if pPostExplosionStuffAction:
			pFullSequence.append(pPostExplosionStuffAction)
			actionsAdded = actionsAdded + 1

		if forceStart:
			for aTimerClass in pFullSequence:
				aTimerClass.Start()

		###
		bFound = 0
		listToDelete = []
		try:
			for sName in Custom.NanoFXv2.NanoFX_Lib.g_LightsOff: # You cannot use a for loop to traverse lists to then delete items on that, not this way - internally C just makes it skip one, which is not good!
				if shipName == sName:
					bFound = 1
				if bFound == 1:
					listToDelete.append(sName)
		except:
			traceback.print_exc()

		try:
			for sName in listToDelete: # Weird cases where you have multiple of the same name.
				Custom.NanoFXv2.NanoFX_Lib.g_LightsOff.remove(sName)
				break
		except:
			traceback.print_exc()


	# -- The following function is the sequence-style patch
	def NewNanoDeathSeq(pShip):
		### Holds the Entire Death Sequence ###
		debug(__name__ + ", NewNanoDeathSeq")
		pFullSequence = App.TGSequence_Create()
		actionsAdded = 0
		###
		### Setup Sequence Timing ###
		fTotalSequenceTime = 14
		fExplosionShift = -8.0
		###
		### Set up Exploding Ship Properties ###
		pExplodingShip = App.ShipClass_Cast(pShip)
		if not pExplodingShip or not hasattr(pExplodingShip, "GetObjID"):
			pFullSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			pFullSequence.Play()
			return

		iShipID = pExplodingShip.GetObjID()

		pExplodingShip = App.ShipClass_GetObjectByID(None, iShipID)
		if not pExplodingShip:
			pFullSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 
			pFullSequence.Play()
			return

		pExplodingShip.SetMass(50000)
		pExplodingShip.SetRotationalInertia(11000)

		fRadius = 0.0
		shipName = pExplodingShip.GetName()
		fExplodingShipRadius = pExplodingShip.GetRadius()
		pWarpSubsys = pExplodingShip.GetPowerSubsystem()
		if (pExplodingShip.GetName() == "Player") or (pExplodingShip.GetName() == "player"):
			pExplodingShip.SetLifeTime (fTotalSequenceTime)
			pWarpPower = 15
			if pWarpSubsys and pWarpSubsys.GetPowerOutput() > 0 and fExplodingShipRadius > 0:
				pWarpPower = pWarpPower * fExplodingShipRadius
			fRadius = pWarpPower
		else:
			pExplodingShip.SetLifeTime (fTotalSequenceTime / 2 + 1)
			if pWarpSubsys:
				pWarpPower = (pWarpSubsys.GetAvailablePower() * 0.025) + (pWarpSubsys.GetPowerOutput() * 0.075)
				pWarpPower = pWarpPower * Custom.NanoFXv2.NanoFX_Config.eFX_SplashRadius
				fRadius = pWarpPower / 50.0
				if pWarpPower:
					pExplodingShip.SetSplashDamage(pWarpPower, fRadius)
					print("Setting splash damage for %s to (%f, %f)" % (pExplodingShip.GetName(), pExplodingShip.GetSplashDamage(), pExplodingShip.GetSplashDamageRadius()))
					debug(__name__ + ", NewNanoDeathSeq Setting splash damage for %s to (%f, %f)" % (pExplodingShip.GetName(), pExplodingShip.GetSplashDamage(), pExplodingShip.GetSplashDamageRadius()))
		###
		### Begin Death Sequence ###
		############################
		###
		### Flicker some lights ###
		if (Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On"):
			pFlickerAction1 = Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pExplodingShip, 3.0, sStatus = "Off")
			if pFlickerAction1:
				pFullSequence.AddAction(pFlickerAction1, App.TGAction_CreateNull(), 1.0)
				actionsAdded = actionsAdded + 1
		###
		### Create Nano's Initial Large explosions ###
		pSmallExpSeq1 = ExpFX.CreateNanoExpSmallSeq(pExplodingShip, 0.01)
		if pSmallExpSeq1:
			pFullSequence.AddAction(pSmallExpSeq1, App.TGAction_CreateNull(), 0.2)
			actionsAdded = actionsAdded + 1
		pLargeExpSeq1 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pLargeExpSeq1:
			pFullSequence.AddAction(pLargeExpSeq1, App.TGAction_CreateNull(), fTotalSequenceTime - 3.2 + fExplosionShift)
			actionsAdded = actionsAdded + 1

		pLargeExpSeq2 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pLargeExpSeq2:
			pFullSequence.AddAction(pLargeExpSeq2, App.TGAction_CreateNull(), fTotalSequenceTime - 3.05 + fExplosionShift)
			actionsAdded = actionsAdded + 1

		pLargeExpSeq3 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pLargeExpSeq3:
			pFullSequence.AddAction(pLargeExpSeq3, App.TGAction_CreateNull(), fTotalSequenceTime - 2.85 + fExplosionShift)
			actionsAdded = actionsAdded + 1
		###
		### Destroy Model into Debris Parts ###
		pSmallExpSeq2 = ExpFX.CreateNanoExpSmallSeq(pExplodingShip, 2.0)
		if pSmallExpSeq2:
			pFullSequence.AddAction(pSmallExpSeq2, App.TGAction_CreateNull(), fTotalSequenceTime - 1.7 + fExplosionShift)
			actionsAdded = actionsAdded + 1
		###
		### Add Random Spin to Model ###
		if (Custom.NanoFXv2.NanoFX_Config.eFX_RotationFX == "On"):
			pRotAction1 = Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq(pExplodingShip, 700)
			if pRotAction1:
				pFullSequence.AddAction(pRotAction1, App.TGAction_CreateNull(), 0.3)
				actionsAdded = actionsAdded + 1
			pRotAction2 = Custom.NanoFXv2.NanoFX_Lib.CreateRotationSeq(pExplodingShip, 1000, 0.5)
			if pRotAction2:
				pFullSequence.AddAction(pRotAction2, App.TGAction_CreateNull(), fTotalSequenceTime - 1.6 + fExplosionShift)
				actionsAdded = actionsAdded + 1
		###
		### Create Nano's Warp Core Explosion ###
		if fRadius and fRadius > 0.0:
			pNovaExpAction1 = ExpFX.CreateNanoExpNovaSeq(pExplodingShip, fRadius / 15)
			if pNovaExpAction1:
				pFullSequence.AddAction(pNovaExpAction1, App.TGAction_CreateNull(), fTotalSequenceTime - 1.7 + fExplosionShift)
				actionsAdded = actionsAdded + 1
			#pShakeSequuence = ExpFX.ShakeSequence(1.5) # This Sequence does not exist in modern NanoFX
			#if pShakeSequuence:
			#	pFullSequence.AddAction(pShakeSequuence, App.TGAction_CreateNull(), fTotalSequenceTime - 1.3 + fExplosionShift)
			#	actionsAdded = actionsAdded + 1
		###
		### Create Nano's Final Explosions ###
		pFinalExpAction1 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pFinalExpAction1:
			pFullSequence.AddAction(pFinalExpAction1, App.TGAction_CreateNull(), fTotalSequenceTime - 1.95 + fExplosionShift)
			actionsAdded = actionsAdded + 1

		pFinalExpAction2 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pFinalExpAction2:
			pFullSequence.AddAction(pFinalExpAction2, App.TGAction_CreateNull(), fTotalSequenceTime - 1.85 + fExplosionShift)
			actionsAdded = actionsAdded + 1

		pFinalExpAction3 = ExpFX.CreateNanoExpLargeSeq(pExplodingShip, 2)
		if pFinalExpAction3:
			pFullSequence.AddAction(pFinalExpAction3, App.TGAction_CreateNull(), fTotalSequenceTime - 1.65 + fExplosionShift)
			actionsAdded = actionsAdded + 1
		###
		#pFullSequence.SetUseRealTime(1)
		pPostExplosionStuffAction = App.TGScriptAction_Create("Custom.NanoFXv2.ExplosionFX.ExpFX", "DoPostExplosionStuff", iShipID)
		if pPostExplosionStuffAction:
			pFullSequence.AppendAction(pPostExplosionStuffAction, fTotalSequenceTime)
			actionsAdded = actionsAdded + 1

		if actionsAdded == 0:
			pFullSequence.AppendAction(App.TGScriptAction_Create(__name__, "ASequenceDummy"), 0.5) 

		#pDestroyTGSequenceAction = App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pFullSequence) # This sequence exists but was commented on newer NanoFX, so I'll leave it commented
		#if pDestroyTGSequenceAction:
		#	pFullSequence.AppendAction(pDestroyTGSequenceAction, fTotalSequenceTime)
		pFullSequence.Play()
		###
		bFound = 0
		listToDelete = []
		try:
			for sName in Custom.NanoFXv2.NanoFX_Lib.g_LightsOff: # You cannot use a for loop to traverse lists to then delete items on that, not this way - internally C just makes it skip one, which is not good!
				if shipName == sName:
					bFound = 1
				if bFound == 1:
					listToDelete.append(sName)
		except:
			traceback.print_exc()

		try:
			for sName in listToDelete: # Weird cases where you have multiple of the same name.
				Custom.NanoFXv2.NanoFX_Lib.g_LightsOff.remove(sName)
		except:
			traceback.print_exc()

	################### ############# ############# ####################
	# ENABLE PATCH TO APPLY IMPROVED SEQUENCE OR NO SEQUENCE VERSION
	if G_PATCHFIX == 1:
		ExpFX.NanoDeathSeq = NewNanoDeathSeq
	elif G_PATCHFIX >= 2:
		ExpFX.NanoDeathSeq = NanoDeathNoSeq
