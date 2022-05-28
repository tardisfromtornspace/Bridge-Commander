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
sShips = []
pPaneID = App.NULL_ID
pName = MissionIDs.HM5
sName = "The Way of the Warrior"
sObjectives = "-Take control of DS9\n-Hold off the Klingon ships until reinforcements arrive"
sBriefing = "The Klingons have withdrawn from the Khitomer Accords after we have found out about their plans to invade Cardassia. The Klingon fleet which was briefly stationed here is turning against us. Take control of the DS9 to repel the invaders. You only need to hold them off until Federation Starships can arrive."

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

        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: The Way of the Warrior"), 0.0, 0.0, None, 1, 0.30, 0.30, kColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, kColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, kColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, kColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Take control of DS9\n-Hold off the Klingon ships until reinforcements arrive"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("The Klingons have withdrawn from the Khitomer Accords after we have found out about their plans to invade Cardassia. The Klingon fleet which was briefly stationed here is turning against us. Take control of the DS9 to repel the invaders. You only need to hold them off until Federation Starships can arrive."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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

        pAction = LineAction("Mission: The Way of the Warrior", pPane, 3, 6, 16)
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

def MissionInitiate(pObject, pEvent):        
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        try:
                pSet.DeleteObjectFromSet("USS Excalibur")
        except:
                pass
        try:
                pSet.DeleteObjectFromSet("USS Defiant")
        except:
                pass
        try:
                pSet.DeleteObjectFromSet("USS Oregon")
        except:
                pass
        try:
                pSet.DeleteObjectFromSet("USS_Lakota")
        except:
                pass

        SetupPlayer()

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

        MissionSetup()

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
        pPlayer = MissionLib.GetPlayer()
        pPlayerName = pPlayer.GetName()
        pSet = pPlayer.GetContainingSet()
        pSet.DeleteObjectFromSet(pPlayerName)

        GetPlayer = MissionLib.GetShip('Deep_Space_9', pSet)

        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(GetPlayer)

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

                FailedTxt(None, None)
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")

                DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
                DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def CrewLost():
        try:
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                FailedTxt(None, None)
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")            
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")                
                DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
                DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
        except:
                pass

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

def MissionSetup():
        global sShips

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        pPlayer = MissionLib.GetPlayer().GetName()
        pSet = MissionLib.GetPlayer().GetContainingSet()

        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                if kShip.GetName() == pPlayer:
                        continue
                elif kShip.GetName() == 'Bajoran Wormhole':
                        continue
                elif kShip.GetName() == 'Comet Alpha':
                        continue
                else:
                        pSet.DeleteObjectFromSet(kShip.GetName())

        sShips = ["IKS TuQmeh", "IKS Jawbogh", "IKS NabVad", "IKS Qu'ta'Dl'Hegh", "IKS QumHa'bogh", "IKS Qochbe'meH", "IKS QuSmey", "IKS Dotlh", "IKS Vuplu'bejnes", "IKS Qo'Joh", "IKS Satlho'Qu'tlh", "IKS IwwIj'ay'Hom"]  

        SpawnShips()

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")

def SpawnShips():
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, "IKS TuQmeh", "FriendlyPos1")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("IKS TuQmeh")
        pMission.GetEnemyGroup().AddName("IKS TuQmeh")

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        ship1 = MissionLib.GetShip("IKS TuQmeh", pSet)

        pship1 = App.ShipClass_Cast(ship1)

        pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship1))


        loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, "IKS Jawbogh", "FriendlyPos2")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("IKS Jawbogh")
        pMission.GetEnemyGroup().AddName("IKS Jawbogh")

        ship2 = MissionLib.GetShip("IKS Jawbogh", pSet)

        pship2 = App.ShipClass_Cast(ship2)

        pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship2))


        loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, "IKS NabVad", "FriendlyPos3")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("IKS NabVad")
        pMission.GetEnemyGroup().AddName("IKS NabVad")

        ship3 = MissionLib.GetShip("IKS NabVad", pSet)

        pship3 = App.ShipClass_Cast(ship3)

        pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship3))


        loadspacehelper.CreateShip(DS9FXShips.Ktinga, pSet, "IKS Qu'ta'Dl'Hegh", "FriendlyPos4")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("IKS Qu'ta'Dl'Hegh")
        pMission.GetEnemyGroup().AddName("IKS Qu'ta'Dl'Hegh")

        ship4 = MissionLib.GetShip("IKS Qu'ta'Dl'Hegh", pSet)

        pship4 = App.ShipClass_Cast(ship4)

        pship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship4))

        loadspacehelper.CreateShip(DS9FXShips.Ktinga, pSet, "IKS QumHa'bogh", "FriendlyPos5")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("IKS QumHa'bogh")
        pMission.GetEnemyGroup().AddName("IKS QumHa'bogh")

        ship5 = MissionLib.GetShip("IKS QumHa'bogh", pSet)

        pship5 = App.ShipClass_Cast(ship5)

        pship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship5))

        Att1 = "IKS Qochbe'meH"
        pAtt1 = loadspacehelper.CreateShip(DS9FXShips.Vorcha, pSet, Att1, "EnemyPos1")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att1)
        pMission.GetEnemyGroup().AddName(Att1)

        Attacker1 = MissionLib.GetShip("IKS Qochbe'meH", pSet) 

        pAttacker1 = App.ShipClass_Cast(Attacker1)

        pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

        Att2 = "IKS QuSmey"
        pAtt2 = loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, Att2, "EnemyPos2")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att2)
        pMission.GetEnemyGroup().AddName(Att2)

        Attacker2 = MissionLib.GetShip("IKS QuSmey", pSet) 

        pAttacker2 = App.ShipClass_Cast(Attacker2)

        pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

        Att3 = "IKS Dotlh"
        pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Neghvar, pSet, Att3, "EnemyPos3")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att3)
        pMission.GetEnemyGroup().AddName(Att3)


        Attacker3 = MissionLib.GetShip("IKS Dotlh", pSet) 

        pAttacker3 = App.ShipClass_Cast(Attacker3)

        pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

        Att4 = "IKS Vuplu'bejnes"
        pAtt4 = loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, Att4, "EnemyPos4")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att4)
        pMission.GetEnemyGroup().AddName(Att4)

        Attacker4 = MissionLib.GetShip("IKS Vuplu'bejnes", pSet) 

        pAttacker4 = App.ShipClass_Cast(Attacker4)

        pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

        Att5 = "IKS Qo'Joh"
        pAtt5 = loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, Att5, "EnemyPos5")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att5)
        pMission.GetEnemyGroup().AddName(Att5)

        Attacker5 = MissionLib.GetShip("IKS Qo'Joh", pSet) 

        pAttacker5 = App.ShipClass_Cast(Attacker5)

        pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

        Att6 = "IKS Satlho'Qu'tlh"
        pAtt6 = loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, Att6, "EnemyPos6")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att6)
        pMission.GetEnemyGroup().AddName(Att6)

        Attacker6 = MissionLib.GetShip("IKS Satlho'Qu'tlh", pSet) 

        pAttacker6 = App.ShipClass_Cast(Attacker6)

        pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))

        Att7 = "IKS IwwIj'ay'Hom"
        pAtt7 = loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, Att7, "EnemyPos7")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att7)
        pMission.GetEnemyGroup().AddName(Att7)

        Attacker7 = MissionLib.GetShip("IKS IwwIj'ay'Hom", pSet) 

        pAttacker7 = App.ShipClass_Cast(Attacker7)

        pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))

def ObjectExploding(pObject, pEvent):
        global sShips
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        ShipName = pShip.GetName()

        if (ShipName in sShips):        
                sShips.remove(ShipName)

                if (len(sShips) == 3):
                        from Custom.DS9FX.DS9FXObjects import DS9Ships
                        DS9Ships.DS9SetShips()

                        ReenableAllButtons()
                        RemoveShips()
                        RestoreToDefault()
                        MissionWin(None, None)
            
                        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")                        

                        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def RemoveShips():
        global sShips
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        for ship in sShips:
                pSet.DeleteObjectFromSet(ship)

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
                bDock = DS9FXMenuLib.GetSubMenuButton("Dock To DS9", "Helm", "DS9FX", "DS9 Options...")

                bDock.SetEnabled()

        except:

                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

        try:
                Custom.DS9FX.DS9FXmain.RestoreWarpButton()

        except:
                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

def MissionWin(pObject, pEvent):
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(WinSequence(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def WinSequence(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Federation support has arrived sir!\n\nMission Completed!", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 10)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)


def RestoreToDefault():
        pShip = DS9FXShips.Galaxy

        pPlayer = MissionLib.GetPlayer()
        pPlayerName = pPlayer.GetName()
        pName = "Player"
        pSet = pPlayer.GetContainingSet()
        pSet.DeleteObjectFromSet(pPlayerName)

        loadspacehelper.CreateShip(pShip, pSet, pName, "Player Start")
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(pName)
        pMission.GetFriendlyGroup().AddName(pName)

        GetPlayer = MissionLib.GetShip(pName, pSet)

        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(GetPlayer)

        from Custom.DS9FX.DS9FXObjects import DS9Stations

        DS9Stations.DS9SetStations()

def KillPane(pAction):
        global pPaneID

        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
        App.g_kRootWindow.DeleteChild(pPane)

        pPaneID = App.NULL_ID

        return 0

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
