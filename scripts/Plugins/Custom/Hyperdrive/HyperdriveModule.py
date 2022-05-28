# by USS Sovereign

# Meet the future!!! This is what will hopefully drive all alternative means of travel anyone can think of.

# All rights reserved. Do not modify this or any part of the mod without extreme permission from the authors!


# Version signature
VERSION = '20070817'

# Imports
import App
import MissionLib
import loadspacehelper
import nt
import string
from Custom.Hyperdrive.Libs import DS9FXMenuLib
from Custom.Hyperdrive.Libs import LoadFlash
from Custom.Hyperdrive.Libs import AimForGoodPos
from Custom.Hyperdrive.Libs import AimForGoodPosExit
from Custom.Hyperdrive.Libs import EngineStats
from Custom.Hyperdrive.Libs import EngineStatsETA
from Custom.Hyperdrive.Libs import EngineStatsIdealETA
from Custom.Hyperdrive.Libs import EngineStatsMenuCalc

# Events
ET_ENGAGE = App.UtopiaModule_GetNextEventType()
ET_UPDATE_SLIDER = App.UtopiaModule_GetNextEventType()
ET_REFRESH = App.UtopiaModule_GetNextEventType()
ET_CLOSE = App.UtopiaModule_GetNextEventType()

# Vars
bButton = None
pTimer = None
pTimerETA = None
pTimerIdealETA = None
pTimerEngineStats = None
pPane = None
pMainPane = None
pSelectedSpeed = None
pTotalEngineStatsText = None
pETAText = None
pIdealETAText = None 
pSelectedSpeedText = None
pSlider = None
pDefault = None
pSupported = 0

# Pane ID
pPaneID = None

# Aiming
pAim = 0

# Cloaked?
pWasCloaked = 0

# List of asteroid scripts
sAsteroidList = ["ships.Asteroid", "ships.Asteroid1", "ships.Asteroid2", "ships.Asteroid3", "ships.Asteroidh1", "ships.Asteroidh2", "ships.Asteroidh3"]

# List of hull properties Hyperdrive looks for
sHyperdriveList = ['Hyperdrive 1', 'Hyperdrive 2', 'Hyperdrive 3', 'Hyperdrive 4', 'Hyperdrive 5', 'Hyperdrive 6', 'Hyperdrive 7', 'Hyperdrive 8', 'Hyperdrive 9', 'Hyperdrive 10', 'Hyperdrive 11', 'Hyperdrive 12', 'Hyperdrive 13', 'Hyperdrive 14', 'Hyperdrive 15', 'Hyperdrive 16', 'Hyperdrive 17', 'Hyperdrive 18', 'Hyperdrive 19', 'Hyperdrive 20']

# Drive Condition List
lStats = []
lStatsETA = []
lStatsIdealETA = []
lStatsEngines = []

# Path
sPath = "scripts\\Custom\\Hyperdrive\\Libs\\EngineStats.py"
sPathETA = "scripts\\Custom\\Hyperdrive\\Libs\\EngineStatsETA.py"
sPathIdealETA = "scripts\\Custom\\Hyperdrive\\Libs\\EngineStatsIdealETA.py"
sPathStats = "scripts\\Custom\\Hyperdrive\\Libs\\EngineStatsMenuCalc.py"


# Main function called by the zzzHyperdrive.py
def init():
        global bButton, pSupported

        if not pSupported == 1:
            return

        # Remove any existing buttons
        RemoveMenu()

        pPlayer = MissionLib.GetPlayer()

        HyperdriveInstalled = HasHyperdrive(pPlayer)
        if not HyperdriveInstalled == 'Hyperdrive Installed':
            return

        # Create & disable the button
        bButton = DS9FXMenuLib.CreateButton("Hyperdrive Details", "Helm", __name__ + ".HyperdriveGUI", sToButton = None)
        NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
	HilightedColor = App.TGColorA() 
	HilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
	DisabledColor = App.TGColorA() 
	DisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
	bButton.SetUseUIHeight(0)
	bButton.SetNormalColor(NormalColor)
        bButton.SetHighlightedColor(HilightedColor)
        bButton.SetSelectedColor(NormalColor)
        bButton.SetDisabledColor(DisabledColor)
        bButton.SetColorBasedOnFlags()
        bButton.SetDisabled()

        # Resolve the small issue when the warp button is enabled and hyperdrive is not
        ClearCourseSetting(None)


# Just activate needed handlers
def handlers():
        global pSupported

        # Check if this is the supported game type
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        if pMission.GetScript() == "QuickBattle.QuickBattle":
            print 'Hyperdrive: Quick Battle is running... Mod is starting up...'
            pSupported = 1
            # Possible bugfix
            init()
        elif pMission.GetScript() == "Custom.QuickBattleGame.QuickBattle":
            print 'Hyperdrive: Quick Battle Replacement is running... Mod is starting up...'
            pSupported = 1
            # Possible bugfix
            init()
	else:
	    print 'Hyperdrive: Unsupported game type is running... Mod is shutting down...'
	    pSupported = 0
	    return
        
        # Detect course set event
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_COURSE, pMission, __name__ + ".CourseSet")


# Disable button 
def disablebutton():
        global bButton, pSupported

        if not pSupported == 1:
            return

        if bButton is None:
            return

        if hasattr(bButton, 'SetDisabled'):
            if bButton.IsEnabled():
                bButton.SetDisabled()
                

# Quitting QB deactivate handlers
def quitting():
        global pMainPane, pPane, pSupported

        if not pSupported == 1:
            return
    
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_COURSE, pMission, __name__ + ".CourseSet")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".FixDarkScreen")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_DESTROYED, pMission, __name__ + ".FixDarkScreenExplosions")
        except:
            pass

	if not pPane == None:
                # Let's not cause any crashes
                try:
                    App.g_kEventManager.RemoveBroadcastHandler(ET_ENGAGE, pMission, __name__ + ".HyperdriveStats")
                except:
                    pass
                try:
                    App.g_kEventManager.RemoveBroadcastHandler(ET_UPDATE_SLIDER, pMission, __name__ + ".UpdateSlider")
                except:
                    pass
                try:
                    App.g_kEventManager.RemoveBroadcastHandler(ET_REFRESH, pMission, __name__ + ".UpdateStats")
                except:
                    pass
                try:
                    App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".CloseGUI")
                except:
                    pass

                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

                try:
                    # Just destroy the window, we don't need it anymore.
                    App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

                    pTCW.DeleteChild(pPane)

                    pPane = None

                except:
                    pass


# Course is set                
def CourseSet(pObject, pEvent):
        global bButton, pDest

        # Compare events
        if not (pEvent.GetInt() == App.CharacterClass.EST_SET_COURSE_INTERCEPT):

            # Hack into the set course destination
            pWarp = App.SortedRegionMenu_GetWarpButton()
            pDest = pWarp.GetDestination()

            # Incompatibility fix for hyperdrive & slipstream
            if hasattr(bButton, 'SetEnabled'):
                if not bButton.IsEnabled():
                    bButton.SetEnabled()

        # Pass event onto the next handler
        pObject.CallNextHandler(pEvent)


# Create the GUI window       
def HyperdriveGUI(pObject, pEvent):
        global pMainPane, pPane

        if not pPane == None:
            return

        # DS9FX code
        pPane = App.TGPane_Create(1.0, 1.0) 
	pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
	pTCW.AddChild(pPane, 0, 0) 
	pMainPane = App.TGPane_Create(0.4, 0.4) 
	pPane.AddChild(pMainPane, 0.35, 0.10)
                
        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        # Setup Events
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_ENGAGE, pMission, __name__ + ".HyperdriveStats")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_UPDATE_SLIDER, pMission, __name__ + ".UpdateSlider")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_REFRESH, pMission, __name__ + ".UpdateStats")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".CloseGUI")

        # Create Entries now
        CreateEntries(None, None)


# Create buttons, windows, entries...
def CreateEntries(pObject, pEvent):
        global pMainPane, pPane, pSelectedSpeed, pTotalEngineStatsText, pETAText, pIdealETAText, pSelectedSpeedText, pSlider, pDetailsWindow, pFunctionsWindow, pSliderWindow, pOptionsWindow

        # We need 3 windows
        pDetailsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Ship/Speed Details"), 0.0, 0.0, None, 1, 0.19, 0.19, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pDetailsWindow, 0, 0)

        pFunctionsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Function Selection"), 0.0, 0.0, None, 1, 0.19, 0.19, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pFunctionsWindow , 0, 0.21)
        
        pSliderWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Speed Selector"), 0.0, 0.0, None, 1, 0.19, 0.19, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pSliderWindow, 0.21, 0)

        pOptionsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Engage Hyperdrive"), 0.0, 0.0, None, 1, 0.19, 0.19, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pOptionsWindow, 0.21, 0.21)

        # Check for specified max speed
        pPlayer = MissionLib.GetPlayer()
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "HyperdriveCustomizations"):
            pCustomization = pModule.HyperdriveCustomizations()
            
            # Customization exists, but does the speed entry exist?!
            if pCustomization.has_key('MaxSpeed'):
                pMaxSpeed = pCustomization['MaxSpeed']
                pMaxSpeed = pMaxSpeed + 0.0
                if pMaxSpeed > 10.0:
                    pMaxSpeed = 10.0

            # It doesn't exist!
            else:
 		pMaxSpeed = 10.0

 	# No customizations of any kind...
	else:
		pMaxSpeed = 10.0

        pSelectedSpeed = pMaxSpeed
        fMaxSpeed = pMaxSpeed / 10.0
        pSelectedSpeed = float(str(pSelectedSpeed)[0:3+1])
        strSpeed = float(str(pMaxSpeed)[0:3+1])
        fMaxSpeed = float(str(fMaxSpeed)[0:3+1])

	pSelectedSpeedText = App.TGParagraph_CreateW(App.TGString("Selected Speed: " + str(pSelectedSpeed)), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pSelectedSpeedText, 0, 0.01)

        pMaxSpeedText = App.TGParagraph_CreateW(App.TGString("Max Speed: " + str(strSpeed)), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pMaxSpeedText, 0, 0.04)

        # We need to calculate the ETA & the engine stats
        pETA = ReturnETA(pSelectedSpeed)
        pIdealETA = ReturnIdealETA(pSelectedSpeed)
                    
        pETAText = App.TGParagraph_CreateW(App.TGString("ETA: " + pETA + " seconds"), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pETAText, 0, 0.07)

        pIdealETAText = App.TGParagraph_CreateW(App.TGString("Ideal ETA: " + pIdealETA + " seconds"), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pIdealETAText, 0, 0.10)

        pTotalEngineStats = ReturnEngineStats()

        pTotalEngineStatsText = App.TGParagraph_CreateW(App.TGString("Engine Status: " + pTotalEngineStats + "%"), pDetailsWindow.GetMaximumInteriorWidth(), None, '', pDetailsWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pDetailsWindow.AddChild(pTotalEngineStatsText, 0, 0.13)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_REFRESH)
        pEvent.SetString("SovRefresh")
        pButton = App.STRoundedButton_CreateW(App.TGString("Refresh Details"), pEvent, 0.13125, 0.034583)
        NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
	HilightedColor = App.TGColorA() 
	HilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
	DisabledColor = App.TGColorA() 
	DisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
	pButton.SetNormalColor(NormalColor)
        pButton.SetHighlightedColor(HilightedColor)
        pButton.SetSelectedColor(NormalColor)
        pButton.SetDisabledColor(DisabledColor)
        pButton.SetColorBasedOnFlags()
        pFunctionsWindow.AddChild(pButton, 0.02, 0.03)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetString("SovClose")
        pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.13125, 0.034583)
        NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
	HilightedColor = App.TGColorA() 
	HilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
	DisabledColor = App.TGColorA() 
	DisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
	pButton.SetNormalColor(NormalColor)
        pButton.SetHighlightedColor(HilightedColor)
        pButton.SetSelectedColor(NormalColor)
        pButton.SetDisabledColor(DisabledColor)
        pButton.SetColorBasedOnFlags()
        pFunctionsWindow.AddChild(pButton, 0.02, 0.09)

        pSlider = CreateSlidebar(App.TGString("Speed Bar"), ET_UPDATE_SLIDER, fMaxSpeed)
        pSlider.Resize(0.16, 0.04, 0)
        pSliderWindow.AddChild(pSlider, 0.01, 0.06, 0)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_ENGAGE)
        pEvent.SetString("SovEngage")
        pButton = App.STRoundedButton_CreateW(App.TGString("Engage"), pEvent, 0.15, 0.06)
        NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
	HilightedColor = App.TGColorA() 
	HilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
	DisabledColor = App.TGColorA() 
	DisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
	pButton.SetNormalColor(NormalColor)
        pButton.SetHighlightedColor(HilightedColor)
        pButton.SetSelectedColor(NormalColor)
        pButton.SetDisabledColor(DisabledColor)
        pButton.SetColorBasedOnFlags()
        pOptionsWindow.AddChild(pButton, 0.02, 0.05)


        # Glass background for pMainPane
	pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode() 
	pLCARS = pGraphicsMode.GetLcarsString() 
	pGlass = App.TGIcon_Create(pLCARS, 120) 
	pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight()) 
	pMainPane.AddChild(pGlass, 0, 0)

	pDetailsWindow.InteriorChangedSize()
        pDetailsWindow.Layout()
        pFunctionsWindow.InteriorChangedSize()
        pFunctionsWindow.Layout()
        pSliderWindow.InteriorChangedSize()
        pSliderWindow.Layout()
        pOptionsWindow.InteriorChangedSize()
        pOptionsWindow.Layout()
        pMainPane.Layout()
        pPane.Layout()

        # Now show the pane
        pPane.SetVisible()


# Update stats
def UpdateStats(pObject, pEvent):
        global pMainPane, pPane, pTotalEngineStatsText, pETAText, pIdealETAText, pDetailsWindow, pFunctionsWindow, pSliderWindow, pOptionsWindow

        pETA = ReturnETA(pSelectedSpeed)
        pIdealETA = ReturnIdealETA(pSelectedSpeed)
        pTotalEngineStats = ReturnEngineStats()

        pETAText.SetString("ETA: " + pETA + " seconds")
        pIdealETAText.SetString("Ideal ETA: " + pIdealETA + " seconds")
        pTotalEngineStatsText.SetString("Engine Status: " + pTotalEngineStats + "%")

        pDetailsWindow.InteriorChangedSize()
        pDetailsWindow.Layout()
        pFunctionsWindow.InteriorChangedSize()
        pFunctionsWindow.Layout()
        pSliderWindow.InteriorChangedSize()
        pSliderWindow.Layout()
        pOptionsWindow.InteriorChangedSize()
        pOptionsWindow.Layout()
        pMainPane.Layout()
        pPane.Layout()

        pObject.CallNextHandler(pEvent)


# Update sliderbar
def UpdateSlider(pObject, pEvent):
        global pMainPane, pPane, pSelectedSpeed, pTotalEngineStatsText, pETAText, pIdealETAText, pSelectedSpeedText, pSlider, pDetailsWindow, pFunctionsWindow, pSliderWindow, pOptionsWindow

        try:
            fValue = pEvent.GetFloat()

        except AttributeError:
            return

        if fValue < 0.01:
            fValue = 0.01
        
        fSpeed = fValue * 10.0

        fSpeed = float(str(fSpeed)[0:3+1])

        pSelectedSpeed = fSpeed

        pETA = ReturnETA(pSelectedSpeed)
        pIdealETA = ReturnIdealETA(pSelectedSpeed)
        pTotalEngineStats = ReturnEngineStats()

        pSelectedSpeedText.SetString("Selected Speed: " + str(pSelectedSpeed))
        pETAText.SetString("ETA: " + pETA + " seconds")
        pIdealETAText.SetString("Ideal ETA: " + pIdealETA + " seconds")
        pTotalEngineStatsText.SetString("Engine Status: " + pTotalEngineStats + "%")

        pSlider.Resize(0.16, 0.04, 0)
        pSlider.SetValue(fValue)

        pDetailsWindow.InteriorChangedSize()
        pDetailsWindow.Layout()
        pFunctionsWindow.InteriorChangedSize()
        pFunctionsWindow.Layout()
        pSliderWindow.InteriorChangedSize()
        pSliderWindow.Layout()
        pOptionsWindow.InteriorChangedSize()
        pOptionsWindow.Layout()
        pMainPane.Layout()
        pPane.Layout()

        pObject.CallNextHandler(pEvent)
    

# Close GUI
def CloseGUI(pObject, pEvent):
        global pMainPane, pPane

        # A bugfix
        try:
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()

                App.g_kEventManager.RemoveBroadcastHandler(ET_ENGAGE, pMission, __name__ + ".HyperdriveStats")
                App.g_kEventManager.RemoveBroadcastHandler(ET_UPDATE_SLIDER, pMission, __name__ + ".UpdateSlider")
                App.g_kEventManager.RemoveBroadcastHandler(ET_REFRESH, pMission, __name__ + ".UpdateStats")
                App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".CloseGUI")
	   
        except:
                pass

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        # Just destroy the window, we don't need it anymore.
        App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

        pTCW.DeleteChild(pPane)

        pPane = None
        
        pMainPane = None
        

# Calculates and returns the ETA
def ReturnETA(pSelectedSpeed):
        global lStatsETA, pTimerETA

        # Reset vars
        lStatsETA = []
        pTimerETA = None
        
        # Grab values
        pPlayer = MissionLib.GetPlayer()
        pIterator = pPlayer.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if pSystem.GetName() in sHyperdriveList:
                   pStats = pSystem.GetConditionPercentage() * 100.0
                   pDisabled = pSystem.GetDisabledPercentage() * 100.0
                   if pStats <= pDisabled:
                       # Engine is disabled, treat it like it's destroyed
                       pStats = 0.0
                       
                   lStatsETA.append(pStats)
                   
		pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

        pPlayer.EndGetSubsystemMatch(pIterator)

        file = nt.open(sPathETA, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "# Do not Edit this file, Hyperdrive uses it to store data\n")
        i = 0
        # Write stats into the file
        for stat in lStatsETA:
            i = i + 1
            nt.write(file, "\nHyperdrive" + str(i) + " = " + str(stat))

        # We need to write all 20 lines into that file
        nTotal = i
        nCount = 20
        loop = 1
        while loop == 1:
            i = i + 1
            nt.write(file, "\nHyperdrive" + str(i) + " = " + "0.0")
            # Kill the loop
            if i >= nCount:
                loop = 0

        # Close file
        nt.close(file)

        # Reload EngineStats to get the latest engine status
        reload(EngineStatsETA)

        iTotal = EngineStatsETA.Hyperdrive1 + EngineStatsETA.Hyperdrive2 + EngineStatsETA.Hyperdrive3 + EngineStatsETA.Hyperdrive4 + EngineStatsETA.Hyperdrive5 + EngineStatsETA.Hyperdrive6 + EngineStatsETA.Hyperdrive7 + EngineStatsETA.Hyperdrive8 + EngineStatsETA.Hyperdrive9  + EngineStatsETA.Hyperdrive10 + EngineStatsETA.Hyperdrive11 + EngineStatsETA.Hyperdrive12 + EngineStatsETA.Hyperdrive13 + EngineStatsETA.Hyperdrive14 + EngineStatsETA.Hyperdrive15 + EngineStatsETA.Hyperdrive16 + EngineStatsETA.Hyperdrive17 + EngineStatsETA.Hyperdrive18 + EngineStatsETA.Hyperdrive19 + EngineStatsETA.Hyperdrive20 

        pTotal = iTotal / nTotal

        # Can't jump if the engines are below 1%, return Engines Disabled ETA
        if pTotal < 1.0:
            return ' '

        # Damn, all of this to get that... It's finally done!!!
        pTimerETA = 10000.0 / pTotal
        
        pTimerETA = pTimerETA / pSelectedSpeed

        pTimerETA = float(str(pTimerETA)[0:3+1])

        pTimerETA = str(pTimerETA)

        return pTimerETA


# Returns ideal ETA
def ReturnIdealETA(pSelectedSpeed):
        global lStatsIdealETA, pTimerIdealETA

        # Reset vars
        lStatsIdealETA = []
        pTimerIdealETA = None
        
        # Grab values
        pPlayer = MissionLib.GetPlayer()
        pIterator = pPlayer.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if pSystem.GetName() in sHyperdriveList:
                   pStats = 100.0
                       
                   lStatsIdealETA.append(pStats)
                   
		pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

        pPlayer.EndGetSubsystemMatch(pIterator)

        file = nt.open(sPathIdealETA, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "# Do not Edit this file, Hyperdrive uses it to store data\n")
        i = 0
        # Write stats into the file
        for stat in lStatsIdealETA:
            i = i + 1
            nt.write(file, "\nHyperdrive" + str(i) + " = " + str(stat))

        # We need to write all 20 lines into that file
        nTotal = i
        nCount = 20
        loop = 1
        while loop == 1:
            i = i + 1
            nt.write(file, "\nHyperdrive" + str(i) + " = " + "0.0")
            # Kill the loop
            if i >= nCount:
                loop = 0

        # Close file
        nt.close(file)

        # Reload EngineStats to get the latest engine status
        reload(EngineStatsIdealETA)

        iTotal = EngineStatsIdealETA.Hyperdrive1 + EngineStatsIdealETA.Hyperdrive2 + EngineStatsIdealETA.Hyperdrive3 + EngineStatsIdealETA.Hyperdrive4 + EngineStatsIdealETA.Hyperdrive5 + EngineStatsIdealETA.Hyperdrive6 + EngineStatsIdealETA.Hyperdrive7 + EngineStatsIdealETA.Hyperdrive8 + EngineStatsIdealETA.Hyperdrive9  + EngineStatsIdealETA.Hyperdrive10 + EngineStatsIdealETA.Hyperdrive11 + EngineStatsIdealETA.Hyperdrive12 + EngineStatsIdealETA.Hyperdrive13 + EngineStatsIdealETA.Hyperdrive14 + EngineStatsIdealETA.Hyperdrive15 + EngineStatsIdealETA.Hyperdrive16 + EngineStatsIdealETA.Hyperdrive17 + EngineStatsIdealETA.Hyperdrive18 + EngineStatsIdealETA.Hyperdrive19 + EngineStatsIdealETA.Hyperdrive20 

        pTotal = iTotal / nTotal

        # Damn, all of this to get that... It's finally done!!!
        pTimerIdealETA = 10000.0 / pTotal
        
        pTimerIdealETA = pTimerIdealETA / pSelectedSpeed

        pTimerIdealETA = float(str(pTimerIdealETA)[0:3+1])

        pTimerIdealETA = str(pTimerIdealETA)

        return pTimerIdealETA


# Return Engine Stats (Too many calculations need to be done)
def ReturnEngineStats():
        global lStatsEngines, pTimerEngineStats

        # Reset vars
        lStatsEngines = []
        pTimerEngineStats = None
        
        # Grab values
        pPlayer = MissionLib.GetPlayer()
        pIterator = pPlayer.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if pSystem.GetName() in sHyperdriveList:
                   pStats = pSystem.GetConditionPercentage() * 100.0
                   pDisabled = pSystem.GetDisabledPercentage() * 100.0
                   if pStats <= pDisabled:
                       # Engine is disabled, treat it like it's destroyed
                       pStats = 0.0
                       
                   lStatsEngines.append(pStats)
                   
		pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

        pPlayer.EndGetSubsystemMatch(pIterator)

        file = nt.open(sPathStats, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "# Do not Edit this file, Hyperdrive uses it to store data\n")
        i = 0
        # Write stats into the file
        for stat in lStatsEngines:
            i = i + 1
            nt.write(file, "\nHyperdrive" + str(i) + " = " + str(stat))

        # We need to write all 20 lines into that file
        nTotal = i
        nCount = 20
        loop = 1
        while loop == 1:
            i = i + 1
            nt.write(file, "\nHyperdrive" + str(i) + " = " + "0.0")
            # Kill the loop
            if i >= nCount:
                loop = 0

        # Close file
        nt.close(file)

        # Reload EngineStats to get the latest engine status
        reload(EngineStatsMenuCalc)

        iTotal = EngineStatsMenuCalc.Hyperdrive1 + EngineStatsMenuCalc.Hyperdrive2 + EngineStatsMenuCalc.Hyperdrive3 + EngineStatsMenuCalc.Hyperdrive4 + EngineStatsMenuCalc.Hyperdrive5 + EngineStatsMenuCalc.Hyperdrive6 + EngineStatsMenuCalc.Hyperdrive7 + EngineStatsMenuCalc.Hyperdrive8 + EngineStatsMenuCalc.Hyperdrive9  + EngineStatsMenuCalc.Hyperdrive10 + EngineStatsMenuCalc.Hyperdrive11 + EngineStatsMenuCalc.Hyperdrive12 + EngineStatsMenuCalc.Hyperdrive13 + EngineStatsMenuCalc.Hyperdrive14 + EngineStatsMenuCalc.Hyperdrive15 + EngineStatsMenuCalc.Hyperdrive16 + EngineStatsMenuCalc.Hyperdrive17 + EngineStatsMenuCalc.Hyperdrive18 + EngineStatsMenuCalc.Hyperdrive19 + EngineStatsMenuCalc.Hyperdrive20 

        pTotal = iTotal / nTotal

        pTotal = str(pTotal)

        return pTotal

        
# Calculate the stats of the drive engines and the time it'll take us to get to the destination
def HyperdriveStats(pObject, pEvent):
        global lStats, pTimer, pSelectedSpeed

        # Reset vars
        lStats = []
        pTimer = None
        
        # Grab values
        pPlayer = MissionLib.GetPlayer()
        pIterator = pPlayer.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

	# Add the stats of each engine into the list
        while (pSystem != None):
		if pSystem.GetName() in sHyperdriveList:
                   pStats = pSystem.GetConditionPercentage() * 100.0
                   pDisabled = pSystem.GetDisabledPercentage() * 100.0
                   if pStats <= pDisabled:
                       # Engine is disabled, treat it like it's destroyed
                       pStats = 0.0
                       
                   lStats.append(pStats)
                   
		pSystem = pPlayer.GetNextSubsystemMatch(pIterator)

        pPlayer.EndGetSubsystemMatch(pIterator)

        file = nt.open(sPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "# Do not Edit this file, Hyperdrive uses it to store data\n")
        i = 0
        # Write stats into the file
        for stat in lStats:
            i = i + 1
            nt.write(file, "\nHyperdrive" + str(i) + " = " + str(stat))

        # We need to write all 20 lines into that file
        nTotal = i
        nCount = 20
        loop = 1
        while loop == 1:
            i = i + 1
            nt.write(file, "\nHyperdrive" + str(i) + " = " + "0.0")
            # Kill the loop
            if i >= nCount:
                loop = 0

        # Close file
        nt.close(file)

        # Reload EngineStats to get the latest engine status
        reload(EngineStats)

        iTotal = EngineStats.Hyperdrive1 + EngineStats.Hyperdrive2 + EngineStats.Hyperdrive3 + EngineStats.Hyperdrive4 + EngineStats.Hyperdrive5 + EngineStats.Hyperdrive6 + EngineStats.Hyperdrive7 + EngineStats.Hyperdrive8 + EngineStats.Hyperdrive9  + EngineStats.Hyperdrive10 + EngineStats.Hyperdrive11 + EngineStats.Hyperdrive12 + EngineStats.Hyperdrive13 + EngineStats.Hyperdrive14 + EngineStats.Hyperdrive15 + EngineStats.Hyperdrive16 + EngineStats.Hyperdrive17 + EngineStats.Hyperdrive18 + EngineStats.Hyperdrive19 + EngineStats.Hyperdrive20 

        pTotal = iTotal / nTotal

        # Can't jump if the engines are below 1%
        if pTotal < 1.0:
            print 'Hyperdrive: Hyperdrive Engines are badly damaged, cannot initiate the jump'
            return

        # Damn, all of this to get that... It's finally done!!!
        pTimer = 10000.0 / pTotal
        
        pTimer = pTimer / pSelectedSpeed

        pTimer = float(str(pTimer)[0:3+1])

        # All OK, Kill the GUI
        CloseGUI(None, None)
        
        PreEngage(None, None)

                        
# Check if the ship is actually equiped with Hyperdrive
def HasHyperdrive(pShip):        
        # Grab values
        pIterator = pShip.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
	pSystem = pShip.GetNextSubsystemMatch(pIterator)

	# No ship has 20 engines! Right?!
        while (pSystem != None):
		if pSystem.GetName() in sHyperdriveList:
                    pStats = pSystem.GetConditionPercentage() * 100.0
                    if pStats >= 1.1:
                        # What's this? Hyperdrive is installed!
                        return 'Hyperdrive Installed'
                        break
		pSystem = pShip.GetNextSubsystemMatch(pIterator)

        pShip.EndGetSubsystemMatch(pIterator)


# Hyperdrive entry sequence
def PreEngage(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()    
        pSequence = App.TGSequence_Create ()
        pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
        pSequence.Play()
        
        # Checking function
        PositionPlayerOldSet(None, None)


# I regret separating this from PreEngage function but first I need to check that we will not smash into anything
def PositionPlayerOldSet(pObject, pEvent):
        global pAim, pDefault
    
        # Positioning function
        AimForGoodPos.GoodAim()

        # Check aim
        sAim = AimForGoodPos.CheckGoodAim()
        
        # Good Aim
        if sAim == 'TRUE':               
                # Who the hell knows, something still might go wrong. Better be safe then sorry!
                pGame = App.Game_GetCurrentGame()
                pGame.SetGodMode(1)
                # Collision settings
                pDefault = App.ProximityManager_GetPlayerCollisionsEnabled()
                App.ProximityManager_SetPlayerCollisionsEnabled(0)
                
                pPlayer = MissionLib.GetPlayer() 
                pSequence = App.TGSequence_Create()
                pAction = App.TGScriptAction_Create(__name__, "MoveForwardAI")
                pSequence.AddAction(pAction, None, 0)
                pAction = App.TGScriptAction_Create(__name__, "EnteringFlash")
                pSequence.AddAction(pAction, None, 1)
                pAction = App.TGScriptAction_Create(__name__, "MaxSpeed")
                pSequence.AddAction(pAction, None, 1)
                pAction = App.TGScriptAction_Create(__name__, "HyperdriveFlash")
                pSequence.AddAction(pAction, None, 3)
                pAction = App.TGScriptAction_Create(__name__, "HidePlayer")
                pSequence.AddAction(pAction, None, 4.5)
                pAction = App.TGScriptAction_Create(__name__, "RestoreSpeedValues")
                pSequence.AddAction(pAction, None, 5)
                pAction = App.TGScriptAction_Create(__name__, "SwapSets")
                pSequence.AddAction(pAction, None, 5)
                pAction = App.TGScriptAction_Create(__name__, "UnhidePlayer")
                pSequence.AddAction(pAction, None, 5.5)
                pAction = App.TGScriptAction_Create(__name__, "DisableHelmMenu")
                pSequence.AddAction(pAction, None, 6)
                pAction = App.TGScriptAction_Create(__name__, "ClearAIsAndBackToNormal")
                pSequence.AddAction(pAction, None, 6)
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName())
                pSequence.AddAction(pAction, None, 6.5)
                pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
                pSequence.AddAction(pAction, None, 6.5)
                
                pSequence.Play()

                # Reset Aim value
                pAim = 0

        # 6 seconds passed, nothing found, translate the ship to an empty location
        elif pAim >= 3:
                pGame = App.Game_GetCurrentGame()
                pGame.SetGodMode(1)
                # Collision settings
                pDefault = App.ProximityManager_GetPlayerCollisionsEnabled()
                App.ProximityManager_SetPlayerCollisionsEnabled(0)
                pPlayer = MissionLib.GetPlayer()
                pSet = pPlayer.GetContainingSet()
                fRadius = pPlayer.GetRadius() * 2.0
                try:
                                
                        pPlacement = App.PlacementObject_GetObject(pSet, "Player Start")               
                        pPlayer.SetTranslate(pPlacement.GetWorldLocation())
                        pPlayer.SetMatrixRotation(pPlacement.GetWorldRotation())                
                                        
                        pPlayer.UpdateNodeOnly()

                # No Player Start Location, use random coordinates
                except:
                                
                        vLocation = pPlayer.GetWorldLocation() 
                        vForward = pPlayer.GetWorldForwardTG()
                                
                        kPoint = App.TGPoint3() 
                        kPoint.Set(vLocation)

                        while pSet.IsLocationEmptyTG(kPoint, fRadius, 1) == 0: 
                                ChooseNewLocation(vLocation, vForward) 
                                kPoint.Set(vLocation) 
                                kPoint.Add(vForward)

                        pPlayer.SetTranslate(kPoint) 
                 
                        pPlayer.UpdateNodeOnly()

                # Update proximity manager info
                ProximityManager = pSet.GetProximityManager() 
                if (ProximityManager): 
                    ProximityManager.UpdateObject(pPlayer)

                pSequence = App.TGSequence_Create()
                pAction = App.TGScriptAction_Create(__name__, "MoveForwardAI")
                pSequence.AddAction(pAction, None, 0)
                pAction = App.TGScriptAction_Create(__name__, "EnteringFlash")
                pSequence.AddAction(pAction, None, 1)
                pAction = App.TGScriptAction_Create(__name__, "MaxSpeed")
                pSequence.AddAction(pAction, None, 1)
                pAction = App.TGScriptAction_Create(__name__, "HyperdriveFlash")
                pSequence.AddAction(pAction, None, 3)
                pAction = App.TGScriptAction_Create(__name__, "HidePlayer")
                pSequence.AddAction(pAction, None, 4.5)
                pAction = App.TGScriptAction_Create(__name__, "RestoreSpeedValues")
                pSequence.AddAction(pAction, None, 5)
                pAction = App.TGScriptAction_Create(__name__, "SwapSets")
                pSequence.AddAction(pAction, None, 5)
                pAction = App.TGScriptAction_Create(__name__, "UnhidePlayer")
                pSequence.AddAction(pAction, None, 5.5)
                pAction = App.TGScriptAction_Create(__name__, "DisableHelmMenu")
                pSequence.AddAction(pAction, None, 6)
                pAction = App.TGScriptAction_Create(__name__, "ClearAIsAndBackToNormal")
                pSequence.AddAction(pAction, None, 6)
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName())
                pSequence.AddAction(pAction, None, 6.5)
                pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
                pSequence.AddAction(pAction, None, 6.5)
                
                pSequence.Play()

                # Reset Aim value
                pAim = 0


        # Bad Aim, repeat process
        else:     
                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".PositionPlayerOldSet", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
                pAim = pAim + 1


# Exiting sequence
def CutsceneExit(pObject, pEvent):
        # Do a sweep to find empty direction
        AimForGoodPosExit.GoodAim()

        # Start the cutscenes
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
 
        pSequence = App.TGSequence_Create ()
        pAction = App.TGScriptAction_Create(__name__, "HidePlayer")
        pSequence.AddAction(pAction, None, 0)
        pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene")
        pSequence.AddAction(pAction, None, 0.5) 
        pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
        pSequence.AddAction(pAction, None, 0.5) 
        pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ())
        pSequence.AddAction(pAction, None, 0.5) 
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
        pSequence.AddAction(pAction, None, 0.5)
        # A bug, sometimes the game doesn't make the new set rendered and we miss the exit sequence
        if App.g_kSetManager.GetSet(pSet.GetName()):
            pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", pSet.GetName())
            pSequence.AddAction(pAction, None, 0.5)       
        pAction = App.TGScriptAction_Create(__name__, "HyperdriveFlash")
        pSequence.AddAction(pAction, None, 1)
        pAction = App.TGScriptAction_Create(__name__, "MoveForwardAI")
        pSequence.AddAction(pAction, None, 1)
        pAction = App.TGScriptAction_Create(__name__, "ExitingFlash")
        pSequence.AddAction(pAction, None, 2)
        pAction = App.TGScriptAction_Create(__name__, "MaxSpeedExit")
        pSequence.AddAction(pAction, None, 2.5)
        pAction = App.TGScriptAction_Create(__name__, "UnhidePlayer")
        pSequence.AddAction(pAction, None, 2.5)
        pAction = App.TGScriptAction_Create(__name__, "RestoreSpeedValues")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "ClearCourseSetting")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "EnableHelmMenu")
        pSequence.AddAction(pAction, None, 5)        
        pAction = App.TGScriptAction_Create(__name__, "StopShip")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "ClearAIsAndBackToNormal")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "TransferPlayer")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ())
        pSequence.AddAction(pAction, None, 5)
        if App.g_kSetManager.GetSet("bridge"):
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "GameCrashFix")
        pSequence.AddAction(pAction, None, 6)
            
        pSequence.Play()


# Entering sound
def EnteringFlash(pAction):
        # Check for custom sounds
        pPlayer = MissionLib.GetPlayer()
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "HyperdriveCustomizations"):
            pCustomization = pModule.HyperdriveCustomizations()
            
            # Customization exists, but does the sound entry exist?!
            if pCustomization.has_key('EntrySound'):
                pSound = "scripts/Custom/Hyperdrive/SFX/" + pCustomization['EntrySound']

                pEnterSound = App.TGSound_Create(pSound, "Enter", 0)
                pEnterSound.SetSFX(0) 
                pEnterSound.SetInterface(1)

            # No sound entry found
            else:
                pEnterSound = App.TGSound_Create("scripts/Custom/Hyperdrive/SFX/enterslipstream.wav", "Enter", 0)
                pEnterSound.SetSFX(0) 
                pEnterSound.SetInterface(1)

        # No customizations of any kind available for this ship.
        else:
            pEnterSound = App.TGSound_Create("scripts/Custom/Hyperdrive/SFX/enterslipstream.wav", "Enter", 0)
            pEnterSound.SetSFX(0) 
            pEnterSound.SetInterface(1)

        App.g_kSoundManager.PlaySound("Enter")

        return 0


# Exiting sound
def ExitingFlash(pAction):
        # Check for custom sounds
        pPlayer = MissionLib.GetPlayer()
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "HyperdriveCustomizations"):
            pCustomization = pModule.HyperdriveCustomizations()
            
            # Customization exists, but does the sound entry exist?!
            if pCustomization.has_key('ExitSound'):
                pSound = "scripts/Custom/Hyperdrive/SFX/" + pCustomization['ExitSound']

            	pExitSound = App.TGSound_Create(pSound, "Exit", 0)
            	pExitSound.SetSFX(0) 
            	pExitSound.SetInterface(1)

            # No sound entry found
            else:
            	pExitSound = App.TGSound_Create("scripts/Custom/Hyperdrive/SFX/exitslipstream.wav", "Exit", 0)
            	pExitSound.SetSFX(0) 
            	pExitSound.SetInterface(1)

        # No customizations of any kind available for this ship.
        else:
            pExitSound = App.TGSound_Create("scripts/Custom/Hyperdrive/SFX/exitslipstream.wav", "Exit", 0)
            pExitSound.SetSFX(0) 
            pExitSound.SetInterface(1)

    
        App.g_kSoundManager.PlaySound("Exit")

        return 0

         
# Sets up a max speed
def MaxSpeed(pAction):
        global pSpeed, pAccel, pPowerSetting

        pPlayer = MissionLib.GetPlayer()
        pImpulseSys = pPlayer.GetImpulseEngineSubsystem()
        pImpulse = pPlayer.GetImpulseEngineSubsystem().GetProperty()
	pSpeed = pImpulse.GetMaxSpeed()
	pAccel = pImpulse.GetMaxAccel()
	pPowerSetting = pImpulseSys.GetPowerPercentageWanted()

	pImpulse.SetMaxSpeed(200)

	pImpulse.SetMaxAccel(50)

	pImpulseSys.SetPowerPercentageWanted(1.0)

	pNewSpeed = pPlayer.GetImpulseEngineSubsystem().GetProperty().GetMaxSpeed()

	pPlayer.SetSpeed(pNewSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

	return 0


# Sets up a max speed
def MaxSpeedExit(pAction):
        global pSpeed, pAccel, pPowerSetting

        pPlayer = MissionLib.GetPlayer()
        pImpulseSys = pPlayer.GetImpulseEngineSubsystem()
        pImpulse = pPlayer.GetImpulseEngineSubsystem().GetProperty()
	pSpeed = pImpulse.GetMaxSpeed()
	pAccel = pImpulse.GetMaxAccel()
	pPowerSetting = pImpulseSys.GetPowerPercentageWanted()

	pImpulse.SetMaxSpeed(50)

	pImpulse.SetMaxAccel(25)

	pImpulseSys.SetPowerPercentageWanted(1.0)

	pNewSpeed = pPlayer.GetImpulseEngineSubsystem().GetProperty().GetMaxSpeed()

	pPlayer.SetSpeed(pNewSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

	return 0


# Restores original speed values
def RestoreSpeedValues(pAction):
        global pSpeed, pAccel, pPowerSetting

        pPlayer = MissionLib.GetPlayer()
        pImpulseSys = pPlayer.GetImpulseEngineSubsystem()
        pImpulse = pPlayer.GetImpulseEngineSubsystem().GetProperty()

        pImpulse.SetMaxSpeed(pSpeed)

	pImpulse.SetMaxAccel(pAccel)

	pImpulseSys.SetPowerPercentageWanted(pPowerSetting)

	pPlayer.SetSpeed(pSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
	
	pPlayer.SetVelocity(App.TGPoint3_GetModelForward())

	return 0


# Make the ship speed up
def SpeedUp(pAction):
        pPlayer = MissionLib.GetPlayer()
        pImpulse = pPlayer.GetImpulseEngineSubsystem().GetProperty()
        pSpeed = pImpulse.GetMaxSpeed()

        pPlayer.SetSpeed(pSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        return 0


# Stops a ship
def StopShip(pAction):
        pPlayer = MissionLib.GetPlayer()

        pPlayer.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        return 0        


# Sets a DS9FX AI to move the ship forward
def MoveForwardAI(pAction):
        pPlayer = MissionLib.GetPlayer()
        import Custom.Hyperdrive.Libs.DS9FXWormholeExitingSeqAI
        pPlayerCast = App.ShipClass_Cast(pPlayer)
        pPlayerCast.SetAI(Custom.Hyperdrive.Libs.DS9FXWormholeExitingSeqAI.CreateAI(pPlayerCast))

        return 0


# Clears AI and stops the ship
def ClearAIsAndBackToNormal(pAction):
        global pDefault, pWasCloaked
        
        pPlayer = MissionLib.GetPlayer()        
        import Custom.Hyperdrive.Libs.DS9FXStayAI
        pPlayerCast = App.ShipClass_Cast(pPlayer)
        pPlayerCast.SetAI(Custom.Hyperdrive.Libs.DS9FXStayAI.CreateAI(pPlayerCast))

        # Clear AI's
        pPlayer.ClearAI()

        import AI.Player.Stay
	MissionLib.SetPlayerAI("Helm", AI.Player.Stay.CreateAI(pPlayer))

	# Taging along, restore things back to normal
        pGame = App.Game_GetCurrentGame()
        pGame.SetGodMode(0)
        # Collision settings
        App.ProximityManager_SetPlayerCollisionsEnabled(pDefault)

        if pWasCloaked == 1:
            pCloak = pPlayer.GetCloakingSubsystem()
            if pCloak:
                pCloak.InstantCloak()

        return 0


# Swaps sets        
def SwapSets(pAction):
        Engage(None, None)

        return 0


# Hides player
def HidePlayer(pAction):
        pPlayer = MissionLib.GetPlayer()
        pPlayer.SetHidden(1)

        return 0


# Unhides player
def UnhidePlayer(pAction):
        pPlayer = MissionLib.GetPlayer()
        pPlayer.SetHidden(0)

        return 0


# Flash animation properties
def HyperdriveFlash(pAction):
            
        pPlayer = MissionLib.GetPlayer()
            
        # Load texture GFX
        LoadFlash.StartGFX()
        # Create flash
        LoadFlash.CreateGFX(pPlayer)

        return 0

        
# Here we go baby!
def Engage(pObject, pEvent):
        global bButton, pDest, pDestName, pTimer, pWasCloaked

        # Resolve the dark screen problem after a new object is created in the slipstream\hyperdrive set
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".FixDarkScreen")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_DESTROYED, pMission, __name__ + ".FixDarkScreenExplosions")

        # Clear players target first
        import TacticalInterfaceHandlers
	TacticalInterfaceHandlers.ClearTarget(None, None)

        # Disable the button
        bButton.SetDisabled()

        # Grab & initialize the dummy set
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pWasCloaked = 0
        
        if App.g_kSetManager.GetSet("HyperdriveTunnel1"):
            
                pDummySet = App.g_kSetManager.GetSet("HyperdriveTunnel1")

        else:
        
                pDummy = __import__("Systems.HyperdriveTunnel.HyperdriveTunnel1")
            
                pDummy.Initialize()

                pDummySet = pDummy.GetSet()

        pSys = __import__(pDest)

        pDestName = pSys.GetSetName()

        # Do the transfer
        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                # WTF, where did these asteroids come from... Time to filter them out
                fShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                fScript = fShip.GetScript()
                if fScript in sAsteroidList:
                    # print 'Asteroid detected, skipping'
                    continue

                # Hyperdrive ability?!
                HyperdriveInstalled = HasHyperdrive(fShip)
                if not HyperdriveInstalled == 'Hyperdrive Installed':
                    # For those we leave behind...
                    pWarp = fShip.GetWarpEngineSubsystem()
                    if pWarp:
                        DisableWarp(fShip, pWarp)
                    continue
                
		pSet.RemoveObjectFromSet(kShip.GetName())
		if kShip.GetName() == pPlayer.GetName():
                    if pPlayer.IsCloaked():
                        pWasCloaked = 1
                        pCloak = pPlayer.GetCloakingSubsystem()
                        if pCloak:
                            pCloak.InstantDecloak()
		pDummySet.AddObjectToSet(kShip, kShip.GetName())

                # Get location of the player
		pLocation = pPlayer.GetWorldLocation() 

                # New way to choose new location
                kShipX = pLocation.GetX()
                
                kShipY = pLocation.GetY()
                
                kShipZ = pLocation.GetZ()

                RateX = GetRandomRate(50, 5)

                RateY = GetRandomRate(50, 5)

                RateZ = GetRandomRate(50, 5)

                pXCoord = kShipX + RateX

                pYCoord = kShipY + RateY

                pZCoord = kShipZ + RateZ

                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                kShip.UpdateNodeOnly() 


                # Update proximity manager info
                ProximityManager = pDummySet.GetProximityManager() 
                if (ProximityManager): 
                        ProximityManager.UpdateObject(kShip)
                        

        # Purge memory when transfering between sets
        App.g_kLODModelManager.Purge()

        scale = 1000

        # Create the tunnel
        TunnelString = "Hyperdrive Outer"
        pTunnel = loadspacehelper.CreateShip("hyperdrive", pDummySet, TunnelString, "Player Start")
       
        # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
        fTunnel = MissionLib.GetShip(TunnelString, pDummySet) 
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.3, 0)
        fTunnel.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        # Invincible
        fTunnel.SetInvincible(1)
        fTunnel.SetHurtable(0)
        fTunnel.SetTargetable(0)

        # Very large ;)
        fTunnel.SetScale(scale)
        
        # Create the tunnel
        TunnelString2 = "Hyperdrive Inner"
        pTunnel2 = loadspacehelper.CreateShip("hyperdrive", pDummySet, TunnelString2, "Player Start")
       
        # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
        fTunnel2 = MissionLib.GetShip(TunnelString2, pDummySet)
        # Disable collisions with the 2 models
        fTunnel2.EnableCollisionsWith(fTunnel, 0)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.3, 0)
        fTunnel2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        # Invincible
        fTunnel2.SetInvincible(1)
        fTunnel2.SetHurtable(0)
        fTunnel2.SetTargetable(0)

        # Very large ;)
        fTunnel2.SetScale(scale)

	# Custom tunnel textures?
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "HyperdriveCustomizations"):
            pCustomization = pModule.HyperdriveCustomizations()
            
            # Customization exists, but does the tunnel texture entry exist?!
            if pCustomization.has_key('TunnelTexture'):
                # Bingo, replace textures for both tunnels then
                GFX = "scripts/Custom/Hyperdrive/GFX/" + pCustomization['TunnelTexture']

 		fTunnel.ReplaceTexture(GFX, "outer_glow")
		fTunnel2.ReplaceTexture(GFX, "outer_glow")

		fTunnel.RefreshReplacedTextures()
            	fTunnel2.RefreshReplacedTextures()
            	

        # Disable player collision with the cone
        fTunnel.EnableCollisionsWith(pPlayer, 0)
        fTunnel2.EnableCollisionsWith(pPlayer, 0)

        # Disable any ship collisions with the cone
        for kShip in pDummySet.GetClassObjectList(App.CT_SHIP):
            pShip = App.ShipClass_GetObject(pDummySet, kShip.GetName())
            fTunnel.EnableCollisionsWith(pShip, 0)
            fTunnel2.EnableCollisionsWith(pShip, 0)

        
        # Position the tunnel so that it appears you're inside it
        pPlayerBackward = pPlayer.GetWorldBackwardTG()
        pPlayerDown = pPlayer.GetWorldDownTG()
        pPlayerPosition = pPlayer.GetWorldLocation()

        fTunnel.AlignToVectors(pPlayerBackward, pPlayerDown)
        fTunnel.SetTranslate(pPlayerPosition)
        fTunnel.UpdateNodeOnly()

        fTunnel2.AlignToVectors(pPlayerBackward, pPlayerDown)
        fTunnel2.SetTranslate(pPlayerPosition)
        fTunnel2.UpdateNodeOnly()

        # Interface fix
        App.InterfaceModule_DoTheRightThing()

        # Speed the ship up
        SpeedUp(None)

        # Print the destination
        DestinationOutput(None, None)

        # Timer to call in the next sequence
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitingRedirect", App.g_kUtopiaModule.GetGameTime() + pTimer, 0, 0)


# Exit in the desired set
def Exiting(pObject, pEvent):
        global pDest, pDefault, pWasCloaked

        pGame = App.Game_GetCurrentGame()
        pGame.SetGodMode(1)

        # Collision settings
        pDefault = App.ProximityManager_GetPlayerCollisionsEnabled()
        App.ProximityManager_SetPlayerCollisionsEnabled(0)

        # Clear players target first
        import TacticalInterfaceHandlers
	TacticalInterfaceHandlers.ClearTarget(None, None)
        
        # Now the magic happens
        pPlayer = MissionLib.GetPlayer()
        pPlayerName = pPlayer.GetName()
        pSet = pPlayer.GetContainingSet()
        fRadius = pPlayer.GetRadius() * 2.0
        pWasCloaked = 0

        pSys = __import__(pDest)

        pSysName = pSys.GetSetName()

        if App.g_kSetManager.GetSet(pSysName):

            pModule = App.g_kSetManager.GetSet(pSysName)

        else:
            
            # Import the dest set & initialize it
            pSys.Initialize()
            
            pModule = pSys.GetSet()

        pSet.RemoveObjectFromSet(pPlayerName)
        if pPlayer.IsCloaked():
            pWasCloaked = 1
            pCloak = pPlayer.GetCloakingSubsystem()
            if pCloak:
                pCloak.InstantDecloak()
        pModule.AddObjectToSet(pPlayer, pPlayerName)

        # Avoiding any potential problems
        try:
                        
                pPlacement = App.PlacementObject_GetObject(pModule, "Player Start")               
                pPlayer.SetTranslate(pPlacement.GetWorldLocation())
                pPlayer.SetMatrixRotation(pPlacement.GetWorldRotation())                
                                
                pPlayer.UpdateNodeOnly()

        # No Player Start Location, use random coordinates
        except:
                        
                vLocation = pPlayer.GetWorldLocation() 
                vForward = pPlayer.GetWorldForwardTG()
                        
                kPoint = App.TGPoint3() 
                kPoint.Set(vLocation)

                while pModule.IsLocationEmptyTG(kPoint, fRadius, 1) == 0: 
                        ChooseNewLocation(vLocation, vForward) 
                        kPoint.Set(vLocation) 
                        kPoint.Add(vForward)

                pPlayer.SetTranslate(kPoint) 
         
                pPlayer.UpdateNodeOnly()


        # Update proximity manager info
        ProximityManager = pModule.GetProximityManager() 
        if (ProximityManager): 
            ProximityManager.UpdateObject(pPlayer)
                        

        # Purge memory when transfering between sets
        App.g_kLODModelManager.Purge()

        # Deactivate the fix, we don't need it anymore
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".FixDarkScreen")
        except:
            pass
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_DESTROYED, pMission, __name__ + ".FixDarkScreenExplosions")
        except:
            pass

        # Restore warp and force ai's back on
        for kShip in pModule.GetClassObjectList(App.CT_SHIP):
            fShip = App.ShipClass_GetObject(pModule, kShip.GetName())
            pWarp = fShip.GetWarpEngineSubsystem()
            if pWarp:
                EnableWarp(fShip, pWarp)

        # Make sure we execute everything in a timely manner by delaying the exiting sequence
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".CutsceneExit", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)

        # Delay AI ships
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".AIExit", App.g_kUtopiaModule.GetGameTime() + 7, 0, 0)


# AI exits now
def AIExit(pObject, pEvent):
        global pDest
        
        # Now the magic happens
        pPlayer = MissionLib.GetPlayer()
        pSet = App.g_kSetManager.GetSet('HyperdriveTunnel1')

        pSys = __import__(pDest)

        pSysName = pSys.GetSetName()

        if App.g_kSetManager.GetSet(pSysName):

            pModule = App.g_kSetManager.GetSet(pSysName)

        else:
            
            # Import the dest set & initialize it
            pSys.Initialize()
            
            pModule = pSys.GetSet()

        # Delete models from memory, we no longer need them until the next trip
        pSet.DeleteObjectFromSet("Hyperdrive Outer")
        pSet.DeleteObjectFromSet("Hyperdrive Inner")

        # Do the transfer
        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                # WTF, where did these asteroids come from... Time to filter them out
                fShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                fScript = fShip.GetScript()
                if fScript in sAsteroidList:
                    # print 'Asteroid detected, skipping'
                    continue
                
		pSet.RemoveObjectFromSet(kShip.GetName()) 
		pModule.AddObjectToSet(kShip, kShip.GetName())
		
                # Get location of the player
		pLocation = pPlayer.GetWorldLocation() 

                # Position all ships near the player
                kShipX = pLocation.GetX()
                
                kShipY = pLocation.GetY()
                
                kShipZ = pLocation.GetZ()

                RateX = GetRandomRate(100, 25)

                RateY = GetRandomRate(100, 25)

                RateZ = GetRandomRate(100, 25)

                pXCoord = kShipX + RateX

                pYCoord = kShipY + RateY

                pZCoord = kShipZ + RateZ

                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                kShip.UpdateNodeOnly() 

                # Update proximity manager info
                ProximityManager = pModule.GetProximityManager() 
                if (ProximityManager): 
                        ProximityManager.UpdateObject(kShip)

                # Play the sounds
                pModules = __import__(fScript)
                # Is there a customization for this ship available?
                if hasattr(pModules, "HyperdriveCustomizations"):
                    pCustomization = pModules.HyperdriveCustomizations()
                    
                    # Customization exists, but does the sound entry exist?!
                    if pCustomization.has_key('ExitSound'):
                        pSound = "scripts/Custom/Hyperdrive/SFX/" + pCustomization['ExitSound']

                        pExitSound = App.TGSound_Create(pSound, "Exit", 0)
                        pExitSound.SetSFX(0) 
                        pExitSound.SetInterface(1)

                    # No sound entry found
                    else:
                        pExitSound = App.TGSound_Create("scripts/Custom/Hyperdrive/SFX/exitslipstream.wav", "Exit", 0)
                        pExitSound.SetSFX(0) 
                        pExitSound.SetInterface(1)

                # No customizations of any kind available for this ship.
                else:
                    pExitSound = App.TGSound_Create("scripts/Custom/Hyperdrive/SFX/exitslipstream.wav", "Exit", 0)
                    pExitSound.SetSFX(0) 
                    pExitSound.SetInterface(1)
            
                App.g_kSoundManager.PlaySound("Exit")

      
# Redirect function
def ExitingRedirect(pObject, pEvent):
        Exiting(None, None)

            
# Clears set course menu
def ClearCourseSetting(pAction):
        pButton = App.SortedRegionMenu_GetWarpButton()
	if (pButton != None):
		pButton.SetDestination(None)

        return 0


# Disable helm menu, just like warping
def DisableHelmMenu(pAction):
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pHelmMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString("Helm"))
	App.g_kLocalizationManager.Unload(pDatabase)

	pHelmMenu.SetDisabled()

	return 0


# Enable helm menu
def EnableHelmMenu(pAction):
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pHelmMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString("Helm"))
	App.g_kLocalizationManager.Unload(pDatabase)

	pHelmMenu.SetEnabled()

	return 0


# Clever way of fixing the smash into planet bug.
def TransferPlayer(pAction):
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        fRadius = pPlayer.GetRadius() * 2.0
        try:
                                
            pPlacement = App.PlacementObject_GetObject(pSet, "Player Start")               
            pPlayer.SetTranslate(pPlacement.GetWorldLocation())
            pPlayer.SetMatrixRotation(pPlacement.GetWorldRotation())                
                                        
            pPlayer.UpdateNodeOnly()

        # No Player Start Location, use random coordinates
        except:
                                
            vLocation = pPlayer.GetWorldLocation() 
            vForward = pPlayer.GetWorldForwardTG()
                                
            kPoint = App.TGPoint3() 
            kPoint.Set(vLocation)

            while pSet.IsLocationEmptyTG(kPoint, fRadius, 1) == 0: 
                    ChooseNewLocation(vLocation, vForward) 
                    kPoint.Set(vLocation) 
                    kPoint.Add(vForward)

            pPlayer.SetTranslate(kPoint) 
                 
            pPlayer.UpdateNodeOnly()

        # Update proximity manager info
        ProximityManager = pSet.GetProximityManager() 
        if (ProximityManager): 
            ProximityManager.UpdateObject(pPlayer)

        return 0


# Disable warp on ships we leave behind
def DisableWarp(pShip, pSubsystem, bIsChild = 0):
        if (bIsChild != 0) or (pSubsystem.GetNumChildSubsystems() == 0):
                fStats = pSubsystem.GetProperty().GetDisabledPercentage()
                pSubsystem.GetProperty().SetDisabledPercentage(2.0)

	for i in range(pSubsystem.GetNumChildSubsystems()):
		pChild = pSubsystem.GetChildSubsystem(i)

		if (pChild != None):
			DisableWarp(pShip, pChild, 1)        


# Enable warp on ships we've tampered with, check the unique signature that we leave on those ships
def EnableWarp(pShip, pSubsystem, bIsChild = 0):
        if (bIsChild != 0) or (pSubsystem.GetNumChildSubsystems() == 0):
                fStats = pSubsystem.GetProperty().GetDisabledPercentage()
                if fStats > 1.0:
                    pSubsystem.GetProperty().SetDisabledPercentage(0.5)
                    # This is our ship which also means that it's ai might not respond, let's fix this
                    pGame = App.Game_GetCurrentGame()
                    pEpisode = pGame.GetCurrentEpisode()
                    pMission = pEpisode.GetCurrentMission()
                    pEnemy = pMission.GetEnemyGroup()	
                    pNeutral = pMission.GetNeutralGroup()	
                    pFriendly = pMission.GetFriendlyGroup()

                    if (pFriendly.IsNameInGroup(pShip.GetName())):
                        FriendlyAI(pShip)

                    elif (pNeutral.IsNameInGroup(pShip.GetName())):
                        NeutralAI(pShip)

                    elif (pEnemy.IsNameInGroup(pShip.GetName())):
                        EnemyAI(pShip)
                    
	for i in range(pSubsystem.GetNumChildSubsystems()):
		pChild = pSubsystem.GetChildSubsystem(i)

		if (pChild != None):
			 EnableWarp(pShip, pChild, 1)


# Assign Friendly AI
def FriendlyAI(pShip):
        NoQBR = None
        import QuickBattle.QuickBattle
        try:
            import Custom.QuickBattleGame.QuickBattle
        except:
            NoQBR = 'NoQBR'

        if NoQBR == 'NoQBR':
            if QuickBattle.QuickBattle.pFriendlies:
		if (pShip.GetShipProperty().IsStationary() == 1):

			import QuickBattle.StarbaseFriendlyAI
			pShip.SetAI(QuickBattle.StarbaseFriendlyAI.CreateAI(pShip))
		else:
			import QuickBattle.QuickBattleFriendlyAI
			pShip.SetAI(QuickBattle.QuickBattleFriendlyAI.CreateAI(pShip))

        else:
            if QuickBattle.QuickBattle.pFriendlies:
                    if (pShip.GetShipProperty().IsStationary() == 1):

                            import QuickBattle.StarbaseFriendlyAI
                            pShip.SetAI(QuickBattle.StarbaseFriendlyAI.CreateAI(pShip))
                    else:
                            import QuickBattle.QuickBattleFriendlyAI
                            pShip.SetAI(QuickBattle.QuickBattleFriendlyAI.CreateAI(pShip))

            elif Custom.QuickBattleGame.QuickBattle.pFriendlies:
                    if (pShip.GetShipProperty().IsStationary() == 1):

                            import Custom.QuickBattleGame.StarbaseFriendlyAI
                            pShip.SetAI(Custom.QuickBattleGame.StarbaseFriendlyAI.CreateAI(pShip))
                    else:
                            import Custom.QuickBattleGame.QuickBattleFriendlyAI
                            pShip.SetAI(Custom.QuickBattleGame.QuickBattleFriendlyAI.CreateAI(pShip, 1, 1))


# Assign Enemy AI
def EnemyAI(pShip):
        NoQBR = None
        import QuickBattle.QuickBattle
        try:
            import Custom.QuickBattleGame.QuickBattle
        except:
            NoQBR = 'NoQBR'

        if NoQBR == 'NoQBR':
            if QuickBattle.QuickBattle.pEnemies:
		if (pShip.GetShipProperty().IsStationary() == 1):

			import QuickBattle.StarbaseAI
			pShip.SetAI(QuickBattle.StarbaseAI.CreateAI(pShip))
		else:
			import QuickBattle.QuickBattleAI
			pShip.SetAI(QuickBattle.QuickBattleAI.CreateAI(pShip))

	else:
            if QuickBattle.QuickBattle.pEnemies:
                    if (pShip.GetShipProperty().IsStationary() == 1):

                            import QuickBattle.StarbaseAI
                            pShip.SetAI(QuickBattle.StarbaseAI.CreateAI(pShip))
                    else:
                            import QuickBattle.QuickBattleAI
                            pShip.SetAI(QuickBattle.QuickBattleAI.CreateAI(pShip))

            elif Custom.QuickBattleGame.QuickBattle.pEnemies:
                    if (pShip.GetShipProperty().IsStationary() == 1):

                            import Custom.QuickBattleGame.StarbaseAI
                            pShip.SetAI(Custom.QuickBattleGame.StarbaseAI.CreateAI(pShip))
                    else:
                            import Custom.QuickBattleGame.QuickBattleAI
                            pShip.SetAI(Custom.QuickBattleGame.QuickBattleAI.CreateAI(pShip, 1, 1))	


# Assign Neutral AI
def NeutralAI(pShip):
        NoQBR = None
        import QuickBattle.QuickBattle
        try:
            import Custom.QuickBattleGame.QuickBattle
        except:
            NoQBR = 'NoQBR'

        if NoQBR == 'NoQBR':
            return

        if Custom.QuickBattleGame.QuickBattle.pNeutrals:
		if (pShip.GetShipProperty().IsStationary() == 1):

			import Custom.QuickBattleGame.StarbaseNeutralAI
			pShip.SetAI(Custom.QuickBattleGame.StarbaseNeutralAI.CreateAI(pShip))
		else:
			import Custom.QuickBattleGame.NeutralAI
			pShip.SetAI(Custom.QuickBattleGame.NeutralAI.CreateAI(pShip, 1, 1))


# Returns a random number
def GetRandomRate(Max, Number):
    
        return App.g_kSystemWrapper.GetRandomNumber(Max) + Number


# Tell the user where's he headed
def DestinationOutput(pObject, pEvent):
        global pPaneID
        
        # Attach a pane
        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        # Create a sequence and play it
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(TextSequence(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()


# Print the text to the screen
def TextSequence(pPane):
        global pTimer
        
        # Sequence 
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
            
        # Print the destination
        pLine = "Destination: " + pDestName
        pAction = LineAction(pLine, pPane, 2, pTimer, 16)
        pSequence.AddAction(pAction, None, 0)
        # ETA Counter
        sETA = pTimer
        sETA = int(sETA)
        pLine = "ETA: " + str(sETA) + " seconds"
        pAction = LineAction(pLine, pPane, 4, 0.8, 16)
        pSequence.AddAction(pAction, None, 0)
        sETA = sETA - 1
        fTime = 0.8
        while sETA > 0:
            pLine = "ETA: " + str(sETA) + " seconds"
            pAction = LineAction(pLine, pPane, 4, 0.8, 16)
            pSequence.AddAction(pAction, None, fTime)
            sETA = sETA - 1
            fTime = fTime + 1
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 1)
        pSequence.Play()


# Add a line action 
def LineAction(sLine, pPane, fPos, duration, fontSize):
	fHeight = fPos * 0.0375
	App.TGCreditAction_SetDefaultColor(0.65, 0.65, 1.0, 1.0)
	pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
	return pAction


# Kill the pane, just a reuse of the code from DS9FX
def KillPane(pAction):
        global pPaneID
        
        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
	App.g_kRootWindow.DeleteChild(pPane)
		
	pPaneID = App.NULL_ID
	
	return 0


# When a new object is created in the hyperdrive set it collides with the massive tunnel thus darkening the screen
def FixDarkScreen(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()

        if (pSet.GetName() == "HyperdriveTunnel1"):            
            fTunnel = MissionLib.GetShip("Hyperdrive Outer", pSet) 
            fTunnel2 = MissionLib.GetShip("Hyperdrive Inner", pSet) 
            
            # Disable player collision with the cone
            try:
                fTunnel.EnableCollisionsWith(pPlayer, 0)
            except:
                pass
            try:
                fTunnel2.EnableCollisionsWith(pPlayer, 0)
            except:
                pass

            # Disable any ship collisions with the cone
            for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                try:
                    fTunnel.EnableCollisionsWith(pShip, 0)
                except:
                    pass
                try:
                    fTunnel2.EnableCollisionsWith(pShip, 0)
                except:
                    pass


# When a ship explodes, sometimes also the dark screen will show up
def FixDarkScreenExplosions(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        
        pSet.DeleteObjectFromSet('Hyperdrive Outer')
        pSet.DeleteObjectFromSet('Hyperdrive Inner')

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".FixDarkScreenExplosionsDelay", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)


# Event delayed
def FixDarkScreenExplosionsDelay(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        scale = 1000
        
        # Create the tunnel
        TunnelString = "Hyperdrive Outer"
        pTunnel = loadspacehelper.CreateShip("hyperdrive", pSet, TunnelString, "Player Start")
       
        # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
        fTunnel = MissionLib.GetShip(TunnelString, pSet) 
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.3, 0)
        fTunnel.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        # Invincible
        fTunnel.SetInvincible(1)
        fTunnel.SetHurtable(0)
        fTunnel.SetTargetable(0)

        # Very large ;)
        fTunnel.SetScale(scale)
        
        # Create the tunnel
        TunnelString2 = "Hyperdrive Inner"
        pTunnel2 = loadspacehelper.CreateShip("hyperdrive", pSet, TunnelString2, "Player Start")
       
        # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
        fTunnel2 = MissionLib.GetShip(TunnelString2, pSet)
        # Disable collisions with the 2 models
        fTunnel2.EnableCollisionsWith(fTunnel, 0)
        vCurVelocity = App.TGPoint3()
        vCurVelocity.SetXYZ(0, 0.3, 0)
        fTunnel2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

        # Invincible
        fTunnel2.SetInvincible(1)
        fTunnel2.SetHurtable(0)
        fTunnel2.SetTargetable(0)

        # Very large ;)
        fTunnel2.SetScale(scale)

	# Custom tunnel textures?
        pModule = __import__(pPlayer.GetScript())

        # Is there a customization for this ship available?
        if hasattr(pModule, "HyperdriveCustomizations"):
            pCustomization = pModule.HyperdriveCustomizations()
            
            # Customization exists, but does the tunnel texture entry exist?!
            if pCustomization.has_key('TunnelTexture'):
                # Bingo, replace textures for both tunnels then
                GFX = "scripts/Custom/Hyperdrive/GFX/" + pCustomization['TunnelTexture']

 		fTunnel.ReplaceTexture(GFX, "outer_glow")
		fTunnel2.ReplaceTexture(GFX, "outer_glow")

		fTunnel.RefreshReplacedTextures()
            	fTunnel2.RefreshReplacedTextures()
            	

        # Disable player collision with the cone
        fTunnel.EnableCollisionsWith(pPlayer, 0)
        fTunnel2.EnableCollisionsWith(pPlayer, 0)

        # Disable any ship collisions with the cone
        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
            pShip = App.ShipClass_GetObject(pSet, kShip.GetName())
            fTunnel.EnableCollisionsWith(pShip, 0)
            fTunnel2.EnableCollisionsWith(pShip, 0)

        
        # Position the tunnel so that it appears you're inside it
        pPlayerBackward = pPlayer.GetWorldBackwardTG()
        pPlayerDown = pPlayer.GetWorldDownTG()
        pPlayerPosition = pPlayer.GetWorldLocation()

        fTunnel.AlignToVectors(pPlayerBackward, pPlayerDown)
        fTunnel.SetTranslate(pPlayerPosition)
        fTunnel.UpdateNodeOnly()

        fTunnel2.AlignToVectors(pPlayerBackward, pPlayerDown)
        fTunnel2.SetTranslate(pPlayerPosition)
        fTunnel2.UpdateNodeOnly()        


# From QB.py
def ChooseNewLocation(vOrigin, vOffset): 
	# Add some random amount to vOffset 
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0 
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber (50) + 1) 
 
	vOffset.SetX( vOffset.GetX() + fUnitRandom ) 
 
 
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0 
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber (50) + 1) 
 
	vOffset.SetY( vOffset.GetY() + fUnitRandom ) 
 
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0 
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber (50) + 1) 
 
	vOffset.SetZ( vOffset.GetZ() + fUnitRandom ) 
 
	return 0 


# Somehow this piece of code prevents a game crash which sometimes occurs
def GameCrashFix(pAction):

        pTop = App.TopWindow_GetTopWindow()
        pTop.ForceTacticalVisible()
        pTop.ForceBridgeVisible()

        return 0


# Removes a menu button
def RemoveMenu():
        global bButton
        pBridge = App.g_kSetManager.GetSet("bridge")
        pHelm = App.CharacterClass_GetObject(pBridge, "Helm")
        pMenu = pHelm.GetMenu()
	if (pMenu != None):
		pButton = pMenu.GetButton("Hyperdrive Details")
		if (pButton != None):
			pMenu.DeleteChild(pButton)
			bButton = None


# From CWS 2.0
def CreateSlidebar (pName, eType, fMaxSpeed):
        global maxWarp, cruiseWarp
        
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pBar = App.STNumericBar_Create()

        ##### Set Our Range. 
	pBar.SetRange(0.0, fMaxSpeed)
	pBar.SetKeyInterval(0.01)
	pBar.SetMarkerValue(fMaxSpeed)
	pBar.SetValue(fMaxSpeed)
	pBar.SetUseMarker(0)
	pBar.SetUseAlternateColor(0)
	pBar.SetUseButtons(0)

	NormalColor = App.TGColorA() 
	NormalColor.SetRGBA(0.5, 0.5, 1.0, 1.0)
	EmptyColor = App.TGColorA() 
	EmptyColor.SetRGBA(0.5, 0.5, 0.5, 1.0)

	pBar.SetNormalColor(NormalColor)
	pBar.SetEmptyColor(EmptyColor)
	pText = pBar.GetText()
	pText.SetStringW(pName)

	pBar.Resize(0.25, 0.04, 0)

	pEvent = App.TGFloatEvent_Create()
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetFloat(fMaxSpeed)
	pEvent.SetEventType(eType)

	pBar.SetUpdateEvent(pEvent)

	return pBar


# Sometimes BC doesn't acknowledge AI so we 'force' him to do so       
def CreateAI(pShip):
	pPlayer = MissionLib.GetPlayer()

        Random = lambda fMin, fMax : App.g_kSystemWrapper.GetRandomNumber((fMax - fMin) * 1000.0) / 1000.0 - fMin
        # Range values used in the AI.
        fInRange = 150.0 + Random(-25, 20)

	#########################################
	# Creating PlainAI Intercept at (279, 253)
	pIntercept = App.PlainAI_Create(pShip, "Intercept")
	pIntercept.SetScriptModule("Intercept")
	pIntercept.SetInterruptable(1)
	pScript = pIntercept.GetScriptInstance()
	pScript.SetTargetObjectName(pPlayer.GetName())
	# Done creating PlainAI Intercept
	#########################################
	#########################################
	# Creating ConditionalAI ConditionIntercept at (148, 273)
	## Conditions:
	#### Condition HaveToIntercept
	pHaveToIntercept = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fInRange, pPlayer.GetName(), pShip.GetName())
	## Evaluation function:
	def EvalFunc(bHaveToIntercept):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bHaveToIntercept:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionIntercept = App.ConditionalAI_Create(pShip, "ConditionIntercept")
	pConditionIntercept.SetInterruptable(1)
	pConditionIntercept.SetContainedAI(pIntercept)
	pConditionIntercept.AddCondition(pHaveToIntercept)
	pConditionIntercept.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionIntercept
	#########################################
	#########################################
	# Creating PlainAI Follow at (280, 181)
	pFollow = App.PlainAI_Create(pShip, "Follow")
	pFollow.SetScriptModule("FollowObject")
	pFollow.SetInterruptable(1)
	pScript = pFollow.GetScriptInstance()
	pScript.SetFollowObjectName(pPlayer.GetName())
	pScript.SetRoughDistances(10,20,30)
	# Done creating PlainAI Follow
	#########################################
	#########################################
	# Creating ConditionalAI PlayerInSameSet at (164, 201)
	## Conditions:
	#### Condition InSet
	pInSet = App.ConditionScript_Create("Conditions.ConditionAllInSameSet", "ConditionAllInSameSet", pShip.GetName(), pPlayer.GetName())
	## Evaluation function:
	def EvalFunc(bInSet):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInSet:
			# Player is in the same set as we are.
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pPlayerInSameSet = App.ConditionalAI_Create(pShip, "PlayerInSameSet")
	pPlayerInSameSet.SetInterruptable(1)
	pPlayerInSameSet.SetContainedAI(pFollow)
	pPlayerInSameSet.AddCondition(pInSet)
	pPlayerInSameSet.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI PlayerInSameSet
	#########################################
	#########################################
	# Creating CompoundAI FollowWarp at (281, 125)
	import AI.Compound.FollowThroughWarp
	pFollowWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName())
	# Done creating CompoundAI FollowWarp
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (47, 125)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (139, 132)
	pPriorityList.AddAI(pConditionIntercept, 1)
	pPriorityList.AddAI(pPlayerInSameSet, 2)
	pPriorityList.AddAI(pFollowWarp, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (6, 188)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
