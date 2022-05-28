# Xtended Mission

# by Smbw

import App
import MissionLib
import loadspacehelper
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXShips, DS9FXMissionLib, DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX.DS9FXAILib import DS9FXGenericEnemyAI, DS9FXStayAI
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict

pName = MissionIDs.MM21
sName = "Missing Ship"
sObjectives = "-Go to the Dosi-System\n-Scan for any traces of the starship"
sBriefing = "Captain, the USS Neptune is missing. The last known position is within the Dosi-System. You have to investigate the disappearance of the Neptune."
sModule = "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission21"

mSystems = ["DS9FXDosi1", "DS9FXTrialus1", "DS9FXYadera1"]
ShipIDs = []
ScanningDone = 0
KillDerelict = 0
pDerelictID = None

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
        Continue()

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

    pSystemName = pSet.GetName()
    if pSystemName == mSystems[0]:
        mSystems.pop(0)
        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
        
        if pSystemName == "DS9FXDosi1":
            ObjectiveTxt()
            StartScanning()
            iRand = GetRandomNumber(2, 0)
        elif pSystemName == "DS9FXYadera1":
            iRand = 2
            CreateDerelict()
        else:
            ObjectiveTxt2()
            StartScanning()
            iRand = GetRandomNumber(2, 0)

        if iRand != 2: # 33% chance of not creating attackers.
            time = GetRandomNumber(50, 5)
            MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateShips", App.g_kUtopiaModule.GetGameTime() + time, 0, 0)
        
        if mSystems == []:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def ObjectiveTxt():
    sText = "We need to scan the area for traces of the USS Neptune"
    iPos = 6
    iFont = 12
    iDur = 10
    iDelay = 10
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def ObjectiveTxt2():
    sText = "We need to scan the area..."
    iPos = 6
    iFont = 12
    iDur = 6
    iDelay = 10
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def CreateDerelict():
    global pDerelictID

    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    
    pDerelict = loadspacehelper.CreateShip(DS9FXShips.Galaxy, pSet, "Derelict", "Dummy Location")
    pDerelict = MissionLib.GetShip("Derelict", pSet) 
    pDerelict = App.ShipClass_Cast(pDerelict)
    pDerelict.SetAI(DS9FXStayAI.CreateAI(pDerelict))
    pX = pLocation.GetX()
    pY = pLocation.GetY()
    pZ = pLocation.GetZ()
    adX = GetRandomNumber(1500, 100)
    adY = GetRandomNumber(1500, 100)
    adZ = GetRandomNumber(1500, 100)
    pX = pX + adX
    pY = pY + adY
    pZ = pZ + adZ
    pDerelict.SetTranslateXYZ(pX, pY, pZ)
    pDerelict.UpdateNodeOnly()
    
    pDerelictID = pDerelict.GetObjID()
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DamageDerelict", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_REACTIVATED, pMission, __name__ + ".Derelict_Recovered")

    # Created with DamageTool (BC SDK):
    pDerelict.AddObjectDamageVolume(-1.254220, -0.303694, 0.121119, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(1.173486, 0.426941, 0.444825, 1.000000, 600.000000)
    pDerelict.AddObjectDamageVolume(0.352987, -1.400812, -0.342611, 1.000000, 600.000000)
    pDerelict.AddObjectDamageVolume(-0.247181, 0.324699, 0.482312, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(-0.503045, 0.852930, 0.567325, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(-0.772409, 1.431208, 0.617189, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(-1.247512, 1.902934, 0.585369, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(0.617727, 2.516571, 0.615892, 1.000000, 600.000000)
    pDerelict.AddObjectDamageVolume(0.651509, 2.509501, 0.193497, 1.000000, 600.000000)
    pDerelict.AddObjectDamageVolume(1.270166, -0.329782, -0.070574, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(1.289659, -0.265669, -0.064809, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(1.230930, -0.280894, -0.067703, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(-0.142219, 0.236569, -0.000235, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(-0.520779, -0.123577, -0.492664, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(-0.521914, 0.040732, -0.303841, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(1.472613, -1.343345, 0.079947, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(1.506255, -1.986563, 0.046544, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(-1.254567, 2.478717, 0.265232, 0.400000, 300.000000)
    pDerelict.AddObjectDamageVolume(-2.146938, 1.258922, 0.404303, 1.000000, 600.000000)
    pDerelict.AddObjectDamageVolume(-1.962142, 1.340794, 0.349728, 1.000000, 600.000000)
    pDerelict.AddObjectDamageVolume(-1.342126, -1.798727, 0.162724, 0.400000, 300.000000)

def DamageDerelict(pObject, pEvent):
    global pDerelictID, KillDerelict
    pDerelict = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pDerelictID))
    if not pDerelict:
        return 0

    LifeSupport_dict.dCrew[pDerelictID] = 0
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pDerelict)
    
    Properties = pDerelict.GetPropertySet()
    if not Properties:
        return 0

    Subsystems = Properties.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
    if not Subsystems:
        return 0

    Subsystems.TGBeginIteration()
    for i in range(Subsystems.TGGetNumItems()):
        if not pDerelictID:
            return 0
        pSysProp = App.SubsystemProperty_Cast(Subsystems.TGGetNext().GetProperty())
        pSystem = pDerelict.GetSubsystemByProperty(pSysProp)
        if pSystem:
            if KillDerelict != 1:
                MaxCond = pSystem.GetMaxCondition()
                iRand = GetRandomNumber(74, 1)
                NewCond = (float(iRand) / 75.0) * MaxCond
                if NewCond < 1.0:
                    NewCond = 1.0
                pSystem.SetCondition(NewCond)
            else:
                pDerelictID = None
                pDerelict.DestroySystem(pSystem)

    Subsystems.TGDoneIterating()
    Subsystems.TGDestroy()
    DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
    GoHomeTxt()
    

def Derelict_Recovered(pObject, pEvent):
    global pDerelictID, KillDerelict

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return 0
        
    if pShip.GetObjID() == pDerelictID:
        KillDerelict = 1
        DamageDerelict(None, None)

def CreateShips(pObject = None, pEvent = None):
    global ShipIDs
    
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

    iRand = GetRandomNumber(5, 2)
    for i in range(1, iRand):
        sShip = "Atacker " + str(i)
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
        ShipIDs.append(pShip.GetObjID())

def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat

def StartScanning():
    iRand = GetRandomNumber(120, 60)
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".StopScanning", App.g_kUtopiaModule.GetGameTime() + iRand, 0, 0)

    sText = "Scanning Area..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def StopScanning(pObject, pEvent):
    global ScanningDone
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    ScanningDone = 1
    Continue()
    
def Continue():
    global ScanningDone, ShipIDs
    if ShipIDs == [] and ScanningDone == 1:
        ScanningDone = 0
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        mSystem_len = len(mSystems)
        if mSystem_len == 2:
            HintTxt()
        elif mSystem_len == 1:
            HintTxt2()

def HintTxt():
    sText = "We have detected a warptrail which most likely originated from a Federation vessel. It's leading to the Trialus-System."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 4
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def HintTxt2():
    sText = "We're getting anomalous energy readings\ncomming from the outskirts of the Yadera-System."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 4
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def GoHomeTxt():
    sText = "Captain, we located the remains of the USS Neptune\nWe can't determin the cause of the destruction\nWe'll have to wait for the examination of the data recorders\n\nWe should return to DS9."
    iPos = 4
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
    try:
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_REACTIVATED, pMission, __name__ + ".Derelict_Recovered")
    except:
        pass
    try:
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
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
