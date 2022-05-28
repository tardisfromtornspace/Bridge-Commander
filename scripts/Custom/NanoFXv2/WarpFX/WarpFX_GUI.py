from bcdebug import debug
#####################################################################
#   This code was developed from scratch by me. Almost nothing      #
#   from the former code is in here.                                #
#                                                                   #
#   Original Author: Nanobyte                                       #
#                                                                   #
#   Redesign: USS Sovereign (BCS:TNG)                               #
#                                                                   #
#   License: This file has been modified with the permission from   #
#   the original author. To modify or use the current code, you     #
#   need to ask Nanobyte to modify NanoFX and me to modify this     #
#   current code. Any usage of this code in any other mod needs     #
#   to be credited.                                                 #
#                                                                   #
#   Modified by USS Frontier for increased functionality and        #
#         compatibility with Galaxy Charts                          #
#####################################################################


##### Imports
import App
import Foundation
import MissionLib
import string

##### Events
ET_CLOSE = App.UtopiaModule_GetNextEventType()
ET_CREATE_WINDOW = App.UtopiaModule_GetNextEventType()
ET_WARP_SPEED_CHANGED = App.UtopiaModule_GetNextEventType()
ET_TIMER = App.UtopiaModule_GetNextEventType()
ET_TIMER_2 = App.UtopiaModule_GetNextEventType()

##### Vars
pWindow = None
pSSButton = None


##### Dummy Function, so we don't have to override LoadNanoFX.py
def SetupWarpSpeedButtons(iMaxWarp = 9):
        debug(__name__ + ", SetupWarpSpeedButtons")
        return
    

##### Main Function
def SetupButtons():
        debug(__name__ + ", SetupButtons")
        global pHelm, pSSButton

        ##### A small QBR Quick Fix
        DeleteMenuButton("Helm", "Warp Speed")

        ##### Main Button        
        pSSButton = CreateMenuButton("Select Travel Speed", "Helm", __name__ + ".Window")

        ##### Event Types        
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pBridge = App.g_kSetManager.GetSet("bridge")
        pHelm = App.CharacterClass_GetObject(pBridge, "Helm")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".CloseWindow")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WARP_SPEED_CHANGED, pMission, __name__ + ".UpdateSlider")

        if pHelm != None:
	        pHelm.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow")

        ##### Timer
        CreateTimer(ET_TIMER, __name__ + ".CreateWindow", App.g_kUtopiaModule.GetGameTime() + 2)



##### Create Window Frame                
def CreateWindow(pObject, pEvent):
        debug(__name__ + ", CreateWindow")
        global pWindow

        pWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Travel Speed Selector"), 0.0, 0.0, None, 1, 0.3, 0.4, App.g_kMainMenuBorderMainColor)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(pWindow, 0.3, 0.3)

        pWindow.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".MousePass")
        pWindow.SetNotVisible()


##### Create Buttons in Window        
def CreateWindowPartII():
	debug(__name__ + ", CreateWindowPartII")
	global pWindow, pText, pSlider, maxWarp, cruiseWarp, pCurrentWarpText, pMaxWarpText, pButton, pActualCurrentWarpText, pActualMaxWarpText
        
	x = 0.02
	y = 0.04
	fWarpSpeed = GetWarpSpeed()
	pSlider = CreateWarpSlidebar(App.TGString("Speed Bar"), ET_WARP_SPEED_CHANGED, fWarpSpeed)
	pSlider.Resize(0.25, 0.04, 0)
	pWindow.AddChild(pSlider, x, y, 0)

	x = 0.02
	y = y + 0.08
	pText = App.TGParagraph_CreateW(App.TGString("Selected Speed: "+str(fWarpSpeed)), pWindow.GetMaximumInteriorWidth(), None, '', pWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
	pWindow.AddChild(pText, x, y, 0)

            
	x = 0.02
	y = y + 0.04
	pMaxWarpText = App.TGParagraph_CreateW(App.TGString("Ships Max Speed: " + str(maxWarp)), pWindow.GetMaximumInteriorWidth(), None, '', pWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
	pWindow.AddChild(pMaxWarpText, x, y, 0)

            
	x = 0.02
	y = y + 0.02
	pCurrentWarpText = App.TGParagraph_CreateW(App.TGString("Ships Cruise Speed: " + str(cruiseWarp)), pWindow.GetMaximumInteriorWidth(), None, '', pWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
	pWindow.AddChild(pCurrentWarpText, x, y, 0)

	#######################
	pPlayer = App.Game_GetCurrentPlayer()
	pTravel = App.g_kTravelManager.GetTravel(pPlayer)
	ActualMaximumWarp = "???"
	ActualCruisingWarp = "???"
	if pTravel != None:
		ActualMaximumWarp = pTravel.GetActualMaxSpeed()
		ActualCruisingWarp = pTravel.GetActualCruiseSpeed()

	x = 0.02
	y = y + 0.04
	pActualMaxWarpText = App.TGParagraph_CreateW(App.TGString("Actual Max Speed: " + str(ActualMaximumWarp)), pWindow.GetMaximumInteriorWidth(), None, '', pWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
	pWindow.AddChild(pActualMaxWarpText , x, y, 0)
            
	x = 0.02
	y = y + 0.02
	pActualCurrentWarpText = App.TGParagraph_CreateW(App.TGString("Actual Cruise Speed: " + str(ActualCruisingWarp)), pWindow.GetMaximumInteriorWidth(), None, '', pWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
	pWindow.AddChild(pActualCurrentWarpText, x, y, 0)
	#######################

	x = 0.02
	y = y + 0.06
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(ET_CLOSE)
	pEvent.SetDestination(pHelm)
	pEvent.SetInt(0)
	pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.13125, 0.034583)
	pButton.SetNormalColor(App.g_kMainMenuButtonColor)
	pButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	pButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	pButton.SetDisabledColor(App.g_kSTMenu1Disabled)
	pButton.SetColorBasedOnFlags()
	pWindow.AddChild(pButton, x, y, 0)
        
	pWindow.InteriorChangedSize()
        
	pWindow.Layout()



##### Display Selected Warp Speed        
def UpdateSlider(pObject, pEvent):
	debug(__name__ + ", UpdateSlider")
	global pText, pWindow, pSlider

	try:
		fSpeed = pEvent.GetFloat()
	except AttributeError:
		return

	fSpeed = float(str(fSpeed)[0:3+1])
        
	pText.SetString("Selected Speed: " + str(fSpeed))

	SetWarpSpeed(fSpeed)

	##########
	# This window can be called from the Galaxy Map, so update it as well.
	import Custom.GalaxyCharts.GalaxyMapGUI
	Custom.GalaxyCharts.GalaxyMapGUI.UpdateInformation()
	##########

	pSlider.Resize(0.25, 0.04, 0)

	pSlider.SetValue(fSpeed)

	pWindow.InteriorChangedSize()
        
	pWindow.Layout()

	pObject.CallNextHandler(pEvent)


##### Mouse Pass Over The Window	
def MousePass(Window, pEvent):
    
        debug(__name__ + ", MousePass")
        Window.CallNextHandler(pEvent)

        if pEvent.EventHandled() == 0:
                pEvent.SetHandled()


##### Close Window        
def CloseWindow(pObject, pEvent):
        debug(__name__ + ", CloseWindow")
        global pWindow, pText, pSlider, pCurrentWarpText, pMaxWarpText, pButton

        if not pWindow:
                return

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        
        if pWindow.IsVisible():
                pTCW.MoveToBack(pWindow)
                pWindow.SetNotVisible()
                pWindow.DeleteChild(pText)
                pWindow.DeleteChild(pSlider)
                pWindow.DeleteChild(pCurrentWarpText)
                pWindow.DeleteChild(pMaxWarpText)
                pWindow.DeleteChild(pActualCurrentWarpText)
                pWindow.DeleteChild(pActualMaxWarpText)
                pWindow.DeleteChild(pButton)

        pObject.CallNextHandler(pEvent)


##### Open Window Function      
def Window(pObject, pEvent):
        debug(__name__ + ", Window")
        global pWindow
        
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        if not pWindow:
                return

        if not pWindow.IsVisible():
                CreateWindowPartII()
                pWindow.SetVisible()
                pTCW.MoveToFront(pWindow)                
                pTCW.MoveTowardsBack(pWindow)


##### Mostly from SetVolumeButton made by Totally Games
def CreateWarpSlidebar (pName, eType, fValue):
        debug(__name__ + ", CreateWarpSlidebar")
        global maxWarp, cruiseWarp
        
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pBar = App.STNumericBar_Create()

        ##### Grab specific ship speed values
	maxWarp = GetMaxWarp()
	cruiseWarp = GetCruiseWarp()
	pPlayer = App.Game_GetCurrentPlayer()
	pTravel = App.g_kTravelManager.GetTravel(pPlayer)
	fMinSpeed = 0.0
	if pTravel != None:
		fMinSpeed = pTravel.GetMinAllowedSpeed()

        ##### Set Our Range. 
	pBar.SetRange(fMinSpeed, maxWarp)
	pBar.SetKeyInterval(0.01)
	pBar.SetMarkerValue(cruiseWarp)
	pBar.SetValue(fValue)
	pBar.SetUseMarker(0)
	pBar.SetUseAlternateColor(0)
	pBar.SetUseButtons(0)

	kNormalColor = App.g_kSTMenu3NormalBase
	kEmptyColor = App.g_kSTMenu3Disabled

	pBar.SetNormalColor(kNormalColor)
	pBar.SetEmptyColor(kEmptyColor)
	pText = pBar.GetText()
	pText.SetStringW(pName)

	pBar.Resize(0.25, 0.04, 0)

	pEvent = App.TGFloatEvent_Create()
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetFloat(fValue)
	pEvent.SetEventType(eType)

	pBar.SetUpdateEvent(pEvent)

	return pBar
    


##### Called At Exiting                
def exiting(pObject, pEvent):
        debug(__name__ + ", exiting")
        global pWindow

        if pWindow:
                pWindow.KillChildren()
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                pTCW.DeleteChild(pWindow)



##### The stuff here will create a Button                
def CreateMenuButton(ButtonName, Person, Function, EventInt = 0):        
        debug(__name__ + ", CreateMenuButton")
        pMenu = GetBridgeMenu(Person)
        ET_EVENT = App.Mission_GetNextEventType()

        pMenu.AddPythonFuncHandlerForInstance(ET_EVENT, Function)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_EVENT)
        pEvent.SetDestination(pMenu)
        pEvent.SetInt(EventInt)
        pButton = App.STButton_CreateW(App.TGString(ButtonName), pEvent)

        pMenu.AddChild(pButton)
        
        pLowest = FindLowestChild(pMenu)
	pButton.SetPosition(pLowest.GetLeft(), pLowest.GetBottom(), 0)

        pMenu.AddChild(None) 

        return pButton


##### Find the lowest child for the new button position
def FindLowestChild(Pane):
        debug(__name__ + ", FindLowestChild")
        Index = Pane.GetTrueNumChildren() - 1
        iBottom = 0
        LowestChild = None
        Current = None
        while Index >= 0:
            Current = Pane.GetTrueNthChild(Index)
            CurrentBottom = Current.GetBottom()
            if(CurrentBottom > iBottom):
                iBottom = CurrentBottom
                LowestChild = Current
            Index = Index - 1
        return LowestChild
    


##### Deletes specified menu button
def DeleteMenuButton(sMenuName, sButtonName, sSubMenuName = None):
                debug(__name__ + ", DeleteMenuButton")
                pMenu   = GetBridgeMenu(sMenuName)
                pButton = pMenu.GetButton(sButtonName)
                if sSubMenuName != None:
                        pMenu = pMenu.GetSubmenu(sSubMenuName)
                        pButton = pSubMenu.GetButton(sButtonName)

                pMenu.DeleteChild(pButton)


##### Get Bridge Menu Button    
def GetBridgeMenu(Person):
        debug(__name__ + ", GetBridgeMenu")
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
        pMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString(Person))
        App.g_kLocalizationManager.Unload(pDatabase)
        return pMenu
    

##### Create Timer    
def CreateTimer(event, sFunctionHandler, fStart):
	# Setup the handler function.
	debug(__name__ + ", CreateTimer")
	pGame = App.Game_GetCurrentGame()
	if (pGame == None):
		return None
	pEpisode = pGame.GetCurrentEpisode()
	if (pEpisode == None):
		return None
	pMission = pEpisode.GetCurrentMission()
	if (pMission == None):
		return None

	pMission.AddPythonFuncHandlerForInstance(event, sFunctionHandler)

	# Create the event and the event timer.
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(event)
	pEvent.SetDestination(pMission)
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(fStart)
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pEvent)

        # Add the timer to the game.
	App.g_kTimerManager.AddTimer(pTimer)
	
	return pTimer


##### Reset Warp Speed    
def ResetWarpSpeed():
	debug(__name__ + ", ResetWarpSpeed")
	pPlayer = App.Game_GetCurrentPlayer()
	pTravel = App.g_kTravelManager.GetTravel(pPlayer)
	if pTravel != None:
		pTravel.SetSpeed(ReturnCruiseSpeed())


##### Set Warp Speed
def SetWarpSpeed(i):
	debug(__name__ + ", SetWarpSpeed")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer != None:
		pTravel = App.g_kTravelManager.GetTravel(pPlayer)
		if pTravel != None:
			pTravel.SetSpeed(i)
		else:
			pPlayer.SetWarpSpeed(i)


##### Get Warp Speed	
def GetWarpSpeed():
	debug(__name__ + ", GetWarpSpeed")
	pPlayer = App.Game_GetCurrentPlayer()
	try:
		pTravel = App.g_kTravelManager.GetTravel(pPlayer)
		if pTravel != None:
			return pTravel.GetSpeed()
		else:
			return 9.0
	except:
		return 9.0


##### Returns Cruising Speed of the ship
def ReturnCruiseSpeed():
        debug(__name__ + ", ReturnCruiseSpeed")
        return GetCruiseWarp()


##### Get Max Warp Speed From The Ships Foundation File
def GetMaxWarp():
	debug(__name__ + ", GetMaxWarp")
	pPlayer = MissionLib.GetPlayer()
	pTravel = App.g_kTravelManager.GetTravel(pPlayer)
	if pTravel != None:
		return pTravel.GetMaxSpeed()
	else:
		return 9.0
        

##### Get Cruise Warp Speed
def GetCruiseWarp():
	debug(__name__ + ", GetCruiseWarp")
	pPlayer = MissionLib.GetPlayer()
	pTravel = App.g_kTravelManager.GetTravel(pPlayer)
	if pTravel != None:
		return pTravel.GetCruiseSpeed()
	else:
		return 9.0


##### It returns currently used Ship HP
def GetShipType(pShip):
                debug(__name__ + ", GetShipType")
                if pShip.GetScript():
                        return string.split(pShip.GetScript(), '.')[-1]
                return None
