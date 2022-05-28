# by USS Sovereign

# Imports
import App

# Event types
ET_CLOSE = App.UtopiaModule_GetNextEventType()

# Start the script
def Prompt():
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.AddPythonFuncHandlerForInstance(ET_CLOSE, __name__ + ".Close")

        StartWindow()

# Initiate Window
def StartWindow():
        # Bring up the modal dialog
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
        pModalDialogWindow = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MODAL_DIALOG))

        # Define events
        pCloseEvent = App.TGStringEvent_Create()
        pCloseEvent.SetEventType(ET_CLOSE)
        pCloseEvent.SetString("Closing")
        pCloseEvent.SetDestination(pOptionsWindow)

        # Load the database
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/DS9FXPromptDatabase.tgl")

        pTitle = pDatabase.GetString("Title")
        pText = pDatabase.GetString("Text")
        pClose = pDatabase.GetString("Close")

        # Unload database
        App.g_kLocalizationManager.Unload(pDatabase)

        # Run the dialog window
        pModalDialogWindow.Run(pTitle, pText, pClose, pCloseEvent, None, None)


# Remove events
def Close(pObject, pEvent):
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.RemoveHandlerForInstance(ET_CLOSE, __name__ + ".Close")

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)
