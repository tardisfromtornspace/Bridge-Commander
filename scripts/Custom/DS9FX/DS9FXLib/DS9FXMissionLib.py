# DS9FX Mission Lib

# by Sov

import App
import MissionLib
import string
import Custom.DS9FX.DS9FXmain
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

ET_ACCEPT = App.UtopiaModule_GetNextEventType()
ET_DECLINE = App.UtopiaModule_GetNextEventType()
ET_BACK = App.UtopiaModule_GetNextEventType()

i = 0
dPanes = {}
pPane = None
pMainPane = None
pPaneID = App.NULL_ID
pMissionName = None
pName = None
pModule = None

def Briefing(sMission, sObjectives, sBriefing, sID, sModule):
        global pMainPane, pPane, pMissionName, pName, pModule

        if not pPane == None:
                Decline(None, None)
                return

        pMissionName = sMission
        pName = sID
        pModule = sModule

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

        CreateEntries(sMission, sObjectives, sBriefing)    

def CreateEntries(sMission, sObjectives, sBriefing):
        global pMainPane, pPane, dPanes, i

        kColor = App.TGColorA() 
        kColor.SetRGBA(1, 0.81, 0.41, 1.0)

        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString(sMission), 0.0, 0.0, None, 1, 0.30, 0.30, kColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, kColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, kColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, kColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString(sObjectives), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString(sBriefing), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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

        i = i + 1
        dPanes[i] = pPane

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

        StartMission()

        MissionTitle()

        PlayMissionMovies()

        pPane = None

        pMainPane = None

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

def ShowMissionMenu(pObject, pEvent):
        Decline(None, None)
        Custom.DS9FX.DS9FXmain.RecallMissionMenu()
        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def StartMission():
        global pModule
        pMod = __import__(str(pModule))
        pMod.MissionInitiate()

def MissionTitle():
        global pMissionName
        sText = "Mission: " + str(pMissionName)
        iPos = 3
        iFont = 16
        iDur = 6
        iDelay = 10
        PrintText(sText, iPos, iFont, iDur, iDelay)

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

def PrintText(sText, iPos, iFont, iDur, iDelay):
        global pPaneID

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime(1)
        pSequence.AppendAction(TextSequence(pPane, sText, iPos, iFont, iDur, iDelay))
        pPaneID = pPane.GetObjID()
        pSequence.Play()

def TextSequence(pPane, sText, iPos, iFont, iDur, iDelay):
        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime(1)

        pAction = LineAction(sText, pPane, iPos, iDur, iFont)
        pSequence.AddAction(pAction, None, iDelay)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)
        pSequence.Play()

def LineAction(sLine, pPane, fPos, duration, fontSize):
        bLog = 1
        lLines = ["Mission:", "Time:"]
        for s in lLines:
                i = string.find(sLine, s)
                if i == 0:
                        bLog = 0
                        break
        if bLog:
                from Custom.DS9FX.DS9FXMissions import MissionStatus
                MissionStatus.AddLOGEntry(sLine)

        fHeight = fPos * 0.0375
        App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
        pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
        return pAction

def KillPane(pAction):
        global pPaneID

        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
        App.g_kRootWindow.DeleteChild(pPane)

        pPaneID = App.NULL_ID

        return 0

def Quit():
        global pMainPane, pPane, dPanes

        try:
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()

                App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
                App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")
                App.g_kEventManager.RemoveBroadcastHandler(ET_BACK, pMission, __name__ + ".ShowMissionMenu")
        except:
                pass

        for k in dPanes.keys():
                try:
                        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                        App.g_kFocusManager.RemoveAllObjectsUnder(dPanes[k])
                        pTCW.DeleteChild(dPanes[k])
                except:
                        pass

        pPane = None
        pMainPane = None
        dPanes = {}
