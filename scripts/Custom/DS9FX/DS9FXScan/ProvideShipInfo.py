# by USS Sovereign

# It shows ship descriptions when you scan a ship & ships current crew count

# Imports
import App
import Foundation
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict, AIBoarding, CaptureShip

# Events
ET_CLOSE = App.UtopiaModule_GetNextEventType()

# Vars
pPane = None
pMainPane = None
bTGLDesc = 0

# Functions
def ScanObject():
    global bTGLDesc, pPane
    
    sDesc = "No information available"
    iCurrCrew = 0
    iAttackers = 0
    iDefenders = 0
    iMaxCrew = 0
    iMaxAllowedCrew = 0
    sCanTransportCrew = "N/A"
    sCanBeBoarded = "N/A"
    sCanBeRecovered = "N/A"
    bTGLDesc = 0 

    if not pPane == None:
        KillGUI(None, None)
        return 0

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    
    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    if not pTarget:
        return 0

    pShip = DS9FXLifeSupportLib.GetShipType(pTarget)
    if not pShip:
        return 0

    if Foundation.shipList.has_key(pShip):
        fShip = Foundation.shipList[pShip]
        if fShip:
            pDatabase = App.g_kLocalizationManager.Load("data/TGL/Ships.tgl")
            if pDatabase.HasString(fShip.abbrev + " Description") and hasattr(fShip, "hasTGLDesc"):
                if fShip.hasTGLDesc == 1:
                    sDesc = pDatabase.GetString(fShip.abbrev + " Description")
                    bTGLDesc = 1
                else:
                    sDesc = fShip.desc
                    bTGLDesc = 0
            else:
                sDesc = fShip.desc
                bTGLDesc = 0
            if hasattr(fShip, "fCrew"):
                if fShip.fCrew == "Off":
                    bNoCrew = 1
                    iMaxCrew = "N/A"
                else:
                    bNoCrew = 0
                    iMaxCrew = fShip.fCrew
            else:
                iMaxCrew = DS9FXLifeSupportLib.CalculateMaxCrew(pTarget)
                bNoCrew = 0
            if bNoCrew:
                iCurrCrew = "N/A"
                iMaxAllowedCrew = "N/A"
                iAttackers = "N/A"
                iDefenders = "N/A"                
            else:
                pShipID = pTarget.GetObjID()
                if LifeSupport_dict.dCrew.has_key(pShipID):
                    iCurrCrew = LifeSupport_dict.dCrew[pShipID]
                else:
                    iCurrCrew = "Unknown"
                if CaptureShip.captureships.has_key(pShipID):
                    lInfo = CaptureShip.captureships[pShipID]
                    iDefenders = lInfo[1]
                    iAttackers = lInfo[0]
                if AIBoarding.dCombat.has_key(pShipID):
                    dData = AIBoarding.dCombat[pShipID]
                    iDefenders = iDefenders + dData["Defender"]
                    iAttackers = iAttackers + dData["Attacker"]
                if iDefenders <= 0:
                    iDefenders = iCurrCrew
                if iAttackers <= 0:
                    iAttackers = 0
                iMaxAllowedCrew = int(iMaxCrew * 1.5)
            if IsNumeric(iMaxAllowedCrew) and IsNumeric(iCurrCrew):
                if iCurrCrew >= iMaxAllowedCrew:
                    sCanTransportCrew = "No"
                else:
                    pFriendly = MissionLib.GetFriendlyGroup()
                    if pFriendly:
                        if pFriendly.IsNameInGroup(pTarget.GetName()):
                            sCanTransportCrew = "Yes"
                        else:
                            sCanTransportCrew = "No"
                    else:
                        sCanTransportCrew = "No"
            if CaptureShip.ShieldCheck(pTarget.GetObjID()) and not bNoCrew:
                sCanBeBoarded = "Yes"
            else:
                if not bNoCrew:
                    sCanBeBoarded = "No"
            if IsNumeric(iCurrCrew):
                if iCurrCrew <= 0:
                    lSides = [MissionLib.GetFriendlyGroup(), MissionLib.GetEnemyGroup(), MissionLib.GetNeutralGroup()]
                    bCanRecover = 1
                    for pSide in lSides:
                        if pSide:
                            if pSide.IsNameInGroup(pTarget.GetName()):
                                bCanRecover = 0
                                break
                    if bCanRecover:
                        sCanBeRecovered = "Yes"
                    else:
                        sCanBeRecovered = "No"
                else:
                    sCanBeRecovered = "No"          
            App.g_kLocalizationManager.Unload(pDatabase)
            App.g_kUtopiaModule.Pause(1)
            ShowDescription(sDesc, iMaxCrew, iCurrCrew, iMaxAllowedCrew, iAttackers, iDefenders, sCanTransportCrew, sCanBeBoarded, sCanBeRecovered)
        else:
            return 0     
    else:
        return 0
    
def IsNumeric(sVal):
    try:
        f = float(sVal)
    except:
        f = None
    if f != None:
        return 1
    return 0

def ShowDescription(sText, iMaxCrew, iCurrCrew, iMaxAllowedCrew, iAttackers, iDefenders, sCanTransportCrew, sCanBeBoarded, sCanBeRecovered):
    global pMainPane, pPane

    pPane = App.TGPane_Create(1.0, 1.0) 
    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
    pTCW.AddChild(pPane, 0, 0) 
    pMainPane = App.TGPane_Create(0.4, 0.55) 
    pPane.AddChild(pMainPane, 0.35, 0.15)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")

    ShowWindow(pMainPane, pPane, sText, iMaxCrew, iCurrCrew, iMaxAllowedCrew, iAttackers, iDefenders, sCanTransportCrew, sCanBeBoarded, sCanBeRecovered)

def ShowWindow(pMainPane, pPane, sText, iMaxCrew, iCurrCrew, iMaxAllowedCrew, iAttackers, iDefenders, sCanTransportCrew, sCanBeBoarded, sCanBeRecovered):
    global bTGLDesc

    kColor = App.TGColorA() 
    kColor.SetRGBA(1, 0.81, 0.41, 1.0)
    
    pScanWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Scan Output:"), 0.0, 0.0, None, 1, 0.40, 0.29, kColor)
    pMainPane.AddChild(pScanWindow, 0, 0)

    pCrewWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Life Support:"), 0.0, 0.0, None, 1, 0.40, 0.14, kColor)
    pMainPane.AddChild(pCrewWindow, 0, 0.30)    

    pButtonsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Complete Scan:"), 0.0, 0.0, None, 1, 0.40, 0.10, kColor)
    pMainPane.AddChild(pButtonsWindow , 0, 0.45)

    pScanText = App.TGParagraph_CreateW(App.TGString(str(sText)), pScanWindow.GetMaximumInteriorWidth(), None, '', pScanWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pScanWindow.AddChild(pScanText, 0, 0.01)

    sShipInfo = "Max Allowed Ship Crew Complement: " + str(iMaxAllowedCrew) + "\n" + "Standard Ship Crew Complement: " + str(iMaxCrew) + "\n" + "Current Ship Crew Complement: " + str(iCurrCrew) + "\nDefenders: " + str(iDefenders) + "\nAttackers: " + str(iAttackers) + "\nCan Receive More Crew: " + str(sCanTransportCrew) + "\nCan Be Boarded: " + str(sCanBeBoarded) + "\nCan Be Recovered: " + str(sCanBeRecovered)
    pCrewText = App.TGParagraph_CreateW(App.TGString(str(sShipInfo)), pCrewWindow.GetMaximumInteriorWidth(), None, '', pCrewWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pCrewWindow.AddChild(pCrewText, 0, 0.01)    

    if bTGLDesc:
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
    pCrewWindow.InteriorChangedSize()
    pCrewWindow.Layout()
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
