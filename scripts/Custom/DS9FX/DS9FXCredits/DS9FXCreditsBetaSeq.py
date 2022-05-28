# Play the beta credits sequence

# by USS Sovereign

# Imports
import App

# Vars
pSeq = App.NULL_ID
pSeq2 = App.NULL_ID

# DS9FX Version
pDS9FXVer = __import__("Custom.DS9FX.DS9FXVersionSignature")
pVer = pDS9FXVer.DS9FXVersion

def PlaySeq(pAction, pEvent):

        DS9FXCredits(None, None)

def DS9FXCredits(pObject, pEvent):
        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return

        pTopWindow.SetNotVisible()

        pTopWindow.DisableOptionsMenu(1)

        pPane = App.TGPane_Create(1.0, 1.0)
        App.g_kRootWindow.PrependChild(pPane)


        pPane.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD,	__name__ + ".HandleKeyboard")

        import MainMenu.mainmenu

        MainMenu.mainmenu.StopBackgroundMovies()

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.AddAction(App.TGScriptAction_Create("MainMenu.mainmenu", "ShowWarpBackground", 1))
        pSequence.AppendAction(CreditsSeq(pPane))
        pAction = App.TGScriptAction_Create(__name__, "BackToOptions")
        pAction.SetUseRealTime (1)
        pSequence.AppendAction(pAction, 1.0)
        pSequence.Play()

        global pSeq2
        pSeq2 = pSequence.GetObjID()


def CreditsSeq(pPane):
        App.InterfaceModule_DoTheRightThing()

        pSequence = App.TGSequence_Create()
        pSequence.SetUseRealTime (1)
        pSequence.SetSkippable(1)

        pAction = LineAction("DS9FX " + pVer, pPane, 8, 6, 20)
        pSequence.AddAction(pAction, None, 0)

        pAction = LineAction("by", pPane, 13, 5, 15)
        pSequence.AddAction(pAction, None, 1)

        pAction = LineAction("BCS : TNG", pPane, 18, 4, 18)
        pSequence.AddAction(pAction, None, 2)

        pAction = LineAction("Beta Squad:", pPane, 10, 11, 18)
        pSequence.AddAction(pAction, None, 8)

        pAction = LineAction("AndrewJ\nB.C. Xtreme\nBlackrook32\nBren\nCaptainGMAN\ncordanilus\nDalek\nDante Leonhart\ndenster\nEaglePryde\nFekLeyr Targ", pPane, 14, 4, 9)
        pSequence.AddAction(pAction, None, 9)

        pAction = LineAction("Jb06\nJimmyB76\nkirk2164\nlimey98\nNebula\nNero\nsbpaabck\nShinzon\nSMBW\nThe Stig\ntiqhud\ntrekie80", pPane, 14, 4, 9)
        pSequence.AddAction(pAction, None, 15)

        pAction = LineAction("Thanks to all past and present Beta Testers.", pPane, 10, 5, 14)
        pSequence.AddAction(pAction, None, 21)

        pSequence.Play()

        global pSeq
        pSeq = pSequence.GetObjID()

        return pSequence

def LineAction(sLine, pPane, fPos, duration, fontSize):
        fHeight = fPos * 0.0375
        App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
        pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
        return pAction

def HandleKeyboard(pPane, pEvent):
        global pSeq, pSeq2

        KeyType = pEvent.GetKeyState()
        CharCode = pEvent.GetUnicode()

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
                if pPane and pEvent:
                        pPane.CallNextHandler(pEvent)

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
        App.g_kRootWindow.DeleteChild (pPane)

        pTopWindow.SetVisible ()

        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
        MainMenu.mainmenu.SetVisible (pOptionsWindow, 1)
        pTopWindow.DisableOptionsMenu (0)

        App.InterfaceModule_DoTheRightThing()

        return 0
