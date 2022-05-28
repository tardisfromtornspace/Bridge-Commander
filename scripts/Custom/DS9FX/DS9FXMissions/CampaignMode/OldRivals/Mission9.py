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
pName = MissionIDs.ORM8
sName = "Elevation"
sObjectives = "-Go to Idran system\n-Defeat any enemy Borg ships trying to go through the wormhole"
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission9"
sProgress  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\OldRivals\\Save\\MissionState.py"
pShipType = None
lDominion = ["Dreadnought", "Escort 1", "Escort 2", "Escort 3"]
lFederation = ["USS Icarus", "USS Tungsten", "USS Aberdeen", "USS Wanderer"]
sBorg = "Borg Cube"

ET_YES = App.UtopiaModule_GetNextEventType()
ET_NO = App.UtopiaModule_GetNextEventType()

def Briefing():
    global pPlayerName, sBriefing
    pPlayerName = App.g_kUtopiaModule.GetCaptainName().GetCString()
    sBriefing = "Stardate 64840.32\n\nCaptain " + str(pPlayerName) + " good job with the Klingons, I would have tried to be more diplomatic instead but these are strange times and we need all the help we can get.\n\nDeep Space 9 is on the highest alert as of today. We've lost contact with our Gamma Quadrant scout task force and we know they encountered a Borg Cube. We are presuming that the Cube is headed for Idran and it is likely that more Borg ships will follow in the future, we are not absolutely certain about that however because we don't know the state the Borg is in.\n\nWhat's important is that we focus on here and now. We've assembled as many ships as we can to aid you Captain. We hope that it is enough for you to defeat the Cube.\n\nGodspeed Captain!"
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)
    
def MissionInitiate():
    global pShipType
    
    SetupPlayer()
    
    pPlayer = MissionLib.GetPlayer()
    pShipType = DS9FXLifeSupportLib.GetShipType(pPlayer)

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
    
def CreateFriendlies():
    global lFederation
    lTypes = [DS9FXShips.Galaxy, DS9FXShips.Nebula, DS9FXShips.Miranda, DS9FXShips.Miranda]
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyFollowAI
    iLen = len(lFederation)
    for i in range(0, iLen):
        sShip = lFederation[i]
        sType = lTypes[i]
        pShip = loadspacehelper.CreateShip(sType, pSet, sShip, "FriendlyPos1")            
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
    
    if pSet.GetName() == "GammaQuadrant1":
        DominionText()
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateDominion", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DeleteDominion", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DominionPrompt", App.g_kUtopiaModule.GetGameTime() + 40, 0, 0)
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def DominionText():
    sText = "I'm detecting Dominion ships in the distance sir... they are hailing us..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def CreateDominion(pObject, pEvent):
    global lDominion
    lTypes = [DS9FXShips.DomBC, DS9FXShips.Bugship, DS9FXShips.Bugship, DS9FXShips.Bugship]
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyFollowAI
    iLen = len(lDominion)
    for i in range(0, iLen):
        sShip = lDominion[i]
        sType = lTypes[i]
        pShip = loadspacehelper.CreateShip(sType, pSet, sShip, "Location 1")            
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetFriendlyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyFollowAI.CreateAI(pShip))
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
        
def DeleteDominion(pObject, pEvent):
    lGamma = ["Bugship 1", "Bugship 2", "Bugship 3"]
    pPlayer = MissionLib.GetPlayer()
    if pPlayer:
        pSet = pPlayer.GetContainingSet()
        if pSet:
            for s in lGamma:
                try:
                    pSet.DeleteObjectFromSet(s)
                except:
                    pass  

def DominionPrompt(pObject, pEvent):
    sTitle = "Dominion Communication"
    sText = "We know that you will attempt to engage the Borg ship, we would like to join you to help clean up the mess we helped create. Will you allow us?"
    SetupModalDialog(sTitle, sText)    
    
def SetupModalDialog(sTitle, sText):    
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    pOptionsWindow.AddPythonFuncHandlerForInstance(ET_YES, __name__ + ".Yes")
    pOptionsWindow.AddPythonFuncHandlerForInstance(ET_NO, __name__ + ".No")
    
    import MainMenu.mainmenu
    App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])
    
    pModalDialogWindow = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MODAL_DIALOG))
    
    pEvent1 = App.TGStringEvent_Create()
    pEvent1.SetEventType(ET_YES)
    pEvent1.SetString("DS9FXYES")
    pEvent1.SetDestination(pOptionsWindow)
    
    pEvent2 = App.TGStringEvent_Create()
    pEvent2.SetEventType(ET_NO)
    pEvent2.SetString("DS9FXNO")
    pEvent2.SetDestination(pOptionsWindow)
    
    pTitle = App.TGString(sTitle)
    pText = App.TGString(sText)
    pOpt1 = App.TGString("Yes")
    pOpt2 = App.TGString("No")
    
    pModalDialogWindow.Run(pTitle, pText, pOpt1, pEvent1, pOpt2, pEvent2)
    
def Yes(pObject, pEvent):
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    pOptionsWindow.RemoveHandlerForInstance(ET_YES, __name__ + ".Yes")
    pOptionsWindow.RemoveHandlerForInstance(ET_NO, __name__ + ".No")
    
    PrepareForBorg()
    
    if pObject and pEvent:
            pObject.CallNextHandler(pEvent)        

def No(pObject, pEvent):
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    pOptionsWindow.RemoveHandlerForInstance(ET_YES, __name__ + ".Yes")
    pOptionsWindow.RemoveHandlerForInstance(ET_NO, __name__ + ".No")
    
    PrepareForBorg(0)
    
    if pObject and pEvent:
            pObject.CallNextHandler(pEvent)

def PrepareForBorg(bCanStay = 1):
    if not bCanStay:
        global lDominion
        pPlayer = MissionLib.GetPlayer()
        if pPlayer:
            pSet = pPlayer.GetContainingSet()
            if pSet:
                for s in lDominion:
                    try:
                        pSet.DeleteObjectFromSet(s)
                    except:
                        pass
    
    BorgText()
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".BorgTimer", App.g_kUtopiaModule.GetGameTime() + 25, 0, 0)

def BorgText():
    sText = "Borg ship incoming in 30 seconds sir..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 3
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def BorgTimer(pObject, pEvent):
    global sBorg
    s = sBorg
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    pLocation = pPlayer.GetWorldLocation()
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    pShip = loadspacehelper.CreateShip(DS9FXShips.BorgCube, pSet, s, "Location 1")
    DS9FXLifeSupportLib.ClearFromGroup(s)
    pMission.GetEnemyGroup().AddName(s)
    pShip = MissionLib.GetShip(s, pSet) 
    pShip = App.ShipClass_Cast(pShip)
    pX = pLocation.GetX()
    pY = pLocation.GetY()
    pZ = pLocation.GetZ()
    adX = GetRandomNumber(1000, 2000)
    adY = GetRandomNumber(1000, 2000)
    adZ = GetRandomNumber(1000, 2000)
    pX = pX + adX
    pY = pY + adY
    pZ = pZ + adZ
    pShip.SetTranslateXYZ(pX, pY, pZ)
    pShip.UpdateNodeOnly()
    
def ObjectExploding(pObject, pEvent):
    global sBorg
    
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if (pShip == None):
            if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
            return
    
    if pShip.GetName() == sBorg:
            GoHomeTxt()
            CleanUp()
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
    sText = "Borg Cube destroyed, we should get back to DS9!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 3
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def CleanUp():
    pPlayer = MissionLib.GetPlayer()
    if pPlayer:
        pSet = pPlayer.GetContainingSet()
        if pSet:
            for s in lDominion:
                try:
                    pSet.DeleteObjectFromSet(s)
                except:
                    pass    

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
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".RemoveShips", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
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
    
def RemoveShips(pObject, pEvent):
    global lFederation
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    for s in lFederation:
        try:
            pSet.DeleteObjectFromSet(s)
        except:
            pass

def SaveProgress():
    global pShipType
    if not pShipType:
        return
    from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Save import MissionState
    reload(MissionState)
    if MissionState.OnMission > 10:
        i = MissionState.OnMission
    else:
        i = 10
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