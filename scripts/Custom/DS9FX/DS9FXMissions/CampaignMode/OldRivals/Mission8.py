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
sName = "Trepidation"
sObjectives = "-Go to Qo'nos system\n-Negotiate an alliance with Klingons\n-Return to DS9"
sBriefing = ""
sModule = "Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Mission8"
sProgress  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\OldRivals\\Save\\MissionState.py"
pShipType = None
iAction = 0
iStep = 0

ET_EV1 = App.UtopiaModule_GetNextEventType()
ET_EV2 = App.UtopiaModule_GetNextEventType()

def Briefing():
    global pPlayerName, sBriefing
    reload(DS9FXSavedConfig)
    if not DS9FXSavedConfig.QonosPlanets == 1:
        PlanetsTxt()
        return     
    if DS9FXSavedConfig.KlingonSide != 1:
        KlingonsText()
        return      
    pPlayerName = App.g_kUtopiaModule.GetCaptainName().GetCString()
    sBriefing = "Stardate 64818.29\n\nCaptain " + str(pPlayerName) + " we now know that Borg is behind these attacks. Starfleet is on the highest alert. Aside from us, the Romulans are the only ones with enough military strength to currently defend Alpha quadrant, unfortunately they are in a state of civil war. Which leaves us in a vulnerable state.\n\nWe are mobilizing all our ships and fleets as we are not sure if this is a prelude to an invasion or this is an isolated incident. We've never been fully sure if the the Borg actually ever fully recovered from the losses Admiral Janeway inflicted to the Collective.\n\nCaptain, you've been given a mission of vital importance, Klingons are still rebuilding their Military but we need their help. Your orders are simple: go to Klingon Homeworld and negotiate Military support from the Klingons.\n\nThis won't be a simple task Captain, as Klingons have suffered much in the Dominion war and in recent years our relations have strained due to Nemesis incident and our later negotiations of a more permanent alliance with the Romulans. Give it your best Captain.\n\nUsually this mission would fall to someone with a diplomatic background but you know that Klingons respect warriors and lately you've made a name for yourself, we're certain that Klingons would be more open to you."
    DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)
    
def PlanetsTxt():
    sText = "Planets in Qo'nos system are not turned on..."
    iPos = 3
    iFont = 12
    iDur = 6
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def KlingonsText():
    sText = "Klingons are currently set as enemy..."
    iPos = 3
    iFont = 12
    iDur = 6
    iDelay = 0
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def MissionInitiate():
    global pShipType, iAction, iStep
    
    iAction = 0
    iStep = 0
    
    SetupPlayer()
    
    pPlayer = MissionLib.GetPlayer()
    pShipType = DS9FXLifeSupportLib.GetShipType(pPlayer)

    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    
    pCondition = App.ConditionScript_Create("Conditions.ConditionPlayerOrbitting", "ConditionPlayerOrbitting", "Qo'nos")
    MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "InOrbit", pCondition)
    
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
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
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
    
    if pSet.GetName() == "DS9FXQonos1":
        ObjectiveTxt() 
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def ObjectiveTxt():
    sText = "We should enter Qo'nos's orbit sir to begin negotiating..."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 20
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def InOrbit(bInOrbit):
    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
    Notify()
    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DelayNegotiations", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)
    
def Notify():
    sText = "Stanby... You Federation types think you can gain\nour trust by sending a warrior to do the bidding... pathetic!"
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 10
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def DelayNegotiations(pObject, pEvent):
    sTitle = "Transported to surface"
    sText = "You've transported yourself to the Qo'nos surface. As soon as you transport you are challenged by a Klingon warrior. Do you accept his challenge to the death?"
    sAction1 = "Accept challenge"
    sAction2 = "Decline challenge"
    iCorrect = 1
    SetupModalDialog(sTitle, sText, sAction1, sAction2, iCorrect)
    
def SetupModalDialog(sTitle, sText, sAction1, sAction2, iCorrect):
    global iAction
    
    iAction = iCorrect
    
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    pOptionsWindow.AddPythonFuncHandlerForInstance(ET_EV1, __name__ + ".Action1")
    pOptionsWindow.AddPythonFuncHandlerForInstance(ET_EV2, __name__ + ".Action2")
    
    import MainMenu.mainmenu
    App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])
    
    pModalDialogWindow = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MODAL_DIALOG))
    
    pEvent1 = App.TGStringEvent_Create()
    pEvent1.SetEventType(ET_EV1)
    pEvent1.SetString("DS9FXEV1")
    pEvent1.SetDestination(pOptionsWindow)
    
    pEvent2 = App.TGStringEvent_Create()
    pEvent2.SetEventType(ET_EV2)
    pEvent2.SetString("DS9FXEV2")
    pEvent2.SetDestination(pOptionsWindow)
    
    pTitle = App.TGString(sTitle)
    pText = App.TGString(sText)
    pOpt1 = App.TGString(sAction1)
    pOpt2 = App.TGString(sAction2)
    
    if sAction2 == "":
        pModalDialogWindow.Run(pTitle, pText, pOpt1, pEvent1, None, None)
    else:
        pModalDialogWindow.Run(pTitle, pText, pOpt1, pEvent1, pOpt2, pEvent2)
    
def Action1(pObject, pEvent):
    global iAction
    
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    pOptionsWindow.RemoveHandlerForInstance(ET_EV1, __name__ + ".Action1")
    pOptionsWindow.RemoveHandlerForInstance(ET_EV2, __name__ + ".Action2")
    
    i = 1
    if i == iAction:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Correct", App.g_kUtopiaModule.GetGameTime() + 3, 0, 0)
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Incorrect", App.g_kUtopiaModule.GetGameTime() + 3, 0, 0)

    if pObject and pEvent:
            pObject.CallNextHandler(pEvent)        

def Action2(pObject, pEvent):
    global iAction
    
    pTopWindow = App.TopWindow_GetTopWindow()
    pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

    pOptionsWindow.RemoveHandlerForInstance(ET_EV1, __name__ + ".Action1")
    pOptionsWindow.RemoveHandlerForInstance(ET_EV2, __name__ + ".Action2")
    
    i = 2
    if i == iAction:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Correct", App.g_kUtopiaModule.GetGameTime() + 3, 0, 0)
    else:
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Incorrect", App.g_kUtopiaModule.GetGameTime() + 3, 0, 0)

    if pObject and pEvent:
            pObject.CallNextHandler(pEvent)

def Correct(pObject, pEvent):
    global iStep
    iStep = iStep + 1
    if iStep == 1:
        sTitle = "Won the challenge"
        sText = "You've defeated the Klingon warrior in the challenge. Do you spare his life or kill him?"
        sAction1 = "Kill"
        sAction2 = "Spare"
        iCorrect = 1
        SetupModalDialog(sTitle, sText, sAction1, sAction2, iCorrect)
    elif iStep == 2:
        sTitle = "Killed Klingon"
        sText = "By Killing the Klingon you've shown yourself to be a true Klingon in heart. Several Klingons gather around you, what do you do next?\n\nOption 1 = Say that you were only defending yourself\nOption 2 = Say that he was without honor"
        sAction1 = "Option 1"
        sAction2 = "Option 2"
        iCorrect = 2
        SetupModalDialog(sTitle, sText, sAction1, sAction2, iCorrect)
    elif iStep == 3:
        sTitle = "Indeed he had no honor"
        sText = "In the gathered crowd is one Klingon Ambassador who is quite impressed by your actions. He offers to escort you to address the Klingon houses. Do you accept his offer?"
        sAction1 = "Accept offer"
        sAction2 = "Decline offer"
        iCorrect = 2
        SetupModalDialog(sTitle, sText, sAction1, sAction2, iCorrect)
    elif iStep == 4:
        sTitle = "You can find your way on your own"
        sText = "You've finally found your way to the Chambers. Klingons give you a chance to speak why they should give you military support.\n\nOption 1 = Say that the Federation was always there for them\nOption 2 = Say if they don't, they are all cowards"
        sAction1 = "Option 1"
        sAction2 = "Option 2"
        iCorrect = 2
        SetupModalDialog(sTitle, sText, sAction1, sAction2, iCorrect)
    elif iStep == 5:
        sTitle = "Klingons are shocked"
        sText = "Many of the present Klingons want to kill you for saying that. Finally after some unrest order is restored, you are given a chance to take back your words, you being human after all. What do you say to that?\n\nOption 1 = Question current state of Klingon Empire\nOption 2 = Stand by your statement"
        sAction1 = "Option 1"
        sAction2 = "Option 2"
        iCorrect = 1
        SetupModalDialog(sTitle, sText, sAction1, sAction2, iCorrect)
    elif iStep == 6:
        sTitle = "Klingons ask you to elaborate"
        sText = "Klingons ask you to explain yourself.\n\nOption 1 = You explain to the Klingons that ever since the Dominion War they seem to the others like they are afraid of conflict and this is their chance to show to the rest that they are still warriors\nOption 2 = Tell to the Klingons that it was a mistake for you to come and ask their help. Klingons are nothling like they used to be and Federation doesn't need their help anyway. Glory is for the Federation alone."
        sAction1 = "Option 1"
        sAction2 = "Option 2"
        iCorrect = 2
        SetupModalDialog(sTitle, sText, sAction1, sAction2, iCorrect)
    elif iStep == 7:
        sTitle = "You are halted"
        sText = "Klingons are quite impressed by your perfomance and promise you to send ships to DS9 when its needed. You can now go back to your ship."
        sAction1 = "Return to Ship"
        sAction2 = ""
        iCorrect = 1
        SetupModalDialog(sTitle, sText, sAction1, sAction2, iCorrect)
    elif iStep == 8:
        SetupEnding()
    
def Incorrect(pObject, pEvent):
    global iStep
    iStep = 0
    DelayNegotiations(None, None)
    
def SetupEnding():
    sText = "We should get back to DS9 sir."
    iPos = 6
    iFont = 12
    iDur = 12
    iDelay = 15
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()    
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
    
    App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
    
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
            MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
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
    iDelay = 15
    DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)
    
def SaveProgress():
    global pShipType
    if not pShipType:
        return
    from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals.Save import MissionState
    reload(MissionState)
    if MissionState.OnMission > 9:
        i = MissionState.OnMission
    else:
        i = 9
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
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "InOrbit")
        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
    except:
        pass