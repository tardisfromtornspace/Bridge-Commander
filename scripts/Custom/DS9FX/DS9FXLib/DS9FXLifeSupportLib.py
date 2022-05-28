# LifeSupport feature library

# by Sov

# Imports
import App
import Foundation
import MissionLib
import string
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict

# Vars
pPaneID = App.NULL_ID

# Functions
def GetShipMaxCrewCount(pShip, pShipType):
    if Foundation.shipList.has_key(pShipType):
        fShip = Foundation.shipList[pShipType]
        if fShip:
            if hasattr(fShip, "fCrew"):
                if fShip.fCrew == "Off":
                    return 0
                fMaxCrew = fShip.fCrew
                return fMaxCrew
            else:
                fMaxCrew = CalculateMaxCrew(pShip)
                return fMaxCrew
        else:
            return 0    
    else:
        return 0

def GetShipMaxAndMinCrewCount(pShip, pShipID):
    pShipType = GetShipType(pShip)
    if not pShipType:
        return 0

    if Foundation.shipList.has_key(pShipType):
        fShip = Foundation.shipList[pShipType]
        if fShip:
            if hasattr(fShip, "fCrew"):
                if fShip.fCrew == "Off":
                    return 0
                fMax = fShip.fCrew
                fMin = LifeSupport_dict.dCrew[pShipID]
                return {"fMin" : fMin, "fMax" : fMax}
            else:
                fMax = CalculateMaxCrew(pShip)
                fMin = LifeSupport_dict.dCrew[pShipID]
                return {"fMin" : fMin, "fMax" : fMax}
        else:
            return 0    
    else:
        return 0

def GetCrewPercentage(pShip, pShipID):
    pInfo = GetShipMaxAndMinCrewCount(pShip, pShipID)
    if not pInfo:
        return "N/A"
    
    fCurr = float(pInfo["fMin"])
    fMax = float(pInfo["fMax"])
    fPerc = fCurr/fMax*100
    iPerc = int(fPerc)
    
    return iPerc
    
def CalculateMaxCrew(pShip):
    # This ship has no crew count defined... calculate one on our own
    fApproxCrew = float(pShip.GetRadius()) * float(200)
    iApproxCrew = int(fApproxCrew)
    fMaxCrew = iApproxCrew
    return fMaxCrew

def PlayerCheck(pShipID):
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pPlayerID = pPlayer.GetObjID()
    if not pPlayerID:
        return 0

    if pPlayerID == pShipID:
        lSystems = [pPlayer.GetHull(), pPlayer.GetShields(), pPlayer.GetPowerSubsystem(), pPlayer.GetSensorSubsystem(),
                    pPlayer.GetTorpedoSystem(), pPlayer.GetPhaserSystem(), pPlayer.GetPulseWeaponSystem(), pPlayer.GetTractorBeamSystem(),
                    pPlayer.GetImpulseEngineSubsystem(), pPlayer.GetWarpEngineSubsystem(), pPlayer.GetRepairSubsystem(), pPlayer.GetCloakingSubsystem()]

        for pSys in lSystems:
            if pSys:
                KillSystems(pPlayer, pSys)

        import DS9FXDisableEndCombat
        DS9FXDisableEndCombat.RestoreEndCombatButton()
        
        ShowCrewDeadPrint()

def KillSystems(pShip, pSubsystem, bIsChild = 0):
    if (bIsChild != 0) or (pSubsystem.GetNumChildSubsystems() == 0):
        fStats = pSubsystem.GetProperty().GetDisabledPercentage()
        pSubsystem.GetProperty().SetDisabledPercentage(2.0)

    for i in range(pSubsystem.GetNumChildSubsystems()):
        pChild = pSubsystem.GetChildSubsystem(i)

        if (pChild != None):
            KillSystems(pShip, pChild, 1)

def ShowCrewDeadPrint():
    global pPaneID

    pPane = App.TGPane_Create(1.0, 1.0)
    App.g_kRootWindow.PrependChild(pPane)

    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime (1)
    pSequence.AppendAction(ShowCrewDeadPrintAction(pPane))
    pPaneID = pPane.GetObjID()
    pSequence.Play()

def ShowCrewDeadPrintAction(pPane):
    pSequence = App.TGSequence_Create()
    pSequence.SetUseRealTime (1)

    pAction = LineAction("Game Over!\n\nYour crew has died!", pPane, 3, 5, 12)
    pSequence.AddAction(pAction, None, 0.5)
    pAction = App.TGScriptAction_Create(__name__, "KillPane")
    pSequence.AppendAction(pAction, 0.1)
    pSequence.Play()

def LineAction(sLine, pPane, fPos, duration, fontSize):
    fHeight = fPos * 0.0375
    App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
    pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
    return pAction

def KillPane(pAction):
    global pPaneID

    pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
    App.g_kRootWindow.DeleteChild(pPane)
    pPaneID = App.NULL_ID

    return 0          

def GroupCheck(pShip):
    sName = pShip.GetName()
    lGroups = [MissionLib.GetEnemyGroup(), MissionLib.GetFriendlyGroup(), MissionLib.GetNeutralGroup(), App.ObjectGroup()]
    for group in lGroups:
        if group:
            if group.IsNameInGroup(sName):
                i = 0
                if not group.GetNameTuple():
                    group.AddName("This ship doesn't exist: " + str(sName))
                else:
                    for item in group.GetNameTuple():
                        i = i + 1
                    if i <= 1:
                        group.AddName("This ship doesn't exist: " + str(sName))
                group.RemoveName(sName)
                # I have no clue why the engine doesn't update affiliation colors properly
                pMenu = App.STTargetMenu_GetTargetMenu()
                if pMenu != None:
                    pMenu.ResetAffiliationColors()

def ClearFromGroup(sName):
    lGroups = [MissionLib.GetEnemyGroup(), MissionLib.GetFriendlyGroup(), MissionLib.GetNeutralGroup(), App.ObjectGroup()]
    for group in lGroups:
        if group:
            if group.IsNameInGroup(sName):
                i = 0
                if not group.GetNameTuple():
                    group.AddName("This ship doesn't exist: " + str(sName))
                else:
                    for item in group.GetNameTuple():
                        i = i + 1
                    if i <= 1:
                        group.AddName("This ship doesn't exist: " + str(sName))
                group.RemoveName(sName)
                # I have no clue why the engine doesn't update affiliation colors properly
                pMenu = App.STTargetMenu_GetTargetMenu()
                if pMenu != None:
                    pMenu.ResetAffiliationColors()

def ResetAffiliationColors():
    pMenu = App.STTargetMenu_GetTargetMenu()
    if pMenu != None:
        pMenu.ResetAffiliationColors()    

def CreateCrewLabels():
    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
    if not pTCW:
        return 0

    pText = App.TGParagraph_Create("Player Crew: N/A\nTarget Crew: N/A", 1.0, None, "Serpentine", 7.0)
    assert pText
    if not pText:
        return 0

    kTextColor = App.TGColorA() 
    kTextColor.SetRGBA(0.0, 0.0, 0.0, 1.0)
    pText.SetColor(kTextColor)
    pText.Layout()

    pLabel = App.TGPane_Create(pText.GetWidth() + pText.GetWidth() / 8.0, pText.GetHeight() + pText.GetHeight() / 8.0)
    pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
    assert pGraphicsMode
    if not pGraphicsMode:
        return 0

    pLCARS = pGraphicsMode.GetLcarsString()
    kBackColor = App.TGColorA()
    kBackColor.SetRGBA(173.0 / 255.0, 144.0 / 255.0, 99.0 / 255.0, 1.0)
    pBackground = App.TGIcon_Create(pLCARS, 200, kBackColor)
    assert pBackground
    if not pBackground:
        return 0

    pBackground.Resize(pLabel.GetWidth(), pLabel.GetHeight())
    pLabel.AddChild(pText, pLabel.GetWidth() / 2.0 - pText.GetWidth() / 2.0, 0.0)
    pLabel.AddChild(pBackground)
    pRadarDisplay = pTCW.GetRadarDisplay()
    if not pRadarDisplay:
        return 0

    pTCW.AddChild(pLabel, pRadarDisplay.GetRight() + 0.01, pRadarDisplay.GetBottom() - pLabel.GetHeight())

    return {"Label" : pLabel, "Background" : pBackground, "Text" : pText}

def GetShipType(pShip):
    if pShip.GetScript():
        return string.split(pShip.GetScript(), '.')[-1]
    return None

def GetShieldPerc(pShip):
    if not pShip:
        return 0

    pSys = pShip.GetShields()
    if not pSys:
        return 0

    if not pSys.IsOn():
        return 0

    if pSys.IsDisabled():
        return 0

    fTotal = pSys.GetShieldPercentage()

    fTotal = fTotal * 100

    return fTotal
