"""
If enabled it will replace the default intros, by default it's off

by USS Sovereign
"""

import App
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def PlayOpeningMovies():
        import MainMenu.mainmenu
        fMenu = MainMenu.mainmenu

        # Grab values
        g_idMoviePane = fMenu.g_idMoviePane
        g_idMoviePane2 = fMenu.g_idMoviePane2
        g_idOpeningSequence = fMenu.g_idOpeningSequence

        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return

        pTopWindow.SetNotVisible ()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        App.InterfaceModule_DoTheRightThing()

        global g_idMoviePane
        pMoviePane = App.TGPane_Create (1.0, 1.0)
        g_idMoviePane = pMoviePane.GetObjID()

        global g_idMoviePane2
        pMoviePane2 = App.TGPane_Create (1.0, 1.0)
        g_idMoviePane2 = pMoviePane2.GetObjID()

        App.g_kRootWindow.PrependChild(pMoviePane2, 0.00375, 0.005)	
        App.g_kRootWindow.PrependChild(pMoviePane)

        pMoviePane2.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, "MainMenu.mainmenu" + ".HandleKeyboardOpening")

        fMenu.StopBackgroundMovies ()

        pSequence = App.TGSequence_Create()

        # Which movie did the user specify to play at startup?
        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.IntroMovieSel == "Random":
                RandomSel = GetRandomNumber()
                if RandomSel < 33:
                        strMovie = "DS9FXintro.bik"
                elif RandomSel < 66:
                        strMovie = "DS9FXTrailer.bik"
                else:
                        strMovie = "DS9FXXtendedIntro.bik"
        else:
                strMovie = DS9FXSavedConfig.IntroMovieSel

        # Non-skippable for compatibility reasons
        pMovie = App.TGMovieAction_Create("data/Movies/" + strMovie, 1, 1)
        pSequence.AppendAction(pMovie)
        # I'm too lazy to search other functions to override so this will just skip everything once we finish the intro movie
        pSequence.AppendAction(App.TGScriptAction_Create("Custom.DS9FX.DS9FXLib.DS9FXOpeningMovie", "QuitMovieMode"))

        global g_idOpeningSequence
        g_idOpeningSequence = pSequence.GetObjID()

        # Update mainmenu values with the new ones
        fMenu.g_idMoviePane = g_idMoviePane
        fMenu.g_idMoviePane2 = g_idMoviePane2
        fMenu.g_idOpeningSequence = g_idOpeningSequence

        pSequence.Play()

def QuitMovieMode(pAction):
        import MainMenu.mainmenu
        fMenu = MainMenu.mainmenu

        # Movie seq done, update mainmenu values
        fMenu.g_idOpeningSequence = App.NULL_ID
        fMenu.g_idOpeningMovieSequence = App.NULL_ID
        fMenu.g_idOpeningCreditsSequence = App.NULL_ID

        # Finish the sequences
        fMenu.FinishOpeningMovie(None)

        return 0

# Percentage simulation
def GetRandomNumber():
        return App.g_kSystemWrapper.GetRandomNumber(99) + 1

class DS9FXIntroReplacement:
        def __init__(self):
                self.__intro_override__()

        def __intro_override__(self):
                import MainMenu.mainmenu
                fMenu = MainMenu.mainmenu
                fMenu.PlayOpeningMovies = PlayOpeningMovies

def StartUp():		
        IntroReplacement = DS9FXIntroReplacement()

