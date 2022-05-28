# by Sov

import App
import MissionLib

ET_CLOSE = App.UtopiaModule_GetNextEventType()

dRegions = {"DeepSpace91":"Bajor", "BajoranWormhole1":"Wormhole", "GammaQuadrant1":"Idran", "DS9FXBadlands1":"Badlands",
            "DS9FXKaremma1":"Karemma", "DS9FXDosi1":"Dosi", "DS9FXYadera1":"Yadera", "DS9FXNewBajor1":"NewBajor",
            "DS9FXGaia1":"Gaia", "DS9FXKurill1":"Kurill", "DS9FXTrialus1":"Trialus", "DS9FXTRogoran1":"TRogoran",
            "DS9FXVandros1":"Vandros", "DS9FXFoundersHomeworld1":"Founders", "DS9FXQonos1":"Qonos", 
            "DS9FXChintoka1":"Chintoka", "DS9FXVela1":"Vela", "DS9FXCardassia1":"Cardassia", "DS9FXTrivas1":"Trivas"}

pPane = None
pMainPane = None
sDesc = "No information available on this system."
bTgl = 0

def Scan():
    global sDesc, pPane, bTgl

    if not pPane == None:
        KillGUI(None, None)
        return 0

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return 0

    pName = pSet.GetName()
    if not pName:
        return 0

    if dRegions.has_key(pName):
        pTglID = dRegions[pName]
    else:
        pTglID = "None"

    pDatabase = App.g_kLocalizationManager.Load("data/TGL/DS9FXRegionData.tgl")
    if pDatabase.HasString(pTglID):
        sDesc = pDatabase.GetString(pTglID)
        bTgl = 1
    else:
        sDesc = "No information available on this system."
        bTgl = 0

    App.g_kLocalizationManager.Unload(pDatabase)
    App.g_kUtopiaModule.Pause(1)

    ShowDescription(sDesc, bTgl)    

def ShowDescription(sText, bTGL):
    global pMainPane, pPane

    pPane = App.TGPane_Create(1.0, 1.0) 
    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
    pTCW.AddChild(pPane, 0, 0) 
    pMainPane = App.TGPane_Create(0.4, 0.4) 
    pPane.AddChild(pMainPane, 0.35, 0.15)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")

    ShowWindow(pMainPane, pPane, sText, bTGL)

def ShowWindow(pMainPane, pPane, sText, bTGL):
    kColor = App.TGColorA() 
    kColor.SetRGBA(1, 0.81, 0.41, 1.0)

    pScanWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Scan Output:"), 0.0, 0.0, None, 1, 0.40, 0.29, kColor)
    pMainPane.AddChild(pScanWindow, 0, 0)

    pButtonsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Complete Scan:"), 0.0, 0.0, None, 1, 0.40, 0.10, kColor)
    pMainPane.AddChild(pButtonsWindow , 0, 0.30)

    pScanText = App.TGParagraph_CreateW(App.TGString(str(sText)), pScanWindow.GetMaximumInteriorWidth(), None, '', pScanWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pScanWindow.AddChild(pScanText, 0, 0.01)

    if bTGL:
        pScanText.SetStringW(sText)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_CLOSE)
    pEvent.SetString("DS9FXScanClose")
    pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.30, 0.034583)
    kNormalColor = App.TGColorA() 
    kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
    kHilightedColor = App.TGColorA() 
    kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
    kDisabledColor = App.TGColorA() 
    kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pButtonsWindow.AddChild(pButton, 0.05, 0.02)

    pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode() 
    pLCARS = pGraphicsMode.GetLcarsString() 
    pGlass = App.TGIcon_Create(pLCARS, 120) 
    pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight()) 
    pMainPane.AddChild(pGlass, 0, 0)

    pScanWindow.InteriorChangedSize()
    pScanWindow.Layout()
    pButtonsWindow.InteriorChangedSize()
    pButtonsWindow.Layout()
    pMainPane.Layout()
    pPane.Layout()

    pPane.SetVisible()

def KillGUI(pObject, pEvent):
    global pMainPane, pPane

    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")
    except:
        pass

    if not pPane is None:
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        try:
            App.g_kFocusManager.RemoveAllObjectsUnder(pPane)
            pTCW.DeleteChild(pPane)
            pPane = None   
            pMainPane = None
        except:
            pass

    App.g_kUtopiaModule.Pause(0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def Quitting():
    global pMainPane, pPane
    
    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")
    except:
        pass

    if not pPane is None:
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        try:
            App.g_kFocusManager.RemoveAllObjectsUnder(pPane)
            pTCW.DeleteChild(pPane)
            pPane = None   
            pMainPane = None
        except:
            pass
