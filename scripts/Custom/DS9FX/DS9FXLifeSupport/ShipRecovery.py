# Take over non enemy ships - Smbw

# Thank you USS Sovereign for your help!


# Imports
import App
import Foundation
import MissionLib
import string
from Custom.DS9FX.DS9FXAILib import DS9FXGenericStaticFriendlyFollowAI, DS9FXGenericStaticStarbaseFriendlyAI
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict


# Events
ET_CLOSE = App.UtopiaModule_GetNextEventType()
ET_RECOVER = App.UtopiaModule_GetNextEventType()
ET_UPDATE = App.UtopiaModule_GetNextEventType()


# Vars
crewmen = 0
fPercentage = 0.0
pMainPane = None
pPane = None
pSlider = None
pInfoText = None
sInfoText = "N/A"


# Functions
def showGUI():
    global crewmen, pMainPane, pPane, pSlider, fPercentage, pInfoText, sInfoText

    fPercentage = 0.0

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    if not pTarget:
        return 0
    
    if pPlayer.IsCloaked() or pTarget.IsCloaked():
        return 0

    TargetName = pTarget.GetName()
    if not TargetName:
        return 0

    pFriendly = MissionLib.GetFriendlyGroup()
    if pFriendly:
        if pFriendly.IsNameInGroup(TargetName):
            return 0
    else:
        return 0

    pEnemy = MissionLib.GetEnemyGroup()
    if pEnemy: 
        if pEnemy.IsNameInGroup(TargetName):
            return 0
    else:
        return 0

    pNeutral = MissionLib.GetNeutralGroup()
    if pNeutral:
        if pNeutral.IsNameInGroup(TargetName):
            return 0
    else:
        return 0

    if not Distance(pTarget) < 300:
        return 0

    pPlayerID = pPlayer.GetObjID()
    if not pPlayerID:
        return 0

    pTargetID = pTarget.GetObjID()
    if not pTargetID:
        return 0

    pPlayerInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pPlayer, pPlayerID) # Sov Edit
    if not pPlayerInfo:
        return 0

    pTargetInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pTarget, pTargetID) # Sov Edit
    if not pTargetInfo:
        return 0

    fPlayerMaxCrew = pPlayerInfo["fMax"]
    fPlayerCurrCrew = pPlayerInfo["fMin"]
    fTargetMaxCrew = pTargetInfo["fMax"]
    fTargetCurrCrew = pTargetInfo["fMin"]

    if fPlayerCurrCrew < (fPlayerMaxCrew/10.0) or (fPlayerCurrCrew - 2) < 10.0:
        return 0

    if not fTargetCurrCrew == 0: # Wrong.... -> that's one of the other buttons :)
        return 0

    crewmen = int(fTargetMaxCrew/50.0) # calculate how many men will beam over

    if crewmen < 1:
        crewmen = 1

    if (fPlayerCurrCrew - crewmen) < 10.0:
        crewmen = int(fPlayerCurrCrew - 8.0) # Leave the bridge crew on the player ship. They can beam over when the ship is friendly

    if crewmen < 1:
        return 0

    App.g_kUtopiaModule.Pause(1)

    pPane = App.TGPane_Create(1.0, 1.0)
    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
    pTCW.AddChild(pPane, 0, 0)
    pMainPane = App.TGPane_Create(0.4, 0.35)
    pPane.AddChild(pMainPane, 0.4, 0.12)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_RECOVER, pMission, __name__ + ".RecoverShip")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_UPDATE, pMission, __name__ + ".UpdateSlider")

    kColor = App.TGColorA() 
    kColor.SetRGBA(1, 0.81, 0.41, 1.0)

    pMainWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Recovery Management"), 0.0, 0.0, None, 1, 0.4, 0.35, kColor)
    pMainPane.AddChild(pMainWindow, 0.0, 0.0)
    pMainPane.MoveToFront(pMainWindow)

    pInfoWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Info:"), 0.0, 0.0, None, 1, 0.18, 0.11, kColor)
    pMainPane.AddChild(pInfoWindow, 0.11, 0.05)
    pMainPane.MoveToFront(pInfoWindow)

    pSlider = DS9FXMenuLib.CreateSliderbar(App.TGString("Crew Selection"), ET_UPDATE, float(fPercentage), 0.0, 1.0, 0.01, 1.0, 0.15, 0.04)
    pMainWindow.AddChild(pSlider, 0.03, 0.17)
    pMainWindow.MoveToFront(pSlider)

    sInfoText = "Available Engineers: " + str(crewmen) + "\n" + "Selected Engineers: 0"
    pInfoText = App.TGParagraph_CreateW(App.TGString(str(sInfoText)), pInfoWindow.GetMaximumInteriorWidth(), None, '', pInfoWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pInfoWindow.AddChild(pInfoText, 0, 0.01)

    kNormalColor = App.TGColorA() 
    kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
    kHilightedColor = App.TGColorA() 
    kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
    kDisabledColor = App.TGColorA() 
    kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_RECOVER)
    pEvent.SetString("DS9FXRecover")
    pButton = App.STRoundedButton_CreateW(App.TGString("Recover Ship"), pEvent, 0.15, 0.04)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pMainWindow.AddChild(pButton, 0.2, 0.17)
    pMainWindow.MoveToFront(pButton)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_CLOSE)
    pEvent.SetString("DS9FXRecoverClose")
    pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.16, 0.04)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pMainWindow.AddChild(pButton, 0.11, 0.25)
    pMainWindow.MoveToFront(pButton)

    pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode() 
    pLCARS = pGraphicsMode.GetLcarsString() 
    pGlass = App.TGIcon_Create(pLCARS, 120) 
    pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight()) 
    pMainPane.AddChild(pGlass, 0, 0)

    pMainWindow.InteriorChangedSize()
    pMainWindow.Layout()
    pInfoWindow.InteriorChangedSize()
    pInfoWindow.Layout()
    pMainPane.Layout()
    pPane.Layout()

    pPane.SetVisible()

def UpdateSlider(pObject, pEvent):
    global pSlider, fPercentage, crewmen, pInfoText, sInfoText

    if hasattr(pEvent, "GetFloat"):
        fPercentage = pEvent.GetFloat()
    else:
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return 0

    pSlider.SetValue(fPercentage)

    sInfoText = sInfoText = "Available Engineers: " + str(crewmen) + "\n" + "Selected Engineers: " + str(int(crewmen * float(fPercentage)))
    pInfoText.SetString(str(sInfoText))

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def RecoverShip(pObject, pEvent):
    global crewmen, fPercentage, pPane

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    if not pTarget:
        return 0

    pTargetID = pTarget.GetObjID()
    if not pTargetID:
        return 0

    crewmen = int(crewmen * float(fPercentage))

    if crewmen < 8: # calculate time
        tPrLS = 16 # /4
        tSeLS = 12 # /4
        tTakeover = 11

    elif crewmen > 35:
        tPrLS = 4 # /4
        tSeLS = 6 # /4.0
        tTakeover = 5

    else:
        tPrLS = 8 # /4
        tSeLS = 6 # /4.0
        tTakeover = int((((crewmen ** 2) + (37 * crewmen)) / 360) + 4)

    tLS = 2
    chshield = 1
    if not ShieldCheck(pTargetID) == 1:
        chshield = 0
        tLS = 12

    pPane.SetNotVisible()
    App.g_kUtopiaModule.Pause(0)
    Quitting()

    Transfer(-crewmen) # beam them over Scotty!

    # ok that was easy - now we need to get the Life Support property
    # Thx Sovereign! Much better now!

    pSequence = App.TGSequence_Create()
    pIterator = pTarget.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
    pSystem = pTarget.GetNextSubsystemMatch(pIterator)

    while (pSystem != None):
        pSystemname = pSystem.GetName()

        if pSystemname == "Life Support":
            pLifeSupport = App.HullClass_Cast(pSystem)
            if pLifeSupport.IsDisabled():
                pLScurcond = pLifeSupport.GetCondition()
                pLSdisper = pLifeSupport.GetDisabledPercentage()
                pLSmaxcond = pLifeSupport.GetMaxCondition()
                pLSdiscond = pLSmaxcond * pLSdisper

                if pLScurcond < pLSdiscond:
                    repairunit = pLSdiscond - pLScurcond
                    repairunit = int(repairunit / 4.0)
                    calcfutcond = ((repairunit * 4) + pLScurcond)

                    if calcfutcond <= pLSdiscond:
                        repairunit = repairunit + int((pLSdiscond - calcfutcond) / 4) + 1

                    NewCondition = pLScurcond + repairunit

                    if (tLS > 2 and chshield == 1) or (tLS > 12 and chshield == 0):
                        tPrLS = tSeLS

                    tLS = tLS + (tPrLS / 4.0)

                    pAction = App.TGScriptAction_Create(__name__, "repairLifeSupport", pLifeSupport, NewCondition)
                    pSequence.AddAction(pAction, None, tLS)

                    NewCondition = NewCondition + repairunit
                    tLS = tLS + (tPrLS / 4.0)

                    pAction = App.TGScriptAction_Create(__name__, "repairLifeSupport", pLifeSupport, NewCondition)
                    pSequence.AddAction(pAction, None, tLS)

                    NewCondition = NewCondition + repairunit
                    tLS = tLS + (tPrLS / 4.0)

                    pAction = App.TGScriptAction_Create(__name__, "repairLifeSupport", pLifeSupport, NewCondition)
                    pSequence.AddAction(pAction, None, tLS)

                    NewCondition = NewCondition + repairunit
                    tLS = tLS + (tPrLS / 4.0)

                    pAction = App.TGScriptAction_Create(__name__, "repairLifeSupport", pLifeSupport, NewCondition)
                    pSequence.AddAction(pAction, None, tLS)

        pSystem = pTarget.GetNextSubsystemMatch(pIterator)

    pTarget.EndGetSubsystemMatch(pIterator)

    # now make the target friendly...

    tLS = tLS + tTakeover

    pAction = App.TGScriptAction_Create(__name__, "Reactivate", pTarget)
    pSequence.AddAction(pAction, None, tLS)
    pSequence.Play()
    
    from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pTarget)
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pPlayer)

    # that was easy again... :)
    return 0

def repairLifeSupport(pAction, pLifeSupport, NewCondition):
    pLifeSupport.SetCondition(NewCondition)
    return 0

def KillGUI(pObject, pEvent):
    Quitting()

    App.g_kUtopiaModule.Pause(0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def Quitting():
    global pMainPane, pPane, pSlider, sInfoText, pInfoText

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
        App.g_kEventManager.RemoveBroadcastHandler(ET_RECOVER, pMission, __name__ + ".RecoverShip")
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
    pInfoText = None
    sInfoText = "N/A"

def Reactivate(pAction, pShip):
    pFriendly = MissionLib.GetFriendlyGroup()
    if not pFriendly:
        return 0

    sName = pShip.GetName()
    if not sName:
        return 0
    
    DS9FXLifeSupportLib.ClearFromGroup(sName)

    pFriendly.AddName(str(sName))
    
    DS9FXLifeSupportLib.ResetAffiliationColors()

    # Ok - now we need Sovereign's AI code.

    if not (pFriendly.IsNameInGroup(pShip.GetName())): # well I guess it's there, it was just added...
        return 0

    NoQBR = None
    import QuickBattle.QuickBattle
    try:
        import Custom.QuickBattleGame.QuickBattle
    except:
        NoQBR = 'NoQBR'

    if QuickBattle.QuickBattle.pFriendlies:
        if (pShip.GetShipProperty().IsStationary() == 1):

            pShip.SetAI(DS9FXGenericStaticStarbaseFriendlyAI.CreateAI(pShip))
        else:
            pShip.SetAI(DS9FXGenericStaticFriendlyFollowAI.CreateAI(pShip))


    if not NoQBR == 'NoQBR':
        if Custom.QuickBattleGame.QuickBattle.pFriendlies:
            if (pShip.GetShipProperty().IsStationary() == 1):

                pShip.SetAI(DS9FXGenericStaticStarbaseFriendlyAI.CreateAI(pShip))
            else:
                pShip.SetAI(DS9FXGenericStaticFriendlyFollowAI.CreateAI(pShip))

    from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
    DS9FXGlobalEvents.Trigger_Ship_Reactivated(MissionLib.GetPlayer(), pShip)
    
    return 0

def ShieldCheck(pShipID):
    pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
    if not pShip:
        return 0

    tarshields = pShip.GetShields()

    if tarshields:
        if tarshields.IsOn() == 1:
            s1 = tarshields.GetSingleShieldPercentage(tarshields.FRONT_SHIELDS)
            s2 = tarshields.GetSingleShieldPercentage(tarshields.REAR_SHIELDS)
            s3 = tarshields.GetSingleShieldPercentage(tarshields.TOP_SHIELDS)
            s4 = tarshields.GetSingleShieldPercentage(tarshields.BOTTOM_SHIELDS)
            s5 = tarshields.GetSingleShieldPercentage(tarshields.LEFT_SHIELDS)
            s6 = tarshields.GetSingleShieldPercentage(tarshields.RIGHT_SHIELDS)

            if s1 < 0.175 or s2 < 0.175 or s3 < 0.175 or s4 < 0.175 or s5 < 0.175 or s6 < 0.175:
                return 1

            else:
                return 0
        else:
            return 1
    else:
        return 1

def Transfer(fToTransfer):    
    pPlayer = MissionLib.GetPlayer()
    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    pPlayerID = pPlayer.GetObjID()
    pTargetID = pTarget.GetObjID()

    iToTransfer = int(fToTransfer)

    pTargetInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pTarget, pTargetID) # Sov Edit
    if not pTargetInfo:
        return 0

    fTargetCurrCrew = pTargetInfo["fMin"]

    pPlayerInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pPlayer, pPlayerID) # Sov Edit
    if not pPlayerInfo:
        return 0

    fPlayerCurrCrew = pPlayerInfo["fMin"]

    if fToTransfer >= 0: # The player gets crew
        if iToTransfer >= fTargetCurrCrew:
            iToTransfer = fTargetCurrCrew

    else:
        if (iToTransfer * -1) >= fPlayerCurrCrew:
            iToTransfer = (fPlayerCurrCrew * -1)

    if pPlayer.GetShields().IsOn() == 1:
        pSequence = App.TGSequence_Create()
        g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
        pSequence.AppendAction(App.CharacterAction_Create(App.CharacterClass_GetObject(App.g_kSetManager.GetSet('bridge'), 'Engineer'), App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, 4))
        pSequence.Play()

    App.g_kSoundManager.PlaySound("DS9FXTransportSound")

    iPlayerCurrStats = LifeSupport_dict.dCrew[pPlayerID]
    iTargetCurrStats = LifeSupport_dict.dCrew[pTargetID]

    iPlayerCurrStats = iPlayerCurrStats + iToTransfer
    iTargetCurrStats = iTargetCurrStats - iToTransfer

    if iPlayerCurrStats <= 0:
        iPlayerCurrStats = 0
        DS9FXLifeSupportLib.GroupCheck(pPlayer)
        DS9FXLifeSupportLib.PlayerCheck(pPlayerID)

    if iTargetCurrStats <= 0:
        iTargetCurrStats = 0
        pTarget.ClearAI()
        DS9FXLifeSupportLib.GroupCheck(pTarget)
        DS9FXLifeSupportLib.PlayerCheck(pTargetID)

    LifeSupport_dict.dCrew[pPlayerID] = iPlayerCurrStats
    LifeSupport_dict.dCrew[pTargetID] = iTargetCurrStats

def Distance(pObject):
    pPlayer = App.Game_GetCurrentPlayer()
    vDifference = pObject.GetWorldLocation()
    vDifference.Subtract(pPlayer.GetWorldLocation())

    return vDifference.Length()
