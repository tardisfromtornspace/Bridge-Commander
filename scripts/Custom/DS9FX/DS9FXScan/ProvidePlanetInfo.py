# by Sov

import App
import MissionLib

ET_CLOSE = App.UtopiaModule_GetNextEventType()

dPlanets={"Bajor 1":"Bajor1", "Bajor 2":"Bajor2", "Bajoran Homeworld":"Bajor3", "Bajor 4":"Bajor4", "Bajor 5":"Bajor5",
          "Bajor 6":"Bajor6", "Bajor 7":"Bajor7", "Bajor 8":"Bajor8", "Bajor 9":"Bajor9", "Bajor 10":"Bajor10", "Bajor 11":"Bajor11",
          "Bajor 12":"Bajor12", "Bajor 13":"Bajor13", "Bajor 14":"Bajor14", "Dosi 1":"Dosi1", "Dosi 2":"Dosi2", "Dosi Homeworld":"Dosi3",
          "Founders Homeworld":"Founders1", "Gaia I":"Gaia1", "Gaia II":"Gaia2", "Gaia III":"Gaia3", "Gaia IV":"Gaia4",
          "Karemma 1":"Karemma1", "Karemman Homeworld":"Karemma2", "Kurill Prime":"Kurill1", "Kurill 2":"Kurill2", "New Bajor 1":" NewBajor1",
          "New Bajor Colony":"NewBajor2", "New Bajor 3":"NewBajor3", "New Bajor 4":"NewBajor4", "Meridian":"Trialus1", "T-Rogoran 1":"TRogoran1",
          "T-Rogoran 2":"TRogoran2", "T-Rogoran Homeworld":"TRogoran3", "Vandros I":"Vandros1", "Vandros II":"Vandros2", "Vandros III":"Vandros3",
          "Vandros IV":"Vandros4", "Yadera 1":"Yadera1", "Yadera 2":"Yadera2", "Yadera 3":"Yadera3", "Yadera Prime":"Yadera4", "Yadera 5":"Yadera5",
          "Qo'nos 1":"Qonos1", "Qo'nos 2":"Qonos2", "Qo'nos":"Qonos3", "Qo'nos 4":"Qonos4", "Qo'nos 5":"Qonos5", "Qo'nos 6":"Qonos6",
          "Chin'toka 1":"Chintoka1", "Chin'toka 2":"Chintoka2", "Chin'toka 3":"Chintoka3", "Chin'toka 4":"Chintoka4", 
          "AR 558":"Chintoka5", "Idran":"Idran1", "Cardassia 1":"Cardassia1", "Cardassia 2":"Cardassia2", "Cardassia 3":"Cardassia3", 
          "Cardassia 4":"Cardassia4", "Cardassia 5":"Cardassia5", "Cardassia Prime":"Cardassia6", "Cardassia 7":"Cardassia7", 
          "Cardassia 8":"Cardassia8", "Trivas 1":"Trivas1", "Trivas 2":"Trivas2", "Trivas 3":"Trivas3", "Trivas 4":"Trivas4"}

pPane = None
pMainPane = None
sDesc = "No information available on this object."
bTgl = 0

def Scan():
    global sDesc, pPane, bTgl

    if not pPane == None:
        KillGUI(None, None)
        return 0

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    
    pTarget = pPlayer.GetTarget()
    if not pTarget:
        return 0

    pName = pTarget.GetName()
    if not pName:
        return 0

    # Just check if we can cast this object as a planet
    pPlanet = App.Planet_Cast(pTarget)
    if not pPlanet:
        return 0

    if dPlanets.has_key(pName):
        pTglID = dPlanets[pName]
    else:
        pTglID = "None"

    pDatabase = App.g_kLocalizationManager.Load("data/TGL/DS9FXPlanetaryData.tgl")
    if pDatabase.HasString(pTglID):
        sDesc = pDatabase.GetString(pTglID)
        bTgl = 1
    else:
        sDesc = "No information available on this object."
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
