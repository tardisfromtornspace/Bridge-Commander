# Xtended Mission

# by Smbw

import App
import MissionLib
import loadspacehelper
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXShips, DS9FXMissionLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXAILib import DS9FXGenericEnemyAI, DS9FXGenericFriendlyAI
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

pName = MissionIDs.HM6
sName = "Save Odo"
sObjectives = "- Warp to the Founder's Homeworld\n- Locate Odo\n- Return Odo to the Station"
sBriefing = "A Romulan/Cardassian joint fleet is attacking the Founder's Homeworld. Heavy forces of the Dominion were attacking the Romulan/Cardassian taskforce. Captain, take the Defiant and try to rescue Odo."
sModule = "Custom.DS9FX.DS9FXMissions.HistoricMode.HistoricMission6"

pOdo_Ship = None

def Briefing():
    # Life support is used so we need to check if it is enabled
    reload(DS9FXSavedConfig)
    if not DS9FXSavedConfig.LifeSupport == 1:
        LifeSupportTxt()
        return
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)
    
def LifeSupportTxt():
    sText = "Life Support is required to this mission..."
    iPos = 3
    iFont = 12
    iDur = 6
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def MissionInitiate():
    global pOdo_Ship

    pOdo_Ship = None
    pGame = App.Game_GetCurrentGame()
    pMission = pGame.GetCurrentEpisode().GetCurrentMission()
    pPlayer = MissionLib.GetPlayer()
    pPlayerName = pPlayer.GetName()
    pSet = pPlayer.GetContainingSet()

    pSet.DeleteObjectFromSet(pPlayerName)
    loadspacehelper.CreateShip(DS9FXShips.Defiant, pSet, pPlayerName, "PlayerStart")
    DS9FXLifeSupportLib.ClearFromGroup(pPlayerName)
    pMission.GetFriendlyGroup().AddName(pPlayerName)
    NewPlayer = MissionLib.GetShip(pPlayerName, pSet)
    pGame.SetPlayer(NewPlayer)

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")    
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")

def DisableDS9FXMenuButtons(pObject, pEvent):
    try:
        bHail = DS9FXMenuLib.GetSubMenuButton("Hail DS9", "Helm", "DS9FX", "DS9 Options...")
        bHail.SetDisabled()
    except:
        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

def ObjectExploding(pObject, pEvent):
    global pOdo_Ship

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    pPlayer = MissionLib.GetPlayer()
      
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return

    IsOdo = 0
    if pOdo_Ship != None:
        if pShip.GetObjID() == pOdo_Ship.GetObjID():
            IsOdo = 1
        
    if (pShip.GetObjID() == pPlayer.GetObjID()) or (IsOdo == 1):
        FailedTxt()
        pOdo_Ship = None
        RemoveHandler()

        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def FailedTxt():
    sText = "Mission Failed!"
    iPos = 6
    iFont = 12
    iDur = 6
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def MissionHandler(pObject, pEvent):
    global pOdo_Ship
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return

    if not pPlayer.GetObjID() == pShip.GetObjID():
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return
    
    if pSet.GetName() == "DS9FXFoundersHomeworld1":
        ObjectiveTxt()
        CreateShips()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
        
        # Now, let's try this Condition thingy...
        pCon = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 60, pPlayer.GetName(), pOdo_Ship.GetName())
        MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "OdoDetected", pCon)

    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def OdoDetected(bInRange):
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "OdoDetected")
    App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
    DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
    GetOdo()
    GoHomeTxt()

def GetOdo():
    global pOdo_Ship
    
    sText = "Odo was dtected on " + pOdo_Ship.GetName() + "\n\nBeaming him over, now!"
    DS9FXMissionLib.PrintText(sText, 6, 12, 6, 1)

    # Do all the beaming stuff...
    pPlayer = MissionLib.GetPlayer()
    pPlayerID = pPlayer.GetObjID()
    pOdoID = pOdo_Ship.GetObjID()
    
    if pPlayer.GetShields().IsOn() == 1:
        pSequence = App.TGSequence_Create()
        g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
        pSequence.AppendAction(App.CharacterAction_Create(App.CharacterClass_GetObject(App.g_kSetManager.GetSet('bridge'), 'Engineer'), App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, 4))
        pSequence.Play()

    if pOdo_Ship.GetShields().IsOn() == 1:
        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "KillTargetShields", pOdo_Ship.GetName())
        pSequence.AddAction(pAction, None, 0)
        pAction = App.TGScriptAction_Create(__name__, "RestoreTargetShields", pOdo_Ship.GetName())
        pSequence.AddAction(pAction, None, 4) 
        pSequence.Play()        
    
    App.g_kSoundManager.PlaySound("DS9FXTransportSound")
    
    pPlayerCrew = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pPlayer, pPlayerID)
    if pPlayerCrew:
        PlayerCurrCrew = pPlayerCrew["fMin"]
        LifeSupport_dict.dCrew[pPlayerID] = PlayerCurrCrew + 1

    pOdoCrew = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pOdo_Ship, pOdoID)
    if pOdoCrew:
        pOdoCurrCrew = pOdoCrew["fMin"]
        if pOdoCurrCrew >= 2:
            LifeSupport_dict.dCrew[pOdoID] = PlayerCurrCrew - 1

def ObjectiveTxt():
    sText = "Scanning ships for Odo's life signs!\n\nIt's hard to get clear readings..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def CreateShips():
    global pOdo_Ship
    
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    iRand = GetRandomNumber(3, 1)
    
    for i in range(1, 19):
        sShip = "Dominion Defender " + str(i)
        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetEnemyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(DS9FXGenericEnemyAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(1500, 100)
        adY = GetRandomNumber(1500, 100)
        adZ = GetRandomNumber(1500, 100)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()

    for i in range(1, 7):
        sShip = "Keldon " + str(i)
        pShip = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetFriendlyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(DS9FXGenericFriendlyAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(1500, 100)
        adY = GetRandomNumber(1500, 100)
        adZ = GetRandomNumber(1500, 100)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()

    for i in range(1, 5):
        sShip = "Warbird " + str(i)
        pShip = loadspacehelper.CreateShip(DS9FXShips.Warbird, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetFriendlyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(DS9FXGenericFriendlyAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(1500, 100)
        adY = GetRandomNumber(1500, 100)
        adZ = GetRandomNumber(1500, 100)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()
        if i == iRand:
            pOdo_Ship = pShip

def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat

def GoHomeTxt():
    sText = "Odo is on board\n\nWe should take him back to DS9"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 10
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def MissionEnd(pObject, pEvent):
    global pOdo_Ship
    
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    pOdo_Ship = None

    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return

    if not pPlayer.GetObjID() == pShip.GetObjID():
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return
    
    if pSet.GetName() == "DeepSpace91":
        CompletedTxt()
        RemoveHandler()

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def CompletedTxt():
    sText = "Mission Completed!"
    iPos = 6
    iFont = 12
    iDur = 6
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def RemoveHandler():
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")        
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    except:
        pass
    try:
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "OdoDetected")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
    except:
        pass
    
def CrewLost():
    global pOdo_Ship
    try:
        pOdo_Ship = None
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        FailedTxt()
        RemoveHandler()
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass
