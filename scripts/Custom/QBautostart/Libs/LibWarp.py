from bcdebug import debug
import App
import Effects
import LibStarstreaks
import MissionLib
import WarpSequence
import Foundation
import LibEngineering
import Custom.NanoFXv2.WarpFX.WarpFX_GUI
from math import exp
from LibQBautostart import *

iDefaultMaxSpeed = 8
iDefaultSpeed = 6
dCurWarpSpeeds = {}
MP_SEND_WARP_SPEED_MSG = 201
fMaxPower = 1.25
dWarpSetLocations = {}
iLastXoff = 0
iLastYoff = 0
iLastZoff = 0
dWarpScenes = {}
lDisAllowJoin = []

NonSerializedObjects = (
"dCurWarpSpeeds",
"iLastXoff",
"iLastYoff",
"iLastZoff",
"dWarpSetLocations",
"dWarpScenes",
"lDisAllowJoin",
)


def GetEntryDelayTime(pShip):
	debug(__name__ + ", GetEntryDelayTime")
	sShipType = GetShipType(pShip)
	if Foundation.shipList.has_key(sShipType):
		pFoundationShip = Foundation.shipList[sShipType]
		if pFoundationShip and hasattr(pFoundationShip, "fWarpEntryDelayTime"):
			return pFoundationShip.fWarpEntryDelayTime
	return 6.0 + pShip.GetRadius() / 2.0


def GetMaxWarp(pShip):
	debug(__name__ + ", GetMaxWarp")
	sShipType = GetShipType(pShip)
	if not sShipType or not pShip.GetWarpEngineSubsystem():
		return 0

	if Foundation.shipList.has_key(sShipType):
		pFoundationShip = Foundation.shipList[sShipType]
		if pFoundationShip and hasattr(pFoundationShip, "fMaxWarp"):
			return pFoundationShip.fMaxWarp
	return iDefaultMaxSpeed


def SetCurWarpSpeed(pShip, fSpeed, bNoMessage=0):
	debug(__name__ + ", SetCurWarpSpeed")
	if fSpeed > 10: # not possible
		fSpeed = 10.0
	elif fSpeed < 1.0:
		fSpeed = 1.0
	if not pShip:
		return
	
	# only 3 digits after .
	fSpeed = float("%.3f" % fSpeed)
	dCurWarpSpeeds[pShip.GetName()] = fSpeed
	
	if App.g_kUtopiaModule.IsMultiplayer() and not bNoMessage:
		MPSendMyWarpSpeed(pShip, fSpeed)


def GetCurWarpSpeed(sShipName):
	debug(__name__ + ", GetCurWarpSpeed")
	if dCurWarpSpeeds.has_key(sShipName):
		return dCurWarpSpeeds[sShipName]
	elif MissionLib.GetPlayer() and sShipName == MissionLib.GetPlayer().GetName():
		return Custom.NanoFXv2.WarpFX.WarpFX_GUI.GetWarpSpeed()
	return iDefaultSpeed


def GetSystem(pSet):
	debug(__name__ + ", GetSystem")
	if not pSet or not pSet.GetRegionModule():
		return ""
	return string.split(pSet.GetRegionModule(), '.')[1]


def GetDistance(sSet1, sSet2):
	# same set, different planet
	debug(__name__ + ", GetDistance")
	if sSet1 == sSet2:
		return 1
	
	# another set
	return 10000
	

def CalcWarpTime(pShip, pWarpSeq):
	debug(__name__ + ", CalcWarpTime")
	sFromSet = GetSystem(pWarpSeq.GetOrigin())
	sToSet = GetSystem(pWarpSeq.GetDestinationSet())
	fSpeed = GetCurWarpSpeed(pShip.GetName())
	fMaxSpeed = GetMaxWarp(pShip)
	fDist = GetDistance(sFromSet, sToSet)
	if not pShip.GetWarpEngineSubsystem():
		return 1e9
	
	fPower = pShip.GetWarpEngineSubsystem().GetPowerPercentageWanted()
	
	if fPower < 1.0 and fSpeed > fPower * fMaxSpeed:
		fSpeed = fPower * fMaxSpeed
		SetCurWarpSpeed(pShip, fSpeed)
	if fPower > 1.0 and fSpeed >= int(fMaxSpeed) and fMaxSpeed > int(fMaxSpeed):
		fSpeedDiff = fMaxSpeed - int(fMaxSpeed)
		fSpeedPowerFac = fSpeedDiff / (fMaxPower - 1.0)
		fSpeed = int(fSpeed) + fSpeedPowerFac * (fPower - 1.0)
		SetCurWarpSpeed(pShip, fSpeed)
	
	fSpeed = GetCurWarpSpeed(pShip.GetName())
	if fSpeed < 10:
		fFac = exp(-2.82 + 3.21*fSpeed - 0.41*fSpeed**2 + 0.02*fSpeed**3) + 1
	else: # trans warp
		fFac = 1e50
	fTime = fDist / fFac
	print "Warp - dist: %f, speed: %f, fac: %f, time: %f" % (fDist, fSpeed, fFac, fTime)
	return fTime


def MPSendMyWarpSpeed(pShip, fSpeed):
	debug(__name__ + ", MPSendMyWarpSpeed")
	if not pShip:
		return
	
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)
	kStream = App.TGBufferStream()
	kStream.OpenBuffer(256)
	kStream.WriteChar(chr(MP_SEND_WARP_SPEED_MSG))

	kStream.WriteInt(pShip.GetObjID())
	kStream.WriteFloat(fSpeed)

        pMessage.SetDataFromStream(kStream)
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        kStream.CloseBuffer()


def ProcessMessageHandler(pObject, pEvent):
	debug(__name__ + ", ProcessMessageHandler")
	pMessage = pEvent.GetMessage()
	if pMessage:
		kStream = pMessage.GetBufferStream()
		cType = kStream.ReadChar()
		cType = ord(cType)
		if cType == MP_SEND_WARP_SPEED_MSG:
			iShipID = kStream.ReadInt()
			fSpeed = kStream.ReadFloat()
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
		
			if pShip:
				SetCurWarpSpeed(pShip, fSpeed, bNoMessage=1)
				if App.g_kUtopiaModule.IsHost():
					MPSendMyWarpSpeed(pShip, fSpeed)
		kStream.Close()


def IncXYZOffsets():
	debug(__name__ + ", IncXYZOffsets")
	global iLastXoff, iLastYoff, iLastZoff
	if iLastXoff >= iLastYoff and iLastXoff > iLastZoff:
		iLastXoff = iLastXoff + 10000
	elif iLastYoff > iLastXoff and iLastYoff > iLastZoff:
		iLastYoff = iLastYoff + 10000
	else:
		iLastZoff = iLastZoff + 10000


def SetInWarpLocationAction(pAction, pShip, pWarpSeq, pFromSet, pWarpSet):
	debug(__name__ + ", SetInWarpLocationAction")
	global dWarpSetLocations
	sFromSet = GetSystem(pFromSet)
	sToSet = GetSystem(pWarpSeq.GetDestinationSet())
	pPlayer = MissionLib.GetPlayer()
	
	if sFromSet != sToSet:
		sWarpName = sFromSet + "_" + sToSet
	elif pWarpSeq.GetOrigin():
		sWarpName = pWarpSeq.GetOrigin().GetRegionModule() + "_" + pWarpSeq.GetDestinationSet().GetRegionModule()
	elif pWarpSeq.GetDestinationSet():
		sWarpName = pWarpSeq.GetDestinationSet().GetRegionModule()
	else:
		sWarpName = "Unknown"
	
	if not dWarpSetLocations.has_key(sWarpName):
		IncXYZOffsets()
		dWarpSetLocations[sWarpName] = [iLastXoff, iLastYoff, iLastZoff, None]

	vPoint = App.TGPoint3()
	vPoint.SetX(dWarpSetLocations[sWarpName][0])
	vPoint.SetY(dWarpSetLocations[sWarpName][1])
	vPoint.SetZ(dWarpSetLocations[sWarpName][2])
	dWarpSetLocations[sWarpName][0] = dWarpSetLocations[sWarpName][0] + 20 * (-1)**App.g_kSystemWrapper.GetRandomNumber(2)
	dWarpSetLocations[sWarpName][1] = dWarpSetLocations[sWarpName][1] - 50
	dWarpSetLocations[sWarpName][2] = dWarpSetLocations[sWarpName][2] + 20 * (-1)**App.g_kSystemWrapper.GetRandomNumber(2)

	fWarpFactor = GetCurWarpSpeed(pShip.GetName())
	if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
		oWarpEffect = LibStarstreaks.WarpSetv2_Create(pShip, fWarpFactor)
		dWarpSetLocations[sWarpName][3] = oWarpEffect
	
	if pShip.GetPhaserSystem():
		pShip.GetPhaserSystem().TurnOff()

	pShip.SetTranslate(vPoint)
	pShip.UpdateNodeOnly()
	
	#if pShip.GetImpulseEngineSubsystem():
	#	pShip.GetImpulseEngineSubsystem().TurnOff()

	if pShip.GetPhaserSystem():
		pShip.GetPhaserSystem().TurnOff()
	DisableMVAMMenu(pShip)

	return 0


def DisableMVAMMenu(pShip, iEnable=0):
		debug(__name__ + ", DisableMVAMMenu")
		pPlayer = MissionLib.GetPlayer()
		
		if pPlayer and pPlayer.GetObjID() == pShip.GetObjID():
			pMenu = LibEngineering.GetBridgeMenu("XO")
			pMVAMMenu = LibEngineering.GetButton("MVAM Menu", pMenu)
			if pMVAMMenu:
				if iEnable and pMVAMMenu.GetNumChildren():
					pMVAMMenu.SetEnabled()
				else:
					pMVAMMenu.SetDisabled()


class InWarpTimer:
	def __init__(self, pShip, pWarpSeq, iTimeToWarp, pDuringWarpAction, pPostDuringWarpAction, ExitWarpSeq, pcDest, iWarpSpeed):
		debug(__name__ + ", __init__")
		self.pShip = pShip
		self.pWarpSeq = pWarpSeq
		self.iTimeToWarp = iTimeToWarp
		self.pDuringWarpAction = pDuringWarpAction
		self.pPostDuringWarpAction = pPostDuringWarpAction
		self.pTimerProcess = None
		self.ExitWarpSeq = ExitWarpSeq
		self.SetupTimer()
		self.DeWarpTooEarly = 0
		self.iTimeToWarpSave = iTimeToWarp
		self.iShipID = pShip.GetObjID()
		self.pcDest = pcDest
		self.iWarpSpeed = iWarpSpeed
		if self.iWarpSpeed > 10:
			self.iWarpSpeed = 10
		
		#if pShip.GetName() in lDisAllowJoin:
		#	lDisAllowJoin.remove(pShip.GetName())
		#if App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsHost() and not lDisAllowJoin:
		#	pGame = App.Game_GetCurrentGame()
		#	pMultGame = App.MultiplayerGame_Cast(pGame)
		#	pMultGame.SetReadyForNewPlayers(1)
	
	def SetupTimer(self):
		debug(__name__ + ", SetupTimer")
		if self.pTimerProcess:
			# We already have a timer.
			return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetDelay(0.5)
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.CRITICAL)

	
	def FlyForward(self):
		debug(__name__ + ", FlyForward")
		self.pShip.GetImpulseEngineSubsystem().TurnOn()
		if not self.pShip.GetImpulseEngineSubsystem().GetMaxSpeed():
			print "Warp Error: Unable to set Impulse speed."
			return
		fMax = (1.0/self.pShip.GetImpulseEngineSubsystem().GetMaxSpeed())/10 # make sure that we all use the same speed base
		fSpeed = fMax*self.iWarpSpeed # set the speed linear to the warp speed
		vImpPoint = App.TGPoint3()
		vImpPoint.SetXYZ(0, 1, 0) # forward
		self.pShip.SetImpulse(fSpeed, vImpPoint, App.ShipClass.DIRECTION_MODEL_SPACE)

	def Update(self, dTimeAvailable):
		debug(__name__ + ", Update")
		
		self.pShip = App.ShipClass_GetObjectByID(None, self.iShipID)
		if not self.pShip:
			self.pTimerProcess = None
			return
		
		self.CheckCondition()
		if self.pShip.GetImpulseEngineSubsystem():
			#self.pShip.GetImpulseEngineSubsystem().TurnOff()
			self.FlyForward()
		if self.pShip.GetPhaserSystem():
			self.pShip.GetPhaserSystem().TurnOff()
		
		# make sure we run at least 10 seconds ahead
		if self.iTimeToWarp - self.iTimeToWarpSave > 10:
			return
		
		if MissionLib.GetPlayer() and MissionLib.GetPlayer().GetObjID() == self.pShip.GetObjID():
			pAction = App.TGScriptAction_Create("MissionLib", "TextBanner", App.TGString("ETA: " + str(self.iTimeToWarp) + " seconds"), 0, 0.10, 0.8, 12)
			self.pWarpSeq.AppendAction(pAction, 1)
			pAction = App.TGScriptAction_Create("MissionLib", "TextBanner", App.TGString("Destination: " + self.pcDest), 0,  0.02, 1.0, 12)
			self.pWarpSeq.AppendAction(pAction)
			pAction = App.TGScriptAction_Create("MissionLib", "TextBanner", App.TGString("Warp Speed: Warp " + str(self.iWarpSpeed)), 0,  0.06, 1.0, 12)
			self.pWarpSeq.AppendAction(pAction)
		else:
			pAction = App.TGScriptAction_Create(__name__, "DoNothingAction")
			self.pWarpSeq.AppendAction(pAction, 1)

		pActionDecrement = App.TGScriptAction_Create(__name__, "DecrementAction", self)
		self.pWarpSeq.AppendAction(pActionDecrement)
		
		self.iTimeToWarpSave = self.iTimeToWarpSave - 1

		#if not self.pShip.GetName() in lDisAllowJoin and self.iTimeToWarp < 15 and App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsHost():
		#	pGame = App.Game_GetCurrentGame()
		#	pMultGame = App.MultiplayerGame_Cast(pGame)
		#	pMultGame.SetReadyForNewPlayers(0)
		#	lDisAllowJoin.append(self.pShip.GetName())

		if self.iTimeToWarp <= 1:
			self.ExitWarp()

	def CheckCondition(self):
		debug(__name__ + ", CheckCondition")
		pWarp = self.pShip.GetWarpEngineSubsystem()
		
		if self.pShip.IsDead() or self.pShip.IsDying():
			print "Dead ship", self.pShip.GetName(), "breaking warp cutscene"
			DeWarp(self.pShip)
		elif pWarp and pWarp.IsDisabled() or not self.pShip.GetPowerSubsystem() or self.pShip.GetPowerSubsystem().IsDisabled():
			print self.pShip.GetName(), "lost his warp engines. Beaking warp cutscene"
			DeWarp(self.pShip)

	def ExitWarp(self):
		#if not self.pShip.GetName() in lDisAllowJoin and App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsHost():
		#	pGame = App.Game_GetCurrentGame()
		#	pMultGame = App.MultiplayerGame_Cast(pGame)
		#	pMultGame.SetReadyForNewPlayers(0)
		#	lDisAllowJoin.append(self.pShip.GetName())
		debug(__name__ + ", ExitWarp")
		if self.pTimerProcess:
			self.pWarpSeq.AppendAction(self.pPostDuringWarpAction)
			self.ExitWarpSeq(self.pWarpSeq, self.pShip.GetContainingSet(), MissionLib.GetPlayer(), self.pShip)
			self.pTimerProcess = None
			if self.pShip.GetImpulseEngineSubsystem():
				self.pShip.GetImpulseEngineSubsystem().TurnOn()

def DecrementAction(pAction, pWarpTimer):
	debug(__name__ + ", DecrementAction")
	pWarpTimer.iTimeToWarp = pWarpTimer.iTimeToWarp - 1
	return 0
	

def DoNothingAction(pAction):
	debug(__name__ + ", DoNothingAction")
	return 0


def RunInWarp(pAction, pShip, pWarpSeq, iTimeToWarp, pDuringWarpAction, pPostDuringWarpAction, ExitWarpSeq, pcDest, iWarpSpeed):
	debug(__name__ + ", RunInWarp")
	global dWarpScenes
	dWarpScenes[pShip.GetName()] = InWarpTimer(pShip, pWarpSeq, iTimeToWarp, pDuringWarpAction, pPostDuringWarpAction, ExitWarpSeq, pcDest, iWarpSpeed)
	return 0


def DeWarp(pShip):
	debug(__name__ + ", DeWarp")
	global dWarpScenes
	if dWarpScenes.has_key(pShip.GetName()):
		dWarpScenes[pShip.GetName()].DeWarpTooEarly = 1
		dWarpScenes[pShip.GetName()].ExitWarp()
		del dWarpScenes[pShip.GetName()]


def ExitedWarpTooEarly(pShip, pWarpSeq):
	debug(__name__ + ", ExitedWarpTooEarly")
	if not dWarpScenes.has_key(pShip.GetName()):
		return 1
	elif dWarpScenes[pShip.GetName()].DeWarpTooEarly:
		return 1
	return 0


def GetWarpDestination(pShip, pWarpSeq):
	debug(__name__ + ", GetWarpDestination")
	if not ExitedWarpTooEarly(pShip, pWarpSeq):
		return pWarpSeq.GetDestination()
	return "Systems.DeepSpace.DeepSpace"


def GetWarpDestinationSet(pShip, pWarpSeq):
	debug(__name__ + ", GetWarpDestinationSet")
	if not ExitedWarpTooEarly(pShip, pWarpSeq):
		return pWarpSeq.GetDestinationSet()
	pSet = App.g_kSetManager.GetSet("DeepSpace")
	if not pSet:
		import Systems.DeepSpace.DeepSpace
		Systems.DeepSpace.DeepSpace.Initialize()
		pSet = App.g_kSetManager.GetSet("DeepSpace")
	return pSet


def DoWarpOutPostMoveAction(pAction, pShip, pWarpSeq, pDestSet):
	debug(__name__ + ", DoWarpOutPostMoveAction")
	if ExitedWarpTooEarly(pShip, pWarpSeq):	
		pOldSet = pShip.GetContainingSet()
		if pOldSet:
			pOldSet.RemoveObjectFromSet(pShip.GetName())
		if pDestSet and pShip and not (pShip.IsDead() or pShip.IsDying()):
			pDestSet.AddObjectToSet(pShip, pShip.GetName())
	
	return 0


def DoMiscPostWarpStuff(pAction, pShip):
	debug(__name__ + ", DoMiscPostWarpStuff")
	if pShip.GetName() in lDisAllowJoin:
		lDisAllowJoin.remove(pShip.GetName())
	if App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsHost() and not lDisAllowJoin:
		pGame = App.Game_GetCurrentGame()
		pMultGame = App.MultiplayerGame_Cast(pGame)
		pMultGame.SetReadyForNewPlayers(1)

	if pShip.GetPhaserSystem() and pShip.GetAlertLevel() == App.ShipClass.RED_ALERT:
		pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
		if pShip and not pShip.IsDead() and not pShip.IsDying():
			pShip.GetPhaserSystem().TurnOn()
	if pShip:
		DisableMVAMMenu(pShip, 1)

	debug(__name__ + ", DoMiscPostWarpStuff Done")
	return 0


# from WarpSequence
###############################################################################
#	CheckWarpInPath
#	
#	Check the path that this ship is going to be warping in along.
#	If it's not clear of obstacles, change it.
#	
#	Args:	pAction			- The TGScriptAction calling us.
#			pWarpSequence	- The warp sequence controlling the script action
#							  (and controlling the ship)
#			idShip			- The ship that's warping.
#	
#	Return:	0
###############################################################################
def CheckWarpInPath(pAction, pWarpSequence, idShip, pDestSet):	
	# Get various things we'll need...
	debug(__name__ + ", CheckWarpInPath")
	
	pWarpSet = App.WarpSequence_GetWarpSet()
	try:
		pShip = App.ShipClass_GetObjectByID(None, idShip)
		pSet = pDestSet
		if not pSet:
			return 0
		pWarpEngines = pShip.GetWarpEngineSubsystem()

		vStart = pWarpEngines.GetWarpExitLocation()
		pEndPlacement = App.PlacementObject_GetObject(pSet, pWarpSequence.GetPlacementName())
		vEnd = pEndPlacement.GetWorldLocation()
		fShipRadius = pShip.GetRadius()
	except AttributeError:
		return 0

	# Search through all ships warping in the set right now...
	lpShips = []
	for pSetShip in pSet.GetClassObjectList(App.CT_SHIP):
		lpShips.append((pSetShip, None))
	for pSetShip in pWarpSet.GetClassObjectList(App.CT_SHIP):
		if pSetShip.GetWarpEngineSubsystem():
			pWarpSystem = pSetShip.GetWarpEngineSubsystem()
			if pWarpSystem.GetWarpState() != App.WarpEngineSubsystem.WES_NOT_WARPING:
				# Make sure this is the set it's arriving at, not the set it's departing.
				pWS = App.WarpSequence_Cast(pWarpSystem.GetWarpSequence())
				pDestinationSet = pDestSet
				if pDestinationSet and pDestinationSet.GetObjID() == pSet.GetObjID():
					# This ship is warping into this set.  Add it...
					lpShips.append((pSetShip, pWarpSystem))

	# Check the path that that these ships are warping in along...
	iIndex = 0
	fRandomMax = 15.0
	bChanged = 0
	while iIndex < len(lpShips):
		pWarpingShip, pWarpingSubsystem = lpShips[iIndex]
		iIndex = iIndex + 1

		if pWarpingSubsystem:
			vWarpStart = pWarpingSubsystem.GetWarpExitLocation()
			pEndPlacement = pWarpingSubsystem.GetPlacement()

			if pEndPlacement:
				vWarpEnd = pWarpingSubsystem.GetPlacement().GetWorldLocation()
			else:
				vWarpEnd = pWarpingShip.GetWorldLocation()
		else:
			# If the ship's not warping, we still don't want to warp in near it.
			vWarpStart = pWarpingShip.GetWorldLocation()
			vWarpEnd = pWarpingShip.GetWorldLocation()
			vWarpEnd.Add( pWarpingShip.GetWorldForwardTG() )

		# If our line is ever too close to their line, adjust our line.
		# Find the distance between the two line segments...
		vClosestStart, vClosestEnd = WarpSequence.FindSegmentBetweenSegments( vStart, vEnd, vWarpStart, vWarpEnd )
		vDiff = App.TGPoint3()
		vDiff.Set(vClosestEnd)
		vDiff.Subtract( vClosestStart )
		fDistance = vDiff.Unitize()
		#debug("Distance between segments is %f" % fDistance)

		# Just in case...
		if fDistance == 0:
			vDiff.SetXYZ(1.0, 0, 0)

		# Got the distance.  Are we too close?
		if fDistance < (fShipRadius * 4.0):
			# Yeah, it's probably too close.  Push our line away.  Far away...
			bChanged = 1
			vDiff.Scale( fShipRadius * (App.g_kSystemWrapper.GetRandomNumber(fRandomMax) + 2.0) )
			vStart.Add(vDiff)
			vEnd.Add(vDiff)
			# And reset our checks, so we check from the beginning again.
			iIndex = 0
			# And bump up the random max, in case we keep looping...  We'll eventually break out.
			fRandomMax = fRandomMax + 8.0

	if bChanged:
		# Our warp-in point has changed.  We need to make a new placement to warp into,
		# at the new location.
		iAttempt = 0
		while 1:
			sPlacement = "WarpAdjusted %d" % iAttempt
			if not App.PlacementObject_GetObject(pSet, sPlacement):
				break
			iAttempt = iAttempt + 1

		pPlacement = App.PlacementObject_Create(sPlacement, pSet.GetName(), None)

		pPlacement.SetTranslate(vEnd)
		if pEndPlacement:
			pPlacement.SetMatrixRotation(pEndPlacement.GetRotation())
		pPlacement.UpdateNodeOnly()

		pWarpSequence.SetPlacement(sPlacement)
		pWarpEngines.SetPlacement(pPlacement)
#		debug("Adjusted warp-in point for %s (to %s)" % (pShip.GetName(), sPlacement))
		#App.Breakpoint()

	return 0
