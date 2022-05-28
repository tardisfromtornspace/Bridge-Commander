# A new submenu in UMM menu and it calls this file. It basically allows people to see all movies directly!

# by USS Sovereign

# Imports
import App
import MissionLib

# Vars
SeqID = App.NULL_ID
pMoviePaneID = App.NULL_ID
bMusicState = 0

# Play the movie
def PlayMovieSeq():
        global SeqID, pMoviePaneID

        import MainMenu.mainmenu

        MainMenu.mainmenu.StopBackgroundMovies()

        pMoviePane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pMoviePane)
        pMoviePane.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__ + ".HandleKeyboard")
        pSequence = App.TGSequence_Create()
        pSequence.AddAction(App.TGScriptAction_Create("MainMenu.mainmenu", "ShowWarpBackground", 1))
        pAction = App.TGScriptAction_Create(__name__, "EnterMovie")
        pSequence.AppendAction(pAction)
        pMovie = App.TGMovieAction_Create("data/Movies/DS9FXWormholeSeq.bik", 1, 1)
        pMovie.SetSkippable(1)
        pSequence.AppendAction(pMovie)
        pAction = App.TGScriptAction_Create(__name__, "ExitMovie")
        pSequence.AppendAction(pAction)
        pAction = App.TGScriptAction_Create(__name__, "Normal")
        pSequence.AppendAction(pAction)
        pAction = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAction, 0.1)

        SeqID = pSequence.GetObjID()
        pMoviePaneID = pMoviePane.GetObjID()

        pSequence.Play()


def EnterMovie(pAction):
        global bMusicState
        
        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

        pTopWindow.SetNotVisible()

        pTopWindow.DisableOptionsMenu(1)
        pTopWindow.AllowMouseInput(0)

        App.g_kUtopiaModule.Pause(1)

        bMusicState = App.g_kMusicManager.IsEnabled()
        
        App.g_kMusicManager.SetEnabled(0)

        App.InterfaceModule_DoTheRightThing()

        return 0

def ExitMovie(pAction):
        global bMusicState 
        
        App.g_kMovieManager.SwitchOutOfMovieMode()

        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

        pTopWindow.SetVisible()

        pTopWindow.DisableOptionsMenu(0)
        pTopWindow.AllowMouseInput(1)

        App.g_kUtopiaModule.Pause(0)

        App.g_kMusicManager.SetEnabled(bMusicState)

        return 0


def HandleKeyboard(pPane, pEvent):
        global SeqID

        KeyType = pEvent.GetKeyState()
        CharCode = pEvent.GetUnicode()

        if KeyType == App.TGKeyboardEvent.KS_KEYUP:
                if (CharCode == App.WC_ESCAPE):
                        pSequence = App.TGSequence_Cast(App.TGObject_GetTGObjectPtr(SeqID))
                        try:
                                pSequence.Skip()
                        except:
                                pass

                        SeqID = App.NULL_ID

                        BackToNormal(None)

                        pEvent.SetHandled()

        if (pEvent.EventHandled() == 0):
                if pPane and pEvent:
                        pPane.CallNextHandler(pEvent)

def BackToNormal(pAction):
        global SeqID
        SeqID = App.NULL_ID

        App.g_kMovieManager.SwitchOutOfMovieMode()

        App.g_kUtopiaModule.Pause(0)

        App.g_kMusicManager.SetEnabled(1)

        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return

        pTopWindow.SetVisible()

        import MainMenu.mainmenu

        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
        MainMenu.mainmenu.SetVisible (pOptionsWindow, 1)

        pTopWindow.DisableOptionsMenu(0)
        pTopWindow.AllowMouseInput(1)

        pSequence = App.TGSequence_Create()        
        pAct = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAct, 0.1)
        pSequence.Play()

        return 0

def Normal(pAction):
        import MainMenu.mainmenu

        MainMenu.mainmenu.ShowWarpBackground(None, 0)

        MainMenu.mainmenu.SwitchMiddlePane("New Game")

        MainMenu.mainmenu.SwitchMiddlePane("Configure")

        MainMenu.mainmenu.PlayBackgroundMovie(1)

        return 0

def KillPane(pAction):
        global pMoviePaneID

        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pMoviePaneID))
        App.g_kRootWindow.DeleteChild(pPane)

        App.InterfaceModule_DoTheRightThing()

        pMoviePaneID = App.NULL_ID

        return 0
