from bcdebug import debug
import App
import math
import MissionLib

# Credits for this Mod goes to edtheborg with his FTA 2.0 Mod.
# without him, this would have never existed!


SEND_TORP_CREATE_MSG = 191

def PulseFire(pShip, pTarget, pTargetSubsystem, pSet):
        debug(__name__ + ", PulseFire")
        if pTarget:
                pTargetObjID = pTarget.GetObjID()
        else:
                pTargetObjID = App.NULL_ID
        
        # no dummy fire
        if not pTarget:
                return
        
        if pTargetSubsystem:
                pTargetSubsystemObjID = pTargetSubsystem.GetObjID()
        else:
                pTargetSubsystemObjID = App.NULL_ID

        pPulseSystem = pShip.GetPulseWeaponSystem()
        
        if not pPulseSystem or not pPulseSystem.IsOn():
                return
        
        for pChild in range(pPulseSystem.GetNumChildSubsystems()):
                pLauncher=App.PulseWeapon_Cast(pPulseSystem.GetChildSubsystem(pChild))
                if pTarget and not pLauncher.IsInArc(pTarget.GetWorldLocation()):
                        continue
                if pLauncher.GetChargeLevel() >= pLauncher.GetMinFiringCharge() and not pLauncher.IsDumbFire():
                        pLauncher.SetChargeLevel(pLauncher.GetChargeLevel() - pLauncher.GetNormalDischargeRate())

                        if App.g_kUtopiaModule.IsMultiplayer():
                                # inform other hosts
                                MPSendTorpMessage(pShip.GetName(), pLauncher.GetWorldLocation(), pLauncher.GetProperty().GetModuleName(), pTargetObjID, pTargetSubsystemObjID)
                        FireTorpFromPoint(None, pLauncher.GetWorldLocation(), pLauncher.GetProperty().GetModuleName(), pShip.GetObjID(), pTargetObjID, pTargetSubsystemObjID, 0.0, pSet.GetName())
			
			if pPulseSystem.IsSingleFire():
				break


# from edtheborg's FTA2
def TorpFire(pShip, pTarget, pTargetSubsystem, pSet):
	debug(__name__ + ", TorpFire")
	if (pShip==None or pTarget==None):
		return

	pTorpSystem=pShip.GetTorpedoSystem()
	if (pTorpSystem==None):
		return
        
        if not pTorpSystem.IsOn():
                return
        
	pAmmoType=pTorpSystem.GetCurrentAmmoType()
	if (pAmmoType==None):
		return

	TypeNum=pTorpSystem.GetCurrentAmmoTypeNumber()
	pcTorpScriptName=pAmmoType.GetTorpedoScript()

        if pTarget:
                pTargetObjID = pTarget.GetObjID()
        else:
                pTargetObjID = App.NULL_ID
        
        if pTargetSubsystem:
                pTargetSubsystemObjID = pTargetSubsystem.GetObjID()
        else:
                pTargetSubsystemObjID = App.NULL_ID

	pLauncher=None
	for Child in range(pTorpSystem.GetNumChildSubsystems()):
		pTube=App.TorpedoTube_Cast(pTorpSystem.GetChildSubsystem(Child))
		if (pTube.GetNumReady()>0 and pTube.IsInArc(pTarget.GetWorldLocation()) and pShip.IsCloaked() and pTube.GetConditionPercentage()>pTube.GetDisabledPercentage() and not pTube.IsDumbFire()):
			pLauncher=pTube
	if (pLauncher==None):
		return

        if App.g_kUtopiaModule.IsMultiplayer():
                MPSendTorpMessage(pShip.GetName(), pLauncher.GetWorldLocation(), pcTorpScriptName, pTargetObjID, pTargetSubsystemObjID)
        
        FireTorpFromPoint(None, pLauncher.GetWorldLocation(), pcTorpScriptName, pShip.GetObjID(), pTargetObjID, pTargetSubsystemObjID, 0.0, pSet.GetName())
        pLauncher.UnloadTorpedo()
        pTorpSystem.LoadAmmoType(TypeNum,-1)


# Note: the only difference from the version in MissionLib is that we do set the parent
def FireTorpFromPoint(pAction, kPoint, pcTorpScriptName, FireingId, idTarget = App.NULL_ID, idTargetSubsystem = App.NULL_ID, fSpeed = 0.0, pcSetName = None):
	debug(__name__ + ", FireTorpFromPoint")
	pTarget = App.ObjectClass_GetObjectByID(App.SetClass_GetNull(), idTarget)

	if (pcSetName != None):
		pSet = App.g_kSetManager.GetSet(pcSetName)
	elif (pTarget != None):
		pSet = pTarget.GetContainingSet()
	else:
		# No idea what set this is supposed to be in.
		return 0

	if (pSet == None):
		# No set.
		return 0

	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)

	if (idTargetSubsystem != App.NULL_ID):
		pSubsystem = App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(idTargetSubsystem))
		if (pSubsystem != None):
			pTorp.SetTargetOffset(pSubsystem.GetPosition())
		else:
			pTorp.SetTargetOffset(kPoint)
	else:
		pTorp.SetTargetOffset(kPoint)

	# Set parent for the torpedo so we don't hit ourselves
	pTorp.SetParent(FireingId)

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, None)

	pTorp.UpdateNodeOnly()

	# If there was a target, then orient the torpedo towards it.
	if (pTarget != None):
		kTorpLocation = pTorp.GetWorldLocation()
		kTargetLocation = pTarget.GetWorldLocation()

		kTargetLocation.Subtract(kTorpLocation)
		kFwd = kTargetLocation
		kFwd.Unitize()
		kPerp = kFwd.Perpendicular()
		kPerp2 = App.TGPoint3()
		kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

		pTorp.AlignToVectors(kFwd, kPerp2)
		pTorp.UpdateNodeOnly()

	# Give the torpedo an appropriate speed.
	kVelocity = pTorp.GetWorldForwardTG()
	if (fSpeed == 0.0):
		kVelocity.Scale(pTorp.GetLaunchSpeed())
	else:
		kVelocity.Scale(fSpeed)

	pTorp.SetVelocity(kVelocity)

	# Play the torpedo firing sound
	pcLaunchSound = pTorp.GetLaunchSound()
	if pcLaunchSound != None:
		pSound = App.g_kSoundManager.GetSound(pcLaunchSound)
		if pSound != None:
			pSound.AttachToNode(pTorp.GetNode())

			# Associate this sound with the sound region for the set we're in.
			pSoundRegion = App.TGSoundRegion_GetRegion(pSet.GetName())
			if pSoundRegion != None:
				pSoundRegion.AddSound(pSound)

			pSound.Play()

	return 0


def AIPulseFire(pAIShip):
        #print(pAIShip, "Fireing")

        debug(__name__ + ", AIPulseFire")
        pTarget = pAIShip.GetTarget()
        pTargetSubsystem = pAIShip.GetTargetSubsystem()
        pSet = pAIShip.GetContainingSet()
        
        PulseFire(pAIShip, pTarget, pTargetSubsystem, pSet)


def AITorpFire(pAIShip):
        #print(pAIShip, "Fireing Torp")
        
        debug(__name__ + ", AITorpFire")
        pTarget = pAIShip.GetTarget()
        pTargetSubsystem = pAIShip.GetTargetSubsystem()
        pSet = pAIShip.GetContainingSet()
        
        TorpFire(pAIShip, pTarget, pTargetSubsystem, pSet)


def AIFireTorpAndPulse(pAIShip):
        #print(pAIShip, "Fireing All")
        
        debug(__name__ + ", AIFireTorpAndPulse")
        pTarget = pAIShip.GetTarget()
        pTargetSubsystem = pAIShip.GetTargetSubsystem()
        pSet = pAIShip.GetContainingSet()
        
        PulseFire(pAIShip, pTarget, pTargetSubsystem, pSet)
        TorpFire(pAIShip, pTarget, pTargetSubsystem, pSet)


def MPSendTorpMessage(sShipName, pos, pcTorpScriptName, pTargetObjID, pTargetSubsystemObjID):        
        # Now send a message to everybody else
        # allocate the message.
        debug(__name__ + ", MPSendTorpMessage")
        pMessage = App.TGMessage_Create()
        pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet

        # Setup the stream.
        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
        kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.

        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SEND_TORP_CREATE_MSG))

        # Write the name of fireing ship
        for i in range(len(sShipName)):
                kStream.WriteChar(sShipName[i])
        # set the last char:
        kStream.WriteChar('\0')
                
        # torp script
        for i in range(len(pcTorpScriptName)):
                kStream.WriteChar(pcTorpScriptName[i])
        # set the last char:
        kStream.WriteChar('\0')

        # pos
        kStream.WriteFloat(pos.GetX())
        kStream.WriteFloat(pos.GetY())
        kStream.WriteFloat(pos.GetZ())
        
        # Target information
        kStream.WriteInt(pTargetObjID)
        kStream.WriteInt(pTargetSubsystemObjID)

        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)

        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def ProcessMessageHandler(pObject, pEvent):
        debug(__name__ + ", ProcessMessageHandler")
        pMessage = pEvent.GetMessage()
	if not App.IsNull(pMessage):
                kStream = pMessage.GetBufferStream();
		cType = kStream.ReadChar();
		cType = ord(cType)
                
                if cType == SEND_TORP_CREATE_MSG:
                        # 1. Get fireing ship
                        sMessage = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                sMessage = sMessage + iChar
                        sShipName = sMessage
                        
                        # 2. Get Torp script
                        sMessage = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                sMessage = sMessage + iChar
                        pcTorpScriptName = sMessage
                        
                        # 3. Get position
                        pos = App.TGPoint3()
                        pos.SetX(kStream.ReadFloat())
                        pos.SetY(kStream.ReadFloat())
                        pos.SetZ(kStream.ReadFloat())
                        
                        # 4. Target informations
                        pTargetObjID = kStream.ReadInt()
                        pTargetSubsystemObjID = kStream.ReadInt()
                        
                        # send to clients
                        if App.g_kUtopiaModule.IsHost():
                                MPSendTorpMessage(sShipName, pos, pcTorpScriptName, pTargetObjID, pTargetSubsystemObjID)
                        
                        # create Torp
                        #print("Torp Received: ", sShipName, pcTorpScriptName)
                        MPCreateTorp(sShipName, pos, pcTorpScriptName, pTargetObjID, pTargetSubsystemObjID)
                                
                kStream.Close()


def MPCreateTorp(sShipName, pos, pcTorpScriptName, pTargetObjID, pTargetSubsystemObjID):
        debug(__name__ + ", MPCreateTorp")
        pShip = MissionLib.GetShip(sShipName)
        if pShip:
                pSet = pShip.GetContainingSet()
                #print("Status: ", pShip.GetName(), "fires on", App.ShipClass_GetObjectByID(None, pTargetObjID))
                FireTorpFromPoint(None, pos, pcTorpScriptName, pShip.GetObjID(), pTargetObjID, pTargetSubsystemObjID, 0.0, pSet.GetName())


#
# FireScript
#
# Use this with any AI to have our ship always try to
# fire its weapons at our target (if we have a good shot).
#
class myFireScript:
	# Arguments to the constructor:
	# pOurShip	- The ship object we're controlling
	# sTarget	- The object we're trying to shoot
	def __init__(self, sTarget, **kw):
		debug(__name__ + ", __init__")
		self.sTarget = sTarget

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		self.fMaxFiringRange = 1.0e20
		if kw.has_key("MaxFiringRange"):
			self.fMaxFiringRange = kw["MaxFiringRange"]

		self.bHighPower = 1
		if kw.has_key("HighPower"):
			self.bHighPower = kw["HighPower"]

		self.bChangePowerSetting = 1
		self.bHullSelectedChooseAlternate = 0

		self.lTargetSubsystems = []
		self.bChooseSubsystemTargets = 0
		if kw.has_key("TargetSubsystems"):
			# Target subsystems have been specified explicitly.
			lSubsystems = kw["TargetSubsystems"]
			for eSubsystem, iPriority in lSubsystems:
				self.AddTargetSubsystem(eSubsystem, iPriority)
		elif kw.has_key("ChooseSubsystemTargets")  and  kw["ChooseSubsystemTargets"]:
			self.bChooseSubsystemTargets = 1

		self.bChooseTorpsWisely = 0
		if kw.has_key("SmartTorpSelection")  and  kw["SmartTorpSelection"]:
			self.bChooseTorpsWisely = 1

		self.bSmartPhasers = 0
		if kw.has_key("SmartPhasers")  and  kw["SmartPhasers"]:
			self.bSmartPhasers = 1

		self.lWeapons = []
		self.idTargetedSubsystem = None
		self.iLastUpdate = -1

		self.dTargetSubsystemRating = {}
		self.iTargetSubsystemUpdateNum = 0
		self.iNumTargetSubsystemsToUpdate = 4

		self.bEnabled = 1
		self.bAttackDisabledSubsystems = 1
		self.bAttackIfNoSubsystemsLeft = 1

		self.bCallUsingWeaponTypeFunc = 1

		# Angle of accuracy we need to fire.  We'll
		# go with 10 degrees if we should be accurate, 50 degrees
		# if not.
		if kw.has_key("InaccurateTorps")  and  kw["InaccurateTorps"]:
			# Inaccurate.
			self.fFireDotThreshold = math.cos((50.0) * (App.PI / 180.0))
		else:
			# Accurate.
			self.fFireDotThreshold = math.cos((10.0) * (App.PI / 180.0))

		self.bDumbFireTorps = 0
		if kw.has_key("DumbFireTorps"):
			self.bDumbFireTorps = kw["DumbFireTorps"]

		self.bDisableFirst = 0
		if kw.has_key("DisableBeforeDestroy"):
			self.bDisableFirst = kw["DisableBeforeDestroy"]

		# Check if we're only trying to disable the target, and not
		# destroy it.
		if kw.has_key("DisableOnly"):
			bDisableOnly = kw["DisableOnly"]
			self.SetAttackDisabled(not bDisableOnly)
			self.SetAttackWithoutValidSubsystems(not bDisableOnly)
			if not kw.has_key("HighPower"):
				self.bHighPower = not bDisableOnly

		# Whether or not our target is currently visible to us.		
		self.bTargetVisible = 0

		# Tractor beam mode, if we're firing a tractor beam.
		self.eTractorBeamMode = None
		
		# The radius around the line between us and our target
		# that we consider an object to be obstructing our view.
		self.fObstructionRadius = 0.5

		self.fNextVisibilityCheck = 0

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)


	def CodeAISet(self):
		# Further initialization we can do once our self.pCodeAI
		# member has been set.
		# Register external functions.
		debug(__name__ + ", CodeAISet")
		self.pCodeAI.RegisterExternalFunction("SetTarget",
			{ "Name" : "SetTarget" } )

	# Add the weapon systems that you want
	# to fire.
	def AddWeaponSystem(self, pSystem):
		# If this is a weapon system type we didn't
		# previously have, set a flag to call the
		# "UsingWeaponSystem" external AI function
		# during the next update.
		debug(__name__ + ", AddWeaponSystem")
		bAlreadyThere = 0
		for pExistingSystem in self.lWeapons:
			if pSystem.IsTypeOf( pExistingSystem.GetObjType() ):
				# Already got one of these.
				bAlreadyThere = 1
				break

		if not bAlreadyThere:
			# Not there.  Gotta call the function.
			self.bCallUsingWeaponTypeFunc = 1

		# Add the weapon system to our list.
		self.lWeapons.append(pSystem)

	# Tractor beams are a special case.
	def AddTractorBeam(self, pShip, eTractorBeamMode):
		debug(__name__ + ", AddTractorBeam")
		pTractorBeam = pShip.GetTractorBeamSystem()
		if pTractorBeam:
			self.AddWeaponSystem(pTractorBeam)
			self.eTractorBeamMode = eTractorBeamMode

	def RemoveAllWeaponSystems(self):
		debug(__name__ + ", RemoveAllWeaponSystems")
		self.StopFiring()

		if self.lWeapons:
			self.bCallUsingWeaponTypeFunc = 1

		self.lWeapons = []

	def GetWeapons(self):
		debug(__name__ + ", GetWeapons")
		return self.lWeapons

	# Enable or disable firing from this AI.
	def SetEnabled(self, bEnabled):
		debug(__name__ + ", SetEnabled")
		if self.bEnabled != bEnabled:
			if self.bEnabled:
				self.StopFiring()

			self.bEnabled = bEnabled

	# Whether or not this AI will attack disabled subsystems.
	def SetAttackDisabled(self, bAttack):
		debug(__name__ + ", SetAttackDisabled")
		self.bAttackDisabledSubsystems = bAttack

	# Whether or not this AI continues to attack if it has
	# a list of subsystems to target but none of those
	# subsystems are valid targets anymore.
	def SetAttackWithoutValidSubsystems(self, bAttack):
		debug(__name__ + ", SetAttackWithoutValidSubsystems")
		self.bAttackIfNoSubsystemsLeft = bAttack

	# Add the subsystems we want the ship to target, with
	# a given priority.  Higher priority systems are targeted
	# first.  Once those are no longer worth firing at (eg.
	# destroyed), we target the next priorities.
	# Subsystems are specified by TGObjectType (for example,
	# CT_TORPEDO_SYSTEM).
	def AddTargetSubsystem(self, eSubsystem, iPriority):
		debug(__name__ + ", AddTargetSubsystem")
		iIndex = 0
		while iIndex < len(self.lTargetSubsystems):
			if self.lTargetSubsystems[iIndex][1] < iPriority:
				# Insert it here.
				break
			iIndex = iIndex + 1
		self.lTargetSubsystems.insert(iIndex, (eSubsystem, iPriority))

	def HasSubsystemTargets(self):
		debug(__name__ + ", HasSubsystemTargets")
		return len(self.lTargetSubsystems) > 0

	def IgnoreSubsystemTargets(self):
		debug(__name__ + ", IgnoreSubsystemTargets")
		if self.HasSubsystemTargets():
			self.lIgnoredSubsystemTargets = self.lTargetSubsystems
			self.lTargetSubsystems = []

	def RestoreSubsystemTargets(self):
		debug(__name__ + ", RestoreSubsystemTargets")
		if not self.HasSubsystemTargets():
			try:
				self.lTargetSubsystems = self.lIgnoredSubsystemTargets
				del self.lIgnoredSubsystemTargets
			except AttributeError:
				pass

	# Convenience function, for player AI's.
	def UsePlayerSettings(self, bDisableOnly = 0):
		debug(__name__ + ", UsePlayerSettings")
		self.SetAttackDisabled(not bDisableOnly)
		self.SetAttackWithoutValidSubsystems(not bDisableOnly)
		self.bHighPower = not bDisableOnly
		self.bChangePowerSetting = 0
		self.bHullSelectedChooseAlternate = bDisableOnly

	def SetTarget(self, sName):
		debug(__name__ + ", SetTarget")
		"Change to a new target."
		self.StopFiring()

		self.sTarget = sName
		self.idTargetedSubsystem = None

	def GetTarget(self):
		debug(__name__ + ", GetTarget")
		"Get our target object, if we can."
		pOurShip = self.pCodeAI.GetShip()
		if (pOurShip == None):
			return None

		pSet = pOurShip.GetContainingSet()
		if (pSet == None):
			# We're not in a set.  What do we do?
			return None

		pTarget = App.ObjectClass_GetObject(pSet, self.sTarget)
		if (pTarget == None):
			# Our target is gone.
			return None
		
		return pTarget

	# We're being deactivated.  Stop firing our weapons.
	def LostFocus(self):
		debug(__name__ + ", LostFocus")
		self.StopFiring()
	
	def StopFiring(self):
		debug(__name__ + ", StopFiring")
		pTarget = self.GetTarget()

		if pTarget:
			for pWeaponSystem in self.lWeapons:
				pWeaponSystem.StopFiringAtTarget(pTarget)

	def GetNextUpdateTime(self):
		# We want to be updated every 0.2 seconds
		debug(__name__ + ", GetNextUpdateTime")
		return 0.2

	# Our update function.
	def Update(self, dEndTime):
		debug(__name__ + ", Update")
		pTarget = self.GetTarget()
		if not pTarget:
			return App.PreprocessingAI.PS_DONE

		# If we're supposed to call the UsingWeaponType external
		# AI function, do that...
		if self.bCallUsingWeaponTypeFunc:
			for pAI in self.pCodeAI.GetAllAIsInTree()[1:]:
				pAI.CallExternalFunction("UsingWeaponType", self.lWeapons)
			self.bCallUsingWeaponTypeFunc = 0

		if len(self.lWeapons) == 0:
			# No weapons to fire, but we're normal...
			return App.PreprocessingAI.PS_NORMAL

		if not self.bEnabled:
			# Firing has been temporarily disabled.
			return App.PreprocessingAI.PS_NORMAL

		# If we can't see our target, just keep checking until we can, and
		# don't do anything else in here.  Or if iLastUpdate is -2, check
		# TargetVisible.
		# If iLastUpdate is -1, we're choosing a subsystem to target.
		# If iLastUpdate is >= 0, we're firing one of the weapon systems.
		if (not self.bTargetVisible)  or  (self.iLastUpdate == -2)  or  (not self.TargetInRange(pTarget)):
			self.TargetVisible(pTarget)
			# If the target isn't visible, make sure iLastUpdate stays at -2.
			if not self.bTargetVisible:
				# Make sure we're not firing.
				self.StopFiring()

				self.iLastUpdate = -2
				return App.PreprocessingAI.PS_NORMAL
		elif self.iLastUpdate == -1:
			# Choose a subsystem to target.  This will save the ID of the
			# subsystem for the next update.
			idTiming = App.TGProfilingInfo_StartTiming("FireScript Update->ChooseTargetSubsystem")
			self.ChooseTargetSubsystem(pTarget)
			App.TGProfilingInfo_StopTiming(idTiming)
		else:
			# It's a weapon firing frame.  Get the subsystem we're supposed to be firing at...
			# Subsystem we're targeting is the same as last frame.
			pSubsystem = None
			if self.idTargetedSubsystem is not None:
				pSubsystem = App.ShipSubsystem_Cast( App.TGObject_GetTGObjectPtr( self.idTargetedSubsystem ) )

			# Based on the subsystem we're targeting, determine whether we should fire at all or not.
			if (pSubsystem is None)  and  (not self.bAttackIfNoSubsystemsLeft):
				# We have a list of target subsystems, but none of the
				# subsystems are valid targets.  And we're not supposed
				# to fire if we don't have a valid target subsystem.
				self.StopFiring()
				return App.PreprocessingAI.PS_NORMAL

			# Fire the weapon system we're supposed to fire this update.
			self.FireSystemAtTarget(self.lWeapons[ self.iLastUpdate % len(self.lWeapons) ], pTarget, pSubsystem)

		# Cycle the iLastUpdate counter..
		self.iLastUpdate = ((self.iLastUpdate + 3) % (len( self.lWeapons ) + 2)) - 2

		return App.PreprocessingAI.PS_NORMAL

	def TargetVisible(self, pTarget):
		# For now, skip this check.
		debug(__name__ + ", TargetVisible")
		self.bTargetVisible = 1
		return self.bTargetVisible

		# Check if we're supposed to wait before doing
		# another visibility check...
		fCurrentTime = App.g_kUtopiaModule.GetGameTime()
		if fCurrentTime < self.fNextVisibilityCheck:
			# It's not yet time to check.  Return the
			# same result we did last time.
			return self.bTargetVisible

		# Time to do a check.
		pOurShip = self.pCodeAI.GetShip()
		if (pOurShip == None):
			return 0

		pFrom = pOurShip.GetWorldLocation()
		pTo = pTarget.GetWorldLocation()
		
		pSet = pOurShip.GetContainingSet()
		pProxManager = pSet.GetProximityManager()
		if (pProxManager == None):
			# No proximity manager in this set...  we can't test
			# to see if we have a clear line of sight to our target.
			# By default, we'll say our target is not visible.
			return 0

		pIterator = pProxManager.GetLineIntersectObjects(pFrom, pTo, self.fObstructionRadius)

		iOccludingObjects = 0
		while 1:
			pObject = pProxManager.GetNextObject(pIterator)
			if (pObject == None):
				# We're done.
				break
			
			# There's an object along the line.  If it's
			# us or our target, we don't care.  Otherwise,
			# increment the Occluding Objects count.
			if pObject.GetObjID() != pOurShip.GetObjID() and pObject.GetObjID() != pTarget.GetObjID():
				# It's not one of our two objects.  It must
				# be something else, occluding the two.

				# If it's a weapon projectile, ignore it.
				bOccludes = 1
				for eType in ( App.CT_TORPEDO ):
					if pObject.IsTypeOf(eType):
						bOccludes = 0
				if not bOccludes:
					continue

				iOccludingObjects = iOccludingObjects + 1

				# We only need to check for the existence of
				# an occluding object, not the number of them.
				# We're done...
				break

		pProxManager.EndObjectIteration(pIterator)
		
		if iOccludingObjects:
			# No, our target isn't visible.
			self.bTargetVisible = 0
		else:
			self.bTargetVisible = 1

		fAddTime = ((App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0)
		self.fNextVisibilityCheck = fCurrentTime + fAddTime
		
		return self.bTargetVisible

	def TargetInRange(self, pTarget):
		debug(__name__ + ", TargetInRange")
		pShip = self.pCodeAI.GetShip()
		if pShip:
			vDiff = pTarget.GetWorldLocation()
			vDiff.Subtract(pShip.GetWorldLocation())
			fSqrLength = vDiff.SqrLength()
			if fSqrLength <= (self.fMaxFiringRange * self.fMaxFiringRange):
				return 1
		return 0

	def FireSystemAtTarget(self, pWeaponSystem, pTarget, pSubsystem):
                #print("Preprocessing I should fire now")
		# Make sure this system is configured correctly for
		# its attack on this target.
		debug(__name__ + ", FireSystemAtTarget")
		if not self.ConfigureWeaponSystem(pWeaponSystem, pTarget, pSubsystem):
			# Some sort of problem configuring it.  This system isn't
			# ready to fire right now.
			return

		# Check if we have a good shot.  If so, we
		# should start firing this weapon system.
		if self.CheckGoodShot(pWeaponSystem, pTarget, pSubsystem):
			# We have a good shot.
			# Fire.  If we're already firing, this just updates the
			# targeted subsystem.
			vSubsystemOffset = App.TGPoint3()

			# If this is a torp system, only specify a target if
			# we're not dumb-firing.
			if self.bDumbFireTorps  and  App.TorpedoSystem_Cast(pWeaponSystem):
				if pSubsystem:
					vToTarget = pSubsystem.GetWorldLocation()
				else:
					vToTarget = pTarget.GetWorldLocation()
				vToTarget.Subtract(pWeaponSystem.GetWorldLocation())
				# Make sure we only fire torpedo tubes that are facing the
				# correct direction (dumb firing will fire any torp tube, not
				# just ones pointed toward a target).
				for iChild in range(pWeaponSystem.GetNumChildSubsystems()):
					pTube = App.TorpedoTube_Cast( pWeaponSystem.GetChildSubsystem(iChild) )
					if vToTarget.Dot( pTube.CalculateRoughDirection() ) > 0:
						# It's within 90 degrees of the correct direction.  Fire it.
                                                #print("Preprocessing Fire Torp")
                                                if self.pCodeAI.GetShip().IsCloaked():
                                                        pSet = self.pCodeAI.GetShip().GetContainingSet()
                                                        TorpFire(self.pCodeAI.GetShip(), pTarget, pSubsystem, pSet)
                                                else:
						        pTube.FireDumb(0, 1)
			else:
				if pSubsystem:
					vSubsystemOffset.Set( pSubsystem.GetPositionTG() )
				else:
					vSubsystemOffset.SetXYZ(0, 0, 0)

                                #print("Preprocessing AI Fires Weapons")
                                if self.pCodeAI.GetShip().IsCloaked():
                                        pSet = self.pCodeAI.GetShip().GetContainingSet()
                                        PulseFire(self.pCodeAI.GetShip(), pTarget, pSubsystem, pSet)
                                        TorpFire(self.pCodeAI.GetShip(), pTarget, pSubsystem, pSet)
                                else:
				        pWeaponSystem.StartFiring(pTarget, vSubsystemOffset)
				
		else:
			# We don't have a good shot.  We should stop firing
			# this system.
			pWeaponSystem.StopFiringAtTarget(pTarget)

	def ConfigureWeaponSystem(self, pWeaponSystem, pTarget, pSubsystem):
		# If this weapon system will do too much damage, and we're just
		# trying to disable subsystems, don't fire this weapon.
		debug(__name__ + ", ConfigureWeaponSystem")
		if self.WeaponTooDangerous(pWeaponSystem, pTarget, pSubsystem):
			return 0

		# If this system is a tractor beam, make sure its
		# tractor beam mode is set appropriately.
		pTractor = App.TractorBeamSystem_Cast(pWeaponSystem)
		if pTractor:
			if (self.eTractorBeamMode is not None)  and  (pTractor.GetMode() != self.eTractorBeamMode):
				# Set the mode..  -The only exception to
				# this is if our mode is Docking Stage 1,
				# the tractor beam is firing, and the
				# tractor beam is in Docking Stage 2.
				if not (pTractor.IsFiring()  and  pTractor.GetMode() == App.TractorBeamSystem.TBS_DOCK_STAGE_2 and self.eTractorBeamMode == App.TractorBeamSystem.TBS_DOCK_STAGE_1):
					pTractor.SetMode(self.eTractorBeamMode)
			# Tractor beam has been configured.
			return 1

		# If it's a phaser system, make sure its power level
		# is set appropriately.
		pPhaserSystem = App.PhaserSystem_Cast(pWeaponSystem)
		if pPhaserSystem:
			if not self.bHighPower:
				# Always use low power:
				pPhaserSystem.SetPowerLevel(App.PhaserSystem.PP_LOW)
			else:
				# Conditions are good.  High power.
				pPhaserSystem.SetPowerLevel(App.PhaserSystem.PP_HIGH)
			# Phaser system has been configured.
			return 1

		# If it's a torpedo system, make sure its torp type is
		# set correctly.
		pTorpSystem = App.TorpedoSystem_Cast(pWeaponSystem)
		if pTorpSystem:
			if self.bChooseTorpsWisely:
				# You have chosen to choose wisely.
				# Pick a torp type based on whether torps are already loaded,
				# distance to the target, and overall favorability of the
				# various torpedo types available.
				if pSubsystem:
					vTargetLocation = pSubsystem.GetWorldLocation()
				else:
					vTargetLocation = pTarget.GetWorldLocation()

				fSpeed = 0.0
				pShipTarget = App.ShipClass_Cast(pTarget)
				if pShipTarget:
					pImpulseEngines = pShipTarget.GetImpulseEngineSubsystem()
					if pImpulseEngines:
						fSpeed = pImpulseEngines.GetCurMaxSpeed()

				self.ChooseTorpType(pTorpSystem, vTargetLocation, fSpeed)

			# Torp system has been configured
			return 1

		# No special configuration.  It's ready.
		return 1

	def ChooseTorpType(self, pTorpSystem, vTargetLocation, fTargetSpeed):
		# Get the torp types that have ammo left...
		debug(__name__ + ", ChooseTorpType")
		lTorpTypes = []
		for iType in range( pTorpSystem.GetNumAmmoTypes() ):
			if pTorpSystem.GetNumAvailableTorpsToType(iType) > 0:
				# This type has ammo available.
				lTorpTypes.append( (iType, pTorpSystem.GetAmmoType(iType)) )

		if len(lTorpTypes) == 0:
			return
		if len(lTorpTypes) == 1:
			# Only one choice available.  Make sure this type
			# is selected.
			if pTorpSystem.GetAmmoTypeNumber() != lTorpTypes[0][0]:
				# It's a different one.  Switch to the available one.
				pTorpSystem.SetAmmoType(lTorpTypes[0][0])
			return

		# Find the range to the target.
		vDiff = pTorpSystem.GetWorldLocation()
		vDiff.Subtract(vTargetLocation)
		fDistance = vDiff.Length()

		# Rate the various torpedo types available to us
		# based on range and on target speed...
		# ***FIXME: These calculations only need to be done once.
		lTorpAmmoRatings = []
		for iAmmoIndex, pAmmo in lTorpTypes:
			# Grab information about this ammo type.
			fLaunchSpeed = pAmmo.GetLaunchSpeed()
			fPowerCost = pAmmo.GetPowerCost()

			try:
				pScript = __import__(pAmmo.GetTorpedoScript())
				fTorpDamage = pScript.GetDamage()
				fGuidanceLifetime = pScript.GetGuidanceLifetime()
				fTurnRate = pScript.GetMaxAngularAccel()
			except:
				fTorpDamage = 0.0
				fGuidanceLifetime = 0.0
				fTurnRate = pScript.GetMaxAngularAccel()

			# From this information, try to determine what its ideal
			# distance is...
			fIdealDistMin = 0.0
			fIdealDistMax = 0.0
			if fGuidanceLifetime > 0:
				fIdealDistMax = fGuidanceLifetime * fLaunchSpeed

			# And what the ideal speed of its target is (this ends
			# up just being a rating of how likely it is to hit a
			# fast-moving target).
			fIdealTargetSpeedMin = 0.0
			fIdealTargetSpeedMax = 0.0
			if (fGuidanceLifetime > 0)  or  (fLaunchSpeed > 0):
				# It's slightly guided or it moves a little.  Max speed
				# rating is based on turn rate and launch speed.
				fIdealTargetSpeedMax = (fTurnRate * 4.0) + fLaunchSpeed

			# And what its overall rating is at its ideals...
			fRating = fTorpDamage - fPowerCost

			#debug("Rating ammo type %s(%d).  Dists(%f,%f), Speed(%f,%f), Ideal %f" % (
			#	pAmmo.GetAmmoName(), iAmmoIndex,
			#	fIdealDistMin, fIdealDistMax,
			#	fIdealTargetSpeedMin, fIdealTargetSpeedMax,
			#	fRating))
			lTorpAmmoRatings.append(
				( iAmmoIndex, fIdealDistMin, fIdealDistMax, fIdealTargetSpeedMin, fIdealTargetSpeedMax, fRating ))

		# Find the torp type with the best rating for our current situation.
		fBestScore = -1.0e20
		iChosenAmmo = 0
		for iAmmo, fMinDist, fMaxDist, fMinSpeed, fMaxSpeed, fRating in lTorpAmmoRatings:
			if fMinDist > 0:
				fUnderMin, fLowIdeal, fHighIdeal, fFar = App.FuzzyLogic_BreakIntoSets(fDistance, ( 0.0, fMinDist, fMaxDist, (fMaxDist - fMinDist) * 1.5 ))
			else:
				fLowIdeal, fHighIdeal, fFar = App.FuzzyLogic_BreakIntoSets(fDistance, ( fMinDist, fMaxDist, fMaxDist * 1.5 ))

			# Rate the distance score...
			fDistScore = fRating * (fLowIdeal + fHighIdeal)

			if fMinSpeed > 0:
				fUnderMin, fLowIdeal, fHighIdeal, fFar = App.FuzzyLogic_BreakIntoSets(fTargetSpeed, ( 0.0, fMinSpeed, fMaxSpeed, (fMaxSpeed - fMinSpeed) * 1.5 ))
			else:
				#App.Breakpoint()
				fLowIdeal, fHighIdeal, fFar = App.FuzzyLogic_BreakIntoSets(fTargetSpeed, ( fMinSpeed, fMaxSpeed, fMaxSpeed * 1.5 ))

			# Rate the speed score...
			fSpeedScore = fRating * (fLowIdeal + fHighIdeal)

			# Overall score of this torp type:
			fScore = (0.25 * fDistScore) + fSpeedScore

			#debug("Ammo type %d from (d%f, s%f) gets a score of (d%f, s%f):%f" % (
			#	iAmmo,
			#	fDistance, fTargetSpeed,
			#	fDistScore, fSpeedScore,
			#	fScore))

			if fScore > fBestScore:
				iChosenAmmo = iAmmo
				fBestScore = fScore

		# Switch to the new ammo type, if it's not the current one.
		if pTorpSystem.GetAmmoTypeNumber() != iChosenAmmo:
			#debug("Switching to ammo type %d" % iChosenAmmo)
			pTorpSystem.SetAmmoType(iChosenAmmo)

	def CheckGoodShot(self, pWeaponSystem, pTarget, pSubsystem):
		# Check if this is a weapon system that needs to be aimed...
		debug(__name__ + ", CheckGoodShot")
		if not pWeaponSystem.ShouldBeAimed():
			# Nope.  It can be fired from any direction.  We
			# have a good shot anytime.
			return 1
		
		# Get our ship...
		pOurShip = self.pCodeAI.GetShip()
		if (pOurShip == None):
			return 1

		# This system needs to be aimed.  Check which direction
		# it's facing (if applicable), and see if it's good enough
		# to hit our target.
		# Alas, there is no easy way to get the facing if this weapon
		# system, because not all weapon systems have this information.
		# Figure out what kind of weapon system it is and get the info
		# we need...
		lDirections, fSpeed = self.GetWeaponInfo(pWeaponSystem)

		if len(lDirections):
			# Predict the location of our target.
			vTargetLocation = self.PredictTargetLocation(pTarget, pSubsystem, fSpeed)

			# Move the target location into our model space...
			vTargetLocation.Subtract( pOurShip.GetWorldLocation() )
			vTargetLocation.MultMatrixLeft( pOurShip.GetWorldRotation().Transpose() )
			fTargetDistance = vTargetLocation.Unitize()

			for vDirection in lDirections:
				# What's the angle between this direction
				# and the predicted target position.
				fDot = vTargetLocation.Dot( vDirection )

				# If the angle is within our angle threshold,
				# we have a good shot.
				if fDot >= self.fFireDotThreshold:
					return 1
			
			# No good shot.
			return 0

		# No direction information.  Might as well shoot.
#		debug("Aimed weapon system has no direction info.")
		return 1

	def WeaponTooDangerous(self, pWeaponSystem, pTarget, pSubsystem):
		# This is only relevant if we're just trying to disable systems.
		debug(__name__ + ", WeaponTooDangerous")
		if self.bAttackDisabledSubsystems:
			# We'll attack even the disabled subsystems.  Nothing's
			# too dangerous.
			return 0

		# So far this is only a problem with torpedo systems.  Check
		# if this is a torp system.
		pTorpSystem = App.TorpedoSystem_Cast(pWeaponSystem)
		if pTorpSystem:
			# Check if there are other torps in the air right now.
			pSet = pTarget.GetContainingSet()
			idTarget = pTarget.GetObjID()
			if pSet:
				fIncomingDamage = 0.0
				lTorps = pSet.GetClassObjectList(App.CT_TORPEDO)
				for pTorp in lTorps:
					if pTorp.GetTargetID() == idTarget:
						fIncomingDamage = fIncomingDamage + pTorp.GetDamage()

				# Add the damage from one of our torps, so we know
				# what the damage will be if we choose to fire.
				fTorpDamage = 0.0
				pAmmoType = pTorpSystem.GetCurrentAmmoType()
				pScript = __import__(pAmmoType.GetTorpedoScript())
				if pScript:
					fTorpDamage = pScript.GetDamage()
					#debug("Got torp damage %f" % fTorpDamage)
				fIncomingDamage = fIncomingDamage + fTorpDamage
				fResultingCondition = pSubsystem.GetCondition() - fIncomingDamage

				if (fResultingCondition / pSubsystem.GetMaxCondition()) < pSubsystem.GetDisabledPercentage():
					# There's already enough stuff incoming to disable the
					# system.  Or it's within 1 torp of being disabled, in which
					# case we'll just hold our fire anyways, and let another weapon
					# system do the job.
					return 1

		return 0

	def PredictTargetLocation(self, pTarget, pSubsystem, fSpeed):
		# Find how far we are to our target.
		debug(__name__ + ", PredictTargetLocation")
		vDiff = pTarget.GetWorldLocation()
		pOurShip = self.pCodeAI.GetShip()
		if (pOurShip == None):
			return vDiff

		vDiff.Subtract( pOurShip.GetWorldLocation() )
		fDistance = vDiff.Unitize()
		
		# Get a rough estimate of how long it'll take our weapon
		# to hit the target.
		fTime = fDistance / fSpeed
		
		# Predict the target's position in that amount of time.
		vPredicted = pTarget.GetWorldLocation()
		pPhysicsTarget = App.PhysicsObjectClass_Cast(pTarget)
		if (pPhysicsTarget != None):
			vPredicted.Set(pPhysicsTarget.GetPredictedPosition( pTarget.GetWorldLocation(), pPhysicsTarget.GetVelocityTG(), pPhysicsTarget.GetAccelerationTG(), fTime ))

		# Now find the subsystem's predicted position...
		if pSubsystem:
			vSubsystemPos = pSubsystem.GetPositionTG()
			vSubsystemPos.MultMatrixLeft( pTarget.GetWorldRotation() )
			vPredicted.Add(vSubsystemPos)
		
		return vPredicted

	def GetWeaponInfo(self, pWeaponSystem):
		debug(__name__ + ", GetWeaponInfo")
		lDirections = []
		fSpeed = 1.0
		
		# Figure out which kind of weapon system it is.
		pTorp = App.TorpedoSystem_Cast(pWeaponSystem)
		if (pTorp != None):
			for iWeapNum in range( pTorp.GetNumChildSubsystems() ):
				pWeapon = App.TorpedoTube_Cast( pTorp.GetChildSubsystem(iWeapNum) )
				lDirections.append( pWeapon.GetDirection() )
			fSpeed = pTorp.GetCurrentAmmoType().GetLaunchSpeed()
		else:
			# Check to see if it's a pulse weapon.
			pPulseSystem = App.PulseWeaponSystem_Cast(pWeaponSystem)

			if (pPulseSystem != None):
				for iWeapNum in range(pPulseSystem.GetNumChildSubsystems()):
					pWeapon = App.PulseWeapon_Cast(pPulseSystem.GetChildSubsystem(iWeapNum))
					if (pWeapon != None):
						lDirections.append(pWeapon.GetProperty().GetOrientationForward())
						if (pWeapon.GetLaunchSpeed() > fSpeed):
							fSpeed = pWeapon.GetLaunchSpeed()
		
		# Ummm...   If it's not one of the above systems,
		# we have no idea what it is.  Somebody added a weapon
		# system.  -And because this code is inflexible (because
		# there's no other way to get the info we need), it can't
		# get the information we need.

		return (lDirections, fSpeed)
	
	def ChooseTargetSubsystem(self, pTarget):
		debug(__name__ + ", ChooseTargetSubsystem")
		pShipTarget = App.ShipClass_Cast(pTarget)
		if not pShipTarget:
			return None

		pOurShip = self.pCodeAI.GetShip()
		if not pOurShip:
			return None

		pTargetSubsystem = None
		if len(self.lTargetSubsystems):
			iCurrentPriority = self.lTargetSubsystems[0][1]
			lpPossibleTargets = []
			iNumDisabled = 0
			
			# Find the best priority level that still
			# has systems we can target, and get all the
			# subsystems at that priority level.
			for eSystemType, iPriority in self.lTargetSubsystems:
				if len(lpPossibleTargets) and iPriority > iCurrentPriority:
					# This subsystem is too low on the priority list.
					# Keep building the list only if we're supposed to
					# disable all systems before destroying any, and
					# all the systems in the list are disabled.
					if (not self.bDisableFirst)  or  (iNumDisabled < len(lpPossibleTargets)):
						# We can stop.
						break

				iCurrentPriority = iPriority
				pIter = pShipTarget.StartGetSubsystemMatch(eSystemType)
				pSubsystem = pShipTarget.GetNextSubsystemMatch(pIter)
				while pSubsystem:
					if pSubsystem.GetCondition() > 0:
						# We can still destroy this system.
						# If it's disabled, should we still target it?
						if self.bAttackDisabledSubsystems or (not pSubsystem.IsDisabled()):
							# Can this subsystem actually be hit?  LOS
							# check to subsystem...
							#if pSubsystem.IsHittableFromLocation(pOurShip.GetWorldLocation()):

							# If this subsystem isn't targetable but has
							# targetable children, add the children.
							if not pSubsystem.IsTargetable():
								lTargets = pSubsystem.GetChildSubsystems()
								for pTarget in lTargets:
									if pSubsystem.IsDisabled():
										iNumDisabled = iNumDisabled + 1
									lpPossibleTargets.append(pSubsystem)
							else:
								if pSubsystem.IsDisabled():
									iNumDisabled = iNumDisabled + 1
								lpPossibleTargets.append(pSubsystem)
					pSubsystem = pShipTarget.GetNextSubsystemMatch(pIter)
			
			if len(lpPossibleTargets):
				# We have some subsystems we can target...
				# If we're supposed to disable all systems before
				# destroying any, look at the list of all non-disabled
				# systems first.
				lNonDisabled = []
				for pTargetSystem in lpPossibleTargets:
					if not pTargetSystem.IsDisabled():
						lNonDisabled.append( pTargetSystem )
				if lNonDisabled:
					# There are some systems that haven't been disabled
					# yet.  Choose from those systems.
					lpPossibleTargets = lNonDisabled

				# Pick one.
				pTargetSubsystem = self.PickTargetSubsystemFromList(lpPossibleTargets)
				#debug("Targeting subsystem %s" % pTargetSubsystem.GetName())
		elif self.bChooseSubsystemTargets:
			# There's no set list of subsystems we should target, but we
			# should choose our target subsystem intelligently.
			# Check out all our choices, rating each of them...
			lTargetSubsystems = []
			for pSubsystem in pShipTarget.GetSubsystems():
				# Build up a list of all targetable subsystems.
				lTargetSubsystems.extend( self.GetTargetableSubsystems(pSubsystem) )

			# Remove keys from self.dTargetSubsystemRating that don't appear
			# in lTargetSubsystems.
			for idKey in self.dTargetSubsystemRating.keys():
				# Check if this key is in lTargetSubsystems.
				bExists = 0
				for pSubsystem in lTargetSubsystems:
					if pSubsystem.GetObjID() == idKey:
						bExists = 1
						break
				if not bExists:
					del self.dTargetSubsystemRating[idKey]

			# In any 1 update, we only want to look through a small number of the
			# systems, so we don't take too long.  The systems that have been looked
			# at in the past are stored in self.dTargetSubsystemRating.
			# Pull out the systems that need to be updated...
			lNeedUpdates = []
			while (not lNeedUpdates)  and  lTargetSubsystems:
				for pSubsystem in lTargetSubsystems:
					if not self.dTargetSubsystemRating.has_key(pSubsystem.GetObjID()):
						# This subsystem doesn't have a rating yet.  It needs an update.
						lNeedUpdates.append(pSubsystem)
					else:
						# This subsystem is in self.dTargetSubsystemRating.  Check its
						# update sequence number, to see if it needs to be updated.
						if self.dTargetSubsystemRating[pSubsystem.GetObjID()][0] < self.iTargetSubsystemUpdateNum:
							lNeedUpdates.append(pSubsystem)

				if not lNeedUpdates:
					# The subsystems must have all been updated on this sequence num.  Increment to the next.
					self.iTargetSubsystemUpdateNum = self.iTargetSubsystemUpdateNum + 1

			# Got a list of subsystems whose ratings need to be updated.  Pick some of
			# them at random.
			if len(lNeedUpdates) <= self.iNumTargetSubsystemsToUpdate:
				lTargetSubsystems = lNeedUpdates
			elif lNeedUpdates:
				lTargetSubsystems = []
				for iSys in range(self.iNumTargetSubsystemsToUpdate):
					iIndex = App.g_kSystemWrapper.GetRandomNumber(len(lNeedUpdates))
					lTargetSubsystems.append( lNeedUpdates[iIndex] )
					lNeedUpdates.remove( lNeedUpdates[iIndex] )

			# Update the randomly chosen ones.
			#debug("Rating %d systems (%d already done)." % (len(lTargetSubsystems), len(self.dTargetSubsystemRating.keys())))
			for pSubsystem in lTargetSubsystems:
				self.dTargetSubsystemRating[pSubsystem.GetObjID()] = (self.iTargetSubsystemUpdateNum,
																	  self.RateSubsystemForTargeting(pOurShip, pShipTarget, pSubsystem))

			# Now choose a subsystem, from the history of ratings we've been
			# gathering.
			fHighestRating = -1.0e20
			for idSubsystem, lData in self.dTargetSubsystemRating.items():
				iSeqNum, fRating = lData
				if fRating > fHighestRating:
					fHighestRating = fRating
					pTargetSubsystem = App.ShipSubsystem_Cast( App.TGObject_GetTGObjectPtr( idSubsystem ) )

			#if pTargetSubsystem:
				#debug("Choose subsystem targets chose subsystem %s." % pTargetSubsystem.GetName())
		else:
			# No subsystems in our list.  If our ship has
			# a target subsystem set already, use that one.
			# This should only be the case for the player's
			# ship.
			pShip = self.pCodeAI.GetShip()
			pTargetSubsystem = pShip.GetTargetSubsystem()

			# If it's disabled and we won't fire on disabled subsystems,
			# return None.
			if pTargetSubsystem  and  (pTargetSubsystem.IsDisabled()  and  (not self.bAttackDisabledSubsystems)):
				pTargetSubsystem = None

		if pTargetSubsystem:
			self.idTargetedSubsystem = pTargetSubsystem.GetObjID()
		else:
			self.idTargetedSubsystem = None

		return pTargetSubsystem

	def GetTargetableSubsystems(self, pSubsystem):
		debug(__name__ + ", GetTargetableSubsystems")
		lTargetable = []
		if pSubsystem.GetCondition() > 0.0:
			# This system or its children may be targetable.
			if pSubsystem.IsTargetable():
				lTargetable.append(pSubsystem)
			else:
				# This one isn't targetable, but its children may be.
				for iChild in range(pSubsystem.GetNumChildSubsystems()):
					pChild = pSubsystem.GetChildSubsystem(iChild)
					lTargetable.extend( self.GetTargetableSubsystems(pChild) )

		return lTargetable

	def RateSubsystemForTargeting(self, pOurShip, pTargetShip, pSubsystem):
		# Whether or not the system is critical is important...
		debug(__name__ + ", RateSubsystemForTargeting")
		fCritical = float( pSubsystem.IsCritical() )

		# How many points of damage it'll take to disable it has a factor...
		fDamageToDisable = 0.0
		fMaxCondition = pSubsystem.GetMaxCondition()
		fDisabledCondition = pSubsystem.GetDisabledPercentage() * fMaxCondition
		fCondition = pSubsystem.GetCondition()
		if fCondition > fDisabledCondition:
			fDamageToDisable = fCondition - fDisabledCondition

		fIsDisabled = float( pSubsystem.IsDisabled() )

		# How many points to destroy has a factor...
		fDamageToDestroy = fCondition

		# Whether or not it's easy to hit from here has some influence.
		fHittable = pSubsystem.IsHittableFromLocation( pOurShip.GetWorldLocation() )

		# Certain types of systems have different overall ratings...
		fSystemRating = 0.0
		for eType, fRating in (
			(App.CT_WEAPON_SYSTEM,				5.0),
			(App.CT_WEAPON,						5.0),
			(App.CT_SHIELD_SUBSYSTEM,			5.0),
			(App.CT_CLOAKING_SUBSYSTEM,			4.0),
			(App.CT_IMPULSE_ENGINE_SUBSYSTEM,	3.0),
			(App.CT_HULL_SUBSYSTEM,				-200.0),
			):
			if pSubsystem.IsTypeOf(eType):
				fSystemRating = fRating
				break

		# Combine all these factors...
		fRating = 0.0
		for fFactor, fImportance in (
			(fCritical,			6.0),
			(fDamageToDisable,	-0.0005),
			(fIsDisabled,		-3.0 * self.bDisableFirst),
			(fDamageToDestroy,	-0.0005),
			(fHittable,			1.0),
			(fSystemRating,		1.0),
			):
			fRating = fRating + (fFactor * fImportance)

		#debug("Subsystem target %s rated at %f" % (pSubsystem.GetName(), fRating))
		return fRating

	def PickTargetSubsystemFromList(self, lSubsystems):
		debug(__name__ + ", PickTargetSubsystemFromList")
		if len(lSubsystems) == 1:
			return lSubsystems[0]

		# Loop through and rate the subsystems, and choose the one
		# with the highest rating.
		pTarget = None
		fTargetRating = None
		for pSubsystem in lSubsystems:
			# If it's already our target, that affects our decision.
			fIsTargetRating = 0.0
			if self.idTargetedSubsystem == pSubsystem.GetObjID():
				fIsTargetRating = 1.0

			# If it's healthy/unhealthy, that affects our decision.
			fHealthyRating = pSubsystem.GetConditionPercentage()

			# If it's disabled, that affects our decision.
			fDisabledRating = pSubsystem.IsDisabled()

			# Find this subsystem's overall rating...
			fRating = 0.0
			for fValue, fScale in (
				( fIsTargetRating,	1.0 ),
				( fHealthyRating,	-1.0 ),
				( fDisabledRating,	-1.0 )
				):
				fRating = fRating + (fValue * fScale)

			if (pTarget is None)  or  (fRating > fTargetRating):
				pTarget = pSubsystem
				fTargetRating = fRating

		return pTarget
