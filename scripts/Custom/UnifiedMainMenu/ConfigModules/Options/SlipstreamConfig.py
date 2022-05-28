# by USS Sovereign


# Imports
import App
import nt
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import SlipstreamConfiguration

# Events
ET_OPTION = App.UtopiaModule_GetNextEventType()

# Timer properties
ET_TIMER_EVENT = App.UtopiaModule_GetNextEventType()
idTimer = App.NULL_ID

# Config path
sPath = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\SlipstreamConfiguration.py"

# lists
lGFXTunnel = ["Default", "Alternate 1", "Alternate 2", "Alternate 3", "Alternate 4", "Alternate 5", "Alternate 6", "Alternate 7"]
lFlash = ["Default", "Alternate"]
lBackdrop = ["Default", "Alternate", "Off"]

# dicts
dGFXTunnel = {"Default" : "Default", "Alternate 1" : "SlipstreamTunnelAlt1.tga", "Alternate 2" : "SlipstreamTunnelAlt2.tga", "Alternate 3" : "SlipstreamTunnelAlt3.tga", "Alternate 4" : "SlipstreamTunnelAlt4.tga", "Alternate 5" : "SlipstreamTunnelAlt5.tga", "Alternate 6" : "SlipstreamTunnelAlt6.tga", "Alternate 7" : "SlipstreamTunnelAlt7.tga"}
dGFXTunnelTrans = {"Default" : "Default", "SlipstreamTunnelAlt1.tga" : "Alternate 1", "SlipstreamTunnelAlt2.tga": "Alternate 2", "SlipstreamTunnelAlt3.tga" : "Alternate 3", "SlipstreamTunnelAlt4.tga" : "Alternate 4", "SlipstreamTunnelAlt5.tga" : "Alternate 5", "SlipstreamTunnelAlt6.tga" : "Alternate 6", "SlipstreamTunnelAlt7.tga" : "Alternate 7"}
dFlash = {"Default" : "Default", "Alternate" : "SlipstreamFlashAlternate.tga"}
dFlashTrans = {"Default" : "Default", "SlipstreamFlashAlternate.tga" : "Alternate"}
dBackdrop = {"Default" : "Default", "Alternate" : "SlipstreamBackdropAlt.tga", "Off" : "Off"}
dBackdropTrans = {"Default" : "Default", "SlipstreamBackdropAlt.tga" : "Alternate", "Off" : "Off"}


# Returns a name to Unified Main Menu
def GetName():
        return "The Slipstream"


# Creates menus
def CreateMenu(pOptionPane, pContentPanel, bGameEnded = 0):
        CreateGFXOptions(pOptionPane, pContentPanel)
        CreateMiscOptions(pOptionPane, pContentPanel)
        CreateAdditionalOptions(pOptionPane, pContentPanel)
        
        return App.TGPane_Create(0,0)
    

# Creates GFX option selections
def CreateGFXOptions(pOptionPane, pContentPanel):
        global pGFX, pFlash, pBackdop
        
        pMainMenu = App.STCharacterMenu_Create("Slipstream GFX")
        pContentPanel.AddChild(pMainMenu)

        pGFX = CreateButton("None", pMainMenu, pOptionPane, pContentPanel, __name__ + ".SelectTunnelGFX", EventInt = 0)
        pFlash = CreateButton("None", pMainMenu, pOptionPane, pContentPanel, __name__ + ".SelectFlashGFX", EventInt = 0)
        pBackdop = CreateButton("None", pMainMenu, pOptionPane, pContentPanel, __name__ + ".SelectBackdropGFX", EventInt = 0)
        
        for s in lGFXTunnel:
            if dGFXTunnelTrans[SlipstreamConfiguration.TunnelGFX] == s:
                pGFX.SetName(App.TGString("Tunnel GFX:  " + s))
                break

        for s in lFlash:
            if dFlashTrans[SlipstreamConfiguration.FlashGFX] == s:
                pFlash.SetName(App.TGString("Flash GFX:  " + s))
                break

        for s in lBackdrop:
            if dBackdropTrans[SlipstreamConfiguration.BackdropGFX] == s:
                pBackdop.SetName(App.TGString("Backdrop GFX:  " + s))
                break

        return pMainMenu


# Create misc options
def CreateMiscOptions(pOptionPane, pContentPanel):
        global pButtonLoop, pButtonPrint, pButtonArrivingAt
        
        pMainMenu = App.STCharacterMenu_Create("Misc Options")
        pContentPanel.AddChild(pMainMenu)
        
        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_OPTION)
        pButtonLoop = App.STButton_Create("Engine Loop Sound", pEvent)
        pEvent.SetSource(pButtonLoop)
        pButtonLoop.SetChoosable(1)
        pButtonLoop.SetAutoChoose(1)
        pEvent.SetDestination(pMainMenu)
        pEvent.SetString("Engine Loop Sound")
        pLoop = SlipstreamConfiguration.LoopSound
        pButtonLoop.SetChosen(pLoop, 0)
        pMainMenu.AddChild(pButtonLoop)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_OPTION)
        pButtonPrint = App.STButton_Create("Destination\ETA Prints", pEvent)
        pEvent.SetSource(pButtonPrint)
        pButtonPrint.SetChoosable(1)
        pButtonPrint.SetAutoChoose(1)
        pEvent.SetDestination(pMainMenu)
        pEvent.SetString("Destination\ETA Prints")
        pPrints = SlipstreamConfiguration.Prints
        pButtonPrint.SetChosen(pPrints, 0)
        pMainMenu.AddChild(pButtonPrint)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_OPTION)
        pButtonArrivingAt = App.STButton_Create("Disable Arriving At Text", pEvent)
        pEvent.SetSource(pButtonArrivingAt)
        pButtonArrivingAt.SetChoosable(1)
        pButtonArrivingAt.SetAutoChoose(1)
        pEvent.SetDestination(pMainMenu)
        pEvent.SetString("Disable Arriving At Text")
        pArrivingAt = SlipstreamConfiguration.ArrivingAt
        pButtonArrivingAt.SetChosen(pArrivingAt, 0)
        pMainMenu.AddChild(pButtonArrivingAt)

        pMainMenu.AddPythonFuncHandlerForInstance(ET_OPTION, __name__ + ".SelectOption")

        return pMainMenu


# Create credits\movies menu
def CreateAdditionalOptions(pOptionPane, pContentPanel):
        pMainMenu = App.STCharacterMenu_Create("Credits\Previews")
        pContentPanel.AddChild(pMainMenu)
        
        pButton = CreateButton("Preview GFX", pMainMenu, pOptionPane, pContentPanel, __name__ + ".PreviewAllGFX", EventInt = 0)
        pButton = CreateButton("Slipstream Credits", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ModCredits", EventInt = 0)

        return pMainMenu


# Handle Tunnel GFX Selection
def SelectTunnelGFX(pObject, pEvent):
        global pGFX, pFlash, pBackdop, pButtonLoop, pButtonPrint, pButtonArrivingAt

        pGFX.SetDisabled()
        pFlash.SetDisabled()
        pBackdop.SetDisabled()
        pButtonLoop.SetDisabled()
        pButtonPrint.SetDisabled()
        pButtonArrivingAt.SetDisabled()

        pNextSel = 0
        iCounter = 0
        for s in lGFXTunnel:
            iCounter = iCounter + 1
            if dGFXTunnelTrans[SlipstreamConfiguration.TunnelGFX] == s:
                pNextSel = 1
            elif pNextSel == 1:
                pNextSel = 0
                pGFX.SetName(App.TGString("Tunnel GFX:  " + s))
                SaveConfiguration(s)
                break
            if iCounter >= 8:
                pGFX.SetName(App.TGString("Tunnel GFX:  " + "Default"))
                SaveConfiguration("Default")
                break

        pObject.CallNextHandler(pEvent)
        

# Handle Flash GFX Selection
def SelectFlashGFX(pObject, pEvent):
        global pGFX, pFlash, pBackdop, pButtonLoop, pButtonPrint, pButtonArrivingAt

        pGFX.SetDisabled()
        pFlash.SetDisabled()
        pBackdop.SetDisabled()
        pButtonLoop.SetDisabled()
        pButtonPrint.SetDisabled()
        pButtonArrivingAt.SetDisabled()

        pNextSel = 0
        iCounter = 0
        for s in lFlash:
            iCounter = iCounter + 1
            if dFlashTrans[SlipstreamConfiguration.FlashGFX] == s:
                pNextSel = 1
            elif pNextSel == 1:
                pNextSel = 0
                pFlash.SetName(App.TGString("Flash GFX:  " + s))
                SaveConfiguration(None, s)
                break
            if iCounter >= 2:
                pFlash.SetName(App.TGString("Flash GFX:  " + "Default"))
                SaveConfiguration(None, "Default")
                break

        pObject.CallNextHandler(pEvent)
        

# Handle Backdrop GFX Selection
def SelectBackdropGFX(pObject, pEvent):
        global pGFX, pFlash, pBackdop, pButtonLoop, pButtonPrint, pButtonArrivingAt

        pGFX.SetDisabled()
        pFlash.SetDisabled()
        pBackdop.SetDisabled()
        pButtonLoop.SetDisabled()
        pButtonPrint.SetDisabled()
        pButtonArrivingAt.SetDisabled()

        pNextSel = 0
        iCounter = 0
        for s in lBackdrop:
            iCounter = iCounter + 1
            if dBackdropTrans[SlipstreamConfiguration.BackdropGFX] == s:
                pNextSel = 1
            elif pNextSel == 1:
                pNextSel = 0
                pBackdop.SetName(App.TGString("Backdrop GFX:  " + s))
                SaveConfiguration(None, None, s)
                break
            if iCounter >= 3:
                pBackdop.SetName(App.TGString("Backdrop GFX:  " + "Default"))
                SaveConfiguration(None, None, "Default")
                break
                
        pObject.CallNextHandler(pEvent)


# Handle option selection
def SelectOption(pObject, pEvent):
        global pGFX, pFlash, pBackdop, pButtonLoop, pButtonPrint, pButtonArrivingAt

        pGFX.SetDisabled()
        pFlash.SetDisabled()
        pBackdop.SetDisabled()
        pButtonLoop.SetDisabled()
        pButtonPrint.SetDisabled()
        pButtonArrivingAt.SetDisabled()
        
        SaveConfiguration()
        pObject.CallNextHandler(pEvent)


# Play the movie
def PreviewAllGFX(pObject, pEvent):
    
        from Custom.Slipstream.Libs import PreviewVid

        PreviewVid.PlayMovieSeq(None, None)


# Play credits sequence
def ModCredits(pObject, pEvent):
        from Custom.Slipstream.Libs import Credits

        Credits.PlaySeq(None, None)

    
# Saves configuration
def SaveConfiguration(strGFX = None, strFlash = None, strBackdrop = None):
        global pButtonLoop, pButtonPrint, pButtonArrivingAt
        
        if not strGFX == None:
            sGFX = dGFXTunnel[strGFX]
        else:
            sGFX = SlipstreamConfiguration.TunnelGFX
        if not strFlash == None:
            sFlash = dFlash[strFlash]
        else:
            sFlash = SlipstreamConfiguration.FlashGFX
        if not strBackdrop == None:
            sBackdrop = dBackdrop[strBackdrop]
        else:
            sBackdrop = SlipstreamConfiguration.BackdropGFX

        sLoop = pButtonLoop.IsChosen()
        sPrint = pButtonPrint.IsChosen()
        sArriving = pButtonArrivingAt.IsChosen()
            
        file = nt.open(sPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "TunnelGFX = " + "'" + sGFX + "'" +
                 "\nFlashGFX = " + "'" + sFlash + "'"+
                 "\nBackdropGFX = " + "'" + sBackdrop + "'" +
                 "\nLoopSound = " + str(sLoop) +
                 "\nPrints = " + str(sPrint) +
                 "\nArrivingAt = " + str(sArriving))
        nt.close(file)

        reload(SlipstreamConfiguration)

        KillTimerInstance()
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.AddPythonFuncHandlerForInstance(ET_TIMER_EVENT, __name__ + ".ResetButtons")

	# Create the timer.
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(ET_TIMER_EVENT)
	pEvent.SetDestination(pOptionsWindow)

	pTimer = App.TGTimer_Create()
	pTimer.SetEvent(pEvent)
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetRealTime () + 0.8)
	pTimer.SetDelay(0.0)
	pTimer.SetDuration (0.0)

	global idTimer
	idTimer = pTimer.GetObjID()

	App.g_kRealtimeTimerManager.AddTimer(pTimer)


# Kill timer
def KillTimerInstance():
        global idTimer
	App.g_kRealtimeTimerManager.DeleteTimer(idTimer)
	idTimer = App.NULL_ID        


# Resets buttons
def ResetButtons(pObject, pEvent):
        global pGFX, pFlash, pBackdop, pButtonLoop, pButtonPrint, pButtonArrivingAt
        
        pGFX.SetEnabled()
        pFlash.SetEnabled()
        pBackdop.SetEnabled()
        pButtonLoop.SetEnabled()
        pButtonPrint.SetEnabled()
        pButtonArrivingAt.SetEnabled()

        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
    
        pOptionsWindow.RemoveHandlerForInstance(ET_TIMER_EVENT, __name__ + ".ResetButtons")
        
        pObject.CallNextHandler(pEvent)

        return 0


# Creates a button
def CreateButton(sButtonName, pMenu, pOptionPane, pContentPanel, sFunction, EventInt = 0):        
        ET_EVENT = App.UtopiaModule_GetNextEventType()

        pOptionPane.AddPythonFuncHandlerForInstance(ET_EVENT, sFunction)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_EVENT)
        pEvent.SetDestination(pOptionPane)
        pEvent.SetString(sButtonName)

        pButton = App.STButton_Create(sButtonName, pEvent)
        pButton.SetChosen(0)

        pEvent.SetSource(pButton)            
        pMenu.AddChild(pButton)

        return pButton
