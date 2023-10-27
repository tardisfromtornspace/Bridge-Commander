#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         RealityBomb.py by Alex SL Gato
#         Version 0.5
#         26th October 2023
#         Based on Simulated Point Defense.py and DampeningAOEDefensiveField.py by Alex SL Gato, which was based strongly on scripts\Custom\DS9FX\DS9FXPulsarFX\PulsarManager by USS Sovereign, and slightly on TractorBeams.py, Inversion Beam and Power Drain Beam 1.0 by MLeo Daalder, Apollo, and Dasher; some team-switching torpedo by LJ; and GraviticLance by Alex SL Gato, which was based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team, and AssimilationBeam.py from BCS:TNG and Apollo.
#         Special thanks to USS Sovereign for some tips!                 
#################################################################################################################
# This tech gives a ship the ability to destroy an entire system during an entire play session (meaning the system will also remain destroyedd once you end this simulation).
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file (replace "Sovereign" with the proper abbrev).
# Distance: Range of effect of this ability. Logically cannot be equal or less than 0, so if you don't want this ship to do anything apart from sounds, set it to 0. Default is 1000000 km.
# Period: this is more of a countdown than anything
"""
Foundation.ShipDef.Sovereign.dTechs = {
	'Davros Reality Bomb' : { "Distance": 10000000.0, "Period": 30}
}
"""
# You can also add an immunity:
"""
Foundation.ShipDef.Sovereign.dTechs = {
	'Davros Reality Bomb Immune' : 1
}
"""

import App
#from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
import Foundation
import FoundationTech
import Lib.LibEngineering
import loadspacehelper
import math
import MissionLib
import string
import time

from bcdebug import debug
import traceback

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.4",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

global lImmuneShips # A list meant only for backwards compatibility - do NOT edit
lImmuneShips = (
	"DalekVoidShip",
  )

try:

	# Based on PulsarMonitor from DS9FX, thank you USS Sovereign - Alex SL Gato

	bOverflow = 0
	pTimer = None
	defaultSlice = 10
	defaultDistance = 1000000.0
	defaultPeriod = 20
	defaultExtra = 20
	defaultFromWarningToExplosion = 10 # Explosion time, in seconds
	pAllShipsWithTheTech = {} # Has the ship, with the pInstances as keys

	pAllObjectsSpecialThatNeedToBeRestored = {} # Planets at the moment
	ticksPerKilometer = 225/40 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer

	iPlanetOffset = 300
	fRemoveFPDelay = 10
	fSetNumTilesPerAxisRadiusDiv = 60
	iSetNumAsteroidsPerTile = 1
	fRoidSizeFactor = 0.01
	fFPPowerOutMult = 1.0
	fRemovePlanetDelay = 5
	iNumHitsToDestroy = 1

	sFirepointScript = "BigFirepoint"

	def Start():
		global pTimer, bOverflow

		if not bOverflow:
			pTimer = DalekRealityBombDef()
		else:
			return

	class DalekRealityBombDef(FoundationTech.TechDef):

		
		# Future suggestion: "I preferred to have a single timer, that was a design choice though" - USS Sovereign

		def __init__(self, name):
			debug(__name__ + ", Initiated Reality Bomb counter")
			FoundationTech.TechDef.__init__(self, name)
			self.pEventHandler = App.TGPythonInstanceWrapper()
			self.pEventHandler.SetPyWrapper(self)
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, self.pEventHandler, "PlayerRespawned")
			App.g_kEventManager.RemoveBroadcastHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "PlayerRespawned") #ET_PLAYER_SHIP_CREATED does not exist on App.py
			App.g_kEventManager.AddBroadcastPythonMethodHandler(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, self.pEventHandler, "PlayerRespawned")
			App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_ENTERED_SET, self.pEventHandler, "PlayerRespawned")
			global bOverflow
			bOverflow = 1
			self.pTimer = None
			self.countdown()

		def PlayerRespawned(self, pEvent):
			debug(__name__ + ", PlayerRespawned")
			try:
				App.g_kLODModelManager.Purge()
			except:
				pass

			try:
				App.g_kModelManager.Purge()
			except:
				pass

			#try:
			#	App.g_kSetManager.Purge()
			#except:
			#	pass
			#try:
			#	App.g_kSetManager.ClearRenderedSet()
			#except:
			#	pass
			self.hideSignals()

		def hideSignals(self):
			pPlayer = MissionLib.GetPlayer()
			playerSet = "DeepSpace"
			if pPlayer:
				playerSet = repr(pPlayer.GetContainingSet())
			#print "Looking for player's set (", playerSet ,")"
			for systemSet in pAllObjectsSpecialThatNeedToBeRestored.keys():
				#print "systemSet"
				if playerSet == systemSet:
					#print "FOUND SET"
					for planetToHide in pAllObjectsSpecialThatNeedToBeRestored[systemSet]:
						#print "removing the button of orbit planet for planet ", planetToHide
						try:
							DeleteMenuButton("Helm", planetToHide, "Orbit Planet")
						except:
							pass
					break
			#print "No system match found"

		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:
				global bOverflow, pAllShipsWithTheTech
				dMasterDict = pInstance.__dict__['Davros Reality Bomb']
				pAllShipsWithTheTech[pInstance] = pShip

				if not bOverflow:
					bOverflow = 1
					self.pTimer = None
					#print "RealityBomb: initiating new countdown for:", pShip.GetName()
					self.countdown()
					
			else:
				print "RealityBomb Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
				pass

			pInstance.lTechs.append(self)
			print "RealityBomb: attached to ship:", pShip.GetName()

		def Detach(self, pInstance):
			debug(__name__ + ", Detach")
			pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None:
				global bOverflow, pAllShipsWithTheTech
				dMasterDict = pInstance.__dict__['Davros Reality Bomb']
				
				#pAllShipsWithTheTech.pop(pInstance, None)
				if pAllShipsWithTheTech.has_key(pInstance):
					print "key found, to remove ", pInstance
					del pAllShipsWithTheTech[pInstance]
				self.pShip = None
			else:
				#print "RealityBomb Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
				pass
			pInstance.lTechs.remove(self)
			print "DRB: detached from ship:"
			if pShip != None:
				print "---ship name:", pShip.GetName()

		def Detach2(self, pInstance, pShip):
			debug(__name__ + ", Detach2")
			global bOverflow, pAllShipsWithTheTech
			
			if not pInstance and pShip:
				try:
					pInstance = FoundationTech.dShips[pShip.GetName()]
					if pInstance == None:
						return
				except:
					print "Davros Reality Bomb: cancelling, error in try from Detach2 found..."
					return
				
			if pAllShipsWithTheTech.has_key(pInstance):
				print "key found, to remove ", pInstance
				del pAllShipsWithTheTech[pInstance]
			if pShip == None and pInstance != None:
				pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
			if pShip != None and pInstance != None:
				dMasterDict = pInstance.__dict__['Davros Reality Bomb']
			else:
				print "Davros Reality Bomb Error (at Detach): couldn't acquire ship"
				if pInstance != None:
					print "--- of id", pInstance.pShipID
				pass

			print "Davros Reality Bomb: cleanup-detached from ship"
			if pShip != None:
				print "---ship name:", pShip.GetName()

			if pInstance != None:
				pInstance.lTechs.remove(self)

		def countdown(self):
			debug(__name__ + ", Initiated Reality Bomb counter countdown")
			if not self.pTimer:
				global defaultSlice
				self.pTimer = App.PythonMethodProcess()
				self.pTimer.SetInstance(self)
				self.pTimer.SetFunction("lookclosershipsEveryone")
				self.pTimer.SetDelay(defaultSlice)
				self.pTimer.SetPriority(App.TimeSliceProcess.LOW)	
				self.pTimer.SetDelayUsesGameTime(1)

		def lookclosershipsEveryone(self, fTime):
			debug(__name__ + ", Reality Bomb Counter lookclosershipsEveryone")
			global pAllShipsWithTheTech
			#self.hideSignals() # Dirty way of keeping menu cleared
			for myShipInstance in pAllShipsWithTheTech.keys():
				self.lookcloserships(fTime, pAllShipsWithTheTech[myShipInstance], myShipInstance)

		def lookcloserships(self, fTime, pShip, pInstance):
			debug(__name__ + ", Reality Bomb Counter lookcloserships")

			pShip2 = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID)) # If ship does not exist, do not continue
			if pShip == None or pInstance == None or pShip.IsDead() or pShip.IsDying() or not pShip2:
				self.Detach2(pInstance, pShip)
				return

			#print "The ship which is using it is ", pShip.GetName()

			global defaultPeriod, defaultSlice
			if not pInstance.__dict__['Davros Reality Bomb'].has_key("Period"):
				pInstance.__dict__['Davros Reality Bomb']["Period"] = defaultPeriod + defaultExtra

			if not pInstance.__dict__['Davros Reality Bomb'].has_key("TimeRemaining"):
				pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] = defaultPeriod + defaultExtra

			if not pInstance.__dict__['Davros Reality Bomb'].has_key("Firing"):
				pInstance.__dict__['Davros Reality Bomb']["Firing"] = 0

			goForPlayer = 0
			
			if pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] > defaultExtra:
				if (pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] < (defaultPeriod + defaultSlice + defaultExtra)) and (pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] > (defaultPeriod - defaultSlice + defaultExtra)):
					print "initiating countdown"
					pSeq = App.TGSequence_Create()
					pAction = App.TGScriptAction_Create(__name__, "accionFirstCountdown")
					pSeq.AddAction(pAction, None, 0)
					pSeq.Play()
				pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] = pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] - defaultSlice	
				return
			else:
				if pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] <= 0:
					pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] = pInstance.__dict__['Davros Reality Bomb']["Period"]
					goForPlayer = 1
					print "Test Completed"
				else:
					if pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] > (defaultExtra - defaultSlice):
						pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] = pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] - defaultSlice
						print "Activate planetary alignment field"
						#pInstance.__dict__['Davros Reality Bomb']["Firing"] = 1
					else:
						pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] = pInstance.__dict__['Davros Reality Bomb']["TimeRemaining"] - defaultSlice
						return
					print "Firing The Bomb"

			pSet = pShip.GetContainingSet()
			if not pSet:
				return

			pProx = pSet.GetProximityManager()
			if not pProx:
				return

			global defaultDistance
			# Allowing dynamic modification of this value mid-battle
			if not pInstance.__dict__['Davros Reality Bomb'].has_key("Distance"):
				pInstance.__dict__['Davros Reality Bomb']["Distance"] = defaultDistance

			iRange = pInstance.__dict__['Davros Reality Bomb']["Distance"]

			if iRange <= 0:
				return

			lDrain = []
			detonationNegative = 0

			pGame = App.Game_GetCurrentGame()
			pEpisode = pGame.GetCurrentEpisode()
			pMission = pEpisode.GetCurrentMission()
			pPlayer = MissionLib.GetPlayer()
			shouldIOofplayer = 1
			playerVibeChecker = 0

			global ticksPerKilometer
			kIter = pProx.GetNearObjects(pShip.GetWorldLocation(), iRange * ticksPerKilometer, 1) 
			while 1:
				pObject = pProx.GetNextObject(kIter)
				if not pObject:
					break

				vibechecker = 0
				#if pObject.IsTypeOf(App.CT_SHIP) and not pObject.GetName() == pShip.GetName():
				if not pObject.GetName() == pShip.GetName():
					if pObject.IsTypeOf(App.CT_SHIP):
						#pkShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pObject))
						pkShip = App.ShipClass_Cast(pObject)
						if pkShip:

							#print pkShip

							try: 
								pkShipInst = FoundationTech.dShips[pkShip.GetName()]
								if pkShipInst == None:
									#print "After looking, no instance for ship:", pkShip.GetName(), "How odd..."
									vibechecker = 0
								if pkShipInst.__dict__.has_key("Davros Reality Bomb Immune"):
									vibechecker = 1
							except:
								print "Error, so no instance for attacker:", pkShip.GetName(), "How odd..."
								vibechecker = 0

							if vibechecker == 0:
								global lImmuneShips
								sScript     = pkShip.GetScript()
								sShipScript = string.split(sScript, ".")[-1]
								if sShipScript in lImmuneShips:
									vibechecker = 1

								if sShipScript == "Tardis":
									detonationNegative = 1

							if vibechecker == 0 and pObject.GetName() == pPlayer.GetName():
								playerVibeChecker = 1 # the player is going to die, so we don't trigger things that may cause a crash
								if pInstance.__dict__['Davros Reality Bomb']["Firing"] == 0:
									#vibechecker = 1
									shouldIOofplayer = 0

					if vibechecker == 0:
						lDrain.append(pObject)

			pProx.EndObjectIteration(kIter)
			
			if detonationNegative:
				print "Play detonation Negative"
				self.Detach2(pInstance, pShip) # DoctorDonna disabled our systems!!!
				pSeq3 = App.TGSequence_Create()
				pAction3 = App.TGScriptAction_Create(__name__, "accionDetonationNegative")
				pSeq3.AddAction(pAction3, None, 0)
				pSeq3.Play()
			else:
				self.dissolveObject(lDrain, pShip, pInstance, pSet, shouldIOofplayer, pPlayer, playerVibeChecker, pProx)
				if goForPlayer == 1:
					self.Detach2(pInstance, pShip) # We no longer use our tech
				if pInstance.__dict__['Davros Reality Bomb']["Firing"] == 0:
					pInstance.__dict__['Davros Reality Bomb']["Firing"] = 1
					print "initiating part of the dusting"
					pSeq2 = App.TGSequence_Create()
					pAction2 = App.TGScriptAction_Create(__name__, "accionTestEffects")
					pSeq2.AddAction(pAction2, None, 0)
					pSeq2.Play()
			return 0
					

		def dissolveObject(self, lDrain, pShip, pInstance, pSet, shouldIOofplayer, pPlayer, playerWillDie, pProxManager):
			debug(__name__ + ", Reality Bomb Counter dissolveObject")
			print "Pre-dissolve complete"
			
			if len(lDrain) == 0:
				return 0

			#TO-DO find a way to remove planets
			#TO-DO remove extra sun flares and things
			for aObject in pSet.GetClassObjectList(App.CT_TORPEDO):
				try:
					DestroyEverything(aObject, 1, pSet)
				except:
					print "a CT_TORPEDO survived"

			for aObject in pSet.GetClassObjectList(App.CT_BACKDROP_SPHERE):
				try:
					DestroyEverything(aObject, 1, pSet)
				except:
					print "a BACK. SPHERE survived"

			for aObject in pSet.GetClassObjectList(App.CT_ASTEROID_TILE):
				try:
					DestroyEverything(aObject, 1, pSet)
				except:
					print "a CT_ASTEROID_TILE survived"

			for aObject in pSet.GetClassObjectList(App.CT_ASTEROID_FIELD):
					try:
						DestroyEverything(aObject, 1, pSet)
					except:
						print "a CT_ASTEROID_FIELD survived"

			for aObject in pSet.GetClassObjectList(App.CT_STAR_SPHERE):
				try:
					DestroyEverything(aObject, 1, pSet)
				except:
					print "a CT_STAR_SPHERE survived"

			for aObject in pSet.GetClassObjectList(App.CT_META_NEBULA):
				try:
					DestroyEverything(aObject, 1, pSet)
				except:
					print "a CT_META_NEBULA survived"

			for aObject in pSet.GetClassObjectList(App.CT_NEBULA):
				try:
					DestroyEverything(aObject, 1, pSet)
				except:
					print "a CT_NEBULA survived"

			for aObject in pSet.GetClassObjectList(App.CT_BACKDROP):
				try:
					DestroyEverything(aObject, 1, pSet)
				except:
					print "a BACKDROP survived"

			for aObject in pSet.GetClassObjectList(App.CT_SUN):
				try:
					DestroyEverything2(aObject, 1, pSet, pProxManager)
				except:
					print "a SUN survived"

			for aObject in pSet.GetClassObjectList(App.CT_WAYPOINT):
				try:
					DestroyEverything(aObject, 1, pSet)
				except:
					print "a WAYPOINT survived"
					traceback.print_exc()

			for aObject in pSet.GetClassObjectList(App.CT_LIGHT_PLACEMENT):
				try:
					DestroyEverything(aObject, 1, pSet)
				except:
					print "a LIGHT PLACEMENT survived"
					traceback.print_exc()

			for aObject in pSet.GetClassObjectList(App.CT_PLANET):
				try:
					DestroyEverything2(aObject, 1, pSet, pProxManager)
				except:
					print "a PLANET survived"
					traceback.print_exc()

			#if not playerWillDie: # Planets dying at the same time as players generates a weird issue

			#	for aObject in pSet.GetClassObjectList(App.CT_PLANET):
			#		try:
			#			DestroyEverything(aObject, 1, pSet)
			#		except:
			#			print "a PLANET survived"

			for kObject in lDrain:
				if kObject is not None:
					try:
						myNami = kObject.GetName()
						try:
							myNami = kObject.GetName() + " Atom field"
						except:
							myNami = str(kObject) + " Atom field"
						pFirepoint = loadspacehelper.CreateShip(sFirepointScript, pSet, myNami, None)
						pFirepoint.SetTargetable(0)
						pFirepoint.SetTranslate(kObject.GetWorldLocation())
						pPower = pFirepoint.GetPowerSubsystem().GetProperty()

						if kObject.IsTypeOf(App.CT_TORPEDO):
							pPower.SetPowerOutput(0.0001*fFPPowerOutMult)
						else:
							pPower.SetPowerOutput(kObject.GetRadius()*fFPPowerOutMult)

						if kObject and kObject.IsTypeOf(App.CT_TORPEDO):
							pkTorp = App.Torpedo_Cast(kObject)
							pkTorp.SetTarget(pFirepoint.GetObjID())
						pFirepoint.DestroySystem(pFirepoint.GetHull())
						
					except:
						print "Some error with effects"
						traceback.print_exc()

					notShip = 1
					if kObject.IsTypeOf(App.CT_SHIP):
						#disable all firing subsystems?
						pkShip = App.ShipClass_Cast(kObject)
						if pkShip:
							notShip = 0
							if not pkShip.IsDead() and not pkShip.IsDying():
								pWeaponSystem1 = pkShip.GetPhaserSystem()
								pWeaponSystem2 = pkShip.GetPulseWeaponSystem()
								pWeaponSystem3 = pkShip.GetTorpedoSystem()
								pWeaponSystem4 = pkShip.GetTractorBeamSystem()
								if pWeaponSystem1:
									pSubSystemProp=pWeaponSystem1.GetProperty()
									pSubSystemProp.SetDisabledPercentage(3.14)
								if pWeaponSystem2:
									pSubSystemProp=pWeaponSystem2.GetProperty()
									pSubSystemProp.SetDisabledPercentage(3.14)
								if pWeaponSystem3:
									pSubSystemProp=pWeaponSystem3.GetProperty()
									pSubSystemProp.SetDisabledPercentage(3.14)
								if pWeaponSystem4:
									pSubSystemProp=pWeaponSystem4.GetProperty()
									pSubSystemProp.SetDisabledPercentage(3.14)
								#pSeq = App.TGSequence_Create()
								#pSeq.AppendAction(App.TGScriptAction_Create(__name__, "KillAShip", pSet, pkShip))
								#pAction = App.TGScriptAction_Create(__name__, "accionDummy")
								#pSeq.AddAction(pAction, None, 0)
								#pSeq.Play()
								if kObject.GetName() != pPlayer.GetName() or shouldIOofplayer == 1:
									pkShip.RunDeathScript()
								#pkShip.RunDeathScript()
					
					if not notShip:
						DestroyEverything(kObject, notShip, pSet)

			return 0


	def PlaceAsteroidField(pAction, pSet, sName, fRadius, kLocation):
		debug(__name__ + ", Reality Bomb PlaceAsteroidField")

		global 	fSetNumTilesPerAxisRadiusDiv, iSetNumAsteroidsPerTile, fRoidSizeFactor

		kThis = App.AsteroidFieldPlacement_Create(sName + " Dust field", pSet.GetName(), None)
		kThis.SetStatic(0)
		kThis.SetNavPoint(0)
		kThis.SetTranslate(kLocation)
		kThis.SetFieldRadius(fRadius)
		kThis.SetNumTilesPerAxis(fRadius/fSetNumTilesPerAxisRadiusDiv)
		kThis.SetNumAsteroidsPerTile(iSetNumAsteroidsPerTile)
		kThis.SetAsteroidSizeFactor(fRoidSizeFactor)
		kThis.UpdateNodeOnly()
		kThis.ConfigField()
		kThis.Update(0)
		return 0	

	def DestroyEverything(pObject, notShip, pSet):
		debug(__name__ + ", Reality Bomb Counter DestroyEverything")

		if not pObject:
			return

		#if not pSet:
		#	pSet = pObject.GetContainingSet()
		pSet = pObject.GetContainingSet()

		if not pSet:
			return

		nombre = pObject.GetName()
		radio = pObject.GetRadius()
		location = pObject.GetWorldLocation()
		if notShip:
			#pObject.Destroy()
			if pObject.IsTypeOf(App.CT_TORPEDO):
				pkTorp = App.Torpedo_Cast(pObject)
				if pkTorp:
					pkTorp.SetLifetime(0.0)
			pSet.RemoveObjectFromSet(nombre)

		#if notShip:
		#	#pObject.Destroy()
		#	if pObject.IsTypeOf(App.CT_TORPEDO):
		#		pkTorp = App.Torpedo_Cast(pObject)
		#		if pkTorp:
		#			pkTorp.SetLifetime(0.0)
		#	#pSet.RemoveObjectFromSet(nombre)
		#	try:
		#		pSeq = App.TGSequence_Create()
		#		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RemoveObjectDelayed", pSet, pObject), fRemovePlanetDelay)
		#		pAction = App.TGScriptAction_Create(__name__, "accionDummy")
		#		pSeq.AddAction(pAction, None, 0)
		#		pSeq.Play()
		#	except:
		#		"Error with nonship DestroyEverything"
		#else:
		#	try:
		#		pSeq = App.TGSequence_Create()
		#		pAction = App.TGScriptAction_Create(__name__, "accionDummy")
		#		pSeq.AddAction(pAction, None, 0)
		#		pSeq.Play()
		#	except:
		#		"Error with ship DestroyEverything"

	def DestroyEverything2(pObject, notShip, pSet, pProxManager):
		debug(__name__ + ", Reality Bomb Counter DestroyEverything2")

		if not pObject:
			return

		if not pSet:
			pSet = pObject.GetContainingSet()

		if not pSet:
			return

		nombre = pObject.GetName()
		radio = pObject.GetRadius()
		location = pObject.GetWorldLocation()
		if notShip:
			if pObject.IsTypeOf(App.CT_TORPEDO):
				pkTorp = App.Torpedo_Cast(pObject)
				if pkTorp:
					pkTorp.SetLifetime(0.0)
			
			global pAllObjectsSpecialThatNeedToBeRestored

			if not pAllObjectsSpecialThatNeedToBeRestored.has_key(repr(pSet)):
				pAllObjectsSpecialThatNeedToBeRestored[repr(pSet)] = []

			pAllObjectsSpecialThatNeedToBeRestored[repr(pSet)].append(nombre)

			# Since the game crashes if you delete a planet/Try to remove it from collisions once the player leaves the system or tries to... we'll have to keep us content with hiding it and sending it to the next universe
			# Thanks for this tip, USS Sovereign, even if the removing the planet from the proximity manager part didn't work!
			pPlayer = MissionLib.GetPlayer()
			
			if pPlayer:
				playerTarget = pPlayer.GetTarget()
				if playerTarget and not playerTarget.IsTypeOf(App.CT_SHIP):
					MissionLib.ClearTarget()

			DeleteMenuButton("Helm", nombre, "Orbit Planet")

			pObject.SetHidden(1)
			pObject.SetScannable(0)
			pObject.SetTranslateXYZ(9999999.0, 9999999.0, 9999999.0)# apparently (999999999999999.0, 999999999999999.0, 999999999999999.0) is too much

			pObject.UpdateNodeOnly()

			# Delete the ship.
			#pDeletionEvent = App.TGEvent_Create()
			#pDeletionEvent.SetEventType(App.ET_DELETE_OBJECT_PUBLIC)
			#pDeletionEvent.SetDestination(pObject)
			#App.g_kEventManager.AddEvent(pDeletionEvent)

			#pProxManager.RemoveObject(pObject)

			#pSet.RemoveObjectFromSet(nombre)
			#pDeepSpaceSet	= App.g_kSetManager.GetSet("DeepSpace")
			#pDeepSpaceSet.AddObjectToSet(pObject, nombre)

			pSeq = App.TGSequence_Create()
			pSeq.AppendAction(App.TGScriptAction_Create(__name__, "PlaceAsteroidField", pSet, nombre, radio, location))
			pSeq.Play()
		

	def KillAShip(pAction, pSet, pkShip):
		debug(__name__ + ", Reality Bomb Counter KillAShip")
		pkShip.RunDeathScript()
		return 0

	def RemoveObjectDelayed(pAction, pSet, pObject):
		debug(__name__ + ", Reality Bomb Counter RemoveObjectDelayed")
		pSet.RemoveObjectFromSet(pObject.GetName())
		return 0

	def accionDummy(self):
		debug(__name__ + ", Reality Bomb Counter accionDummy")
		pEnterSound = App.TGSound_Create("sfx/Weapons/vanishToDust.wav", "Enter", 0)
		pEnterSound.SetSFX(0) 
		pEnterSound.SetInterface(1)

		App.g_kSoundManager.PlaySound("Enter")
		return 0

	def accionFirstCountdown(self):
		debug(__name__ + ", Reality Bomb Counter accionFirstCountdown")
		pEnterSound = App.TGSound_Create("sfx/Weapons/TestCountdown.wav", "Enter", 0)
		pEnterSound.SetSFX(0) 
		pEnterSound.SetInterface(1)

		App.g_kSoundManager.PlaySound("Enter")
		return 0

	def accionTestEffects(self):
		debug(__name__ + ", Reality Bomb Counter accionTestEffects")
		pEnterSound = App.TGSound_Create("sfx/Weapons/TestCompleted.wav", "Enter", 0)
		pEnterSound.SetSFX(0) 
		pEnterSound.SetInterface(1)

		App.g_kSoundManager.PlaySound("Enter")
		return 0

	def accionDetonationNegative(self):
		debug(__name__ + ", Reality Bomb Counter accionDetonationNegative")
		# TO-DO add dust sound as .wav
		pEnterSound = App.TGSound_Create("sfx/Weapons/DoctorDonna.wav", "Enter", 0)
		pEnterSound.SetSFX(0) 
		pEnterSound.SetInterface(1)

		App.g_kSoundManager.PlaySound("Enter")
		return 0

	# Deletes a button. From BCS:TNG's mod
	def DeleteMenuButton(sMenuName, sButtonName, sSubMenuName = None):
		debug(__name__ + ", DeleteMenuButton")
		pMenu   = GetBridgeMenu(sMenuName)
		pButton = pMenu.GetButton(sButtonName)
		if sSubMenuName != None:
			pMenu = pMenu.GetSubmenu(sSubMenuName)
			pButton = pMenu.GetButton(sButtonName)

		pMenu.DeleteChild(pButton)


	# From ATP_GUIUtils:
	def GetBridgeMenu(menuName):
		debug(__name__ + ", GetBridgeMenu")
		pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
		pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
		if(pDatabase is None):
			return
		App.g_kLocalizationManager.Unload(pDatabase)
		return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))

	oDalekRealityBomb = DalekRealityBombDef('Davros Reality Bomb')

	class DalekRealityBombImmuneDef(FoundationTech.TechDef):
		def Attach(self, pInstance):
			pInstance.lTechs.append(self)

	oDalekRealityBombImmuneDef = DalekRealityBombImmuneDef('Davros Reality Bomb Immune') # No ship should be immune to this

except:
	print "Something went wrong wih Davros Reality Bomb technology"
	traceback.print_exc()