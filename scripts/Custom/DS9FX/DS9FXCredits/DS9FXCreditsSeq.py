# Play the credits sequence

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
        pAction = App.TGScriptAction_Create(__name__, "ShowSurprise")
        pAction.SetUseRealTime(1)
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

        pAction = LineAction("Project & Programming Lead:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 8)

        pAction = LineAction("USS Sovereign", pPane, 14, 4, 14)
        pSequence.AddAction(pAction, None, 9)

        pAction = LineAction("Project XO:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 15)

        pAction = LineAction("Psycho\nCordanilus", pPane, 14, 4, 12)
        pSequence.AddAction(pAction, None, 16)

        pAction = LineAction("Additional Programming:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 22)

        pAction = LineAction("Wowbagger\nLost_Jedi\nMLeo\nCackad\nSMBW", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 23)

        pAction = LineAction("Models/Textures/Retextures:", pPane, 10, 29, 18)
        pSequence.AddAction(pAction, None, 29)

        pAction = LineAction("LC Amaral\nBlaxxer\nSteven Davis\nZambie Zan\n9 of 9\nMark\nJestr", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 30)

        pAction = LineAction("Chronocidal Guy\nBlackrook32\nLaurelin\nSmiley\nAdonis\nC2X\nDark Drone", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 36)

        pAction = LineAction("P81\nPsycho\nCordanilus\nScotchy\nCaptainRussell\nSean Kennedy\nDurandal", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 42)

        pAction = LineAction("Jeff Wallace\nATRA-HASIS\nWickedZombie45\nRob Archer\nBren\nMRJOHN\nUNIMATRIX ONE", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 48)

        pAction = LineAction("jb06\nDamoclesX\nRedragon\nNeoXarchNova\nZorg / Morpheus\nCube\nCollective Alliance", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 54)

        pAction = LineAction("Hardpoints/Weapon Scripts:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 60)

        pAction = LineAction("Elminster\nPsycho\ntiqhud\nShinzon\nJimmyB76\nUSS Sovereign\nDkealt\nDurandal", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 61)
        
        pAction = LineAction("New Systems:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 67)

        pAction = LineAction("USS Sovereign\nNero", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 68)

        pAction = LineAction("Music/SFX/Dialogue:", pPane, 10, 11, 18)
        pSequence.AddAction(pAction, None, 74)

        pAction = LineAction("Kevin MacLeod (incompetech.com)\nMichael Kramer\nAustralia Telescope National Facility\nWes Janson\nBlackRook32", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 75)

        pAction = LineAction("Creative Inc\nC2X\nZambie Zan\nMRJOHN\nCaptainKeyes\nUSS Sovereign", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 81)

        pAction = LineAction("Logo Designs:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 87)

        pAction = LineAction("Psycho\nMark", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 88)

        pAction = LineAction("Videos:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 94)

        pAction = LineAction("Dante Leonhart\nCyberOps\nUSS Sovereign", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 95)

        pAction = LineAction("Mission Storylines:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 101)

        pAction = LineAction("CaptainKeyes\nBlaxxer\nDante Leonhart\ncordanilus", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 102)

        pAction = LineAction("Misc Credits:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 108)

        pAction = LineAction("MLeo\nNanobyte\nDefiant\nsneaker98\nDasher42", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 109)

        pAction = LineAction("Information Databases Used:", pPane, 10, 5, 18)
        pSequence.AddAction(pAction, None, 115)

        pAction = LineAction("http://memory-alpha.org/\nhttp://memory-beta.wikia.com/", pPane, 14, 4, 10)
        pSequence.AddAction(pAction, None, 116)

        pAction = LineAction("Special thanks to all Beta Testers, \n\n\nto everyone who supported this mod \n\n\nand everyone involved.", pPane, 10, 5, 14)
        pSequence.AddAction(pAction, None, 122)

        pAction = LineAction("We hope that you will enjoy this mod.\n\n\nDS9FX Team wishes you happy gaming.", pPane, 10, 5, 14)
        pSequence.AddAction(pAction, None, 129)

        pAction = LineAction("BCS : TNG Contact:\n\nhttp://bcs-tng.com/", pPane, 10, 5, 14)
        pSequence.AddAction(pAction, None, 136)

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

def ShowSurprise(pAction):
        from Custom.DS9FX.DS9FXPrompts import DS9FXEasterEggPrompt
        DS9FXEasterEggPrompt.Prompt()
        
        return 0
