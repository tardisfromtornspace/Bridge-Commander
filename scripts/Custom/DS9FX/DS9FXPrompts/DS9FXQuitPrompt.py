from bcdebug import debug
# by USS Sovereign, let's tell the user that he has to restart BC in order to allow the changes made to DS9FX to take effect

# Imports
import App

# Event types
ET_CLOSE = App.UtopiaModule_GetNextEventType()

# Start the script
def Prompt():
        debug(__name__ + ", Prompt")
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pOptionsWindow.AddPythonFuncHandlerForInstance(ET_CLOSE, __name__ + ".Close")
        
        StartWindow()

# Initiate Window
def StartWindow():
        # Bring up the modal dialog
        debug(__name__ + ", StartWindow")
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
        debug(__name__ + ", Close")
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
    
        pOptionsWindow.RemoveHandlerForInstance(ET_CLOSE, __name__ + ".Close")
        
        pObject.CallNextHandler(pEvent)
