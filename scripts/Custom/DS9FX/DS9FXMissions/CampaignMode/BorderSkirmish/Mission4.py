# by USS Sovereign: DS9FX v3.0 Mission


# Imports
import App
import loadspacehelper
import MissionLib
import Custom.DS9FX.DS9FXmain
import nt
import string
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLib import DS9FXShips
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig


# Events
ET_ACCEPT = App.UtopiaModule_GetNextEventType()
ET_DECLINE = App.UtopiaModule_GetNextEventType()
ET_BACK = App.UtopiaModule_GetNextEventType()

# Vars
pPane = None
pMainPane = None
pPlayerShipType = None
RenegadeShips = []
pPaneID = App.NULL_ID
pTimer1 = None
pTimer2 = None
pTimer3 = None
pTimer4 = None
pTimer5 = None
pTimer6 = None
pName = MissionIDs.BSM4
sName = "Revenge Is A Dish Best Served Cold"
sObjectives = "-Repel Dominion ships\n-Survive"
sBriefing = "Things have gone from bad to worse, Captain. The destruction of the White facility was not the big victory we expected it to be. The Founders have dispatched a wing of ships to help you find and destroy them. Ah, there they are..."

# Path where we should save a mission progress py file
Path  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\BorderSkirmish\\Save\\mission5.py"

def Briefing():
        global pMainPane, pPane

        if not pPane == None:
                Decline(None, None)
                return

        pPane = App.TGPane_Create(1.0, 1.0) 
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(pPane, 0, 0) 
        pMainPane = App.TGPane_Create(0.60, 0.65) 
        pPane.AddChild(pMainPane, 0.22, 0.12)

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_DECLINE, pMission, __name__ + ".Decline")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_BACK, pMission, __name__ + ".ShowMissionMenu")

        CreateEntries(None, None)

def CreateEntries(pObject, pEvent):
        global pMainPane, pPane

        kColor = App.TGColorA() 
        kColor.SetRGBA(1, 0.81, 0.41, 1.0)

        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: Revenge Is A Dish Best Served Cold"), 0.0, 0.0, None, 1, 0.30, 0.30, kColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, kColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, kColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, kColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Repel Dominion ships\n-Survive"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("Things have gone from bad to worse, Captain. The destruction of the White facility was not the big victory we expected it to be. The Founders have dispatched a wing of ships to help you find and destroy them. Ah, there they are..."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pBriefingWindow.AddChild(pText, 0, 0.01)

        CreateRandomIcon(pIconWindow)

        kNormalColor = App.TGColorA() 
        kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
        kHilightedColor = App.TGColorA() 
        kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
        kDisabledColor = App.TGColorA() 
        kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

        x = 0
        y = 0.01
        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_ACCEPT)
        pEvent.SetString("Accepting")
        pButton = App.STRoundedButton_CreateW(App.TGString("Accept Mission"), pEvent, 0.13125, 0.034583)
        pButton.SetNormalColor(kNormalColor)
        pButton.SetHighlightedColor(kHilightedColor)
        pButton.SetSelectedColor(kNormalColor)
        pButton.SetDisabledColor(kDisabledColor)
        pButton.SetColorBasedOnFlags()
        pButtonWindow.AddChild(pButton, x, y)


        x = 0 + 0.2
        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_DECLINE)
        pEvent.SetString("Declining")
        pButton = App.STRoundedButton_CreateW(App.TGString("Decline Mission"), pEvent, 0.13125, 0.034583)
        pButton.SetNormalColor(kNormalColor)
        pButton.SetHighlightedColor(kHilightedColor)
        pButton.SetSelectedColor(kNormalColor)
        pButton.SetDisabledColor(kDisabledColor)
        pButton.SetColorBasedOnFlags()
        pButtonWindow.AddChild(pButton, x, y)

        x = x + 0.2
        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_BACK)
        pEvent.SetString("BackToMissionSelectioMenu")
        pButton = App.STRoundedButton_CreateW(App.TGString("Select Another Mission"), pEvent, 0.13125, 0.034583)
        pButton.SetNormalColor(kNormalColor)
        pButton.SetHighlightedColor(kHilightedColor)
        pButton.SetSelectedColor(kNormalColor)
        pButton.SetDisabledColor(kDisabledColor)
        pButton.SetColorBasedOnFlags()
        pButtonWindow.AddChild(pButton, x, y)

        pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode() 
        pLCARS = pGraphicsMode.GetLcarsString() 
        pGlass = App.TGIcon_Create(pLCARS, 120) 
        pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight()) 
        pMainPane.AddChild(pGlass, 0, 0) 

        pIconWindow.InteriorChangedSize()
        pIconWindow.Layout()
        pObjectivesWindow.InteriorChangedSize()
        pObjectivesWindow.Layout()
        pBriefingWindow.InteriorChangedSize()
        pBriefingWindow.Layout()
        pButtonWindow.InteriorChangedSize()
        pButtonWindow.Layout()
        pMainPane.Layout()
        pPane.Layout()

        pTop = App.TopWindow_GetTopWindow()
        pTop.ForceTacticalVisible()

        pPane.SetVisible()

def CreateRandomIcon(pWindow):

        from Custom.DS9FX.DS9FXIconManager import IconManager

        IconManager.LoadDS9FX_Icons()

        pIcon = App.TGIcon_Create("DS9FX_Icons", App.SPECIES_UNKNOWN)
        pIcon.Resize(0.26, 0.25)
        pIcon.SetVisible()

        pSelection = GetRandomRate(1)
        pIcon.SetIconNum(pSelection)

        pWindow.AddChild(pIcon,0.01,0.01)

def GetRandomRate(iNumber):

        return App.g_kSystemWrapper.GetRandomNumber(16) + iNumber


def Decline(pObject, pEvent):
        global pMainPane, pPane

        try:
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()

                App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
                App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")
                App.g_kEventManager.RemoveBroadcastHandler(ET_BACK, pMission, __name__ + ".ShowMissionMenu")
        except:
                pass

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

        pTCW.DeleteChild(pPane)

        pPane = None

        pMainPane = None

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)


def Accept(pObject, pEvent):
        global pMainPane, pPane

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_Start(MissionLib.GetPlayer(), pName)

        try:
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()

                App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
                App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")
                App.g_kEventManager.RemoveBroadcastHandler(ET_BACK, pMission, __name__ + ".ShowMissionMenu")
        except:
                pass

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

        pTCW.DeleteChild(pPane)

        pPane = None

        pMainPane = None

        MissionTittle(None, None)

        MissionInitiate(None, None)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)


def ShowMissionMenu(pObject, pEvent):
        Decline(None, None)
        Custom.DS9FX.DS9FXmain.RecallMissionMenu()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def MissionTittle(pObject, pEvent):
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(TextSequence(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def TextSequence(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Mission: Revenge Is A Dish Best Served Cold", pPane, 3, 6, 16)
        pSequence.AddAction(pAction, None, 10)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def LineAction(sLine, pPane, fPos, duration, fontSize):
        i = string.find(sLine, "Mission:")
        if not i == 0:
                from Custom.DS9FX.DS9FXMissions import MissionStatus
                MissionStatus.AddLOGEntry(sLine)

        fHeight = fPos * 0.0375
        App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
        pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
        return pAction

def DisableDS9FXMenuButtons(pObject, pEvent):

        try:

                bHail = DS9FXMenuLib.GetSubMenuButton("Hail DS9", "Helm", "DS9FX", "DS9 Options...")

                bHail.SetDisabled()

        except:

                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

        try:
                bEnter = DS9FXMenuLib.GetSubMenuButton("Enter Wormhole", "Helm", "DS9FX", "Wormhole Options...")

                bEnter.SetDisabled()

        except:

                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

        try:

                Custom.DS9FX.DS9FXmain.DisableWarpButton()

        except:
                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())

def MissionInitiate(pObject, pEvent):
        global pPlayerShipType, RenegadeShips
        global pTimer1, pTimer2, pTimer3, pTimer4, pTimer5, pTimer6

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        SetupPlayer()

        pPlayer = MissionLib.GetPlayer()
        pPlayerShipType = GetShipType(pPlayer)

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        pTimer1 = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".SupportShipsIncoming", App.g_kUtopiaModule.GetGameTime() + 95, 0, 0)
        pTimer2 = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".SupportArriving", App.g_kUtopiaModule.GetGameTime() + 41, 0, 0)
        pTimer3 = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".firstEnemyWave", App.g_kUtopiaModule.GetGameTime() + 17, 0, 0)
        pTimer4 = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".secondEnemyWave", App.g_kUtopiaModule.GetGameTime() + 40, 0, 0)
        pTimer5 = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".thirdEnemyWave", App.g_kUtopiaModule.GetGameTime() + 293, 0, 0)
        pTimer6 = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".fourthEnemyWave", App.g_kUtopiaModule.GetGameTime() + 317, 0, 0)
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".DS9Exploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".DS9Exploding")

        RenegadeShips =	["Renegade 1", "Renegade 2", "Renegade 3", "Renegade 4", "Renegade 5", "Renegade 6", "Renegade 7", "Renegade 8", "Renegade 9", "Renegade 10", "Renegade 11", "Renegade 12", "Renegade 13", "Renegade 14", "Renegade 15", "Renegade 16", "Renegade 17", "Renegade 18", "Renegade 19", "Renegade 20"]

        PlayMissionMovies()

def PlayMissionMovies():
        pPlayer = MissionLib.GetPlayer()
        pPlayer.SetTarget(None)
        pTop = App.TopWindow_GetTopWindow()
        pTop.ForceBridgeVisible()
        pTop.ForceTacticalVisible()        

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.IntroVid == 1:
                if DS9FXSavedConfig.IntroMovieSel == "Random":
                        RandomSel = GetRandomNumberMovie()
                        if RandomSel < 33:
                                from Custom.DS9FX.DS9FXVids import DS9FXIntroVideo
                                DS9FXIntroVideo.PlayMovieSeq()
                        elif RandomSel < 66:
                                from Custom.DS9FX.DS9FXVids import DS9FXIntroVideoAlt
                                DS9FXIntroVideoAlt.PlayMovieSeq()
                        else:
                                from Custom.DS9FX.DS9FXVids import DS9FXXtendedIntroVid
                                DS9FXXtendedIntroVid.PlayMovieSeq()
                else:
                        strMovie = DS9FXSavedConfig.IntroMovieSel
                        from Custom.DS9FX.DS9FXVids import PlaySpecificVideo
                        PlaySpecificVideo.PlayMovieSeq(strMovie)
        else:
                pass

def GetRandomNumberMovie():
        return App.g_kSystemWrapper.GetRandomNumber(99) + 1


def SetupPlayer():
        import Save.mission4
        reload(Save.mission4)
        pShip = Save.mission4.Ship

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


def SupportShipsIncoming(pObject, pEvent):

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        loadspacehelper.CreateShip(DS9FXShips.Galaxy, pSet, "USS Antartica", "Help1")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("USS Antartica")
        pMission.GetFriendlyGroup().AddName("USS Antartica")

        import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

        ship1 = MissionLib.GetShip("USS Antartica", pSet) 

        pship1 = App.ShipClass_Cast(ship1)

        pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))

        loadspacehelper.CreateShip(DS9FXShips.Miranda, pSet, "USS Washington", "Help2")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("USS Washington")
        pMission.GetFriendlyGroup().AddName("USS Washington")

        ship2 = MissionLib.GetShip("USS Washington", pSet) 

        pship2 = App.ShipClass_Cast(ship2)

        pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship2))

        loadspacehelper.CreateShip(DS9FXShips.Defiant, pSet, "USS Avenger", "Help3")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("USS Avenger")
        pMission.GetFriendlyGroup().AddName("USS Avenger")

        ship3 = MissionLib.GetShip("USS Avenger", pSet) 

        pship3 = App.ShipClass_Cast(ship3)

        pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship3))


def firstEnemyWave(pObject, pEvent):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
        pSequence = App.TGSequence_Create()
        pSet = App.g_kSetManager.GetSet("bridge")
        pTactical = App.CharacterClass_GetObject(pSet, "Tactical")
        pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "EnemiesEnteringTheSet", None, 0, Database))
        pSequence.Play()

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        Att1 = "Renegade 1"
        pAtt1 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att1, "Random 1 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att1)
        pMission.GetEnemyGroup().AddName(Att1)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker1 = MissionLib.GetShip("Renegade 1", pSet) 

        pAttacker1 = App.ShipClass_Cast(Attacker1)

        pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

        Att2 = "Renegade 2"
        pAtt2 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att2, "Random 2 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att2)
        pMission.GetEnemyGroup().AddName(Att2)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker2 = MissionLib.GetShip("Renegade 2", pSet) 

        pAttacker2 = App.ShipClass_Cast(Attacker2)

        pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

        Att3 = "Renegade 3"
        pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att3, "Random 3 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att3)
        pMission.GetEnemyGroup().AddName(Att3)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker3 = MissionLib.GetShip("Renegade 3", pSet) 

        pAttacker3 = App.ShipClass_Cast(Attacker3)

        pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

        Att4 = "Renegade 4"
        pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "Random 4 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att4)
        pMission.GetEnemyGroup().AddName(Att4)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker4 = MissionLib.GetShip("Renegade 4", pSet) 

        pAttacker4 = App.ShipClass_Cast(Attacker4)

        pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

        Att5 = "Renegade 5"
        pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att5, "Random 5 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att5)
        pMission.GetEnemyGroup().AddName(Att5)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker5 = MissionLib.GetShip("Renegade 5", pSet) 

        pAttacker5 = App.ShipClass_Cast(Attacker5)

        pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

def secondEnemyWave(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        Att1 = "Renegade 6"
        pAtt1 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att1, "Random 1 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att1)
        pMission.GetEnemyGroup().AddName(Att1)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker1 = MissionLib.GetShip("Renegade 6", pSet) 

        pAttacker1 = App.ShipClass_Cast(Attacker1)

        pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

        Att2 = "Renegade 7"
        pAtt2 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att2, "Random 2 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att2)
        pMission.GetEnemyGroup().AddName(Att2)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker2 = MissionLib.GetShip("Renegade 7", pSet) 

        pAttacker2 = App.ShipClass_Cast(Attacker2)

        pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

        Att3 = "Renegade 8"
        pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att3, "Random 3 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att3)
        pMission.GetEnemyGroup().AddName(Att3)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker3 = MissionLib.GetShip("Renegade 8", pSet) 

        pAttacker3 = App.ShipClass_Cast(Attacker3)

        pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

        Att4 = "Renegade 9"
        pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "Random 4 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att4)
        pMission.GetEnemyGroup().AddName(Att4)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker4 = MissionLib.GetShip("Renegade 9", pSet) 

        pAttacker4 = App.ShipClass_Cast(Attacker4)

        pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


        Att5 = "Renegade 10"
        pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att5, "Random 5 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att5)
        pMission.GetEnemyGroup().AddName(Att5)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker5 = MissionLib.GetShip("Renegade 10", pSet) 

        pAttacker5 = App.ShipClass_Cast(Attacker5)

        pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))


def thirdEnemyWave(pObject, pEvent):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
        pSequence = App.TGSequence_Create()
        pSet = App.g_kSetManager.GetSet("bridge")
        pTactical = App.CharacterClass_GetObject(pSet, "Tactical")
        pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "EnemiesEnteringTheSet", None, 0, Database))
        pSequence.Play()

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        Att1 = "Renegade 11"
        pAtt1 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att1, "Random 1 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att1)
        pMission.GetEnemyGroup().AddName(Att1)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker1 = MissionLib.GetShip("Renegade 11", pSet) 

        pAttacker1 = App.ShipClass_Cast(Attacker1)

        pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

        Att2 = "Renegade 12"
        pAtt2 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att2, "Random 2 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att2)
        pMission.GetEnemyGroup().AddName(Att2)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker2 = MissionLib.GetShip("Renegade 12", pSet) 

        pAttacker2 = App.ShipClass_Cast(Attacker2)

        pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

        Att3 = "Renegade 13"
        pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att3, "Random 3 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att3)
        pMission.GetEnemyGroup().AddName(Att3)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker3 = MissionLib.GetShip("Renegade 13", pSet) 

        pAttacker3 = App.ShipClass_Cast(Attacker3)

        pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

        Att4 = "Renegade 14"
        pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "Random 4 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att4)
        pMission.GetEnemyGroup().AddName(Att4)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker4 = MissionLib.GetShip("Renegade 14", pSet) 

        pAttacker4 = App.ShipClass_Cast(Attacker4)

        pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

        Att5 = "Renegade 15"
        pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att5, "Random 5 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att5)
        pMission.GetEnemyGroup().AddName(Att5)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker5 = MissionLib.GetShip("Renegade 15", pSet) 

        pAttacker5 = App.ShipClass_Cast(Attacker5)

        pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

def fourthEnemyWave(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        Att1 = "Renegade 16"
        pAtt1 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att1, "Random 1 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att1)
        pMission.GetEnemyGroup().AddName(Att1)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker1 = MissionLib.GetShip("Renegade 16", pSet) 

        pAttacker1 = App.ShipClass_Cast(Attacker1)

        pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

        Att2 = "Renegade 17"
        pAtt2 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att2, "Random 2 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att2)
        pMission.GetEnemyGroup().AddName(Att2)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker2 = MissionLib.GetShip("Renegade 17", pSet) 

        pAttacker2 = App.ShipClass_Cast(Attacker2)

        pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

        Att3 = "Renegade 18"
        pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att3, "Random 3 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att3)
        pMission.GetEnemyGroup().AddName(Att3)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker3 = MissionLib.GetShip("Renegade 18", pSet) 

        pAttacker3 = App.ShipClass_Cast(Attacker3)

        pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


        Att4 = "Renegade 19"
        pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "Random 4 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att4)
        pMission.GetEnemyGroup().AddName(Att4)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker4 = MissionLib.GetShip("Renegade 19", pSet) 

        pAttacker4 = App.ShipClass_Cast(Attacker4)

        pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

        Att5 = "Renegade 20"
        pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att5, "Random 5 Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att5)
        pMission.GetEnemyGroup().AddName(Att5)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker5 = MissionLib.GetShip("Renegade 20", pSet) 

        pAttacker5 = App.ShipClass_Cast(Attacker5)

        pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))


def SupportArriving(pObject, pEvent):
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(SupportArrivingTxt(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def SupportArrivingTxt(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Help is on the way Sir!", pPane, 3, 10, 12)
        pSequence.AddAction(pAction, None, 0)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def GetShipType(pShip):
        if pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        return None


def ObjectExploding(pObject, pEvent):
        global RenegadeShips
        
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        ShipName = pShip.GetName()

        if (ShipName in RenegadeShips):

                RenegadeShips.remove(ShipName)

                if (len(RenegadeShips) == 0):
                        SaveProgress(None, None)
                        ReenableAllButtons()
                        HelpExiting(None, None)
                        MissionCompletedPrompt(None, None)
                        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")
                        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".DS9Exploding")
                        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".DS9Exploding")
                        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def HelpExiting(pObject, pEvent):
        pSet = MissionLib.GetPlayer().GetContainingSet()

        try:
                pSet.DeleteObjectFromSet("USS Antartica")
        except:
                pass
        try:
                pSet.DeleteObjectFromSet("USS Washington")
        except:
                pass
        try:
                pSet.DeleteObjectFromSet("USS Avenger")

        except:
                pass


def ReenableAllButtons():

        try:

                bHail = DS9FXMenuLib.GetSubMenuButton("Hail DS9", "Helm", "DS9FX", "DS9 Options...")

                bHail.SetEnabled()

        except:
                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

        try:
                bEnter = DS9FXMenuLib.GetSubMenuButton("Enter Wormhole", "Helm", "DS9FX", "Wormhole Options...")

                bEnter.SetEnabled()

        except:
                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

        try:
                Custom.DS9FX.DS9FXmain.RestoreWarpButton()

        except:
                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."


def MissionCompletedPrompt(pObject, pEvent):
        global pPaneID
        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(Completed(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def Completed(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Mission Completed!\n\nYou saved us all Captain!", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 5)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

def PlayerExploding(pObject, pEvent):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pPlayer = MissionLib.GetPlayer()
        pPlayeName = pPlayer.GetName()

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        ShipName = pShip.GetName()

        if (ShipName == pPlayeName):

                deleteptimers()
                FailedTxt(None, None)
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
                DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def CrewLost(): 
        try:
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                deleteptimers()
                FailedTxt(None, None)
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".DS9Exploding")                
                DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
                DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
        except:
                pass

def DS9Exploding(pObject, pEvent):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pPlayer = MissionLib.GetPlayer()
        pPlayeName = pPlayer.GetName()

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        ShipName = pShip.GetName()

        if (ShipName == "Deep_Space_9"):
                DS9FailedTxt(None, None)
                ReenableAllButtons()
                HelpExiting(None, None)
                deleteptimers()
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
                DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def FailedTxt(pObject, pEvent):
        global pPaneID
        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(Failed(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def Failed(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Mission Failed!", pPane, 6, 6, 12)
        pSequence.AddAction(pAction, None, 0)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()


def DS9FailedTxt(pObject, pEvent):
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(DS9Failed(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def DS9Failed(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Mission Failed!", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 0)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def SaveProgress(pObject, pEvent):
        global pPlayerShipType

        file = nt.open(Path, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "Ship = " + "'" + pPlayerShipType + "'")
        nt.close(file)

def KillPane(pAction):
        global pPaneID

        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
        App.g_kRootWindow.DeleteChild(pPane)

        pPaneID = App.NULL_ID

        return 0

def deleteptimers():
        deleteptimer1()
        deleteptimer2()
        deleteptimer3()
        deleteptimer4()
        deleteptimer5()
        deleteptimer6()

def deleteptimer1():
        global pTimer1

        try:
                App.g_kTimerManager.DeleteTimer(pTimer1.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(pTimer1.GetObjID())
                pTimer1 = None
        except:
                pass

def deleteptimer2():
        global pTimer2

        try:
                App.g_kTimerManager.DeleteTimer(pTimer2.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(pTimer2.GetObjID())
                pTimer2 = None
        except:
                pass

def deleteptimer3():
        global pTimer3

        try:
                App.g_kTimerManager.DeleteTimer(pTimer3.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(pTimer3.GetObjID())
                pTimer3 = None
        except:
                pass

def deleteptimer4():
        global pTimer4

        try:
                App.g_kTimerManager.DeleteTimer(pTimer4.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(pTimer4.GetObjID())
                pTimer4 = None
        except:
                pass

def deleteptimer5():
        global pTimer5

        try:
                App.g_kTimerManager.DeleteTimer(pTimer5.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(pTimer5.GetObjID())
                pTimer5 = None
        except:
                pass

def deleteptimer6():
        global pTimer6

        try:
                App.g_kTimerManager.DeleteTimer(pTimer6.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(pTimer6.GetObjID())
                pTimer6 = None
        except:
                pass

def Quit():
        global pMainPane, pPane

        if not pPane == None:

                try:
                        pGame = App.Game_GetCurrentGame()
                        pEpisode = pGame.GetCurrentEpisode()
                        pMission = pEpisode.GetCurrentMission()

                        App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
                        App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")
                        App.g_kEventManager.RemoveBroadcastHandler(ET_BACK, pMission, __name__ + ".ShowMissionMenu")
                except:
                        pass

                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

                App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

                pTCW.DeleteChild(pPane)

                pPane = None
