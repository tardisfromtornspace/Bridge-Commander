# Enhanced version of Transport Crews based on SMBW's idea

# by SMBW & Sov

# Imports
import App
import MissionLib
from Custom.DS9FX.DS9FXAILib import DS9FXGenericStaticFriendlyFollowAI, DS9FXGenericStaticStarbaseFriendlyAI
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents

# Events
ET_CLOSE = App.UtopiaModule_GetNextEventType()
ET_TRANSFER_TO_PLAYER = App.UtopiaModule_GetNextEventType()
ET_TRANSFER_FROM_PLAYER = App.UtopiaModule_GetNextEventType()
ET_UPDATE = App.UtopiaModule_GetNextEventType()
ET_TRANSFER_PLAYER = App.UtopiaModule_GetNextEventType()

# Vars
pPane = None
pMainPane = None
pSlider = None
pPlayerText = None
pTargetText = None
pTransferButton = None
sPlayerText = "N/A"
sTargetText = "N/A"
fPlayerMaxAllowed = 0
fPlayerMaxCrew = 0
fPlayerCurrCrew = 0
fTargetMaxAllowed = 0
fTargetMaxCrew = 0
fTargetCurrCrew = 0
fPercentage = 0
bTransferPlayer = 0

# Functions
def CreateGUI():
    global pPane, fPlayerMaxAllowed, fPlayerMaxCrew, fPlayerCurrCrew, fTargetMaxAllowed, fTargetMaxCrew, fTargetCurrCrew, fPercentage

    if not pPane == None:
        KillGUI(None, None)
        return 0

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    if not pTarget:
        return 0
    
    if pPlayer.IsCloaked() or pTarget.IsCloaked():
        return 0

    if not Distance(pTarget) < 300:
        return 0

    pFriendly = MissionLib.GetFriendlyGroup()
    if not pFriendly:
        return 0

    if not pFriendly.IsNameInGroup(pTarget.GetName()):
        return 0

    pPlayerID = pPlayer.GetObjID()
    if not pPlayerID:
        return 0

    pTargetID = pTarget.GetObjID()
    if not pTargetID:
        return 0

    if not LifeSupport_dict.dCrew.has_key(pPlayerID) or not LifeSupport_dict.dCrew.has_key(pTargetID):
        return 0

    pPlayerInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pPlayer, pPlayerID)
    if not pPlayerInfo:
        return 0

    fPlayerMaxCrew = pPlayerInfo["fMax"]
    fPlayerCurrCrew = pPlayerInfo["fMin"]
    fPlayerMaxAllowed = int(fPlayerMaxCrew * 1.5)

    pTargetInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pTarget, pTargetID)
    if not pTargetInfo:
        return 0

    fTargetMaxCrew = pTargetInfo["fMax"]
    fTargetCurrCrew = pTargetInfo["fMin"]
    fTargetMaxAllowed = int(fTargetMaxCrew * 1.5)

    fPercentage = 0
    
    App.g_kUtopiaModule.Pause(1)
    
    ShowGUI(fPlayerMaxCrew, fPlayerCurrCrew, fTargetMaxCrew, fTargetCurrCrew, fPlayerMaxAllowed, fTargetMaxAllowed)

def ShowGUI(fPlayerMaxCrew, fPlayerCurrCrew, fTargetMaxCrew, fTargetCurrCrew, fPlayerMaxAllowed, fTargetMaxAllowed):
    global pPane, pMainPane
    
    pPane = App.TGPane_Create(1.0, 1.0) 
    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
    pTCW.AddChild(pPane, 0, 0) 
    pMainPane = App.TGPane_Create(0.5, 0.56) 
    pPane.AddChild(pMainPane, 0.35, 0.15)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_TRANSFER_TO_PLAYER, pMission, __name__ + ".TransferToPlayer")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_TRANSFER_PLAYER, pMission, __name__ + ".TransferPlayer")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_TRANSFER_FROM_PLAYER, pMission, __name__ + ".TransferFromPlayer")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_UPDATE, pMission, __name__ + ".UpdateSlider")

    ShowWindow(pPane, pMainPane, fPlayerMaxCrew, fPlayerCurrCrew, fTargetMaxCrew, fTargetCurrCrew, fPlayerMaxAllowed, fTargetMaxAllowed)

def ShowWindow(pPane, pMainPane, fPlayerMaxCrew, fPlayerCurrCrew, fTargetMaxCrew, fTargetCurrCrew, fPlayerMaxAllowed, fTargetMaxAllowed):
    global pSlider, pTransferButton, fPercentage, sPlayerText, pPlayerText, sTargetText, pTargetText
    
    kColor = App.TGColorA() 
    kColor.SetRGBA(1, 0.81, 0.41, 1.0)

    pSliderWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Crew To Transfer:"), 0.0, 0.0, None, 1, 0.5, 0.12, kColor)
    pMainPane.AddChild(pSliderWindow, 0, 0)

    pPlayerInfoWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Player Details:"), 0.0, 0.0, None, 1, 0.24, 0.12, kColor)
    pMainPane.AddChild(pPlayerInfoWindow, 0, 0.13) 

    pTargetInfoWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Target Details:"), 0.0, 0.0, None, 1, 0.24, 0.12, kColor)
    pMainPane.AddChild(pTargetInfoWindow, 0.25, 0.13) 
    
    pPlayerTransferWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Transfer From Player:"), 0.0, 0.0, None, 1, 0.24, 0.18, kColor)
    pMainPane.AddChild(pPlayerTransferWindow, 0, 0.26)

    pTargetTransferWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Transfer To Player:"), 0.0, 0.0, None, 1, 0.24, 0.18, kColor)
    pMainPane.AddChild(pTargetTransferWindow, 0.25, 0.26)

    pCloseWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Close:"), 0.0, 0.0, None, 1, 0.5, 0.11, kColor)
    pMainPane.AddChild(pCloseWindow, 0, 0.45)

    pSlider = DS9FXMenuLib.CreateSliderbar(App.TGString("Crew Selection"), ET_UPDATE, float(fPercentage), 0.0, 1.0, 0.01, 1.0, 0.44, 0.06)
    pSliderWindow.AddChild(pSlider, 0.03, 0.02)

    sPlayerText = "Max Allowed Crew: " + str(fPlayerMaxAllowed) + "\n" + "Standard Crew: " + str(fPlayerMaxCrew) + "\n" + "Current Crew: " + str(fPlayerCurrCrew) + "\n" + "Crew To Transfer: " + "0"
    pPlayerText = App.TGParagraph_CreateW(App.TGString(str(sPlayerText)), pPlayerInfoWindow.GetMaximumInteriorWidth(), None, '', pPlayerInfoWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pPlayerInfoWindow.AddChild(pPlayerText, 0, 0.01)

    sTargetText = "Max Allowed Crew: " + str(fTargetMaxAllowed) + "\n" + "Standard Crew: " + str(fTargetMaxCrew) + "\n" + "Current Crew: " + str(fTargetCurrCrew) + "\n" + "Crew To Transfer: " + "0"
    pTargetText = App.TGParagraph_CreateW(App.TGString(str(sTargetText)), pTargetInfoWindow.GetMaximumInteriorWidth(), None, '', pTargetInfoWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pTargetInfoWindow.AddChild(pTargetText, 0, 0.01)

    kNormalColor = App.TGColorA() 
    kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
    kHilightedColor = App.TGColorA() 
    kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
    kDisabledColor = App.TGColorA() 
    kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)
    
    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_TRANSFER_FROM_PLAYER)
    pEvent.SetString("DS9FXTransferFromPlayer")
    pButton = App.STRoundedButton_CreateW(App.TGString("Transfer From Player"), pEvent, 0.20, 0.034583)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pPlayerTransferWindow.AddChild(pButton, 0.02, 0.03)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_TRANSFER_PLAYER)
    pEvent.SetString("DS9FXTransferPlayer")
    pTransferButton = App.STRoundedButton_CreateW(App.TGString("Transfer Player : No"), pEvent, 0.20, 0.034583)
    pTransferButton.SetNormalColor(kNormalColor)
    pTransferButton.SetHighlightedColor(kHilightedColor)
    pTransferButton.SetSelectedColor(kNormalColor)
    pTransferButton.SetDisabledColor(kDisabledColor)
    pTransferButton.SetColorBasedOnFlags()
    pPlayerTransferWindow.AddChild(pTransferButton, 0.02, 0.09)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_TRANSFER_TO_PLAYER)
    pEvent.SetString("DS9FXTransferToPlayer")
    pButton = App.STRoundedButton_CreateW(App.TGString("Transfer To Player"), pEvent, 0.20, 0.034583)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pTargetTransferWindow.AddChild(pButton, 0.02, 0.06)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_CLOSE)
    pEvent.SetString("DS9FXTransferClose")
    pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.44, 0.034583)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pCloseWindow.AddChild(pButton, 0.03, 0.03)

    pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode() 
    pLCARS = pGraphicsMode.GetLcarsString() 
    pGlass = App.TGIcon_Create(pLCARS, 120) 
    pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight()) 
    pMainPane.AddChild(pGlass, 0, 0)

    pSliderWindow.InteriorChangedSize()
    pSliderWindow.Layout()
    pPlayerInfoWindow.InteriorChangedSize()
    pPlayerInfoWindow.Layout()
    pTargetInfoWindow.InteriorChangedSize()
    pTargetInfoWindow.Layout()
    pPlayerTransferWindow.InteriorChangedSize()
    pPlayerTransferWindow.Layout()
    pTargetTransferWindow.InteriorChangedSize()
    pTargetTransferWindow.Layout()
    pCloseWindow.InteriorChangedSize()
    pCloseWindow.Layout()
    pMainPane.Layout()
    pPane.Layout()

    pPane.SetVisible()

def TransferToPlayer(pObject, pEvent):
    global fPercentage, fTargetCurrCrew, fPlayerCurrCrew, fPlayerMaxAllowed
    if fPercentage <= 0:
        if pObject and pEvent:
            pObject.pCallNextHandler(pEvent)
        return 0

    HideGUI()

    pPlayer = MissionLib.GetPlayer()
    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    pPlayerID = pPlayer.GetObjID()
    pTargetID = pTarget.GetObjID()

    fToTransfer = float(fTargetCurrCrew) * float(fPercentage)
    iToTransfer = int(fToTransfer)

    if iToTransfer >= fTargetCurrCrew:
        iToTransfer = fTargetCurrCrew

    iPlayerFutureComplement = fPlayerCurrCrew + iToTransfer
    if iPlayerFutureComplement > fPlayerMaxAllowed:
        iPlayerExtraCrew = iPlayerFutureComplement - fPlayerMaxAllowed
        iToTransfer = iToTransfer - iPlayerExtraCrew

    PlayTransportSound()

    if pPlayer.GetShields().IsOn() == 1:
        pSequence = App.TGSequence_Create()
        g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
        pSequence.AppendAction(App.CharacterAction_Create(App.CharacterClass_GetObject(App.g_kSetManager.GetSet('bridge'), 'Engineer'), App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, 4))
        pSequence.Play()

    iPlayerCurrStats = LifeSupport_dict.dCrew[pPlayerID]
    iTargetCurrStats = LifeSupport_dict.dCrew[pTargetID]

    iPlayerCurrStats = iPlayerCurrStats + iToTransfer
    iTargetCurrStats = iTargetCurrStats - iToTransfer

    LifeSupport_dict.dCrew[pPlayerID] = iPlayerCurrStats

    if iTargetCurrStats <= 0:
        iTargetCurrStats = 0
        pTarget.ClearAI()
        DS9FXLifeSupportLib.GroupCheck(pTarget)
        DS9FXLifeSupportLib.PlayerCheck(pTargetID)
        DS9FXGlobalEvents.Trigger_Ship_Dead_In_Space(pTarget)

    LifeSupport_dict.dCrew[pTargetID] = iTargetCurrStats

    DS9FXGlobalEvents.Trigger_Ship_Recrewed(pTarget, pPlayer)
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pPlayer)
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pTarget)

    CloseGUI()

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def TransferFromPlayer(pObject, pEvent):
    global fPercentage, fPlayerCurrCrew, fTargetCurrCrew, fTargetMaxAllowed, bTransferPlayer
    if fPercentage <= 0:
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return 0

    HideGUI()

    pPlayer = MissionLib.GetPlayer()
    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    pPlayerID = pPlayer.GetObjID()
    pTargetID = pTarget.GetObjID()

    fToTransfer = float(fPlayerCurrCrew) * float(fPercentage)
    iToTransfer = int(fToTransfer)

    if iToTransfer >= fPlayerCurrCrew:
        iToTransfer = fPlayerCurrCrew

    iTargetFutureComplement = fTargetCurrCrew + iToTransfer
    if iTargetFutureComplement > fTargetMaxAllowed:
        iTargetExtraCrew = iTargetFutureComplement - fTargetMaxAllowed
        iToTransfer = iToTransfer - iTargetExtraCrew

    PlayTransportSound()

    if pPlayer.GetShields().IsOn() == 1:
        pSequence = App.TGSequence_Create()
        g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
        pSequence.AppendAction(App.CharacterAction_Create(App.CharacterClass_GetObject(App.g_kSetManager.GetSet('bridge'), 'Engineer'), App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, 4))
        pSequence.Play()

    iPlayerCurrStats = LifeSupport_dict.dCrew[pPlayerID]
    iTargetCurrStats = LifeSupport_dict.dCrew[pTargetID]

    iPlayerCurrStats = iPlayerCurrStats - iToTransfer
    iTargetCurrStats = iTargetCurrStats + iToTransfer

    LifeSupport_dict.dCrew[pTargetID] = iTargetCurrStats

    bFireEvent = 0

    if iPlayerCurrStats <= 0:
        bFireEvent = 1
        bTransferPlayer = 0
        iPlayerCurrStats = 0
        pPlayer.ClearAI()
        GoToNewShip(pTarget)
        DS9FXLifeSupportLib.GroupCheck(pPlayer)
        DS9FXLifeSupportLib.PlayerCheck(pPlayerID)

    if bTransferPlayer == 1:
        bFireEvent = 1
        pPlayer.ClearAI()
        GoToNewShip(pTarget)
        if (pPlayer.GetShipProperty().IsStationary() == 1):
            pPlayer.SetAI(DS9FXGenericStaticStarbaseFriendlyAI.CreateAI(pPlayer))
        else:
            pPlayer.SetAI(DS9FXGenericStaticFriendlyFollowAI.CreateAI(pPlayer))

    LifeSupport_dict.dCrew[pPlayerID] = iPlayerCurrStats

    DS9FXGlobalEvents.Trigger_Ship_Recrewed(pPlayer, pTarget)
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pPlayer)
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pTarget)

    if bFireEvent == 1:
        DS9FXGlobalEvents.Trigger_Ship_Dead_In_Space(pPlayer)

    CloseGUI()
    
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def TransferPlayer(pObject, pEvent):
    global bTransferPlayer, pTransferButton

    if bTransferPlayer == 0:
        bTransferPlayer = 1
        pTransferButton.SetName(App.TGString("Transfer Player : Yes"))
    else:
        bTransferPlayer = 0
        pTransferButton.SetName(App.TGString("Transfer Player : No"))
    
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)    

def HideGUI():
    global pPane
    pPane.SetNotVisible()
    App.g_kUtopiaModule.Pause(0)

def PlayTransportSound():
    App.g_kSoundManager.PlaySound("DS9FXTransportSound")

def GoToNewShip(pShip):
    if pShip:
            pSequence = App.TGSequence_Create()
            pSequence.AppendAction(App.TGScriptAction_Create(__name__, "SwapShips", pShip))
            pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pShip.GetContainingSet().GetName()))
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pShip.GetContainingSet().GetName(), pShip.GetName()))
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pShip.GetContainingSet().GetName ()), 4)
            if App.g_kSetManager.GetSet("bridge"):
                pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                pSequence.AppendAction(pAction)
            pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
            pSequence.Play()
    else:
        return 0

def SwapShips(pAction, pShip):
    if pShip:
        pPlayer = MissionLib.GetPlayer()
        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(pShip)
        pPlayer.ClearAI()
        pNewPlayer = MissionLib.GetPlayer()
        pNewPlayer.ClearAI()
        pNewPlayer.SetTarget(None)
    return 0

def CloseGUI():
    Quitting()
    
def UpdateSlider(pObject, pEvent):
    global pSlider, fPercentage, fPlayerMaxCrew, fPlayerCurrCrew, fTargetMaxCrew, fTargetCurrCrew, sPlayerText, pPlayerText, sTargetText, pTargetText, fPlayerMaxAllowed, fTargetMaxAllowed
    
    if hasattr(pEvent, "GetFloat"):
        fPercentage = pEvent.GetFloat()
    else:
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return 0

    pSlider.SetValue(fPercentage)

    fPlayerTransfer = float(fPlayerCurrCrew) * float(fPercentage)
    iPlayerTransfer = int(fPlayerTransfer)

    if iPlayerTransfer >= fPlayerCurrCrew:
        iPlayerTransfer = fPlayerCurrCrew

    fTargetTransfer = float(fTargetCurrCrew) * float(fPercentage)
    iTargetTransfer = int(fTargetTransfer)

    if iTargetTransfer >= fTargetCurrCrew:
        iTargetTransfer = fTargetCurrCrew

    iPlayerFutureComplement = fPlayerCurrCrew + iTargetTransfer
    iTargetFutureComplement = fTargetCurrCrew + iPlayerTransfer
    
    if iPlayerFutureComplement > fPlayerMaxAllowed:
        iPlayerExtraCrew = iPlayerFutureComplement - fPlayerMaxAllowed
        iTargetTransfer = iTargetTransfer - iPlayerExtraCrew

    if iTargetFutureComplement > fTargetMaxAllowed:
        iTargetExtraCrew = iTargetFutureComplement - fTargetMaxAllowed
        iPlayerTransfer = iPlayerTransfer - iTargetExtraCrew

    sPlayerText = "Max Allowed Crew: " + str(fPlayerMaxAllowed) + "\n" + "Standard Crew: " + str(fPlayerMaxCrew) + "\n" + "Current Crew: " + str(fPlayerCurrCrew) + "\n" + "Crew To Transfer: " + str(iPlayerTransfer)

    sTargetText = "Max Allowed Crew: " + str(fTargetMaxAllowed) + "\n" + "Standard Crew: " + str(fTargetMaxCrew) + "\n" + "Current Crew: " + str(fTargetCurrCrew) + "\n" + "Crew To Transfer: " + str(iTargetTransfer)

    pPlayerText.SetString(str(sPlayerText))

    pTargetText.SetString(str(sTargetText))

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def KillGUI(pObject, pEvent):
    global pMainPane, pPane, pSlider, pTransferButton, sPlayerText, pPlayerText, sTargetText, pTargetText

    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_TRANSFER_TO_PLAYER, pMission, __name__ + ".TransferToPlayer")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_TRANSFER_PLAYER, pMission, __name__ + ".TransferPlayer")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_TRANSFER_FROM_PLAYER, pMission, __name__ + ".TransferFromPlayer")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_UPDATE, pMission, __name__ + ".UpdateSlider")
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

    pSlider = None
    pTransferButton = None
    pPlayerText = None
    pTargetText = None
    sPlayerText = "N/A"
    sTargetText = "N/A"

    App.g_kUtopiaModule.Pause(0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def Quitting():
    global pMainPane, pPane, pSlider, pTransferButton, sPlayerText, pPlayerText, sTargetText, pTargetText

    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_TRANSFER_TO_PLAYER, pMission, __name__ + ".TransferToPlayer")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_TRANSFER_PLAYER, pMission, __name__ + ".TransferPlayer")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_TRANSFER_FROM_PLAYER, pMission, __name__ + ".TransferFromPlayer")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_UPDATE, pMission, __name__ + ".UpdateSlider")
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

    pSlider = None
    pTransferButton = None
    pPlayerText = None
    pTargetText = None
    sPlayerText = "N/A"
    sTargetText = "N/A"

def Distance(pObject):
    pPlayer = App.Game_GetCurrentPlayer()
    vDifference = pObject.GetWorldLocation()
    vDifference.Subtract(pPlayer.GetWorldLocation())

    return vDifference.Length()
