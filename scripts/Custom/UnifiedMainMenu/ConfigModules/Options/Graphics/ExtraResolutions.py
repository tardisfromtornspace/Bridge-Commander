from bcdebug import debug

import App
import MainMenu.mainmenu
from Custom.NanoFXv2 import NanoFX_Config

# when adding a new resolution, also add a new file LCARS_ABCD.py to scripts/Icons
lResolutions = [
(1366, 768),
(1440, 900),
(1600, 900),
(1680, 1050),
(1920, 1080),
(1920, 1200),
]



ET_SELECT_BUTTON = App.UtopiaModule_GetNextEventType()
ET_CONFIRM = App.UtopiaModule_GetNextEventType()


def GetName():
	debug(__name__ + ", GetName")
	return "Additional Resolutions"


def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
	debug(__name__ + ", CreateMenu")
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_SELECT_BUTTON, __name__ + ".HandleSelectButton")
	pTopWindow.AddPythonFuncHandlerForInstance(ET_CONFIRM, __name__ + ".HandleConfirmation")

	for i in range(len(lResolutions)):
		pEvent = App.TGIntEvent_Create()
		pEvent.SetEventType(ET_SELECT_BUTTON)
		pEvent.SetInt(i)
		pEvent.SetDestination(pOptionsWindow)
		s = "%d x %d" % (lResolutions[i][0], lResolutions[i][1])
		pButton = App.STButton_Create(s, pEvent)
		pContentPanel.AddChild(pButton)
    
	return App.TGPane_Create(0,0)


def HandleConfirmation(pObject, pEvent):
	debug(__name__ + ", HandleConfirmation")
	pObject.CallNextHandler(pEvent)

	i = pEvent.GetInt()
	if i >= 0:
		App.g_kConfigMapping.SetIntValue("Graphics Options", "Display Width", lResolutions[i][0])
		App.g_kConfigMapping.SetIntValue("Graphics Options", "Display Height", lResolutions[i][1])
		App.g_kConfigMapping.SaveConfigFile("options.cfg")

		import sys
		sys.exit()


def HandleSelectButton(pObject, pEvent):
	debug(__name__ + ", HandleSelectButton")
	pObject.CallNextHandler(pEvent)
	
	i = pEvent.GetInt()

	pTopWindow = App.TopWindow_GetTopWindow()
	pModalDialogWindow = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MODAL_DIALOG))
	pOkayEvent = App.TGIntEvent_Create()
	pOkayEvent.SetEventType(ET_CONFIRM)
	pOkayEvent.SetDestination(pTopWindow)
	pOkayEvent.SetInt(i)

	pCancelEvent = App.TGIntEvent_Create ()
	pCancelEvent.SetEventType(ET_CONFIRM)
	pCancelEvent.SetDestination(pTopWindow)
	pCancelEvent.SetInt(-1)
	
	pTitle = App.TGString("Change Resolution:")
	pOkay = App.TGString("OK")
	pCancel = App.TGString("Cancel")
	pText = App.TGString("""
	Change Resolution?\n
	\n
	This will require a restart.\n
	Clicking yes will quit the Game!
	""")

	pModalDialogWindow.Run (pTitle, pText, pOkay, pOkayEvent, pCancel, pCancelEvent)

