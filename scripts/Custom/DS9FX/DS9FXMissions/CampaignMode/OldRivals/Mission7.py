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
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

pPlayerName = ""
pName = MissionIDs.ORM7
sName = "Humdrum"
sObjectives = "-Go to Yadera system\n-Investigate the system further"
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission7"
sProgress  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\OldRivals\\Save\\MissionState.py"
pShipType = None
lDestroyed = []
iTime = 0
bCreated = 0

def Briefing():
    global pPlayerName, sBriefing
    pPlayerName = App.g_kUtopiaModule.GetCaptainName().GetCString()
    sBriefing = "Stardate 64796.48\n\nCaptain " + str(pPlayerName) + " these are some disturbing news. Dominion Warship was destroyed by an unknown weapon signature, we have never seen anything like it Captain. For this very reason we need you Captain to return to Yadera system and do a complete sweep of the system. We must get more clues to determine what we're dealing with here.\n\nGood luck Captain!"
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)
    
def MissionInitiate():
    global pShipType, lDestroyed, iTime, bCreated
    
    lDestroyed = ["Wreckage 1", "Wreckage 2", "Wreckage 3", "Wreckage 4", "Wreckage 5"]
    iTime = 0
    bCreated = 0

    SetupPlayer()
    
    pPlayer = MissionLib.GetPlayer()
    pShipType = DS9FXLifeSupportLib.GetShipType(pPlayer)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")    
    
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
    
def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat
    
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
    
    if pSet.GetName() == "DS9FXYadera1":
        ObjectiveTxt()
        SetupMissionSpecific()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def ObjectiveTxt():
    sText = "Sir, the original Dominion wreckage is missing...\nI am however detecting wreckage of several more Dominion ships.\nWe should scan them all."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def SetupMissionSpecific():
    global lDestroyed
    for s in lDestroyed:
        SetupCondition(s)
        CreateWreckage(s)
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DamageShip", App.g_kUtopiaModule.GetGameTime() + 3, 0, 0)
    
def SetupCondition(s):
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()    
    pPlayer = MissionLib.GetPlayer()
    DistanceCheckCondition = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 150, pPlayer.GetName(), s)
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InRange", DistanceCheckCondition)    
    
def CreateWreckage(s):
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, s, "Dummy Location")
    DS9FXLifeSupportLib.ClearFromGroup(s)
    pMission.GetNeutralGroup().AddName(s)
    pShip = MissionLib.GetShip(s, pSet) 
    pShip = App.ShipClass_Cast(pShip)
    pX = pLocation.GetX()
    pY = pLocation.GetY()
    pZ = pLocation.GetZ()
    adX = GetRandomNumber(2000, 4000)
    adY = GetRandomNumber(2000, 4000)
    adZ = GetRandomNumber(2000, 4000)
    pX = pX + adX
    pY = pY + adY
    pZ = pZ + adZ
    pShip.SetTranslateXYZ(pX, pY, pZ)
    pShip.UpdateNodeOnly()

def DamageShip(pObject, pEvent):
    global lDestroyed
    
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return
    
    for s in lDestroyed:
        pDerelict = MissionLib.GetShip(s, pSet)
        if not pDerelict:
            continue
        pID = pDerelict.GetObjID()
        LifeSupport_dict.dCrew[pID] = 0
        DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pDerelict)
    
        pDerelict.AddObjectDamageVolume(-0.346769, 0.505777, 0.211104, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.391424, 0.292077, 0.136891, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.480019, 0.478436, 0.055110, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.491906, -0.009849, 0.036503, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.410636, -0.320572, 0.163709, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.033209, -0.662447, 0.254643, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.088509, -1.154540, 0.234934, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.273566, -1.192976, 0.216826, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.311354, -0.558230, 0.230304, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.222401, 0.425513, 0.261027, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.059797, 0.854007, 0.315946, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.056210, 1.548879, 0.118923, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.010570, 1.840008, -0.062665, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.004918, 1.929916, -0.118732, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.001939, 1.938382, -0.123910, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.255125, 1.524279, -0.107981, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.340457, 0.871074, 0.058321, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.000847, 1.163047, 0.295946, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.447814, 0.288307, 0.028379, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.234699, 0.027302, 0.259706, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.335636, -1.328933, 0.166836, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.347983, -0.744068, 0.144445, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.532026, 0.467509, -0.147177, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.482553, -0.298320, -0.226326, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.351669, -0.343077, -0.383422, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.278125, 0.289238, -0.398746, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.178232, 1.112100, -0.162443, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.134755, 0.889398, -0.217919, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.205823, 0.698926, -0.398746, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.296626, 1.243148, -0.134832, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.126445, 1.415870, -0.158072, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.067971, -0.037120, -0.398747, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.149664, 0.196479, -0.398746, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.121442, -0.420599, -0.398748, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.147468, -0.721491, -0.003603, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.034781, -0.636699, -0.041525, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.103933, -1.060943, -0.001106, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.072679, -1.187713, -0.001000, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(-0.037587, -1.391599, -0.000836, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.128441, 0.075653, -0.398749, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.128440, 0.075653, -0.398747, 0.400000, 300.000000)
        pDerelict.AddObjectDamageVolume(0.071726, 0.209187, -0.398747, 0.400000, 300.000000)
    
        pProperties = pDerelict.GetPropertySet()
        if not pProperties:
            return 0
    
        pSubsystems = pProperties.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
        if not pSubsystems:
            return 0
    
        pSubsystems.TGBeginIteration()
        for i in range(pSubsystems.TGGetNumItems()):
            pSysProp = App.SubsystemProperty_Cast(pSubsystems.TGGetNext().GetProperty())
            pSystem = pDerelict.GetSubsystemByProperty(pSysProp)
            if pSystem:
                pRand = GetRandomNumber(15, 15)
                pRand = float(pRand) / 100.0
                pSystem.SetConditionPercentage(pRand)
                pProp = pSystem.GetProperty()
                if pProp:
                    pProp.SetDisabledPercentage(2.0)
        pSubsystems.TGDoneIterating()
        pSubsystems.TGDestroy()
    
def InRange(bInRange):
    global lDestroyed
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return
    lToRemove = []
    for s in lDestroyed:
        pShip = MissionLib.GetShip(s, pSet)
        if not pShip:
            continue
        pDist = DistanceCheck(pShip)
        if pDist < 200:
            lToRemove.append(s)
    for s in lToRemove:
        lDestroyed.remove(s)
    if len(lDestroyed) == 0:
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InRange")
        NotifyDone()
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ScanComplete", App.g_kUtopiaModule.GetGameTime() + 30, 0, 0)
    else:
        MoreToScan()

def DistanceCheck(pObject):
    try:
        pPlayer = App.Game_GetCurrentGame().GetPlayer()
        vDifference = pObject.GetWorldLocation()
        vDifference.Subtract(pPlayer.GetWorldLocation())
        return vDifference.Length()
    except:
        return 5000
    
def NotifyDone():
    sText = "Sir, I've scanned all the wreckages...\nStand by...\nI'm detecting an incoming ship on long range sensors!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 5
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def ScanComplete(pObject, pEvent):
    PowerDownNow()
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".WarpInTimer", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
    
def MoreToScan():
    global lDestroyed
    i = 0
    sShips = ""
    for s in lDestroyed:
        if i == 0:
            sShips = s
        else:
            sShips = sShips + ", " + s
        i = i + 1
    sText = "Scan of the ship is complete...\nWe still have more wreckages to scan: " + sShips
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 5
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def PowerDownNow():
    sText = "BORG! Sir, we must power down our ship now.\nMaybe it'll mistake us for wreckages.\nWe must hurry!!!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def WarpInTimer(pObject, pEvent):
    global iTime, bCreated
    iTime = iTime + 1
    if not bCreated:
        pTime = 20 - iTime
        if pTime >= 1:
            ShowTime(str(pTime))
        bLevel = ProbePlayerPowerSettings()
        if bLevel:
            PowerDownPrompt()
        if iTime > 20:
            CreateBorg(bLevel)
            NotifyBorg(bLevel)
            iTime = 0
            if bLevel:
                return
    else:
        pTime = 60 - iTime
        if pTime >= 1 and pTime <= 55:
            ShowTime(str(pTime))
        bLevel = ProbePlayerPowerSettings()
        if bLevel:
            SetBorgAI()
            NotifyBorg(bLevel)
            return
        if iTime > 60:
            try:
                pSet = MissionLib.GetPlayer().GetContainingSet()
                pSet.DeleteObjectFromSet("Borg Tactical Cube")
            except:
                pass        
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission() 
            MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MissionSuccessText", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
            DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
            return
    
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".WarpInTimer", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
    
def ShowTime(s):
    sText = "Time: " + s
    iPos = 4
    iFont = 12
    fDur = 0.95
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, fDur, iDelay)
    
def ProbePlayerPowerSettings():
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0
    lLevels = [pPlayer.GetImpulseEngineSubsystem(), pPlayer.GetShields(), pPlayer.GetSensorSubsystem(), pPlayer.GetPhaserSystem(), pPlayer.GetTorpedoSystem(), pPlayer.GetPulseWeaponSystem()]
    for pSys in lLevels:
        if pSys:
            if pSys.IsOn():
                return 1
    return 0

def PowerDownPrompt():
    sText = "Power not reduced to 0%."
    iPos = 8
    iFont = 12
    iDur = 0.95
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def CreateBorg(bLevel):
    global bCreated
    bCreated = 1
    s = "Borg Tactical Cube"
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    pShip = loadspacehelper.CreateShip(DS9FXShips.BorgTacticalCube, pSet, s, "Dummy Location")
    DS9FXLifeSupportLib.ClearFromGroup(s)
    pMission.GetEnemyGroup().AddName(s)
    pShip = MissionLib.GetShip(s, pSet) 
    pShip = App.ShipClass_Cast(pShip)
    pX = pLocation.GetX()
    pY = pLocation.GetY()
    pZ = pLocation.GetZ()
    adX = GetRandomNumber(1000, 3000)
    adY = GetRandomNumber(1000, 3000)
    adZ = GetRandomNumber(1000, 3000)
    pX = pX + adX
    pY = pY + adY
    pZ = pZ + adZ
    pShip.SetTranslateXYZ(pX, pY, pZ)
    pShip.UpdateNodeOnly()
    if not bLevel:
        pShip.ClearAI()

def NotifyBorg(bLevel):
    if bLevel:
        sText = "Borg has detected us sir, we have no choice but to fight now sir."
    else:
        sText = "It doesn't look like it has detected us sir. We should remain like this."
    iPos = 6
    iFont = 12
    iDur = 3
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def SetBorgAI():
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return
    pSet = pPlayer.GetContainingSet()
    if not pSet:
        return
    from Custom.DS9FX.DS9FXAILib import DS9FXBorgAI
    pShip = MissionLib.GetShip("Borg Tactical Cube", pSet)
    if not pShip:
        return
    pShip.SetAI(DS9FXBorgAI.CreateAI(pShip, "Friendly"))
    
def MissionSuccessText(pObject, pEvent):
    sText = "Sir, the Borg ship has warped out.\nWe must report this back to DS9 as soon as possible."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 1
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def ObjectExploding(pObject, pEvent):    
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return
    
    if pShip.GetName() == "Borg Tactical Cube":
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
    sText = "Sir, we must report this encounter to DS9 as soon as possible!!!"
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
        SaveProgress()
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
    
def SaveProgress():
    global pShipType
    if not pShipType:
        return
    from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Save import MissionState
    reload(MissionState)
    if MissionState.OnMission > 8:
        i = MissionState.OnMission
    else:
        i = 8
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
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")        
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass
