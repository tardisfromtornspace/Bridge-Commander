# by USS Sovereign, strictly based on the DS9FX Code


# Imports
import App

# Vars
pSeq = App.NULL_ID
pSeq2 = App.NULL_ID


# Call Credits sequence
def PlaySeq(pAction, pEvent):

        Credits(None, None)


# Sequence
def Credits(pObject, pEvent):
        # Grab some values
        pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return

        # Disable top window and options menu
	pTopWindow.SetNotVisible()

	pTopWindow.DisableOptionsMenu(1)

        # Attach a pane
	pPane = App.TGPane_Create(1.0, 1.0)
	App.g_kRootWindow.PrependChild(pPane)

        # Add the keyboard listener function
	pPane.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD,	__name__ + ".HandleKeyboard")

        # Stop all background movies
	import MainMenu.mainmenu

	MainMenu.mainmenu.StopBackgroundMovies()
	
        # Create a credits sequence and switch to warp set which is caled from the mainmenu.py
	pSequence = App.TGSequence_Create()
	pSequence.SetUseRealTime (1)
	pSequence.AddAction(App.TGScriptAction_Create("MainMenu.mainmenu", "ShowWarpBackground", 1))
	pSequence.AppendAction(CreditsSeq(pPane))
	pAction = App.TGScriptAction_Create(__name__, "BackToOptions")
	pAction.SetUseRealTime (1)
	pSequence.AppendAction(pAction, 1.0)
	pSequence.Play()

        # Get the ObjID of the sequence
	global pSeq2
        pSeq2 = pSequence.GetObjID()


# Credits sequence
def CreditsSeq(pPane):
        # Setting up grounds for the sequence
        App.InterfaceModule_DoTheRightThing()
        
	pSequence = App.TGSequence_Create()
	pSequence.SetUseRealTime (1)
	pSequence.SetSkippable(1)

        # Credit lines
        pAction = LineAction("Project & Programming Lead:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 0)

	pAction = LineAction("USS Sovereign", pPane, 14, 4, 14)
	pSequence.AddAction(pAction, None, 1)

        pAction = LineAction("GFX:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 7)

	pAction = LineAction("GDLuque\nDr_McCoy\njb06\nCordanilus", pPane, 14, 4, 14)
	pSequence.AddAction(pAction, None, 8)

	pAction = LineAction("SFX:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 14)

	pAction = LineAction("Blackrook32", pPane, 14, 4, 14)
	pSequence.AddAction(pAction, None, 15)
	
	pAction = LineAction("Beta Testers:", pPane, 10, 11, 18)
	pSequence.AddAction(pAction, None, 21)

	pAction = LineAction("1DeadlySAMURAI\nAndrewJ\nBlackrook32\nCaptainGMAN\ncobie2\ncordanilus\nDante Leonhart\nDr_McCoy\nEvilGrizz", pPane, 14, 4, 12)
	pSequence.AddAction(pAction, None, 22)

	pAction = LineAction("FekLeyr Targ\nGdluque\njb06\nJimmyB76\nMustang\nNebula\nShinzon\nThe Stig\ntrekie80", pPane, 14, 4, 12)
	pSequence.AddAction(pAction, None, 28)	

	pSequence.Play()

        # Grab the ObjID of the seq
        global pSeq
        pSeq = pSequence.GetObjID()
	
	return pSequence


# Add a line action 
def LineAction(sLine, pPane, fPos, duration, fontSize):
	fHeight = fPos * 0.0375
	App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
	pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
	return pAction


# Check keys pressed and kill the credits sequence if needed
def HandleKeyboard(pPane, pEvent):
        global pSeq, pSeq2

        # Basically this is from main menu
        KeyType = pEvent.GetKeyState()
	CharCode = pEvent.GetUnicode()

        # Check if esc key was pressed
        if KeyType == App.TGKeyboardEvent.KS_KEYUP:
            if (CharCode == App.WC_ESCAPE):
                pSequence = App.TGSequence_Cast(App.TGObject_GetTGObjectPtr(pSeq))
                pSequence2 = App.TGSequence_Cast(App.TGObject_GetTGObjectPtr(pSeq2))
                pSequence.Skip()
                pSequence2.Skip()
                pSeq = App.NULL_ID
                pSeq2 = App.NULL_ID

                BackToOptions (None)
                
                pEvent.SetHandled()

        if (pEvent.EventHandled() == 0):
		pPane.CallNextHandler(pEvent)


# Switch back to options
def BackToOptions(pAction):
	global pSeq2, pSeq
	pSeq = App.NULL_ID
        pSeq2 = App.NULL_ID

	App.g_kMovieManager.SwitchOutOfMovieMode()

        import MainMenu.mainmenu
        
	MainMenu.mainmenu.ShowWarpBackground (None, 0)

	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return

	pPane = App.g_kRootWindow.GetNthChild (0)
	App.g_kRootWindow.DeleteChild(pPane)

	pTopWindow.SetVisible ()

	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
	MainMenu.mainmenu.SetVisible (pOptionsWindow, 1)
	pTopWindow.DisableOptionsMenu (0)

	App.InterfaceModule_DoTheRightThing()

	return 0
