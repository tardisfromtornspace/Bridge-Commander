from bcdebug import debug
# LaunchShip.py
# March 22, 2002
#
# by Evan Light aka sleight42, all rights reserved
#
# Permission to redistribute this code as part of any other packaging requires
# the explicit permission of the author in advance.
#
#
##############################################################################

import App
import loadspacehelper
import MissionLib
import ftb.FTB_MissionLib
import ftb.ShipManager
import string

ShuttleCounter = 1
GetOnBoard = 0

# TODO: handle damage to shuttle bays by destroying ships contained within
# when damage == some integer increment X / Y where Y is the # of ships 
# contained in the bay

ET_MAY_LAUNCH_SHUTTLE_AGAIN = App.Mission_GetNextEventType()

#print "ftb.LaunchShip"

#### MISSION START INITIALIZER ####

def MissionStart():
    #print "LaunchShip.MissionStart"
    #### REGISTER EVENT HANDLERS
    debug(__name__ + ", MissionStart")
    App.g_kEventManager.AddBroadcastPythonFuncHandler( ET_MAY_LAUNCH_SHUTTLE_AGAIN, App.Game_GetCurrentGame(), "ftb.LaunchShipHandlers.MayLaunchShuttleAgain")

#### ASSORTED HELPERS #####

class LaunchLocation:
    def __init__(self, sShipClass, pProperty, pLaunchSystem):
        debug(__name__ + ", __init__")
        self.sShipClass = sShipClass
        self.pOEPProperty = pProperty
	self.pLaunchSystem = pLaunchSystem

##############################################################################
# Launches a friendly AI controlled Ship from the specified ship
# pLaunchingShip    - a ShipClass specifying the ship to launch from
# sShipClass        - the class of ship to launch (a String containing the
#                     actual module name for the ship as from /script/ships)
# iLaunchInterval   - the delay time before the pLaunchingShip will be allowed
#                     to launch another vessel
# aiScriptName      - the name of the AI module to use for this ship
def LaunchAIShip(pLaunchingShip, pOEPProperty, pLaunchSystem, sShipClass, iLaunchInterval, aiScriptName, commandable=None, bTimer=None, side="Friendly", sShipName=None, ForceDirectAI=0):
    debug(__name__ + ", LaunchAIShip")
    global ShuttleCounter
    pPlayer = MissionLib.GetPlayer()
    
    ShuttleCounter = ShuttleCounter + 1
    #sShipName = "Ship " + str( ShuttleCounter)
    # Change by Occas
    if sShipName == None:
            sShipName = sShipClass + " - " + str(ShuttleCounter)
    while(MissionLib.GetShip(sShipName)):
            ShuttleCounter = ShuttleCounter + 1
            sShipName = sShipClass + " - " + str(ShuttleCounter)

    # flicker shields
    pShields = pLaunchingShip.GetShields()
    if pShields and pShields.IsOn():
	    pShields.TurnOff()
	    pSequence = App.TGSequence_Create()
	    pSequence.AppendAction(App.TGScriptAction_Create("ftb.FTB_MissionLib", "TurnShieldsOn", pLaunchingShip.GetName()), 3)
	    pSequence.Play()
    if LaunchShipByClass(pLaunchingShip, pOEPProperty, pLaunchSystem, sShipClass, sShipName) == -1:
	    return -1
    pSet = pLaunchingShip.GetContainingSet()
    pLaunchedShip = App.ShipClass_GetObject(pSet, sShipName)
    if not pLaunchedShip:
            print("Unknown Shuttle Launching Error (LaunchShip.py): Ship was not created")
            return -1
    if side == "Friendly":
        ftb.FTB_MissionLib.AddObjectToFriendlyGroup(sShipName)
	if aiScriptName == "ftb.enemyAI":
		aiScriptName = "ftb.friendlyAI"
    elif side == "Neutral":
        ftb.FTB_MissionLib.AddObjectToNeutralGroup(sShipName)
    elif side == "Enemy":
        ftb.FTB_MissionLib.AddObjectToEnemyGroup(sShipName)
	if aiScriptName == "ftb.friendlyAI":
		aiScriptName = "ftb.enemyAI"
    if bTimer:
        StartLaunchIntervalTimer(pLaunchSystem, iLaunchInterval) 
    if commandable:
        MissionLib.AddCommandableShip(sShipName)
    
    if GetOnBoard and pPlayer.GetObjID() == pLaunchingShip.GetObjID():
	debug(__name__ + ", LaunchAIShip SetTarget")
	pPlayer.SetTarget(pLaunchingShip.GetName())
    else:
	pHull = pLaunchingShip.GetHull()
	pLauncherShipName = pLaunchingShip.GetName()
	pRadius = pHull.GetRadius()
        # set AI
        if not (GetOnBoard and pPlayer.GetObjID() == pLaunchingShip.GetObjID()):
                if ForceDirectAI == 0:
	                pDoneAI = aiScriptName
	                pTempAI = __import__ ("ftb.PassThroughAI")
                        pAI = pTempAI.CreateAI(pLaunchedShip, pDoneAI, pRadius, pLauncherShipName)
                        pLaunchingShip.SetAI(pAI)
                else:
                        try:
                                aiModule = __import__(aiScriptName)
                                pLaunchingShip.SetAI(aiModule.CreateAI(pLaunchedShip))
                        except ValueError:
				print "Error Loading", aiScriptName
    return 0


##############################################################################
# Launches a ship from a source ship
# pLaunchingShip    - a ShipClass specifying the ship to launch from
# sShipClass        - the class of ship to launch (a String containing the
#                     actual module name for the ship as from /script/ships)
# sLaunchedShipName - the DisplayName for the new ship
def LaunchShipByClass( pLaunchingShip, pOEPProperty, pLaunchSystem, sShipClass, sLaunchedShipName):
        debug(__name__ + ", LaunchShipByClass")
        "Creates a simple TGSequence to launch a ship"

        if( not pLaunchingShip) or ( pLaunchingShip.IsDoingInSystemWarp() == 1) or not pLaunchingShip.GetContainingSet() or pLaunchingShip.GetContainingSet().GetName() == "warp":
                return -1
        pSequence = App.TGSequence_Create()
        launchLoc = LaunchLocation(sShipClass, pOEPProperty, pLaunchSystem)
        pSequence.AppendAction(App.TGScriptAction_Create(__name__, "LaunchObject", pLaunchingShip.GetObjID(), sLaunchedShipName, launchLoc, pLaunchingShip))
        pSequence.Play()
        return 0


##############################################################################
# Creates a Timer that controls when the launching system will be permitted
# to launch another object
# pLaunchingShip    - a ShipClass specifying the ship to launch from
# iLaunchInterval   - the delay time before the pLaunchingShip will be allowed
#                     to launch another vessel
def StartLaunchIntervalTimer( pSystem, iLaunchInterval):
    debug(__name__ + ", StartLaunchIntervalTimer")
    pEvent = App.TGEvent_Create()
    #pEvent.SetObjPtr( pSystem)
    pEvent.SetEventType( ET_MAY_LAUNCH_SHUTTLE_AGAIN)
    #pEvent.SetSource( pSystem)
    pEvent.SetDestination( pSystem)
    pTimer = App.TGTimer_Create()
    pTimer.SetTimerStart( App.g_kUtopiaModule.GetGameTime() + iLaunchInterval)
    pTimer.SetDelay( 0)
    pTimer.SetDuration( 0)
    pTimer.SetEvent( pEvent)
    App.g_kTimerManager.AddTimer( pTimer)

# NOTE: Lifted from Actions.ShipScriptActions by TG
# Minor modifications by EL
def LaunchObject(pAction, iShipID, pcName, launchLoc, pLaunchingShip):
    debug(__name__ + ", LaunchObject")
    "Launches an object from the given ship."

    pGame = App.Game_GetCurrentGame()
    pMultGame = App.MultiplayerGame_Cast(pGame)
    pShip = App.ShipClass_GetObjectByID(None, iShipID)
    pPlayer = MissionLib.GetPlayer()
    if not pShip:
	debug(__name__ + ", LaunchObject Return no ship")
        return 0

    if pMultGame:
	pGame = pMultGame

    # Find any object emitter properties on the ship.
    pPropSet = pShip.GetPropertySet()
    pFTBCarrier = ftb.ShipManager.GetShip(pShip)

    if (launchLoc.pLaunchSystem and launchLoc.pLaunchSystem.GetParentShip() and launchLoc.pLaunchSystem.GetParentShip().GetObjID() != iShipID) or not pFTBCarrier or not hasattr(pFTBCarrier, "GetLaunchers"):
        print "Error: Intercepting critical Lauching Error in LaunchShip.LaunchObject()"
        print "%s (%s) tried to launch %s" % (pShip.GetName(), pShip.GetScript(), launchLoc.sShipClass)
        print "If you can reproduce this error, contact a BC scripter please"
	debug(__name__ + ", LaunchObject Return Error")
        return 0

    pLaunchProperty = App.ObjectEmitterProperty_Cast(launchLoc.pOEPProperty)

    if pLaunchProperty:
        # We found a valid launch bay. Create the object, and point it 
        # facing out of the shuttle bay.

        pSet = pShip.GetContainingSet()

        # Create the object.
        pcScript = launchLoc.sShipClass
	debug(__name__ + ", LaunchObject Launch %s" % (launchLoc.sShipClass))
        if not pcScript:
            # We can't create anything.
	    debug(__name__ + ", LaunchObject Return no script")
            return 0

        # Create the object.
        pObject = loadspacehelper.CreateShip(pcScript, pSet, pcName, "", 0, 1)

        if pObject:
            pObject.EnableCollisionsWith(pShip, 0)
	    pShip.EnableCollisionsWith(pObject, 0)
            if GetOnBoard and string.find(string.lower(pcScript), "mine") == -1 and pPlayer.GetObjID() == pLaunchingShip.GetObjID():
            	pNetwork = App.g_kUtopiaModule.GetNetwork()
            	if pNetwork:
			try:
				from Custom.MultiplayerExtra.MultiplayerLib import SetNewNetPlayerID, MPSetAutoAI
            			SetNewNetPlayerID(pPlayer, pObject.GetNetPlayerID())
				#MPSetAutoAI(pPlayer)
			except ImportError:
				pass
            		pObject.SetNetPlayerID(pNetwork.GetLocalID())
            	pGame.SetPlayer(pObject)
		if App.g_kUtopiaModule.IsMultiplayer():
			try:
				from Custom.MultiplayerExtra.MultiplayerLib import CreateShipFromShip, SetStopAI
				pPlayerOld = CreateShipFromShip(pPlayer)
				SetStopAI(pPlayerOld)
			except ImportError:
				pass

            # Now change the position and facing of the object to match the 
            #emitter.
            pFwd = pLaunchProperty.GetForward()
            pUp = pLaunchProperty.GetUp()

            pRotation = pShip.GetWorldRotation()

            pPosition = pLaunchProperty.GetPosition()
            pPosition.MultMatrixLeft(pRotation)
            pPosition.Add(pShip.GetWorldLocation())
            pObject.SetTranslate(pPosition)

            pFwd.MultMatrixLeft(pRotation)
            pUp.MultMatrixLeft(pRotation)
            pObject.AlignToVectors(pFwd, pUp)
            pObject.UpdateNodeOnly()

            # Don't collide with the ship that created us.
            pObject.EnableCollisionsWith(pShip, 0)
            # tell other clients to disable collision
            if App.g_kUtopiaModule.IsMultiplayer():
                ftb.FTB_MissionLib.MultiPlayerEnableCollisionWith(pObject, pShip, 0)
            #TODO: Re-enable collisions with pShip using a TGTimer

    # Woohoo, we're done.
    debug(__name__ + ", LaunchObject End")
    return 0
