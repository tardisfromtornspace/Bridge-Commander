# Xtended Mission

# by Smbw

import App
import MissionLib
import loadspacehelper
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXShips, DS9FXMissionLib, DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXAILib import DS9FXStayAI, DS9FXGenericFriendlyFollowAI, DS9FXGenericEnemyAI
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict

pName = MissionIDs.MM17
sName = "Recover Derelict"
sObjectives = "-Go to the Kurill-System\n-Recover Derelict\n-Safely return the Derelict to DS9"
sBriefing = "Starfleet Intelligence informed us about a Derilect which they want us to recover. This mission has top priority! Secure the unkown ship right away!"
sModule = "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission17"

pDerelictID = None
ShipIDs = []

def Briefing():
    # Interactively tell the user that he cannot play the mission and why
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
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()    
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".Create_Derelict")

def DisableDS9FXMenuButtons(pObject, pEvent):
    try:
        bHail = DS9FXMenuLib.GetSubMenuButton("Hail DS9", "Helm", "DS9FX", "DS9 Options...")
        bHail.SetDisabled()
    except:
        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

def ObjectExploding(pObject, pEvent):
    global pDerelictID, ShipIDs

    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    pPlayer = MissionLib.GetPlayer()
      
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return

    pShipID = pShip.GetObjID()
        
    if pShipID == pPlayer.GetObjID():
        pDerelictID = None
        FailedTxt()
        RemoveHandlers()

        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    elif pShipID == pDerelictID:
        pDerelictID = None
        LostDerelict()
        RemoveHandlers()

        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

    elif (pShipID in ShipIDs) and ShipIDs != []:
        ShipIDs.remove(pShipID)
        if ShipIDs == []:
            GoHomeTxt2()
            DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def FailedTxt():
    sText = "Mission Failed!"
    iPos = 6
    iFont = 12
    iDur = 6
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def LostDerelict():
    sText = "The Derelict has been destroyed. Mission Failed!"
    iPos = 2
    iFont = 12
    iDur = 6
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def Create_Derelict(pObject, pEvent):
    global pDerelictID
    
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer.GetObjID() == pShip.GetObjID():
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    pSet = pPlayer.GetContainingSet()

    if pSet.GetName() == "DS9FXKurill1":
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pLocation = pPlayer.GetWorldLocation()

        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
        ObjectiveTxt()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".Create_Derelict")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_REACTIVATED, pMission, __name__ + ".Derelict_Recovered")

        pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, "Derelict", "Dummy Location")
        pShip = MissionLib.GetShip("Derelict", pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(DS9FXStayAI.CreateAI(pShip))
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
        AddVisibleDamage(pShip)
        pDerelictID = pShip.GetObjID()
        
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".AdjustLifeSupport", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
        
        
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def AddVisibleDamage(pThingToDamage): # Created by DamageTool (BC SDK)
    pThingToDamage.AddObjectDamageVolume(-0.994152, -2.993623, 0.662763, 0.400000, 300.000000)
    pThingToDamage.AddObjectDamageVolume(-0.395798, -0.065835, -0.045254, 1.000000, 600.000000)
    pThingToDamage.AddObjectDamageVolume(1.010385, 0.134555, -0.214279, 1.000000, 600.000000)
    pThingToDamage.AddObjectDamageVolume(-0.010486, 1.299560, -0.129306, 0.400000, 300.000000)
    pThingToDamage.AddObjectDamageVolume(0.991783, -1.566548, 0.732074, 0.400000, 300.000000)
    pThingToDamage.AddObjectDamageVolume(-1.686000, -0.677968, -0.232400, 0.400000, 300.000000)
    pThingToDamage.AddObjectDamageVolume(-2.433885, -0.794993, -0.607659, 1.000000, 600.000000)
    pThingToDamage.AddObjectDamageVolume(-0.023906, -2.128467, 0.428931, 0.400000, 300.000000)
    pThingToDamage.AddObjectDamageVolume(2.464945, 1.647501, -0.641771, 0.400000, 300.000000)
    pThingToDamage.AddObjectDamageVolume(0.647501, -2.309343, -0.196577, 0.400000, 300.000000)
    pThingToDamage.AddObjectDamageVolume(0.481983, 2.182763, -0.305179, 0.400000, 300.000000)

def ObjectiveTxt():
    sText = "Captain, we need to recover the wreck!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def AdjustLifeSupport(pObject, pEvent): # Didn't work for when used in Create_Derelict() (guess: overwritten elsewhere?)
    global pDerelictID
    
    pDerelict = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pDerelictID))
    LifeSupport_dict.dCrew[pDerelictID] = 0
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pDerelict)
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".AddSystemDamage", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)

def AddSystemDamage(pObject, pEvent):    
    global pDerelictID
    
    pDerelict = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pDerelictID))
    Properties = pDerelict.GetPropertySet()
    if not Properties:
        return 0

    Subsystems = Properties.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
    if not Subsystems:
        return 0

    Subsystems.TGBeginIteration()

    for i in range(Subsystems.TGGetNumItems()):
        pSysProp = App.SubsystemProperty_Cast(Subsystems.TGGetNext().GetProperty())
        pSystem = pDerelict.GetSubsystemByProperty(pSysProp)
        if pSystem:
            DisPerc = pSystem.GetDisabledPercentage()
            MaxCond = pSystem.GetMaxCondition()
            DisCond = MaxCond * DisPerc

            NewCond = MaxCond - GetRandomNumber(int(MaxCond - DisCond), 0)            
            pSystem.SetCondition(NewCond)

    Subsystems.TGDoneIterating()
    Subsystems.TGDestroy()

def Derelict_Recovered(pObject, pEvent):
    global pDerelictID

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return 0

    if pShip.GetObjID() == pDerelictID:
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_REACTIVATED, pMission, __name__ + ".Derelict_Recovered")
        
        SetpAI()
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        GoHomeTxt()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".Create_Attackers")
    
def SetpAI(): # Nearly the same than AdjustLifeSupport() except for the AI...
    global pDerelictID
    
    if pDerelictID == None:
        return
    
    pDerelict = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pDerelictID))
    if not pDerelict:
        return
    
    pDerelict.SetAI(DS9FXGenericFriendlyFollowAI.CreateAI(pDerelict))

def GoHomeTxt():
    sText = "Ok, seems like we're done here.\n\nWe should return to DS9."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 15
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def Create_Attackers(pObject, pEvent):
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer.GetObjID() == pShip.GetObjID():
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return

    pSet = pPlayer.GetContainingSet()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    
    if pSet.GetName() == "GammaQuadrant1":
        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
        ObjectiveTxt2()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".Create_Derelict")
        CreateShips()

    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def CreateShips():
    global ShipIDs
    
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

    sShip = "Attacker 1"
    pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, sShip, "Dummy Location")
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

    for i in range(2, 6):
        sShip = "Attacker " + str(i)
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

def ObjectiveTxt2():
    sText = "Captain, we need to protect the Derelict!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 12
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def GoHomeTxt2():
    sText = "Now let's return to DS9 befor more enmies enter the area..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 3
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def MissionEnd(pObject, pEvent):    
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pShip = App.ShipClass_Cast(pEvent.GetDestination())

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
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".Create_Derelict")
    except:
        pass
    try:
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".Create_Attackers")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_REACTIVATED, pMission, __name__ + ".Derelict_Recovered")
    except:
        pass
    
def CrewLost():
    global pDerelictID
    try:
        pDerelictID = None
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        FailedTxt()
        RemoveHandlers()
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass
