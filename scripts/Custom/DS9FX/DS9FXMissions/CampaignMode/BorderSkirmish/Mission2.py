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
pTimer = None
pName = MissionIDs.BSM2
sName = "Investigations"
sObjectives = "-Return to Gamma Quadrant\n-Do not engage any enemy ships\n-Wait for 5 minutes for the scan to complete"
sBriefing = "The data recorder you retrieved from the rogue Jem'Hadar bugship has proven extremely useful for us to get a lead on their Ketracel White facility. You are to return to the Gamma Quadrant and perform a long-range scan in order for us to confirm the location of the base. Do not, I repeat DO NOT engage the enemy, you are to return to DS9 at once."

# Path where we should save a mission progress py file
Path  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\BorderSkirmish\\Save\\mission3.py"

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

        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: Investigations"), 0.0, 0.0, None, 1, 0.30, 0.30, kColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, kColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, kColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, kColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Return to Gamma Quadrant\n-Do not engage any enemy ships\n-Wait for 5 minutes for the scan to complete"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("The data recorder you retrieved from the rogue Jem'Hadar bugship has proven extremely useful for us to get a lead on their Ketracel White facility. You are to return to the Gamma Quadrant and perform a long-range scan in order for us to confirm the location of the base. Do not, I repeat DO NOT engage the enemy, you are to return to DS9 at once."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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

        pAction = LineAction("Mission: Investigations", pPane, 3, 6, 16)
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

def SetupPlayer():
        import Save.mission2
        reload(Save.mission2)
        pShip = Save.mission2.Ship

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
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".FiringHandler")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                deleteptimer()
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
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".FiringHandler")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                deleteptimer()
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

def MissionStart(pObject, pEvent):
        global pTimer

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
                pBug1 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug1, "Location 1")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Bug1)
                pMission.GetEnemyGroup().AddName(Bug1)

                import Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI

                Bugship1 = MissionLib.GetShip(Bug1, GammaSet) 

                pBugship1 = App.ShipClass_Cast(Bugship1)

                pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship1))

                Bug2 = "Bugship 5"
                pBug2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug2, "Location 2")

                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                DS9FXLifeSupportLib.ClearFromGroup(Bug2)
                pMission.GetEnemyGroup().AddName(Bug2)

                Bugship2 = MissionLib.GetShip(Bug2, GammaSet) 

                pBugship2 = App.ShipClass_Cast(Bugship2)

                pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship2))

                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")

                pTimer = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".AreaScanned", App.g_kUtopiaModule.GetGameTime() + 300, 0, 0)

                Wait(None, None)

                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".FiringHandler")


        else:
                pass

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def FiringHandler(pObject, pEvent):
        global bEnter

        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())
        pPlayer = MissionLib.GetPlayer()
        if pAttacker.GetName() == pPlayer.GetName():
                pSet = pPlayer.GetContainingSet()

                try:
                        pSet.DeleteObjectFromSet("Bugship 4")
                except:
                        pass
                try:
                        pSet.DeleteObjectFromSet("Bugship 5")
                except:
                        pass
                
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".FiringHandler")
                
                FailedTxt(None, None)
                deleteptimer()
                DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
                DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

                try:
                        bEnter.SetEnabled()

                except:
                        raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

        else:
                pass

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def DisableEnterButton(pObject, pEvent):
        global bEnter

        try:

                bEnter = DS9FXMenuLib.GetSubMenuButton("Enter Wormhole", "Helm", "DS9FX", "Wormhole Options...")

                bEnter.SetDisabled()

        except:

                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

        DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())

def AreaScanned(pObject, pEvent):
        global bEnter, pPaneID

        try:
                bEnter.SetEnabled()
        except:
                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."


        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

        AdditionalHandlersStarted(None, None)

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(MissionLog(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def MissionLog(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("Area Scanned Captain!\n\nWe should return to DS9!", pPane, 6, 10, 12)
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
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".FiringHandler")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")

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

        pAction = LineAction("Mission Completed!\n\nScans are being analyzed!\n\nExcellent job Captain!", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 20)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

def Wait(pObject, pEvent):
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AppendAction(Wait5mins(pPane))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def Wait5mins(pPane):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)

        pAction = LineAction("It will take us\n5 mins to conduct a scan.\nWe mustn't engage the enemy!!!", pPane, 6, 10, 12)
        pSequence.AddAction(pAction, None, 30)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def SaveProgress(pObject, pEvent):
        global pPlayerShipType

        file = nt.open(Path, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
        nt.write(file, "Ship = " + "'" + pPlayerShipType + "'")
        nt.close(file)

def GetShipType(pShip):
        if pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        return None

def KillPane(pAction):
        global pPaneID

        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
        App.g_kRootWindow.DeleteChild(pPane)

        pPaneID = App.NULL_ID

        return 0


def deleteptimer():
        global pTimer

        try:
                App.g_kTimerManager.DeleteTimer(pTimer.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(pTimer.GetObjID())
                pTimer = None
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

