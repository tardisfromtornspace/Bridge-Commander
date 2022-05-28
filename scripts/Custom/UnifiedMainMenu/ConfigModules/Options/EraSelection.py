from bcdebug import debug
###############################################################################
## Era Selection Config plugin for UMM			by Fernando Aluanu aka USS Frontier
#######
# UMM plugin for Era Plugin System,  sub-mod of Galaxy Charts.
# With this menu you'll be able to select the era in which you want to play.
# by using the Era plugins.
################################################################################
import App
import string
import nt
from Custom.GravityFX.GravityFXguilib import *
import Custom.Eras

pModule = __import__("SavedConfigs.SelectedEra")
pGUICreator = None
ET_PRESS = App.UtopiaModule_GetNextEventType()
pDefaultEraButton = None

#####################################################
## Required Functions for UMM
#############################################
def GetName():
	debug(__name__ + ", GetName")
	return "Era Selection"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
	debug(__name__ + ", CreateMenu")
	global pGUICreator
	pGUICreator = GUICreator()
	Custom.Eras.SetSelectedEraPlugin(pModule.Name)

	CreateEraSelectionMenu(pOptionsPane, pContentPanel)

	return App.TGPane_Create(0,0)
##########################################################


#####################################################
## Helper Functions
#############################################
def CreateEraSelectionMenu(pOptionsPane, pContentPanel):
	debug(__name__ + ", CreateEraSelectionMenu")
	global ET_PRESS, pDefaultEraButton

	lEraList = Custom.Eras.GetAllEraPlugins()
	ButtonDict = {'X': 0.0, 'Y': 0.0, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	for pEra in lEraList:
		sEraName = pEra.GetName()
		fValue = 0
		if sEraName == pModule.Name:
			fValue = 1
		pButton = pGUICreator.ButtonCreator.CreateYesNoButton(sEraName, ET_PRESS, None, fValue, pContentPanel, ButtonDict, ButtonDict)
		if sEraName == Custom.Eras.GetDefaultEraName():
			pButton.SetName(App.TGString(sEraName + " (DEFAULT)"))
			pDefaultEraButton = pButton
		ButtonDict["Y"] = ButtonDict["Y"] + ButtonDict["HEIGTH"]

	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_PRESS, App.TopWindow_GetTopWindow(), __name__+".ButtonPressed")

	return pContentPanel

def ButtonPressed(pObject, pEvent):
	debug(__name__ + ", ButtonPressed")
	pButton = pGUICreator.ButtonCreator.GetButtonByID(pEvent.GetSource().GetObjID())
	if pButton != None:
		if pButton.IsChosen() == 0:
			pButton.SetChosen(1)
		else:
			sSelectedEraName = Custom.Eras.GetSelectedEraPlugin().GetName()
			pOldButton = pGUICreator.ButtonCreator.GetButtonByName(sSelectedEraName)
			if pOldButton != None:
				pOldButton.SetChosen(0)
		if pButton.GetObjID() == pDefaultEraButton.GetObjID():
			sEraName = Custom.Eras.GetDefaultEraName()
		else:
			pName = App.TGString("")
			pButton.GetName(pName)
			sEraName = pName.GetCString()
		Custom.Eras.SetSelectedEraPlugin(sEraName)
		SaveEraSelectionConfig()
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def SaveEraSelectionConfig(pObject = None, pEvent = None):
	debug(__name__ + ", SaveEraSelectionConfig")
	ConfigPath  = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\SelectedEra.py"
	file = nt.open(ConfigPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
	sEraName = Custom.Eras.GetSelectedEraPlugin().GetName()
	nt.write(file, "# Saved Configuration File for the selected Era,   by USS Frontier" + "\n")
	nt.write(file, "Name = \"" + str(sEraName) + "\"\n")
	nt.close(file)

	pModule.Name = sEraName

	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)