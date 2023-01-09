# by USS Sovereign, strictly based on the DS9FX Code.


# Imports
import App
import MissionLib

# Vars
SeqID = App.NULL_ID
pMoviePaneID = App.NULL_ID


# Play the movie
def PlayMovieSeq(pAction, pEvent):
                global SeqID, pMoviePaneID

                # Stop all background movies
                import MainMenu.mainmenu

                MainMenu.mainmenu.StopBackgroundMovies()
    
                # Append actions & do the right thing (allow the user to skip the video of course)
                pMoviePane = App.TGPane_Create(1.0, 1.0)
                App.g_kRootWindow.PrependChild(pMoviePane)
                pMoviePane.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__ + ".HandleKeyboard")
                pSequence = App.TGSequence_Create()
                pSequence.AddAction(App.TGScriptAction_Create("MainMenu.mainmenu", "ShowWarpBackground", 1))
                pAction = App.TGScriptAction_Create(__name__, "EnterMovie")
                pSequence.AppendAction(pAction)
                pMovie = App.TGMovieAction_Create("scripts/Custom/TimeVortex/Movies/Preview.bik", 1, 1)
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
                
                # Play the sequence when called
                pSequence.Play()


# Movie should be skippable so allow keyboard input
def EnterMovie(pAction):
        
                # Grab some values
                pTopWindow = App.TopWindow_GetTopWindow()
                if (pTopWindow == None):
                        return None

                pTopWindow.SetNotVisible()

                # Disable options menu
                pTopWindow.DisableOptionsMenu(1)
                pTopWindow.AllowMouseInput(0)

                # Game paused
		App.g_kUtopiaModule.Pause(1)

		App.InterfaceModule_DoTheRightThing()
		
                return 0


# Restore all options back to normal
def ExitMovie(pAction):
        
                # Grab some values again and switch out of movie mode
                App.g_kMovieManager.SwitchOutOfMovieMode()
                
                pTopWindow = App.TopWindow_GetTopWindow()
                if (pTopWindow == None):
                        return None

                pTopWindow.SetVisible()

                # Restore all options back to default
                pTopWindow.DisableOptionsMenu(0)
                pTopWindow.AllowMouseInput(1)

                # Game unpaused
		App.g_kUtopiaModule.Pause(0)
		

                return 0


# Check keys pressed and kill the sequence if needed
def HandleKeyboard(pPane, pEvent):
            global SeqID

            # Basically this is from main menu
            KeyType = pEvent.GetKeyState()
            CharCode = pEvent.GetUnicode()

            # Check if esc key was pressed
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
                    pPane.CallNextHandler(pEvent)


# Switch back to normal
def BackToNormal(pAction):
            global SeqID
            SeqID = App.NULL_ID
            
            App.g_kMovieManager.SwitchOutOfMovieMode()

            # Game unpaused
            App.g_kUtopiaModule.Pause(0)
                    
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


# A hack function to play all background movies again
def Normal(pAction):
            import MainMenu.mainmenu

            MainMenu.mainmenu.ShowWarpBackground(None, 0)
            
            MainMenu.mainmenu.SwitchMiddlePane("New Game")

            MainMenu.mainmenu.SwitchMiddlePane("Configure")

            MainMenu.mainmenu.PlayBackgroundMovie(1)

            return 0

# Kill the pane, fixes the crashing bug and several other bugs
def KillPane(pAction):
            global pMoviePaneID
            
            pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pMoviePaneID))
            App.g_kRootWindow.DeleteChild(pPane)
            
            App.InterfaceModule_DoTheRightThing()
            
            pMoviePaneID = App.NULL_ID
            
            return 0
