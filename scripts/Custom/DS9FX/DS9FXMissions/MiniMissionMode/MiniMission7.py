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

pName = MissionIDs.MM7
sName = "Secret Weapon"
sObjectives = "-Go to Dosi system\n-Investigate Dominion activities\n-Do everything in your power to stop the Dominion\n-Return to DS9"
sBriefing = "Captain we have a problem we need you to check out. Recent reports have suggested that the Dominion are trying to destabilize the Alpha Quadrant once again. We have a reason to believe they are developing some sort of technology in the Dosi System. Make your way to the system and do everything in your power to stop the Dominion."
sModule = "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission7"

def Briefing():
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)

def MissionInitiate():
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")
    
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
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
            App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")            
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
    
    if pSet.GetName() == "DS9FXDosi1":
        ObjectiveTxt()
        CreateShips()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def ObjectiveTxt():
    sText = "Dominion seem to be experimenting with Holocloak technology.\n\nSir, we need to destroy this prototype ship!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def CreateShips():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI
    
    for i in range(1, 9):
        sShip = "Dominion Patrol " + str(i)
        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetEnemyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))
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

    sShip = "Dominion Prototype"
    pShip = loadspacehelper.CreateShip(DS9FXShips.Excalibur, pSet, sShip, "Dummy Location")
    DS9FXLifeSupportLib.ClearFromGroup(sShip)
    pMission.GetEnemyGroup().AddName(sShip)
    pShip = MissionLib.GetShip(sShip, pSet) 
    pShip = App.ShipClass_Cast(pShip)
    pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))
    pX = pLocation.GetX()
    pY = pLocation.GetY()
    pZ = pLocation.GetZ()
    adX = GetRandomNumber(2500, 100)
    adY = GetRandomNumber(2500, 100)
    adZ = GetRandomNumber(2500, 100)
    pX = pX + adX
    pY = pY + adY
    pZ = pZ + adZ
    pShip.SetTranslateXYZ(pX, pY, pZ)
    pShip.UpdateNodeOnly()

def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat

def ObjectExploding(pObject, pEvent):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return
        
    if (pShip.GetName() == "Dominion Prototype"):
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
    sText = "Prototype destroyed!!!\n\nWe should get out of here as soon as possible."
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
