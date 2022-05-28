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

pName = MissionIDs.RM1
sName = "Random Dominion Mission"
sObjectives = ""
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.MiniMissionMode.RandomMission1"
lSets = ["GammaQuadrant1", "DS9FXKaremma1", "DS9FXDosi1", "DS9FXYadera1", "DS9FXNewBajor1", "DS9FXGaia1", "DS9FXKurill1", "DS9FXTrialus1", "DS9FXTRogoran1","DS9FXVandros1", "DS9FXFoundersHomeworld1"]
lShips = [DS9FXShips.DomBC, DS9FXShips.Bugship]
lFriendly = [DS9FXShips.Akira, DS9FXShips.Centaur, DS9FXShips.Defiant, DS9FXShips.Excelsior, DS9FXShips.Galaxy, DS9FXShips.Miranda, DS9FXShips.Nebula, DS9FXShips.Sovereign]
lObjective = []
lType = []
lFType = []
lFObjective = []
sSet = ""

def Briefing():
    global lSets, lShips, lObjective, lType, sSet, sObjectives, sBriefing, lFObjective, lFType
    
    sSet = ""
    lObjective = []
    lType = []
    lFObjective = []
    lFType = []
    
    iLen = len(lSets)
    i = GetRandomNumber(iLen, 0)
    sSet = lSets[i]
    
    i = GetRandomNumber(8, 1)
    for i in range(0, i):
        i = i + 1
        iLen = len(lShips)
        j = GetRandomNumber(iLen, 0)
        s = lShips[j]
        lType.append(s)
        s = "Dominion Ship " + str(i)
        lObjective.append(s)
        
    i  = GetRandomNumber(3, 1)
    for i in range(0, i):
        i = i + 1
        iLen = len(lFriendly)
        j = GetRandomNumber(iLen, 0)
        s = lFriendly[j]
        lFType.append(s)
        s = "Escort " + str(i)
        lFObjective.append(s)        
        
    sObjectives = "-Go to " + sSet + "\n-Destroy any Dominion ships found there"
    sBriefing = "Captain you are to go to "  + sSet + " system and engage and destroy any Dominion ships found there.\n\nGood luck."
        
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)
    
def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat

def MissionInitiate():    
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    CreateFriendlies()

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")   
    
def CreateFriendlies():
    global lFObjective, lFType

    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyFollowAI
    iLen = len(lFObjective)
    
    for i in range(0, iLen):
        sShip = lFObjective[i]
        sType = lFType[i]
        pShip = loadspacehelper.CreateShip(sType, pSet, sShip, "")            
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetFriendlyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyFollowAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(500, 100)
        adY = GetRandomNumber(500, 100)
        adZ = GetRandomNumber(500, 100)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()
    
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
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")            
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        except:
            pass

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
    global sSet
    
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

    if pSet.GetName() == sSet:
        ObjectiveTxt()
        CreateShips()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)
        
def ObjectiveTxt():
    sText = "I'm detecting our target sir."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def CreateShips():
    global lObjective, lType
    
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI
    iLen = len(lObjective)
    
    for i in range(0, iLen):
        sShip = lObjective[i]
        sType = lType[i]
        pShip = loadspacehelper.CreateShip(sType, pSet, sShip, "")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetEnemyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet)
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(4000, 1000)
        adY = GetRandomNumber(4000, 1000)
        adZ = GetRandomNumber(4000, 1000)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()
        
def ObjectExploding(pObject, pEvent):
    global lObjective
    
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return
    
    if pShip.GetName() in lObjective:
        lObjective.remove(pShip.GetName())
        if len(lObjective) == 0:
            GoHomeTxt()
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")                
            except:
                pass

            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            
            DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)
        
def GoHomeTxt():
    sText = "We've destroyed all ships, we should go back to DS9."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 3
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
        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")            
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
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

def CrewLost():
    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        FailedTxt()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")        
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass