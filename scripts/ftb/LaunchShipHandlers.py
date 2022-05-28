from bcdebug import debug
# LaunchShipHandlers.py
# April 17, 2002
#
# by Evan Light aka sleight42, all rights reserved
#
# Permission to redistribute this code as part of any other packaging requires
# the explicit permission of the author in advance.
##############################################################################

import App
import loadspacehelper
import MissionLib
import QuickBattle.QuickBattle
import ftb.ShipManager
import ftb.GUIUtils
import ftb.LauncherManager
import ReturnShuttles
import ftb.FTB_MissionLib
import ftb.LaunchShip

# import Custom.Carriers.Dauntless

# TODO: Have the Launchers/LauncherGroups own the buttons
# TODO: handle damage to shuttle bays by destroying ships contained within
# TODO: Re-enable collision detection after launch
# when damage == some integer increment X / Y where Y is the # of ships 
# contained in the bay

ET_LAUNCH_SHIP = None
ET_TOGGLE_LAUNCH_TYPE = None
ET_TOGGLE_SHIP_TYPE = None
ET_RETURN_SHIP = None

pToggleLaunchTypeButton = []
pLaunchButton = []
ButtonToggleLaunchType = None # Thats our LaunchType -Button. We use this one instead of crashing the game - Defiant 
launchTypeSave = None # Save the last Button state
launchTypeSaveNum = 0
pShipMenu = None
ShuttleLaunchShip = None # Ship we launch From
lToggleLaunchTypeShowErrorDone = []

#### EVENT HANDLERS ####


# Switches the Launch Type
def ToggleLaunchType(pObject, pEvent):
    debug(__name__ + ", ToggleLaunchType")
    global pLaunchButton, pToggleLaunchTypeButton, ShuttleLaunchShip, pShipMenu, lToggleLaunchTypeShowErrorDone
    
    pLaunchShip = MissionLib.GetShip(ShuttleLaunchShip)
    try:
    	pFTBCarrier = ftb.ShipManager.GetShip(pLaunchShip)
    except AttributeError:
	if not ShuttleLaunchShip in lToggleLaunchTypeShowErrorDone:
		print "Shuttle Launching Error: ship %s has no Shuttle launching points" % str(ShuttleLaunchShip)
		lToggleLaunchTypeShowErrorDone.append(ShuttleLaunchShip)
	return
    if not pFTBCarrier: # Our previous Ship maybe destroyed
        pShipMenu.SetName(App.TGString("None" + " " + "Selected"))
        return
    if not hasattr(pFTBCarrier, "GetLaunchers"): # Our previous Ship maybe not configured to have Shuttles
        pShipMenu.SetName(App.TGString("None" + " " + "Selected"))
        return
    pFTBLauncher = pFTBCarrier.GetLaunchers() # No we can't do it with the Event Number here.
    numTypes = len(pFTBLauncher)
    for index in range(numTypes):
        launchType = pFTBLauncher[index].NextLaunchType()
    
    SetToggleLaunchButton() # rename the Button


# rename the Button - by Defiant
# most stuff is off AddLaunchButtons()
def SetToggleLaunchButton():
    debug(__name__ + ", SetToggleLaunchButton")
    global ButtonToggleLaunchType, launchTypeSave, launchTypeSaveNum, pLaunchButton, ShuttleLaunchShip
    
    pLaunchShip = MissionLib.GetShip(ShuttleLaunchShip)
    pFTBCarrier = ftb.ShipManager.GetShip(pLaunchShip)
    if not hasattr(pFTBCarrier, "GetLaunchers"): # Our previous Ship maybe destroyed or is not configured to have Shuttles
        pShipMenu.SetName(App.TGString("None" + " " + "Selected"))
        return
    pFTBLauncher = pFTBCarrier.GetLaunchers()
    numTypes = len(pFTBLauncher)
    launcherIndex = 0

    # cycle our whole Shuttle Type list
    for index in range( numTypes):
        launchType = pFTBLauncher[index].GetLaunchType()
        numLaunches =  pFTBLauncher[index].GetNumLaunches(launchType)
        buttonLabel = launchType + ": " + str(numLaunches)
        ButtonToggleLaunchType.SetName(App.TGString(buttonLabel))
        launcherIndex = index
    
    # Test if the the Start Button is disabled but we still have Shuttles
    if (numLaunches > 0 and not pLaunchButton[launcherIndex].IsEnabled()):
        # Now lets make the launching Framework operational again.
        launcher = ftb.LauncherManager.GetLauncher(ftb.FTB_MissionLib.GetFirstShuttleBayName(), pLaunchShip)
	if launcher:
		pLaunchButton[launcherIndex].SetEnabled()
        	launcher.SetClearToLaunch(1)
    
    # Saves the vars. We can use them for testing later.
    launchTypeSave = launchType
    launchTypeSaveNum = numLaunches


def MayLaunchShuttleAgain( pObject, pEvent):
    debug(__name__ + ", MayLaunchShuttleAgain")
    global pLaunchButton, ShuttleLaunchShip
    if not ShuttleLaunchShip:
	    return
    pLaunchShip = MissionLib.GetShip(ShuttleLaunchShip)
    pSystem = App.ShipSubsystem_Cast( pEvent.GetDestination())
    if not pSystem:
            return
    pFTBLauncher = ftb.LauncherManager.GetLauncherBySystem(pSystem)
    pFTBLauncher.SetClearToLaunch(1)
    pFTBCarrier = ftb.ShipManager.GetShip(pLaunchShip)
    launcherIndex = -1 
    if not hasattr(pFTBCarrier, "GetLaunchers"):
        return
    for index in range( len( pFTBCarrier.GetLaunchers())):
        if pFTBCarrier.GetLaunchers()[index].Equals( pFTBLauncher):
            launcherIndex = index
            break
    if( launcherIndex == -1):
        return
    pLaunchButton[launcherIndex].SetEnabled()


# Launches the Ship
def LaunchShip( pObject, pEvent):
    debug(__name__ + ", LaunchShip")
    global pLaunchButton, launchTypeSave, launchTypeSaveNum, ShuttleLaunchShip, pShipMenu
    
    pLaunchShip = MissionLib.GetShip(ShuttleLaunchShip)
    pFTBCarrier = ftb.ShipManager.GetShip(pLaunchShip)
    if not pFTBCarrier: # Our previous Ship maybe destroyed
        pShipMenu.SetName(App.TGString("None" + " " + "Selected"))
        return
    if pLaunchShip.IsCloaked(): # No we can't launch Ships while cloaked
        print("Sorry, can't launch while cloaked")
        return

    if not hasattr(pFTBCarrier, "GetLaunchers"): # Our previous Ship maybe destroyed or is not configured to have Shuttles
        pShipMenu.SetName(App.TGString("None" + " " + "Selected"))
        return
    
    pFTBLauncher = pFTBCarrier.GetLaunchers()[0]
    sShipName = pFTBLauncher.GetLaunchType()
    
    # test for the right selection here.
    if (launchTypeSaveNum != pFTBLauncher.GetNumLaunches(sShipName) or str(launchTypeSave) != str(sShipName)):
        ToggleLaunchType(None, None)
        return
    
    ftb.FTB_MissionLib.LaunchShip(pLaunchShip)

    if( pFTBLauncher.HasMoreLaunches( sShipName) == 0):
        pFTBLauncher.NextLaunchType()
    launchTypeSave = pFTBLauncher
    SetToggleLaunchButton()
    pLaunchButton[0].SetDisabled()


def ObjectKilledHandler(pObject, pEvent):
        debug(__name__ + ", ObjectKilledHandler")
        pKilledObject = pEvent.GetDestination()
        if pKilledObject.IsTypeOf(App.CT_SHIP):
                pShip = App.ShipClass_Cast(pKilledObject)
                ftb.ShipManager.RemoveShip(pShip)
        pObject.CallNextHandler(pEvent)

        
def MissionStart():
	debug(__name__ + ", MissionStart")
	global ET_LAUNCH_SHIP, ET_TOGGLE_LAUNCH_TYPE, ET_TOGGLE_SHIP_TYPE, ET_RETURN_SHIP
	ET_LAUNCH_SHIP = ftb.FTB_MissionLib.GetFTBNextEventType()
	ET_TOGGLE_LAUNCH_TYPE = ftb.FTB_MissionLib.GetFTBNextEventType()
	ET_TOGGLE_SHIP_TYPE = ftb.FTB_MissionLib.GetFTBNextEventType()
	ET_RETURN_SHIP = ftb.FTB_MissionLib.GetFTBNextEventType()
	SHUTTLE_COUNT_TIMER = ftb.FTB_MissionLib.GetFTBNextEventType()
	pMission = MissionLib.GetMission()
	
	pMission.AddPythonFuncHandlerForInstance(ET_LAUNCH_SHIP, __name__+".LaunchShip")
	pMission.AddPythonFuncHandlerForInstance(ET_TOGGLE_LAUNCH_TYPE, __name__+".ToggleLaunchType")
	pMission.AddPythonFuncHandlerForInstance(ET_TOGGLE_SHIP_TYPE, __name__+".ToggleFTBShip")
	pMission.AddPythonFuncHandlerForInstance(ET_RETURN_SHIP, "ReturnShuttles.ReturnWithoutTractor")
	# restart
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, App.Game_GetCurrentGame(), __name__ + ".MissionRestart")
	# ship kill
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectKilledHandler")
	ftb.LaunchShip.MissionStart() # call the Handlers to set up in LaunchShip and ReturnShuttles.
	ReturnShuttles.MissionStart(SHUTTLE_COUNT_TIMER)
	#PreLoadAssets()
	AddLaunchButtons(ftb.GUIUtils.GetScienceMenu())


# Called on Mission restart, makes sure we select the right thing - Defiant
def MissionRestart(pObject, pEvent):
        debug(__name__ + ", MissionRestart")
        global pShipMenu, ShuttleLaunchShip
        
        pPlayer = MissionLib.GetPlayer()
        # Set all config to normal
        ShuttleLaunchShip = pPlayer.GetName()
        if not pShipMenu:
            AddLaunchButtons(ftb.GUIUtils.GetScienceMenu())
        if not pShipMenu:
            print("Shuttle Launching Framework not loading....bye bye!")
            return
        pShipMenu.SetName(App.TGString(ShuttleLaunchShip + " " + "Selected"))
        ToggleLaunchType(pObject, pEvent)


#### Handler Helpers #### 

# Add the Buttons here
def AddLaunchButtons( pMenu):
    debug(__name__ + ", AddLaunchButtons")
    global pToggleLaunchTypeButton, pLaunchButton, ButtonToggleLaunchType, launchTypeSave, launchTypeSaveNum, pShipMenu, ShuttleLaunchShip

    if not MissionLib.GetPlayer() or not ET_LAUNCH_SHIP:
            return
    ShuttleLaunchShip = MissionLib.GetPlayer().GetName()
    pLaunchShip = MissionLib.GetShip(ShuttleLaunchShip)
    pCarrier = ftb.ShipManager.GetShip(pLaunchShip)
    if not hasattr(pCarrier, "GetLaunchers"):
        return
    pLaunchers = pCarrier.GetLaunchers()
    numTypes = len( pLaunchers)

    pToggleLaunchTypeButton = []
    pLaunchButton = []
    
    # FleetButton
    pShipMenu = App.STMenu_CreateW(App.TGString("Player Selected"))
    pMenu.AddChild(pShipMenu)
    pShipMenu.AlignTo(pMenu.GetFirstChild(), App.TGUIObject.ALIGN_BL, App.TGUIObject.ALIGN_BR)
    # Add Player
    pSelectPlayerButton = ftb.GUIUtils.CreateIntButton("Player", ET_TOGGLE_SHIP_TYPE, MissionLib.GetMission(), 0)
    pShipMenu.PrependChild(pSelectPlayerButton)
    # Add Target
    pSelectPlayerButton = ftb.GUIUtils.CreateIntButton("Get Target", ET_TOGGLE_SHIP_TYPE, MissionLib.GetMission(), 1)
    pShipMenu.PrependChild(pSelectPlayerButton)
    # Get on board
    #if ftb.FTB_MissionLib.IsMultiplayerHostAlone():
    pSelectPlayerButton = ftb.GUIUtils.CreateIntButton("Get on Board", ET_TOGGLE_SHIP_TYPE, MissionLib.GetMission(), 2)
    pShipMenu.PrependChild(pSelectPlayerButton)


    for index in range( numTypes):
        # Launch Button
        buttonLabel = "Launch " + str(index + 1)
        pButton = ftb.GUIUtils.CreateIntButton( buttonLabel, ET_LAUNCH_SHIP, MissionLib.GetMission(), index)
	if not pButton:
		return
        pMenu.AddChild( pButton)
        pLowest = ftb.GUIUtils.FindLowestChild( pMenu)
        pButton.SetPosition( pLowest.GetLeft(), pLowest.GetBottom(), 0)
        pLaunchButton.append( pButton)

        # group Button
        launchType = pLaunchers[index].GetLaunchType()
        numLaunches = pLaunchers[index].GetNumLaunches( launchType)
        buttonLabel = launchType + ": " + str( numLaunches)
        ButtonToggleLaunchType = ftb.GUIUtils.CreateIntButton( buttonLabel, ET_TOGGLE_LAUNCH_TYPE, MissionLib.GetMission(), index)
        pMenu.AddChild(ButtonToggleLaunchType)
        ButtonToggleLaunchType.AlignTo( pMenu.GetFirstChild(), App.TGUIObject.ALIGN_BL, App.TGUIObject.ALIGN_BR)
        pToggleLaunchTypeButton.append(ButtonToggleLaunchType)
        if( numLaunches == 0):
            pButton.SetDisabled()
        launchTypeSave = launchType
        launchTypeSaveNum = numLaunches
    
    # Add Return Shuttle
    pReturnShuttleButton = ftb.GUIUtils.CreateIntButton("Return Shuttle", ET_RETURN_SHIP, MissionLib.GetMission(), index)
    pMenu.AddChild(pReturnShuttleButton)
    pReturnShuttleButton.AlignTo( pMenu.GetFirstChild(), App.TGUIObject.ALIGN_BL, App.TGUIObject.ALIGN_BR)



# Launching a Shuttle really cost nothing
def PreLoadAssets():
    debug(__name__ + ", PreLoadAssets")
    "Cache up all of the launchable ships to avoid a framerate hit"
    pCarrier = ftb.ShipManager.GetShip(MissionLib.GetPlayer())
    if not hasattr(pCarrier, "GetLaunchers"):
        return
    pLaunchers = pCarrier.GetLaunchers()
    for launcher in pCarrier.GetLaunchers():
        for shipScript in launcher.GetComplement()._keyList.keys():
            #print "preloading %s %d times" % (shipScript, \
            #                             launcher.GetNumLaunches( shipScript))
            loadspacehelper.PreloadShip(shipScript, launcher.GetNumLaunches(shipScript))



# Change the Ship
def ToggleFTBShip(pObject, pEvent):
        debug(__name__ + ", ToggleFTBShip")
        global pShipMenu, ShuttleLaunchShip
        pPlayer         = MissionLib.GetPlayer()
        pGame           = App.Game_GetCurrentGame()
        pEpisode	= pGame.GetCurrentEpisode()
        pMission	= pEpisode.GetCurrentMission()
        pTarget         = pPlayer.GetTarget()
        pFriendlies     = pMission.GetFriendlyGroup()
        
        # If the Event Number is 0, then it is the Players ship.
        if (pEvent.GetInt() == 0):
            ShuttleLaunchShip = pPlayer.GetName()
            ftb.LaunchShip.GetOnBoard = 0
            
            # Change the name of the Button
            pShipMenu.SetName(App.TGString(ShuttleLaunchShip + " " + "Selected"))
        # If it is 1, use the Target
        elif (pEvent.GetInt() == 1):
            if not pTarget:
                print("No Target")
                return
            if not pFriendlies.IsNameInGroup(pTarget.GetName()):
                print("Target is not friendly - failed.")
                return
                
            ShuttleLaunchShip = pTarget.GetName()
            ftb.LaunchShip.GetOnBoard = 0
        
            # Change the name of the Button
            pShipMenu.SetName(App.TGString(ShuttleLaunchShip + " " + "Selected"))
    
        # if 2, we transport
        elif (pEvent.GetInt() == 2):
            ShuttleLaunchShip = pPlayer.GetName()
            ftb.LaunchShip.GetOnBoard = 1
                
            # Change the name of the Button
            pShipMenu.SetName(App.TGString("GetOnBoard" + " " + "Selected"))
        else:
                return
        SetToggleLaunchButton()
