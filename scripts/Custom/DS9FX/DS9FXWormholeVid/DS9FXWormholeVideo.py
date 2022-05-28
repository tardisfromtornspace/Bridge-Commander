# by USS Sovereign

# Imports
import App
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Vars
iAllowExitFromVideoView = 0

# Movie sequence
def PlayMovieSeq():
        global iAllowExitFromVideoView 

        if DS9FXSavedConfig.VideoSelection == 1:
                pSequence = App.TGSequence_Create()        
                pAction = App.TGScriptAction_Create(__name__, "EnterMovie")
                pSequence.AppendAction(pAction)
                pMovie = App.TGMovieAction_Create("data/Movies/DS9FXWormholeSeq.bik", 1, 1)
                pSequence.AppendAction(pMovie)
                pAction = App.TGScriptAction_Create(__name__, "ExitMovie")
                pSequence.AppendAction(pAction)

                pSequence.Play()

                iAllowExitFromVideoView = None
                iAllowExitFromVideoView = 0

        else:
                App.g_kSoundManager.PlaySound("DS9FXWormLoop")

                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".AllowExit", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

def EnterMovie(pAction):
        global iAllowExitFromVideoView

        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

        pTopWindow.SetNotVisible()

        pTopWindow.DisableOptionsMenu(1)
        pTopWindow.AllowKeyboardInput(0)
        pTopWindow.AllowMouseInput(0)

        iAllowExitFromVideoView = None
        iAllowExitFromVideoView = 0

        return 0

def ExitMovie(pAction):
        global iAllowExitFromVideoView

        App.g_kMovieManager.SwitchOutOfMovieMode()

        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

        pTopWindow.SetVisible()

        pTopWindow.DisableOptionsMenu(0)
        pTopWindow.AllowKeyboardInput(1)
        pTopWindow.AllowMouseInput(1)

        iAllowExitFromVideoView = None
        iAllowExitFromVideoView = 1

        return 0


def CheckExitFromVideo():
        global iAllowExitFromVideoView

        return iAllowExitFromVideoView


def AllowExit(pObject, pEvent):
        global iAllowExitFromVideoView

        iAllowExitFromVideoView = None
        iAllowExitFromVideoView = 1
