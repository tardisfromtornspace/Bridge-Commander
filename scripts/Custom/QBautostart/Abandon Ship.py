from bcdebug import debug
#!/usr/bin/python1.5
# Abandon Ship script by Defiant <mail@defiant.homedns.org>
#
# Lisence: GPL - see README

# Settings:
# ----------
# How much Pods for Radius = 1
PodsPerSize = 4
# chance that the abandon process will really work in %
iAbandonShipSuccessQuote = 30
# maximum pods per ship in multiplayer
iMultMaxPods = 10
# maximum pods in QB
iMaxPods = 30

iPositionSizeMult = float(100)

# Please do not edit below this line - except you know what you are doing
# ================================================================================

# Import all that stuff we need
import App 
import MissionLib 
import loadspacehelper
import math
import Lib.LibEngineering
import string
import Foundation
import AI.Player.FlyForward
from Libs.LibQBautostart import *
from Libs.Races import Races


MODINFO = {     "Author": "\"Defiant\" erik@defiant.homedns.org",
                "Download": "http://defiant.homedns.org/~erik/STBC/AbandonShip/",
                "Version": "0.6",
                "License": "GPL",
                "Description": "Abandon Ship Script",
                "needBridge": 0
            }


# Vars
pPlayerOld = None
AS_TIMER1 = None
AS_END_SCENE_TIMER = None
sAIAbandonShipMutator = "AI Abandon Ship"
lAbandonDone = []

NonSerializedObjects = (
"lAbandonDone"
)

# Red Alert, Abandon Ship now! -what todo:
def AbandonShip(pObject, pEvent): 
	debug(__name__ + ", AbandonShip")
	global lAbandonDone
	
	#print("Abandon Ship")
	pShip = App.Game_GetCurrentPlayer()

	if not pShip:
		return

	if pShip.GetObjID() in lAbandonDone:
		print "Abandon Ship for %s was already running, exiting" % pShip.GetName()
		return
	lAbandonDone.append(pShip.GetObjID())

	if ( pShip.GetRadius() < 0.5 ):
		print("This Ship is to small - nothing to Abandon")
		return
	
	# First stop the Ship
	#import AI.Player.Stay
	#MissionLib.SetPlayerAI("Helm", AI.Player.Stay.CreateAI(pShip))
		
	# Play the sound
	pSound = App.TGSound_Create("sfx/Interface/new_game.wav", "AS_Sound", 0)
	pSound.SetSFX(0)
	pSound.SetInterface(1)
	App.g_kSoundManager.PlaySound("AS_Sound")

	# Start the Cutscene
	pSequence = App.TGSequence_Create()

	pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene")
	pSequence.AppendAction(pAction)

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
	pSequence.AppendAction(pAction)	# Start cinematic mode first

	pAction	= App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pShip.GetContainingSet().GetName())
	pSequence.AppendAction(pAction)

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pShip.GetContainingSet().GetName(), pShip.GetName())
	pSequence.AppendAction(pAction)

	pSequence.Play()
	
	AbandonShipTimer(2, AS_TIMER1)


def StartAbandonShip_Player(pObject, pEvent):
	debug(__name__ + ", StartAbandonShip_Player")
	if StartAbandonShip(MissionLib.GetPlayer()):
		AbandonShipTimer(2, AS_END_SCENE_TIMER)
	

def StartAbandonShip(pShip):
	debug(__name__ + ", StartAbandonShip")
	global pPlayerOld, PodsPerSize
	
	# Some things we need
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pMission = MissionLib.GetMission()
	pFriendlies = pMission.GetFriendlyGroup()
	sSetName = pSet.GetName()
	pPlayerOld = pPlayer
	itemp = None
	
	if not pShip.GetHull() or pShip.IsDead() or pShip.IsDying():
		return 0

	pMultGame = App.MultiplayerGame_Cast(pGame)
	if pMultGame:
		pGame = pMultGame

	# Creater Hull-Radius * 4 Escape Pods
	ShipSize = pShip.GetRadius()
	CreateShipsNum = round(ShipSize, 0) * PodsPerSize
	#print(CreateShipsNum)
        
        # limit pods in mp
        if App.g_kUtopiaModule.IsMultiplayer() and CreateShipsNum > iMultMaxPods:
                CreateShipsNum = iMultMaxPods
	if CreateShipsNum > iMaxPods:
		CreateShipsNum = iMaxPods

	# staions do not have pods
	if pShip.GetShipProperty().IsStationary():
		return

        # Get the Pod Model
	try:
		ShipType = GetShipType(pShip)
		if not ShipType:
			print "Abandon Ship Error: No Shiptype for this ship"
		elif not Foundation.shipList.has_key(ShipType):
			print "Abandon Ship Error: %s not known to Foundation" % (ShipType)
		FdtnShip = Foundation.shipList[ShipType]
		if not FdtnShip:
			print "Abandon Ship Error: No Foundation Ship", ShipType
		if not FdtnShip.GetRace():
			print "Abandon Ship Error: No Race Informations for", FdtnShip.GetRace()
		RaceName = FdtnShip.GetRace().name
		if (RaceName == "Federation"):
			if ShipLike(ShipType, "Defiant") or ShipLike(ShipType, "Intrepid") or ShipLike(ShipType, "Voyager") or ShipLike(ShipType, "yeager") or ShipLike(ShipType, "AdminDef"):
				PodModel = "defpod"
			elif ShipLike(ShipType, "Galaxy") or ShipLike(ShipType, "Nebula"):
				PodModel = "Galaxy Escape Pod"
			else:
				PodModel = "EscapePod"
		elif (RaceName == "Klingon"):
		    PodModel = "greenmisc"
		else:
		    PodModel = "card pod"
	except:
		PodModel = "EscapePod"	

	# clear AI, this ship is abendoned
	pShip.ClearAI()
	
        loadspacehelper.PreloadShip(PodModel, CreateShipsNum)

	# Choosing an Escape Pod for the Bridge Crew
	AS_BridgePod = 0
	CreateShipsNum = int(CreateShipsNum)
	if CreateShipsNum > 0:
		AS_BridgePod = App.g_kSystemWrapper.GetRandomNumber(CreateShipsNum)
	if ( AS_BridgePod == 0 ):
		AS_BridgePod = 1

	#print("Bridge Pod is", AS_BridgePod)

	# Get the Players Location
	PlayerXpos = pShip.GetWorldLocation().GetX()
	PlayerYpos = pShip.GetWorldLocation().GetY()
	PlayerZpos = pShip.GetWorldLocation().GetZ()
	
	i = 1
	PodPosxyz = 1
	while (i <= CreateShipsNum):
		# Name of the Pod
		PodName = "Escape Pod " + str(i)
		# test if a Pod with this name already exists
		k = 10
		while ( MissionLib.GetShip(PodName) != None):
			# If its exists try another name (10+)
			itemp = i + k
			PodName = "Escape Pod " + str(itemp)
			k = 2*k
		#print("PodName is ", PodName)
		if itemp:
			i = itemp
			AS_BridgePod = i
		
		# Position Name of the Pod
		PodLaunchPoint = "PodLaunchPoint" + str(i)
		# Distance of Pods
		PodRadius = ShipSize
		# if PodRadius < 1 then the Game crashes, so fix
		if ( PodRadius < 1 ):
			PodRadius = 1
		PodRadius = PodRadius * iPositionSizeMult
	
		# Create the Pod
		AS_EscapePod = loadspacehelper.CreateShip(PodModel, pSet, PodName, PodLaunchPoint)

                # Disable Collisions
                AS_EscapePod.EnableCollisionsWith(pShip, 0)
                AS_EscapePod.DisableCollisionDamage(1)
                i2 = i
                while (i2 >= 1 and i != 1):
			pEnableCollisionPartner = MissionLib.GetShip("Escape Pod " + str(i2))
                        AS_EscapePod.EnableCollisionsWith(pEnableCollisionPartner, 0)
                        i2 = i2 - 1
                collisiondisable = 0

                # Position of the Pod
                kLocation = App.TGPoint3()
                i2 = 0
                while 1:
                       	iVarCoord = App.g_kSystemWrapper.GetRandomNumber(3)
			iVarCoord2 = App.g_kSystemWrapper.GetRandomNumber(2)
			A = App.g_kSystemWrapper.GetRandomNumber(PodRadius) * (-1) ** App.g_kSystemWrapper.GetRandomNumber(2)
			fRandMax = math.sqrt(PodRadius**2 - A**2)
			if fRandMax < 1:
				fRandMax = 1
			B = App.g_kSystemWrapper.GetRandomNumber(fRandMax) * (-1) ** App.g_kSystemWrapper.GetRandomNumber(2)
			C = math.sqrt(PodRadius**2 - A**2 - B**2) * (-1) ** App.g_kSystemWrapper.GetRandomNumber(2)
 
 			A = A / iPositionSizeMult
			B = B / iPositionSizeMult
			C = C / iPositionSizeMult
 
                        if iVarCoord == 0: # X is var
				X = A
				if iVarCoord == 0: # Y is var
					Y = B
					Z = C
				else: # Z is var
					Y = C
					Z = B
			elif iVarCoord == 1: # Y is var
				Y = A
				if iVarCoord2 == 0: # X is var
					X = B
					Z = C
				else: # Z is var
					X = C
					Z = B
			else: # Z is var
				Z = A
				if iVarCoord2 == 0: # X is var
					X = B
					Y = C
				else: # Y is var
					X = C
					Y = B

                        kLocation.SetXYZ(X + PlayerXpos, Y + PlayerYpos, Z + PlayerZpos)

                        if pSet.IsLocationEmptyTG(kLocation, 0.1, 0.1): # go out of this loop here
                                #print("PodCoords: ", X, Y, Z)
                                collisiondisable = 1
                                break

                        i2 = i2 + 1
                        PodPosxyz = PodPosxyz + 1
                        if (i2 > 10): # prevent from looping till the end of the universe, stop at 10
                                break
		kPoint = kLocation
		
		# not using GetLocalRandomPointAndNormalOnModel() -> can crash the game
		"""vLocation = App.TGPoint3()
		vNormal = App.TGPoint3()
		if pShip.GetHull():
		# bc can crash on dying/dead ship when using GetRandomPointOnModel call, try to avoid
		if pShip.IsDead() or pShip.IsDying() or not pShip.GetHull() or pShip.GetHull().GetConditionPercentage() == 0:
			return 1
		pShip.GetLocalRandomPointAndNormalOnModel(vLocation, vNormal)
		vLocation.Add(pShip.GetWorldLocation())
		kPoint = App.TGPoint3()
		kPoint.Set(vLocation)
		
		kforward = pShip.GetWorldForwardTG()
		kup = pShip.GetWorldUpTG()
		
		kforward.Add(vNormal)
		kup.Add(vNormal)"""
		#Now Position them
		AS_EscapePod.SetTranslate(kPoint)
		#AS_EscapePod.AlignToVectors(kforward, kup)
		#debug(__name__ + ", StartAbandonShip, EnableCollisionWith Align Done")
		AS_EscapePod.UpdateNodeOnly()
		
		# Only for Player: if this is our Pod: welcome on Board
		if AS_BridgePod == i and pShip.GetObjID() == pPlayer.GetObjID():
			#print("Welcome on Board of " + PodName + ", captain")
                        if App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsClient():
                                PlayerNetID = pPlayer.GetNetPlayerID()
                                AINetID = AS_EscapePod.GetNetPlayerID()
			pGame.SetPlayer(AS_EscapePod)
			if App.g_kUtopiaModule.IsMultiplayer():
				try:
					from Custom.MultiplayerExtra.MultiplayerLib import CreateShipFromShip, SetStopAI
					pPlayerOld = CreateShipFromShip(pPlayer)
					SetStopAI(pPlayerOld)
				except ImportError:
					pass
                        if App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsClient():
                                pPlayer.SetNetPlayerID(AINetID)
                                AS_EscapePod.SetNetPlayerID(PlayerNetID)
				try:
					from Custom.MultiplayerExtra.MultiplayerLib import SetNewNetPlayerID
					SetNewNetPlayerID(pPlayer, AINetID)
					SetNewNetPlayerID(AS_EscapePod, PlayerNetID)
				except:
					pass
			pTacWeaponsCtrl = App.TacWeaponsCtrl_GetTacWeaponsCtrl()
			if pTacWeaponsCtrl:
				pTacWeaponsCtrl.Init()
				try:
					import Custom.Autoload.ReSet
					if Custom.Autoload.ReSet.mode.IsEnabled():
						Custom.Autoload.ReSet.oPlayerChecking.__call__(None, None, 1)
				except:
					pass
                # else set AI
		#else:
                        #if App.g_kUtopiaModule.IsMultiplayer() and pFriendlies.IsNameInGroup(pShip.GetName()):
			#        pFriendlies.AddName(PodName)
		AS_EscapePod.SetAI(AI.Player.FlyForward.CreateWithAvoid(AS_EscapePod, 10.0))

                # re-enable Collisions
                if collisiondisable:
                        AS_EscapePod.DisableCollisionDamage(0)
                        AS_EscapePod.EnableCollisionsWith(pShip, 1)

		# i++
		i = i + 1
		if ( PodPosxyz != 6 ):
			PodPosxyz = PodPosxyz + 1
		else:
			PodPosxyz = 1

		# End While loop here
	return 1
	


def AS_End_Cutscene(pObject, pEvent):
	debug(__name__ + ", AS_End_Cutscene")
	global pPlayerOld

	pShip = App.Game_GetCurrentPlayer()

	# End the Cutscene
	pSequence = App.TGSequence_Create ()

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pShip.GetContainingSet().GetName())
	pSequence.AppendAction(pAction)

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StopCinematicMode")
	pSequence.AppendAction(pAction)
	
	pAction = App.TGScriptAction_Create("MissionLib", "SetTarget", pPlayerOld.GetName())
	pSequence.AppendAction(pAction)

        if App.g_kSetManager.GetSet("bridge"):
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                pSequence.AppendAction(pAction, 2) # Small 2 seconds Delay

	pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
	pSequence.AppendAction(pAction)
	
	pSequence.Play()
	
	# set AI for the old Player to none
	pPlayerOld = MissionLib.GetShip(pPlayerOld.GetName())
	if pPlayerOld and not App.g_kUtopiaModule.IsMultiplayer():
		pPlayerOld.ClearAI()

        # clear
        App.g_kSoundManager.DeleteSound("AS_Sound")
        
        # Force switch to Tactical if we have no Bridge
        if not App.g_kSetManager.GetSet("bridge"):
                MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ForceTacticalVisible", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)

	#print("Abandon Ship is done - cu")


def ForceTacticalVisible(pObject, pEvent):
        debug(__name__ + ", ForceTacticalVisible")
        pTopWindow = App.TopWindow_GetTopWindow()
        pTopWindow.ToggleCinematicWindow()
        pTopWindow.ToggleCinematicWindow()
                

def AbandonShipTimer(iCountdown, iAction):
		# Create an event - it's a thing that will call this function
		debug(__name__ + ", AbandonShipTimer")
		pTimerEvent = App.TGEvent_Create()
		pTimerEvent.SetEventType(iAction)
		pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())
					
		# Create a timer - it's a thing that will wait for a given time,then do something
		pTimer = App.TGTimer_Create()
		pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + iCountdown)
		pTimer.SetDelay(0)
		pTimer.SetDuration(0)
		pTimer.SetEvent(pTimerEvent)
		App.g_kTimerManager.AddTimer(pTimer)


# also from ReturnShuttles:
def ShipLike(ShipType, ShipLike):
    debug(__name__ + ", ShipLike")
    if (string.find(str(ShipType), ShipLike) != -1):
        return 1
    return 0


def EmergAbandon(pObject, pEvent):
	debug(__name__ + ", EmergAbandon")
	pObject.CallNextHandler(pEvent)

        # Get the ship that was hit
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
	sRace = GetRaceFromShip(pShip)
	
	# don't do anything for the player
	if pShip and not pShip.IsDead() and not pShip.IsDying() and pShip.GetAI() and sRace and not pShip.IsPlayerShip() and not pShip.GetObjID() in lAbandonDone:
		if pShip.GetHull() and pShip.GetHull().GetConditionPercentage() < 0.2:
			# always add them to the list, doesn't matter if we really did
			lAbandonDone.append(pShip.GetObjID())
			if not Races.has_key(sRace):
				return
			fPeaceValue = Races[sRace].GetPeaceValue()
			# use the peace value of the race to determine chance of abandon ship
			# also add a success quote of 30%
			if chance(int(fPeaceValue * 100)) and chance(iAbandonShipSuccessQuote):
				StartAbandonShip(pShip)
	

# lets create the Button now
def init():
        debug(__name__ + ", init")
        global AS_TIMER1, AS_END_SCENE_TIMER, lAbandonDone
	
	#if not IsMultiplayerHostAlone():
	#	return
	
	lAbandonDone = []
        AS_TIMER1 = Lib.LibEngineering.GetEngineeringNextEventType()
        AS_END_SCENE_TIMER = Lib.LibEngineering.GetEngineeringNextEventType()
        pXOMenu = Lib.LibEngineering.GetBridgeMenu("XO")
        MasterASButton = App.STMenu_CreateW(App.TGString("Abandon Ship"))
        pXOMenu.PrependChild(MasterASButton)
        Lib.LibEngineering.CreateMenuButton("Yes", "XO", __name__ + ".AbandonShip", 0, MasterASButton)
        App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(AS_TIMER1, __name__ + ".StartAbandonShip_Player")
        App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(AS_END_SCENE_TIMER, __name__ + ".AS_End_Cutscene")

	#Lib.LibEngineering.AddKeyBind("Abandon Ship", __name__ + ".AbandonShip", Group = "Ship")
	import Custom.Autoload.AbandonShip
	App.g_kEventManager.AddBroadcastPythonFuncHandler(Custom.Autoload.AbandonShip.ET_KEY_EVENT, MissionLib.GetMission(), __name__ + ".AbandonShip")

	# AI stuff
	if Lib.LibEngineering.CheckActiveMutator(sAIAbandonShipMutator) and (not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost()):
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, MissionLib.GetMission(), __name__ + ".EmergAbandon")


def Restart():
	debug(__name__ + ", Restart")
	global lAbandonDone
	lAbandonDone = []
