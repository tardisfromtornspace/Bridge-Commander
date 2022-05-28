# Smbw - 20.06.2009

# Idea by kirk2164

# Just a small window containing:
#   - Mission Briefing
#   - Mission Objectives
#   - Mission Log

# 22.06 - Added mission time


# Imports:
import App
import string


# Globals:
pPane = None
pMainPane = None
MissionScript = None
sLOG = ""
fStartTime = 0.0


# Event:
ET_CLOSE = App.UtopiaModule_GetNextEventType()


# Setup MissionStatus on MissionStart. 
def Setup(pObject, pEvent):
        global MissionScript, fStartTime

        Reset()

        if hasattr(pEvent, "GetCString"):        
                s = pEvent.GetCString()
                import MissionModulePaths
                pModule = MissionModulePaths.GetMissionModulePath(s)
                MissionScript = __import__(pModule)
        else:
                MissionScript = None
        

        fStartTime = App.g_kUtopiaModule.GetGameTime()


# Creates and views MissionStatus window. 
def ViewMissionStatus():
        global pPane, pMainPane, MissionScript, sLOG, fStartTime

        if not pPane == None:
                CloseMissionStatus(None, None)
                return
        
        if MissionScript == None:
                return

        App.g_kUtopiaModule.Pause(1)

        pPane = App.TGPane_Create(1.0, 1.0)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(pPane, 0, 0)
        pMainPane = App.TGPane_Create(0.6, 0.7)
        pPane.AddChild(pMainPane, 0.33, 0.04)

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".CloseMissionStatus")

        kColor = App.TGColorA() 
        kColor.SetRGBA(1, 0.81, 0.41, 1.0)

        pMainWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission Status"), 0.0, 0.0, None, 1, 0.6, 0.69, kColor)
        pMainPane.AddChild(pMainWindow, 0.0, 0.0)
        pMainPane.MoveToFront(pMainWindow)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.3, 0.26, kColor)
        pMainPane.AddChild(pBriefingWindow, 0.03, 0.06)
        pMainPane.MoveToFront(pBriefingWindow)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.19, 0.26, kColor)
        pMainPane.AddChild(pObjectivesWindow, 0.38, 0.06)
        pMainPane.MoveToFront(pObjectivesWindow)

        pMLOGWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission LOG"), 0.0, 0.0, None, 1, 0.51, 0.22, kColor)
        pMainPane.AddChild(pMLOGWindow, 0.05, 0.37)
        pMainPane.MoveToFront(pMLOGWindow)

        try:
                sMissionName = MissionScript.sName
        except AttributeError:
                sMissionName = ""

        try:
                sBriefing = MissionScript.sBriefing
        except AttributeError:
                sBriefing = ""

        try:
                sObjectives = MissionScript.sObjectives
        except AttributeError:
                sObjectives = ""

        pText = App.TGParagraph_CreateW(App.TGString(str(sMissionName + ":\n\n" + sBriefing)), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pBriefingWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString(sObjectives), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        iSeconds = int(App.g_kUtopiaModule.GetGameTime() - fStartTime)
        iMinutes = iSeconds / 60
        iSeconds = iSeconds % 60
        if iMinutes != 1:
                sMinutes = "minutes"
        else:
                sMinutes = "minute"

        if iSeconds != 1:
                sSeconds = "seconds"
        else:
                sSeconds = "second"

        currentLOG = sLOG + "Mission playing for " + str(iMinutes) + " " + sMinutes + " and " + str(iSeconds) + " " + sSeconds + "."

        pText = App.TGParagraph_CreateW(App.TGString(currentLOG), pMLOGWindow.GetMaximumInteriorWidth(), None, '', pMLOGWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pMLOGWindow.AddChild(pText, 0, 0.01)

        kNormalColor = App.TGColorA() 
        kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
        kHilightedColor = App.TGColorA() 
        kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
        kDisabledColor = App.TGColorA() 
        kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetString("DS9FXMStatClose")
        pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.36, 0.04)
        pButton.SetNormalColor(kNormalColor)
        pButton.SetHighlightedColor(kHilightedColor)
        pButton.SetSelectedColor(kNormalColor)
        pButton.SetDisabledColor(kDisabledColor)
        pButton.SetColorBasedOnFlags()
        pMainWindow.AddChild(pButton, 0.12, 0.59)
        pMainWindow.MoveToFront(pButton)

        pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode() 
        pLCARS = pGraphicsMode.GetLcarsString() 
        pGlass = App.TGIcon_Create(pLCARS, 120) 
        pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight()) 
        pMainPane.AddChild(pGlass, 0, 0)


        pMLOGWindow.InteriorChangedSize()
        pMLOGWindow.Layout()
        pObjectivesWindow.InteriorChangedSize()
        pObjectivesWindow.Layout()
        pBriefingWindow.InteriorChangedSize()
        pBriefingWindow.Layout()
        pMainWindow.InteriorChangedSize()
        pMainWindow.Layout()
        pMainPane.Layout()
        pPane.Layout()

        pPane.SetVisible()


# Closes window:
def CloseMissionStatus(pObject, pEvent):
        global pPane, pMainPane

        App.g_kUtopiaModule.Pause(0)

        try:
                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".CloseMissionStatus")
        except:
                pass

        if not pPane is None:
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                try:
                        App.g_kFocusManager.RemoveAllObjectsUnder(pPane)
                        pTCW.DeleteChild(pPane)
                        pPane = None   
                        pMainPane = None
                except:
                        pass

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def AddLOGEntry(sEntry):
        global sLOG

        sLOG = sLOG + NormString(sEntry) + "\n\n"


# Clears everything on MissionEnd. Called from DS9FXMutatorFunctions:
def Reset():
        global MissionScript, sLOG, fStartTime

        try:
                Quit()
        except:
                pass

        MissionScript = None
        sLOG = ""
        fStartTime = 0.0


def NormString(s):
        if not "\n" in s:
                return s

        s = string.replace(s, "\n\n\n", " ")
        s = string.replace(s, "\n\n", " ")
        s = string.replace(s, "\n", " ")

        return s

def Quit():
        global pPane, pMainPane
        
        try:
                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".CloseMissionStatus")
        except:
                pass

        if not pPane is None:
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                try:
                        App.g_kFocusManager.RemoveAllObjectsUnder(pPane)
                        pTCW.DeleteChild(pPane)
                        pPane = None   
                        pMainPane = None
                except:
                        pass
