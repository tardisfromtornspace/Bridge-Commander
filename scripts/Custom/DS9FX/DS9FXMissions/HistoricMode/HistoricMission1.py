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
pTimer = None
iMinesLayed = 0
pPaneID = App.NULL_ID
pName = MissionIDs.HM1
sName = "Plant the minefield"
sObjectives = "-Be sure to be in 10 km range before you plant mines\n-Plant 26 mines\n-Survive attack\n-In the end warp out in any direction"
sBriefing = "Captain, we are loosing at peace time. We have to stop the Dominion convoys which are coming through the wormhole constantly. It's up to you to place a cloaked minefield, you don't have a lot of time before the Dominion and Cardassian fleets arrive from Cardassia. Good luck, Captain. We are all counting on you! This is most likely the first battle of what will people one day call the Dominion Wars, let us pray that we can win."

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

        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: Plant the minefield"), 0.0, 0.0, None, 1, 0.30, 0.30, kColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, kColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, kColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, kColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Be sure to be in 10 km range before you plant mines\n-Plant 26 mines\n-Survive attack\n-In the end warp out in any direction"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("Captain, we are loosing at peace time. We have to stop the Dominion convoys which are coming through the wormhole constantly. It's up to you to place a cloaked minefield, you don't have a lot of time before the Dominion and Cardassian fleets arrive from Cardassia. Good luck, Captain. We are all counting on you! This is most likely the first battle of what will people one day call the Dominion Wars, let us pray that we can win."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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

        pAction = LineAction("Mission: Plant the minefield", pPane, 3, 6, 16)
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
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".DS9Exploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".DS9Exploding")	

        ObjectivesPrompt(None, None)
        LayMines()
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
        pShip = DS9FXShips.Defiant

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
                DeletepTimer(None, None)
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
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
                FailedTxt(None, None)
                DeletepTimer(None, None)
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
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
                DeletepTimer(None, None)
                RemoveShips()
                RemoveMines()
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")   
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".DS9Exploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".DS9Exploding")  
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

def ObjectivesPrompt(pObject, pEvent):
        global pPaneID
        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(ObjectivesSequence(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def ObjectivesSequence(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Captain, we should go over to the \nwormhole and place the minefield!", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 10)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

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

def LayMines():
        global pTimer

        pTimer = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MineLayingCheck", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)


def MineLayingCheck(pObject, pEvent):
        global iMinesLayed, pTimer

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
        pDS9FXWormholeID = pDS9FXWormhole.GetObjID()

        if DistanceCheck(pDS9FXWormhole) < 50:
                if iMinesLayed == 12:
                        SpeedupPrompt()
                        SpawnShips()
                        pTimer = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MineLayingCheck", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)
                        CreateMine()

                elif iMinesLayed > 25:
                        RunPrompt()
                        ReenableAllButtons()
                        pGame = App.Game_GetCurrentGame()
                        pEpisode = pGame.GetCurrentEpisode()
                        pMission = pEpisode.GetCurrentMission()

                        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
                        return

                else:
                        pTimer = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MineLayingCheck", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)
                        CreateMine()


        elif iMinesLayed > 25:
                RunPrompt()
                ReenableAllButtons()
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()

                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
                return


        else:
                pTimer = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MineLayingCheck", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)

def DistanceCheck(pObject):
        pPlayer = App.Game_GetCurrentGame().GetPlayer()
        vDifference = pObject.GetWorldLocation()
        vDifference.Subtract(pPlayer.GetWorldLocation())

        return vDifference.Length()

def CreateMine():
        global iMinesLayed

        RemoveMines()

        iMinesLayed = iMinesLayed + 1

        pPlayer	= MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        pName = "Mine" + str(iMinesLayed)
        pMine = loadspacehelper.CreateShip(DS9FXShips.Mine, pSet, pName, None)

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(pName)
        pMission.GetFriendlyGroup().AddName(pName)

        pPosition = pPlayer.GetWorldLocation()
        pMine.SetTranslate(pPosition)
        pMine.UpdateNodeOnly()

        pMine.SetCollisionsOn(0)

        MinesPlaced()

def SpawnShips():
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, "IKS Rotarran", "Excal Location")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup("IKS Rotarran")
        pMission.GetFriendlyGroup().AddName("IKS Rotarran")

        import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

        ship1 = MissionLib.GetShip("IKS Rotarran", pSet)

        ship1.SetInvincible(1)
        ship1.SetHurtable(0)

        pship1 = App.ShipClass_Cast(ship1)

        pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))

        Att1 = "Enemy 1"
        pAtt1 = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, Att1, "Help1")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att1)
        pMission.GetEnemyGroup().AddName(Att1)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker1 = MissionLib.GetShip("Enemy 1", pSet) 

        pAttacker1 = App.ShipClass_Cast(Attacker1)

        pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

        Att2 = "Enemy 2"
        pAtt2 = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, Att2, "Help2")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att2)
        pMission.GetEnemyGroup().AddName(Att2)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker2 = MissionLib.GetShip("Enemy 2", pSet) 

        pAttacker2 = App.ShipClass_Cast(Attacker2)

        pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

        Att3 = "Enemy 3"
        pAtt3 = loadspacehelper.CreateShip(DS9FXShips.Hideki, pSet, Att3, "Help3")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att3)
        pMission.GetEnemyGroup().AddName(Att3)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker3 = MissionLib.GetShip("Enemy 3", pSet) 

        pAttacker3 = App.ShipClass_Cast(Attacker3)

        pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))

        Att4 = "Enemy 4"
        pAtt4 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att4, "WarpIn 4")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att4)
        pMission.GetEnemyGroup().AddName(Att4)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker4 = MissionLib.GetShip("Enemy 4", pSet) 

        pAttacker4 = App.ShipClass_Cast(Attacker4)

        pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

        Att5 = "Enemy 5"
        pAtt5 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att5, "WarpIn 3")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att5)
        pMission.GetEnemyGroup().AddName(Att5)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker5 = MissionLib.GetShip("Enemy 5", pSet) 

        pAttacker5 = App.ShipClass_Cast(Attacker5)

        pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

        Att6 = "Enemy 6"
        pAtt6 = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, Att6, "WarpIn 2")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att6)
        pMission.GetEnemyGroup().AddName(Att6)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker6 = MissionLib.GetShip("Enemy 6", pSet) 

        pAttacker6 = App.ShipClass_Cast(Attacker6)

        pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))

        Att7 = "Enemy 7"
        pAtt7 = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, Att7, "WarpIn 1")

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        DS9FXLifeSupportLib.ClearFromGroup(Att7)
        pMission.GetEnemyGroup().AddName(Att7)

        import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

        Attacker7 = MissionLib.GetShip("Enemy 7", pSet) 

        pAttacker7 = App.ShipClass_Cast(Attacker7)

        pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))

def DeletepTimer(pObject, pEvent):
        global pTimer

        try:
                App.g_kTimerManager.DeleteTimer(pTimer.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(pTimer.GetObjID())
                pTimer = None
        except:
                pass

def SpeedupPrompt():
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(SpeedupSequence(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def SpeedupSequence(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Sir, Dominion ships have arrived. \n\nWe have to hurry!", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 10)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def RunPrompt():
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(RunSequence(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def RunSequence(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Sir, minefield is in place. \n\nWe have to warp out, \nin any direction", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 10)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def MinesPlaced():
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(MinesSequence(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def MinesSequence(pPane):
        global iMinesLayed

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Mines Placed: " + str(iMinesLayed), pPane, 12, 3, 12)
        pSequence.AddAction(pAction, None, 0.1)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def EvacDS9(pObject, pEvent):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        RemoveShips()
        RemoveMines()
        DeletepTimer(None, None)

        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".DS9Exploding")
        App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".DS9Exploding")  
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")

        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)
                return 0

        pSet = pPlayer.GetContainingSet()
        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                if pShip.GetName() == pPlayer.GetName():
                        continue
                pSet.DeleteObjectFromSet(kShip.GetName())

        from Custom.DS9FX.DS9FXObjects import DS9Objects

        DS9Objects.DS9SetObjects()

        from Custom.DS9FX.DS9FXObjects import DS9Stations

        DS9Stations.DS9SetStations()

        from Custom.DS9FX.DS9FXObjects import DS9Ships

        DS9Ships.DS9SetShips()

        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)


def RemoveShips():
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        try:
                pSet.DeleteObjectFromSet("IKS Rotarran")
        except:
                pass
        try:
                pSet.DeleteObjectFromSet("Enemy 1")
        except:
                pass

        try:
                pSet.DeleteObjectFromSet("Enemy 2")
        except:
                pass

        try:
                pSet.DeleteObjectFromSet("Enemy 3")
        except:
                pass

        try:
                pSet.DeleteObjectFromSet("Enemy 4")
        except:
                pass

        try:
                pSet.DeleteObjectFromSet("Enemy 5")
        except:
                pass

        try:
                pSet.DeleteObjectFromSet("Enemy 6")
        except:
                pass

        try:
                pSet.DeleteObjectFromSet("Enemy 7")
        except:
                pass

def KillPane(pAction):
        global pPaneID

        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
        App.g_kRootWindow.DeleteChild(pPane)

        pPaneID = App.NULL_ID

        return 0

def RemoveMines():
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()

        iMine = 0
        iRemove = 1
        while iRemove == 1:
                if iMine > 25:
                        iRemove = 0

                iMine = iMine + 1
                try:
                        pSet.DeleteObjectFromSet("Mine" + str(iMine))
                except:
                        pass
