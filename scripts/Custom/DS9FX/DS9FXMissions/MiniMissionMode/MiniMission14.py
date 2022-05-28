# Xtended Mission

# by Smbw

import App
import MissionLib
import loadspacehelper
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXShips, DS9FXMissionLib, DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

pName = MissionIDs.MM14
sName = "Patrol"
sObjectives = "-Go to the Trialus-System\n-Patrol the Vandros-System\n-Secure the Karemma-System"
sBriefing = "The Dominion is planning an assault on DS9. Captain, we need you to patrol near the border. Destroy any enemy ships!"
sModule = "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission14"

ShipIDs = []
mSystems = ["DS9FXTrialus1", "DS9FXVandros1", "DS9FXKaremma1"]

def Briefing():
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)

def MissionInitiate():
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

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
    global ShipIDs, mSystems

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    pPlayer = MissionLib.GetPlayer()
      
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return

    pShipID = pShip.GetObjID()
        
    if pShipID == pPlayer.GetObjID():
        FailedTxt()
        RemoveHandlers()

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    elif pShipID in ShipIDs:
        ShipIDs.remove(pShipID)
        if ShipIDs == [] and mSystems == []:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")

            GoHomeTxt()

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
    global mSystems
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

    pSetName = pSet.GetName()
    if pSetName in mSystems:
        ObjectiveTxt()
        CreateShips()
        mSystems.remove(pSetName)
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def ObjectiveTxt():
    sText = "Captain, we need to destroy the enemy ships!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def CreateShips():
    global ShipIDs
    
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pSetName = pSet.GetName()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

    if pSetName == "DS9FXTrialus1":
        for i in range(1, 6):
            sShip = "Attacker " + str(i)
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
            ShipIDs.append(pShip.GetObjID())

        for i in range(6, 9):
            sShip = "Attacker " + str(i)
            pShip = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, sShip, "Dummy Location")
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
            ShipIDs.append(pShip.GetObjID())

    elif pSetName == "DS9FXVandros1":
        for i in range(1, 5):
            sShip = "Attacker " + str(i)
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
            ShipIDs.append(pShip.GetObjID())

        for i in range(5, 7):
            sShip = "Attacker " + str(i)
            pShip = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, sShip, "Dummy Location")
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
            ShipIDs.append(pShip.GetObjID())

        for i in range(7, 11):
            sShip = "Attacker " + str(i)
            pShip = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, sShip, "Dummy Location")
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
            ShipIDs.append(pShip.GetObjID())

    elif pSetName == "DS9FXKaremma1":
        for i in range(1, 4):
            sShip = "Attacker " + str(i)
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
            ShipIDs.append(pShip.GetObjID())

        for i in range(4, 7):
            sShip = "Attacker " + str(i)
            pShip = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, sShip, "Dummy Location")
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
            ShipIDs.append(pShip.GetObjID())

        sShip = "Attacker 7"
        pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, sShip, "Dummy Location")
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
        ShipIDs.append(pShip.GetObjID())

def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat

def GoHomeTxt():
    sText = "Ok, seems like we're done here.\n\nWe should return to DS9."
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
        RemoveHandlers()

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

def RemoveHandlers():
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")        
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    except:
        pass
    
def CrewLost():
    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        FailedTxt()
        RemoveHandlers()
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass
