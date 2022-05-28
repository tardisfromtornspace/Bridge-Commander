# by USS Sovereign, Modal Dialog Window based on the quit prompt. Select which credits seq. should be played

# Imports
import App

# Event types
ET_TEAM = App.UtopiaModule_GetNextEventType()
ET_BETA = App.UtopiaModule_GetNextEventType()


# Start the script
def Prompt():
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.AddPythonFuncHandlerForInstance(ET_TEAM, __name__ + ".Team")
        pOptionsWindow.AddPythonFuncHandlerForInstance(ET_BETA, __name__ + ".Beta")

        StartWindow()

# Initiate Window
def StartWindow():
        # Bring up the modal dialog
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
        pModalDialogWindow = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MODAL_DIALOG))

        # Define events
        pBetaEvent = App.TGStringEvent_Create()
        pBetaEvent.SetEventType(ET_BETA)
        pBetaEvent.SetString("BetaSquad")
        pBetaEvent.SetDestination(pOptionsWindow)

        pTeamEvent = App.TGStringEvent_Create()
        pTeamEvent.SetEventType(ET_TEAM)
        pTeamEvent.SetString("ProductionTeam")
        pTeamEvent.SetDestination(pOptionsWindow)

        # Load the database
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/DS9FXPromptDatabase.tgl")

        pTitle = pDatabase.GetString("CreditsTittle")
        pText = pDatabase.GetString("CreditsSel")
        pBeta = pDatabase.GetString("Beta")
        pTeam = pDatabase.GetString("Team")

        # Unload database
        App.g_kLocalizationManager.Unload(pDatabase)

        # Run the dialog window
        pModalDialogWindow.Run(pTitle, pText, pTeam, pTeamEvent, pBeta, pBetaEvent)


# Play the seq and remove handlers
def Team(pObject, pEvent):
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.RemoveHandlerForInstance(ET_BETA, __name__ + ".Beta")
        pOptionsWindow.RemoveHandlerForInstance(ET_TEAM, __name__ + ".Team")

        # import and play the team seq
        from Custom.DS9FX.DS9FXCredits import DS9FXCreditsSeq

        DS9FXCreditsSeq.PlaySeq(None, None)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)


# Play the seq and remove handlers
def Beta(pObject, pEvent):
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.RemoveHandlerForInstance(ET_BETA, __name__ + ".Beta")
        pOptionsWindow.RemoveHandlerForInstance(ET_TEAM, __name__ + ".Team")

        # import and play the beta seq
        from Custom.DS9FX.DS9FXCredits import DS9FXCreditsBetaSeq

        DS9FXCreditsBetaSeq.PlaySeq(None, None)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
