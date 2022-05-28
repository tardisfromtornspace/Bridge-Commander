from bcdebug import debug
#!/usr/bin/python1.5
## This Mod was created by Defiant <mail@defiant.homedns.org>
## and is under the GNU GPL License (see README)!
## 
## Basic TractorTargetDocked() and TractorBeamOn() are from the SDK and
## some parts of ftb.FTB_MissionLib.GetShuttlesInBay(), ftb.FTB_MissionLib.IncreaseShuttleCount() and ftb.FTB_MissionLib.ShuttlesInBayOfThisType()
## are copied from sleight42 Shuttle Launching Framework.
##
## ftb.FTB_MissionLib.SetMaxShuttlesInBay() & ftb.FTB_MissionLib.GetOEPs() by Sim Rex
## Quote by Sim Rex: "btw, I have no idea what the ftb guys were smoking when they came up
## with this very convoluted way of launching stuff...."
##
# Functions:
# ftb.FTB_MissionLib.GetShuttlesInBay()	-	Returns the count of _all_ Shuttles in all bays
#	Arguments: sFiringShipName (The Name of the Carrer Ship)
# ftb.FTB_MissionLib.IncreaseShuttleCount()	-	Add a Ship to the Carrier
#	Arguments: Shuttle (The name of the Ship we want to add)
# ftb.FTB_MissionLib.GetShuttleBaySize()	-	Returns the Shuttle bay size
#	Arguments: pShip (Shipclass)
# ftb.FTB_MissionLib.ShuttlesInBayOfThisType()	-	Returns the count of Shuttles in the bay.
#	Arguments: Type (Ship Type)
# ftb.FTB_MissionLib.FindAShuttleBay()	-	Returns the first Shuttle bay Hull Property
#	Arguments: pShip (Shipclass)
# ftb.FTB_MissionLib.SetMaxShuttlesInBay()	-	Returns how much Shuttles a Ship can carry
#	Arguments: OurShipName (The Name of the Carrer Ship)
# ftb.FTB_MissionLib.GetOEPs()		-	Returns the whole OEP list.
# ftb.FTB_MissionLib.GetFirstShuttleBayName()	-	Returns the name of the first Shuttle Bay
# GetIgnoredTractors()	-	Tractors not to use for docking
#	Arguments: OurShipName (The Name of the Carrer Ship)
# Transport()		-	Changes the Players Ship with a Sequence
# TractorTargetDocked()	-	Event handler called when tractor target has docked with ship.
#	Arguments: pObject, pEvent
# TractorBeamOn()		-	Event handler called when tractor beam starts hitting a target.
#	Arguments: pObject, pEvent
# ReturnWithoutTractor()	-	Same as TractorTargetDocked() but without Tractors. Maybe called by a button
#	Arguments: pObject, pEvent, NotHost (If the Player's Ship is not the Host set to 1, standard 0)
##
## Have Fun!

import App
import MissionLib
import string
import ftb.ShipManager
import ftb.LaunchShipHandlers
import AI.Compound.ReturnShuttle
# import the stuff we moved to the FTB MissionLib
import ftb.FTB_MissionLib
from Custom.MultiplayerExtra.MultiplayerLib import DeleteObjectFromSet

# Global Vars
verbose                 = 0 # Be verbose
g_pMissionDatabase      = None

# dics
EventToShip_dic         = {}
ShuttleBayInUse_dic     = {}

# Events - we set them up later.
SHUTTLE_COUNT_TIMER     = None
MP_SET_TRACTOR_MODE = 195


def ShuttleBayNavPoint(pShip = None):
	debug(__name__ + ", ShuttleBayNavPoint")
	ShuttleBay = ftb.FTB_MissionLib.GetShuttleOEP(MissionLib.GetShip(pShip))
	ShuttleBay = App.ObjectEmitterProperty_Cast(ShuttleBay)
	if ShuttleBay:
		print("Using Shuttle Bay", ShuttleBay.GetName().GetCString())


def IsPod(ShuttleType):
    debug(__name__ + ", IsPod")
    if (ShuttleType == "EscapePod" or ShuttleType == "card pod" or ShuttleType == "defpod" or ShuttleType == "greenmisc" or ShuttleType == "Galaxy Escape Pod" or ShuttleType == "Green Escape Pod"):
        return 1
    return 0


# Start the Timer
def IncreaseShuttleCountStartTimer(Shuttle, sFiringShipName = None):
        debug(__name__ + ", IncreaseShuttleCountStartTimer")
        global EventToShip_dic, ShuttleBayInUse_dic

	# Small test if the Tractor Firing Ship is not the Players Ships
	if (Shuttle.GetName() == App.Game_GetCurrentGame().GetPlayer().GetName()):
		# then Beam
		Transport(sFiringShipName)

        ShuttleType = ftb.FTB_MissionLib.GetShipType(Shuttle)

        if (IsPod(ShuttleType) == 1):
            # Pods won't be addded to the Launcher
            return

        # If verbose add them without timer - faster for working on it.
        if verbose:
            ftb.FTB_MissionLib.IncreaseShuttleCount(ShuttleType, sFiringShipName)
            return
	
        # Create an event - it's a thing that will call this function
	pTimerEvent = App.TGEvent_Create()
	pTimerEvent.SetEventType(SHUTTLE_COUNT_TIMER)
	pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())

        # Save the Ships into the dic here
        EventToShip_dic[str(pTimerEvent)] = [ShuttleType, sFiringShipName]
        # Lock the bay
        ShuttleBayInUse_dic[sFiringShipName] = 1

	# Create a timer - it's a thing that will wait for a given time, then do something
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 10 + App.g_kSystemWrapper.GetRandomNumber(10))
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pTimerEvent)
	App.g_kTimerManager.AddTimer(pTimer)


# Timer finished, find the Ships and pass it to ftb.FTB_MissionLib.IncreaseShuttleCount()
def IncreaseShuttleCountStartInit(pObject, pEvent):
    debug(__name__ + ", IncreaseShuttleCountStartInit")
    global EventToShip_dic, verbose, ShuttleBayInUse_dic
    # Now get the Event in our dic and grep the Ships out.
    if not EventToShip_dic.has_key(str(pEvent)):
        print("ReturnShuttles: IncreaseShuttleCountStartInit called by nothing?", EventToShip_dic.keys())
        return
    ShuttleType = EventToShip_dic[str(pEvent)][0]
    sFiringShipName = EventToShip_dic[str(pEvent)][1]
    if verbose: print("Ships from Timer are: ", ShuttleType, sFiringShipName)
    # finally delete the dic.
    del EventToShip_dic[str(pEvent)]
    del ShuttleBayInUse_dic[sFiringShipName]
    # yeehah we are done with the timer.
    ftb.FTB_MissionLib.IncreaseShuttleCount(ShuttleType, sFiringShipName)
    ReturnShuttlesSay("ShipAdded", "Science")



# Modified Version of  Sim Rex's ftb.FTB_MissionLib.SetMaxShuttlesInBay()
def GetIgnoredTractors(OurShipName):
	debug(__name__ + ", GetIgnoredTractors")
	global sFiringShipName, verbose
        
        if not sFiringShipName:
            if verbose: print("Problem: No Firing Ship - Using Players Ship as default")
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()
            
	pCarrier = ftb.ShipManager.GetShip(MissionLib.GetShip(sFiringShipName))
	if hasattr(pCarrier, "IgnoreTractors"):
		return pCarrier.IgnoreTractors()
	else:
		return []


def Transport(sFiringShipName = None):        
        debug(__name__ + ", Transport")
        if (sFiringShipName == None):
            sFiringShipName = App.Game_GetCurrentPlayer().GetName()
	
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pShip = MissionLib.GetShip(sFiringShipName)
	pSet = pShip.GetContainingSet()

	pSequence = App.TGSequence_Create()
	pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene")
	pSequence.AppendAction (pAction)
	#pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
	#pSequence.AppendAction(pAction)
	pAction	= App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName())
	pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pSet.GetName(), sFiringShipName)
	pSequence.AppendAction(pAction)
        pSetPlayerAction = App.TGScriptAction_Create(__name__, "SetPlayerAction", pPlayer, MissionLib.GetShip(sFiringShipName))
	pSequence.AppendAction(pSetPlayerAction)
	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pShip.GetContainingSet().GetName())
	pSequence.AppendAction(pAction, 2)
	#pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StopCinematicMode")
	#pSequence.AppendAction(pAction)
	pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
	pSequence.AppendAction(pAction)
	pSequence.Play()

        # clear AI
        pPlayer = pGame.GetPlayer()
        MissionLib.SetPlayerAI("Captain", None)
        pPlayer.ClearAI()

        # Force switch to Tactical if we have no Bridge
        if not App.g_kSetManager.GetSet("bridge"):
                MissionLib.CreateTimer(ftb.FTB_MissionLib.GetFTBNextEventType(), __name__ + ".ForceTacticalVisible", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)


def ForceTacticalVisible(pObject, pEvent):
        debug(__name__ + ", ForceTacticalVisible")
        pTopWindow = App.TopWindow_GetTopWindow()
        pTopWindow.ToggleCinematicWindow()
        pTopWindow.ToggleCinematicWindow()


def SetPlayerAction(pAction, pOldPlayer, pNewPlayer):
        debug(__name__ + ", SetPlayerAction")
        pGame = App.Game_GetCurrentGame()
	pMultGame = App.MultiplayerGame_Cast(pGame)
	if pMultGame:
		pGame = pMultGame
	
        if App.g_kUtopiaModule.IsClient():
                pTargetNetId = pNewPlayer.GetNetPlayerID()
                pPlayerNetId = pOldPlayer.GetNetPlayerID()

        pGame.SetPlayer(pNewPlayer)
        
        if App.g_kUtopiaModule.IsClient():
		try:
			from Custom.MultiplayerExtra.MultiplayerLib import SetNewNetPlayerID
			SetNewNetPlayerID(pOldPlayer, pTargetNetId)
			SetNewNetPlayerID(pNewPlayer, pPlayerNetId)
		except:
			pass
        
        return 0


def ReturnShuttlesSay(SayString, Person = "Felix"):
        debug(__name__ + ", ReturnShuttlesSay")
        global g_pMissionDatabase
        pBridge = App.g_kSetManager.GetSet('bridge')
        g_pScience = App.CharacterClass_GetObject(pBridge, "Science")
        g_pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
        g_pBrex	= App.CharacterClass_GetObject(pBridge, "Engineer")

        if (Person == "Science"):
            Person = g_pScience
        elif (Person == "Brex"):
            Person = g_pBrex
        else:
            Person = g_pFelix

        pSequence = App.TGSequence_Create()
        pSequence.AppendAction(App.CharacterAction_Create(Person, App.CharacterAction.AT_SAY_LINE, SayString, None, 0, g_pMissionDatabase))
        pSequence.Play()  


################################################################################
##	TractorTargetDocked()
##
##	Event handler called when tractor target has docked with ship.
##
##	Args:	pTGObject	- The TGObject object
##			pEvent		- The event that was sent to the object
##
##	Return:	None
################################################################################
def TractorTargetDocked(pTGObject, pEvent):
        debug(__name__ + ", TractorTargetDocked")
        global verbose, g_pMissionDatabase, ShuttleBayInUse_dic
	if verbose: print("Calling TractorTargetDocked()")

        pTGObject.CallNextHandler(pEvent)

	# Get the object that was docked and it's name
	pObject	= App.ShipClass_Cast(pEvent.GetObjPtr())
        sFiringShipName = App.ShipClass_Cast(pEvent.GetDestination()).GetName()
        
	if (pObject == None):
		return
	pShip	= App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip == None):
		return
	
	# sShipName is not used here
	sShipName	= pShip.GetName()
        ShipType = ftb.FTB_MissionLib.GetShipType(pShip)

        # check locked Bays
        if ShuttleBayInUse_dic.has_key(sFiringShipName):
                ReturnShuttlesSay("BayLocked", "Science")  
                return

	# Remove the Object from the set
	if pObject:
		DeleteObjectFromSet(pObject.GetContainingSet(), pObject)
	
	if (IsPod(ShipType) == 1):
		if verbose: print("Play the audio line that will let the player know pod is docked")
		FelixLineIs = "E6M2PodDocked"
	else:
		# and the Audio Line is:
		FelixLineIs = "ShipDocked"
        
        # Increase the captured count
        IncreaseShuttleCountStartTimer(pObject, sFiringShipName)
        
	ReturnShuttlesSay(FelixLineIs)

	if verbose: print("Tractor Target Docked is finished and done")


################################################################################
##	TractorBeamOn()
##
##	Event handler called when tractor beam starts hitting a target.  Checks to
##	see if the target is a pod and starts docking behavior if it is.
##
##	Args:	TGObject	- The TGObject object.
##			pEvent		- The event that was sent.
##
##	Return:	None
################################################################################
def TractorBeamOn(TGObject, pEvent):
        debug(__name__ + ", TractorBeamOn")
        global verbose, sFiringShipName, sTargetName, ShuttleBayInUse_dic
	# Get the event destination (the thing hit by tractor beam)
	if verbose: print("Tractor Beam on")
	
        TGObject.CallNextHandler(pEvent)
        
	ShuttleBaySize		= None
	MaxShuttlesInBay	= None
	pDocking			= None
	
	# Do we have a Ship?
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip == None):
		if verbose: print("failed - no Ship")
		return
	
	# Get the tractor beam system that fired so we
	# can set it's behavior.
	pTractorProjector	= App.TractorBeamProjector_Cast(pEvent.GetSource())
	pTractorSystem		= App.TractorBeamSystem_Cast(pTractorProjector.GetParentSubsystem())
	# Get the name of the ship that fired
	pShip = pTractorSystem.GetParentShip()
	if (pShip == None):
		return
	sFiringShipName = pShip.GetName()
	if not sFiringShipName:
		return
	pTargetShip = pShip.GetTarget()
	if not pTargetShip:
		return
	sTargetName = pTargetShip.GetName()
	
	pTargetShip = MissionLib.GetShip(sTargetName)
	if not ftb.FTB_MissionLib.IsMultiplayerHostAlone() and pTargetShip.GetNetPlayerID() >= 0:
		print "Can not Dock a Player ship"
		return
	
        if pTractorSystem.GetMode() != pTractorSystem.TBS_DOCK_STAGE_1:
                print "Return Shuttles Warning: Tractor System not in Docking Mode"
                return
	
	# Get Target Ship Name
        if not hasattr(MissionLib.GetShip(sFiringShipName), "GetTarget"):
            return
        
	if not MissionLib.GetShip(sFiringShipName).GetTarget():
		return
	
        # check locked Bays
        if ShuttleBayInUse_dic.has_key(sFiringShipName):
                ReturnShuttlesSay("BayLocked", "Science")  
                return
        
	#Lets try to get the size of our Target ship
	TargetHullSize = MissionLib.GetShip(sTargetName).GetRadius()
	if verbose: print("Size of the Target:", TargetHullSize)
	
	if not ftb.FTB_MissionLib.FindAShuttleBay(pShip):
		if verbose: print("No Shuttle Bay - return")
		return
	
	# Test if this Tractor can be used to Dock:
	if ( GetIgnoredTractors(sFiringShipName).count(pTractorProjector.GetName()) != 0 ):
		return
	
	#and the size of our Shuttle Bay
	ShuttleBaySize=ftb.FTB_MissionLib.GetShuttleBaySize(pShip)
	if (ShuttleBaySize == None):
		if verbose: print("ShuttleBaySize not set")
		return
	if verbose: print("Size of our Shuttle Bay:", ShuttleBaySize)
	
	MaxShuttlesInBay=ftb.FTB_MissionLib.SetMaxShuttlesInBay(sFiringShipName)
	if verbose: print("Max Shuttles we can carry:", MaxShuttlesInBay)
	
	ShuttlesInBay=ftb.FTB_MissionLib.GetShuttlesInBay(sFiringShipName)
	if verbose: print("Shuttles currently in Bay:", ShuttlesInBay)
	
	# See if the ship is small enough to fit into out Bay
	if (TargetHullSize < ShuttleBaySize):

                ShipType = ftb.FTB_MissionLib.GetShipType(pTargetShip)
		if (IsPod(ShipType) == 1):
			# It's a pod
			if verbose: print("Playing Brex's .attempting to dock pod. line")	
			ReturnShuttlesSay("E6M2FelixDockPod", "Brex")
			
			# set the tractor beam to pull in and dock the pod
			pTractorSystem.SetMode(pTractorSystem.TBS_DOCK_STAGE_1)
			if App.g_kUtopiaModule.IsMultiplayer():
				MPSendTractorBeamSettings(pShip, pTractorSystem.TBS_DOCK_STAGE_1)
		else:
			# It's not a Pod
			# Test if we got enough space in our Bay left
			if ( MaxShuttlesInBay > ShuttlesInBay ):
				if verbose: print("There is enough space left in our Bay")
				if verbose: print("Target will be docked")
				
				if verbose: print("Playing Brex's attempting to dock line")	
				ReturnShuttlesSay("FelixDockShip", "Brex")

				# set the tractor beam to pull in and dock the pod
				pTractorSystem.SetMode(pTractorSystem.TBS_DOCK_STAGE_1)
				if App.g_kUtopiaModule.IsMultiplayer():
					MPSendTractorBeamSettings(pShip, pTractorSystem.TBS_DOCK_STAGE_1)
			else:
				ReturnShuttlesSay("NoSpaceLeft", "Science")
				return
	else:
                print("Target is NOT small enough to get in our Bay")
		print("Size of the Shuttle Bay: ", ShuttleBaySize)
		print("Size of the Target: ", TargetHullSize)


	# We're done.  Let any other handlers for this event handle it.
	if verbose: print("Tractor beam on finished")
	

# This is a copy of TractorBeamOn() but without using the Tractor
def ReturnWithoutTractor(pObject, pEvent, NotHost = 0):
        debug(__name__ + ", ReturnWithoutTractor")
        global verbose, sFiringShipName, sTargetName, ShuttleBayInUse_dic

	# Get the event destination (the thing hit by tractor beam)
	if verbose: print("Returning without Tractor")

        pGame                   = App.Game_GetCurrentGame()
        pEpisode	        = pGame.GetCurrentEpisode()
        pMission	        = pEpisode.GetCurrentMission()
        pBridge 		= App.g_kSetManager.GetSet("bridge")
        pPlayer                 = MissionLib.GetPlayer()
        pTarget                 = pPlayer.GetTarget()
        pFriendlies             = pMission.GetFriendlyGroup()
        ShuttleBaySize		= None
        MaxShuttlesInBay	= None
        pDocking		= None

        # Check the Target
        if not pTarget:
                if verbose: print("No Target")
                return
        if not pFriendlies.IsNameInGroup(pTarget.GetName()):
                if verbose: print("Target is not friendly - failed.")
                return

	# Get the name of the ship that fired
	if (NotHost == 0):
		#pShip = pPlayer # currently it is only the Player
		pShip = MissionLib.GetShip(ftb.LaunchShipHandlers.ShuttleLaunchShip)
		sTarget = App.ShipClass_Cast(pTarget)
	else:
		pShip = App.ShipClass_Cast(pTarget)
		sTarget = pPlayer
	sFiringShipName = pShip.GetName()
	sTargetName = sTarget.GetName()

        # Same Ship?
        if (sFiringShipName == sTargetName):
            return

        # check locked Bays
        if ShuttleBayInUse_dic.has_key(sFiringShipName):
                ReturnShuttlesSay("BayLocked", "Science")  
                return
        if not sTarget.GetImpulseEngineSubsystem():
                ReturnShuttlesSay("UseTractor", "Science")
                return

	if verbose: print("Target Ship in Tractor is: " + sTargetName)
	
	#Lets try to get the size of our Target ship
	TargetHullSize = MissionLib.GetShip(sTargetName).GetRadius()
	if verbose: print("Size of the Target:", TargetHullSize)
	
	#and the size of our Shuttle Bay
	ShuttleBaySize=ftb.FTB_MissionLib.GetShuttleBaySize(pShip, MissionLib.GetShip(sTargetName))
	if (ShuttleBaySize == None):
		if verbose: print("ShuttleBaySize not set")
		return
	if verbose: print("Size of our Shuttle Bay:", ShuttleBaySize)
	
	MaxShuttlesInBay=ftb.FTB_MissionLib.SetMaxShuttlesInBay(sFiringShipName)
	if verbose: print("Max Shuttles we can carry:", MaxShuttlesInBay)
	
	ShuttlesInBay=ftb.FTB_MissionLib.GetShuttlesInBay(sFiringShipName)
	if verbose: print("Shuttles currently in Bay:", ShuttlesInBay)
	
        # Navpoint stuff
        ShuttleBayNavPoint(sFiringShipName)

	# See if the ship is small enough to fit into out Bay
	if (TargetHullSize < ShuttleBaySize):
            # Test if we got enough space in our Bay left
            if ( MaxShuttlesInBay > ShuttlesInBay ):
                if verbose: print("There is enough space left in our Bay")
                if verbose: print("Target will be docked")

                sTarget.SetAI(AI.Compound.ReturnShuttle.CreateAI(sTarget, sFiringShipName))
            else:
                ReturnShuttlesSay("NoSpaceLeft", "Science")
                return
        else:
                ReturnShuttlesSay("TargetTooBig", "Science")
                print("Target is NOT small enough to get in our Bay")
                print("Size of the Shuttle Bay: ", ShuttleBaySize)
                print("Size of the Target: ", TargetHullSize)


def MissionStart(SHUTTLE_COUNT_TIMER_CALLER):
    debug(__name__ + ", MissionStart")
    global SHUTTLE_COUNT_TIMER, g_pMissionDatabase, verbose
    pGame                   = App.Game_GetCurrentGame()
    pEpisode                = pGame.GetCurrentEpisode()
    pMission                = pEpisode.GetCurrentMission()
    SHUTTLE_COUNT_TIMER     = SHUTTLE_COUNT_TIMER_CALLER
    g_pMissionDatabase      = pMission.SetDatabase("data/TGL/QuickBattle/ReturnShuttles.tgl")
    # Tractor beam target docked event
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_TARGET_DOCKED, pMission, __name__+ ".TractorTargetDocked")
    # Tractor beam starts hitting event
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, pMission, __name__+ ".TractorBeamOn")
    # Shuttle add timer
    App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(SHUTTLE_COUNT_TIMER, __name__ + ".IncreaseShuttleCountStartInit")


    if verbose: print("Loading Defiants event Handlers to get the Shuttles back")


def MPSendTractorBeamSettings(pShip, iMode):
	debug(__name__ + ", MPSendTractorBeamSettings")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
        # Now send a message to everybody else that the score was updated.
        # allocate the message.
        pMessage = App.TGMessage_Create()
        pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
        # Setup the stream.
        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
        kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.

        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(MP_SET_TRACTOR_MODE))

        # Write our Message
        kStream.WriteInt(pShip.GetObjID())
        kStream.WriteInt(iMode)

        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)

        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

        # We're done.  Close the buffer.
        kStream.CloseBuffer()
