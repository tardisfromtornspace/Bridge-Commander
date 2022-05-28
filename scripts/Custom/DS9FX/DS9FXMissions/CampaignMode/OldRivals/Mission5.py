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
pName = MissionIDs.ORM5
sName = "The Mission Continues"
sObjectives = "-Go to New Bajor\n-Take orbit of New Bajor Colony and allow for resupply to take place"
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission5"
sProgress  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\OldRivals\\Save\\MissionState.py"
pShipType = None
iTime = 0

def Briefing():
    global pPlayerName, sBriefing
    pPlayerName = App.g_kUtopiaModule.GetCaptainName().GetCString()
    sBriefing = "Stardate 64763.50\n\nCaptain " + str(pPlayerName) + " that was an excellent job on the last mission. We are sure we won't have any more troubles in the future regarding this, all thanks to you. We will be recommending you for a medal.\n\nWe are now resuming business as usual. Your mission is to go to New Bajor system and orbit the Colony there to resupply it. Don't worry this will all be done automatically by your crew. You just sit and relax and enjoy the ride, you've most certainly earned it! Good luck Captain!"
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)
    
def MissionInitiate():
    global pShipType

    SetupPlayer()
    
    pPlayer = MissionLib.GetPlayer()
    pShipType = DS9FXLifeSupportLib.GetShipType(pPlayer)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    
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
    
    if pSet.GetName() == "DS9FXNewBajor1":
        ObjectiveTxt()
        SetupConditionScript()
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def ObjectiveTxt():
    sText = "I recommend we get into orbit of\nNew Bajor Colony as soon as possible sir."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def SetupConditionScript():
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()    
    pCondition = App.ConditionScript_Create("Conditions.ConditionPlayerOrbitting", "ConditionPlayerOrbitting", "New Bajor Colony")
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InOrbit", pCondition)
    
def InOrbit(bInOrbit):
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
    TransferingSuppliesText()
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".TransferComplete", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0) 
    
def TransferingSuppliesText():
    sText = "Transfer of supplies is in progress sir.\nPlease remain in orbit for the time being..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 5
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def TransferComplete(pObject, pEvent):
    TransferCompleteText()
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".WarpIn", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)
    
def TransferCompleteText():
    sText = "Transfer of supplies is complete sir..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 5
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def WarpIn(pObject, pEvent):
    global iTime
    iTime = 0
    CreateWarship()
    NotifyPresence()
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".StartTheClock", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
    
def CreateWarship():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, "Unknown Dominion Warship", "Dummy Location")
    DS9FXLifeSupportLib.ClearFromGroup("Unknown Dominion Warship")
    pMission.GetNeutralGroup().AddName("Unknown Dominion Warship")
    pShip = MissionLib.GetShip("Unknown Dominion Warship", pSet) 
    pShip = App.ShipClass_Cast(pShip)
    pX = pLocation.GetX()
    pY = pLocation.GetY()
    pZ = pLocation.GetZ()
    adX = GetRandomNumber(1000, 14000)
    adY = GetRandomNumber(1000, 14000)
    adZ = GetRandomNumber(1000, 14000)
    pX = pX + adX
    pY = pY + adY
    pZ = pZ + adZ
    pShip.SetTranslateXYZ(pX, pY, pZ)
    pShip.UpdateNodeOnly()
    
def NotifyPresence():
    sText = "Sir a Dominion Warship has just warped in and\nis not responding to hails. We should check it out.\nWe have just under 360 seconds to take a scan of it.\nWe must get within 500 km range to take a scan!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 1
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def GetRandomNumber(iNum, iStat):
    return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat
    
def StartTheClock(pObject, pEvent):
    global iTime
    iTime = iTime + 1
    
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()    
    pShip = MissionLib.GetShip("Unknown Dominion Warship", pSet)
    pDistance = DistanceCheck(pShip)
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()      
    if pDistance <= 3000:
        try:
            pSet.DeleteObjectFromSet("Unknown Dominion Warship")
        except:
            pass        
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MissionSuccessText", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        return
    if iTime >= 360:
        try:
            pSet.DeleteObjectFromSet("Unknown Dominion Warship")
        except:
            pass
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MissionFailedText", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
        return
    
    ShowElapsedTime()
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".StartTheClock", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

def DistanceCheck(pObject):
    try:
        pPlayer = App.Game_GetCurrentGame().GetPlayer()
        vDifference = pObject.GetWorldLocation()
        vDifference.Subtract(pPlayer.GetWorldLocation())
        return vDifference.Length()
    except:
        return 5000
    
def MissionSuccessText(pObject, pEvent):
    sText = "And not a moment too soon sir.\nI've managed to get a partial scan of the ship.\nWe should report this to DS9 sir!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 1
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def MissionFailedText(pObject, pEvent):
    sText = "Damn, the ship got away. I was unable to scan it. Mission Failed!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 1
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)    
    
def ShowElapsedTime():
    global iTime
    sText = "Time: " + str(iTime)
    iPos = 4
    iFont = 12
    fDur = 0.95
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, fDur, iDelay)
    
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
    if MissionState.OnMission > 6:
        i = MissionState.OnMission
    else:
        i = 6
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
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass
    