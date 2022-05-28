# Xtended Mission

# by Smbw

import App
import MissionLib
import loadspacehelper
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXShips, DS9FXMissionLib, DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX.DS9FXAILib import DS9FXGenericEnemyAI, DS9FXGenericFriendlyAI

pName = MissionIDs.MM20
sName = "Scan"
sObjectives = "-Go to the Trialus-System\n-Scan the Planet Meridian\n-Return the results to DS9"
sBriefing = "Captain, we need you to scan the planet Meridian in the Trialus-System for us. Return the results as soon as possible."
sModule = "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission20"

ShipIDs = []

def Briefing():
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)

def MissionInitiate():
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")    

def DisableDS9FXMenuButtons(pObject, pEvent):
    try:
        bHail = DS9FXMenuLib.GetSubMenuButton("Hail DS9", "Helm", "DS9FX", "DS9 Options...")
        bHail.SetDisabled()
    except:
        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

def ObjectExploding(pObject, pEvent):
    global ShipIDs

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
        if ShipIDs == []:
            pCondition = App.ConditionScript_Create("Conditions.ConditionPlayerOrbitting", "ConditionPlayerOrbitting", "Meridian")
            MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "StartScanning", pCondition)
            
            ObjectiveTxt2()

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
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return

    if not pPlayer.GetObjID() == pShip.GetObjID():
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    if pSet.GetName() == "DS9FXTrialus1":
        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
        ObjectiveTxt()
        CreateShips()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def ObjectiveTxt():
    sText = "Captain, we need to help destroying the renegade dominion\n forces bevore we're able to scan Meridian!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def CreateShips():
    global ShipIDs
    
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

    for i in range(1, 13):
        sShip = "Renegade " + str(i)
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
        DamageShip(pShip)

    for i in range(1, 3):
        sShip = "Defender " + str(i)
        pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, sShip, "Dummy Location")
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
        DamageShip(pShip)

    for i in range(3, 6):
        sShip = "Defender " + str(i)
        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Dummy Location")
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
        DamageShip(pShip)

def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat

def DamageShip(pShip):
    Properties = pShip.GetPropertySet()
    if not Properties:
        return 0

    Subsystems = Properties.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
    if not Subsystems:
        return 0

    Subsystems.TGBeginIteration()

    for i in range(Subsystems.TGGetNumItems()):
        pSysProp = App.SubsystemProperty_Cast(Subsystems.TGGetNext().GetProperty())
        pSystem = pShip.GetSubsystemByProperty(pSysProp)
        if pSystem:
            DisPerc = pSystem.GetDisabledPercentage()
            MaxCond = pSystem.GetMaxCondition()
            
            DisCond = MaxCond * DisPerc
            MaxDmgCond = DisCond - (DisCond * 0.15) # 'Worst Case' new condition
            MaxDmgCond2 = MaxCond * 0.5
            if MaxDmgCond < MaxDmgCond2:
                MaxDmgCond = MaxDmgCond2
                
            iRand = GetRandomNumber(99, 1) # Random number from 1 to 100
            Dmg = ((float(iRand) / 100.0) ** 2) * (MaxCond - MaxDmgCond)

            NewCond = float(MaxCond - Dmg)
            pSystem.SetCondition(NewCond)

    Subsystems.TGDoneIterating()
    Subsystems.TGDestroy()

def ObjectiveTxt2():
    sText = "Now we should be able to scan Meridian if we stay in orbit."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def StartScanning(bInOrbit):
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "StartScanning")
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".StopScanning", App.g_kUtopiaModule.GetGameTime() + 30, 0, 0)
    Scanning()
    
def Scanning():
    sText = "Scanning Meridian..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 10
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def StopScanning(pObject, pEvent):
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
    DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
    GoHomeTxt()

def GoHomeTxt():
    sText = "Scan complete.\n\nWe should return to DS9."
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
    try:
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "StartScanning")
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
