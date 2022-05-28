# Xtended Mission

# by Sov

import App
import MissionLib
import loadspacehelper
import nt
import string
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXShips, DS9FXMissionLib, DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

pPlayerName = ""
pName = MissionIDs.ORM2
sName = "Elucidate"
sObjectives = "-Go to Idran system\n-Scan for warp trails\n-Discover what the Dominion are doing\n-Report to DS9"
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission2"
sProgress  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\OldRivals\\Save\\MissionState.py"
pShipType = None
bScannedIdran = 0

def Briefing():
    global pPlayerName, sBriefing
    reload(DS9FXSavedConfig)
    if not DS9FXSavedConfig.GammaPlanets == 1 and not DS9FXSavedConfig.YaderaPlanets == 1 and not DS9FXSavedConfig.VandrosPlanets == 1 and not DS9FXSavedConfig.GaiaPlanets == 1:
        PlanetsTxt()
        return 
    pPlayerName = App.g_kUtopiaModule.GetCaptainName().GetCString()
    sBriefing = "Stardate 64706.07\n\nThe Dominion has been acting strangely lately and the most recent assault on the Tibet confirms this. Captain " + str(pPlayerName) + " the Tibet's sensor logs don't indicate anything which would help us in discovering why the Dominion are acting the way they do.\n\nAs you may be aware or not, a lone Dominion Bugship has escaped in your last engagement to an unknown system. Your mission is to discover where and uncover any data about the Dominion activities. We must uncover their plot, Starfleet Intelligence speculates that they are doing something which might restore thier former glory..."
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)

def PlanetsTxt():
    sText = "Planets in Idran, Gaia, Vandros and Yadera are not turned on..."
    iPos = 3
    iFont = 12
    iDur = 6
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def MissionInitiate():
    global pShipType, bScannedIdran
    
    SetupPlayer()
    
    bScannedIdran = 0
    pPlayer = MissionLib.GetPlayer()
    pShipType = DS9FXLifeSupportLib.GetShipType(pPlayer)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")

    pCondition = App.ConditionScript_Create("Conditions.ConditionPlayerOrbitting", "ConditionPlayerOrbitting", "Idran")
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InOrbitIdran", pCondition)
    pCondition = App.ConditionScript_Create("Conditions.ConditionPlayerOrbitting", "ConditionPlayerOrbitting", "Vandros I")
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InOrbitGoal", pCondition)
    lInvalidPlanets = ["Gaia I", "Gaia II", "Gaia III", "Gaia IV", "Vandros II", "Vandros III", "Vandros IV", "Yadera 1", "Yadera 2", "Yadera 3", "Yadera Prime", "Yadera 5"]
    for s in lInvalidPlanets:
        pCondition = App.ConditionScript_Create("Conditions.ConditionPlayerOrbitting", "ConditionPlayerOrbitting", s)
        MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InOrbitInvalid", pCondition)  

def SetupPlayer():
    from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Save import MissionState
    reload(MissionState)
    pShip = MissionState.Ship
    pPlayer = MissionLib.GetPlayer()
    pPlayerName = pPlayer.GetName()
    pSet = pPlayer.GetContainingSet()
    pSet.DeleteObjectFromSet(pPlayerName)
    loadspacehelper.CreateShip(pShip, pSet, pPlayerName, "Player Start")
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    DS9FXLifeSupportLib.ClearFromGroup(pPlayerName)
    pMission.GetFriendlyGroup().AddName(pPlayerName)
    GetPlayer = MissionLib.GetShip(pPlayerName, pSet)
    pGame = App.Game_GetCurrentGame()
    pGame.SetPlayer(GetPlayer)

def DisableDS9FXMenuButtons(pObject, pEvent):
    try:
        bHail = DS9FXMenuLib.GetSubMenuButton("Hail DS9", "Helm", "DS9FX", "DS9 Options...")
        bHail.SetDisabled()
    except:
        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

def PlayerExploding(pObject, pEvent):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    pPlayer = MissionLib.GetPlayer()
      
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return
        
    if (pShip.GetObjID() == pPlayer.GetObjID()):
        FailedTxt()
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitIdran")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitGoal")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitInvalid")
        except:
            pass

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
    global bScannedIdran
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return

    if not pPlayer.GetObjID() == pShip.GetObjID():
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return
    
    if pSet.GetName() == "GammaQuadrant1":
        if not bScannedIdran:
            ObjectiveGammaTxt()
    elif pSet.GetName() == "DS9FXGaia1":
        if bScannedIdran:
            ObjectiveTxt()
    elif pSet.GetName() == "DS9FXVandros1":
        if bScannedIdran:
            ObjectiveTxt()
    elif pSet.GetName() == "DS9FXYadera1":
        if bScannedIdran:
            ObjectiveTxt()            
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def ObjectiveGammaTxt():
    sText = "I am picking up many warp trails near the Gas Giant...\nPerhaps we should enter its orbit to get a better view..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def ObjectiveTxt():
    sText = "We should enter orbit of each planet in order to scan it.\nThis will give us clues as to what the Dominion is doing..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def InOrbitIdran(bInOrbit):
    global bScannedIdran
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitIdran")
    bScannedIdran = 1
    IdranTxt()

def IdranTxt():
    sText = "I have several possible locations which we could investigate sir:\nGAIA, VANDROS and YADERA... \nWhere to go first?"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 30
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def InOrbitGoal(bInOrbit):
    global bScannedIdran
    if not bScannedIdran:
        return
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitIdran")
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitGoal")
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitInvalid")
    GoalTxt()
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    except:
        pass
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")

def GoalTxt():
    sText = "Sir, I think we have what we're looking for... We should get back to DS9 ASAP!!!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 30
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def InOrbitInvalid(bInOrbit):
    global bScannedIdran
    if not bScannedIdran:
        return
    InvalidTxt()

def InvalidTxt():
    sText = "Nothing of interest here sir..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 30
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def MissionEnd(pObject, pEvent):
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

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
        SaveProgress()
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitIdran")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitGoal")
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitInvalid")
        except:
            pass

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

def SaveProgress():
    global pShipType
    if not pShipType:
        return
    from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Save import MissionState
    reload(MissionState)
    if MissionState.OnMission > 3:
        i = MissionState.OnMission
    else:
        i = 3
    file = nt.open(sProgress, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
    nt.write(file, "OnMission = " + str(i) + "\n")
    nt.write(file, "Ship = " + "'" + pShipType + "'")
    nt.close(file)

def CrewLost():
    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        FailedTxt()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitIdran")
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitGoal")
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbitInvalid")
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass
