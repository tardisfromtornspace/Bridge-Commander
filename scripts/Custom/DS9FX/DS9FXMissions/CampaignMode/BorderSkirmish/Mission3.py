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
pPaneID = App.NULL_ID
pName = MissionIDs.BSM3
sName = "A Time To Fight"
sObjectives = "-Head to the Gamma Quadrant\n-Destroy enemy base"
sBriefing = "The Klingons and Romulans have dispatched a contigent of their ships to DS9. You are ordered to take command of the taskforce, head to the Gamma Quadrant and put an end to that base once and for all."

# Path where we should save a mission progress py file
Path  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\BorderSkirmish\\Save\\mission4.py"

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

        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: A Time To Fight"), 0.0, 0.0, None, 1, 0.30, 0.30, kColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, kColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, kColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, kColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Head to the Gamma Quadrant\n-Destroy enemy base"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("The Klingons and Romulans have dispatched a contigent of their ships to DS9. You are ordered to take command of the taskforce, head to the Gamma Quadrant and put an end to that base once and for all."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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

        pAction = LineAction("Mission: A Time To Fight", pPane, 3, 6, 16)
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

                Custom.DS9FX.DS9FXmain.DisableWarpButton()


        except:

                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

def MissionInitiate(pObject, pEvent):
        global pPlayerShipType

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        SetupPlayer()

        pPlayer = MissionLib.GetPlayer()
        pPlayerShipType = GetShipType(pPlayer)

        SpawnSupportShips()

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

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

def MissionStart(pObject, pEvent):

        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        if (pSet.GetName() == "GammaQuadrant1"):

                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableEnterButton", App.g_kUtopiaModule.GetGameTime() + 7, 0, 0)


                Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
                GammaSet = Gamma.GetSet()

                Bug1 = "Bugship 4"
                pBug1 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug1, "Bugship 4 Mission Location")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Bug1)
                pMission.GetEnemyGroup().AddName(Bug1)

                import Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI

                Bugship1 = MissionLib.GetShip(Bug1, GammaSet) 

                pBugship1 = App.ShipClass_Cast(Bugship1)

                pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship1))

                Bug2 = "Bugship 5"
                pBug2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug2, "Location 1")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Bug2)
                pMission.GetEnemyGroup().AddName(Bug2)

                Bugship2 = MissionLib.GetShip(Bug2, GammaSet) 

                pBugship2 = App.ShipClass_Cast(Bugship2)

                pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship2))

                Bug3 = "Bugship 6"
                pBug3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug3, "Location 2")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Bug3)
                pMission.GetEnemyGroup().AddName(Bug3)

                Bugship3 = MissionLib.GetShip(Bug3, GammaSet) 

                pBugship3 = App.ShipClass_Cast(Bugship3)

                pBugship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship3))

                Bug4 = "Bugship 7"
                pBug4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug4, "Location 4")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Bug4)
                pMission.GetEnemyGroup().AddName(Bug4)

                Bugship4 = MissionLib.GetShip(Bug4, GammaSet) 

                pBugship4 = App.ShipClass_Cast(Bugship4)

                pBugship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship4))

                Bug5 = "Battlecruiser"
                pBug5 = loadspacehelper.CreateShip(DS9FXShips.DomBC, GammaSet, Bug5, "Location 5")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Bug5)
                pMission.GetEnemyGroup().AddName(Bug5)

                Bugship5 = MissionLib.GetShip(Bug5, GammaSet) 

                pBugship5 = App.ShipClass_Cast(Bugship5)

                pBugship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship5))

                Bug6 = "Ketracel White Facility"
                pBug6 = loadspacehelper.CreateShip(DS9FXShips.MissionStation, GammaSet, Bug6, "Location 3")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Bug6)
                pMission.GetEnemyGroup().AddName(Bug6)

                import Custom.DS9FX.DS9FXAILib.DS9FXEnemyBaseAI

                Bugship6 = MissionLib.GetShip(Bug6, GammaSet) 

                pBugship6 = App.ShipClass_Cast(Bugship6)

                pBugship6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyBaseAI.CreateAI(pBugship6))


                # Kill the handler
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")                

        else:
                pass

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def ObjectExploding(pObject, pEvent):
        global bEnter

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return

        ShipName = pShip.GetName()

        if (ShipName == "Ketracel White Facility"):
                try:
                        bEnter.SetEnabled()
                except:
                        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

                MissionCompleted(None, None)

                AdditionalHandlersStarted(None, None)

                DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")                

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)


def SetupPlayer():
        import Save.mission3
        reload(Save.mission3)
        pShip = Save.mission3.Ship

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


def DisableEnterButton(pObject, pEvent):
        global bEnter

        try:

                bEnter = DS9FXMenuLib.GetSubMenuButton("Enter Wormhole", "Helm", "DS9FX", "Wormhole Options...")

                bEnter.SetDisabled()

        except:

                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())

def DisableButtons(pObject, pEvent):

        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        if (pSet.GetName() == "BajoranWormhole1"):

                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableExitToDS9Button", App.g_kUtopiaModule.GetGameTime() + 7, 0, 0)

                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")


        else:
                pass

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DisableExitToDS9Button(pObject, pEvent):

        try:

                bExitToDS9 = DS9FXMenuLib.GetSubMenuButton("Exit To DS9", "Helm", "DS9FX", "Wormhole Options...")

                bExitToDS9.SetDisabled()


        except:

                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

def GetShipType(pShip):
        if pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        return None

def SpawnSupportShips():

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        loadspacehelper.CreateShip(DS9FXShips.Galaxy, pSet, "USS Croatia", "WarpIn 1")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("USS Croatia")
        pMission.GetFriendlyGroup().AddName("USS Croatia")

        import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

        ship1 = MissionLib.GetShip("USS Croatia", pSet) 

        pship1 = App.ShipClass_Cast(ship1)

        pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))

        loadspacehelper.CreateShip(DS9FXShips.Centaur, pSet, "USS Molotov", "WarpIn 2")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("USS Molotov")
        pMission.GetFriendlyGroup().AddName("USS Molotov")

        ship2 = MissionLib.GetShip("USS Molotov", pSet) 

        pship2 = App.ShipClass_Cast(ship2)

        pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship2))

        loadspacehelper.CreateShip(DS9FXShips.Vorcha, pSet, "IKV Qo'Joh", "WarpIn 3")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("IKV Qo'Joh")
        pMission.GetFriendlyGroup().AddName("IKV Qo'Joh")

        ship3 = MissionLib.GetShip("IKV Qo'Joh", pSet) 

        pship3 = App.ShipClass_Cast(ship3)

        pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship3))

        loadspacehelper.CreateShip(DS9FXShips.Warbird, pSet, "RIS Ptarmigan", "WarpIn 4")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("RIS Ptarmigan")
        pMission.GetFriendlyGroup().AddName("RIS Ptarmigan")

        ship4 = MissionLib.GetShip("RIS Ptarmigan", pSet) 

        pship4 = App.ShipClass_Cast(ship4)

        pship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship4))

def MissionCompleted(pObject, pEvent):
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(RTB(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def RTB(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("We should return to DS9 Sir!", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 0)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def AdditionalHandlersStarted(pObject, pEvent):

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")


def BackToDS9(pObject, pEvent):
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        if (pSet.GetName() == "DeepSpace91"):
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".RemoveFriendlyShips", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
                SaveProgress(None, None)
                MissionCompletedPrompt(None, None)

        else:
                pass

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

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

        pAction = LineAction("Mission Completed!\n\nSupport vessels signing out!\n\nWell Done Captain!", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 20)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

def SaveProgress(pObject, pEvent):
        global pPlayerShipType

        file = nt.open(Path, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "Ship = " + "'" + pPlayerShipType + "'")
        nt.close(file)

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
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")
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
                FailedTxt(None, None)
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")                
                DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
                DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
        except:
                pass
def RemoveFriendlyShips(pObject, pEvent):

        pSet = MissionLib.GetPlayer().GetContainingSet()

        try:
                pSet.DeleteObjectFromSet("USS Croatia")
        except:
                pass
        try:
                pSet.DeleteObjectFromSet("USS Molotov")
        except:
                pass
        try:
                pSet.DeleteObjectFromSet("IKV Qo'Joh")
        except:
                pass
        try:
                pSet.DeleteObjectFromSet("RIS Ptarmigan")            
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

