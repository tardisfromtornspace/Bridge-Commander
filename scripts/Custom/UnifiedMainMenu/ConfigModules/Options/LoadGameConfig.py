from bcdebug import debug
###############################################################################
## Load Game Selection Config plugin for UMM			by USS Frontier
#######
# UMM plugin for Saving System,  sub-mod of Galaxy Charts.
# With this menu you'll be able to select the game to load when QB is initialized
# if the War Simulator is online.
################################################################################
import App
import string
import nt
from Custom.GravityFX.GravityFXguilib import *

pModule = __import__("SavedConfigs.SelectedSaveGame")
pGUICreator = None
ET_PRESS = App.UtopiaModule_GetNextEventType()

#####################################################
## Required Functions for UMM
#############################################
def GetName():
	debug(__name__ + ", GetName")
	return "WarSimulator: Save Game to Load"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
	debug(__name__ + ", CreateMenu")
	global pGUICreator
	pGUICreator = GUICreator()

	CreateSelectionMenu(pOptionsPane, pContentPanel)

	return App.TGPane_Create(0,0)
##########################################################


#####################################################
## Helper Functions
#############################################
def CreateSelectionMenu(pOptionsPane, pContentPanel):
	debug(__name__ + ", CreateSelectionMenu")
	global ET_PRESS, pDefaultEraButton

	NamesList = nt.listdir('scripts/Custom/GalaxyCharts/GameSaves')

	lToBeRemoved = ['__init__.py', '__init__.pyc']
	for sRemovee in lToBeRemoved:
		if sRemovee in NamesList:
			NamesList.remove(sRemovee)

	lNamesChecked = []
	lNames = ["None"]

	for sFile in NamesList:
		sFileStrings = string.split(sFile, '.')
		sSaveName = sFileStrings[0]
		sExt = sFileStrings[-1]
		if (sExt == "py" or sExt == "pyc") and (not sSaveName in lNamesChecked):
			lNamesChecked.append(sSaveName)
			lNames.append(str(sSaveName))

	ButtonDict = {'X': 0.0, 'Y': 0.0, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	for sSaveGameName in lNames:
		fValue = 0
		if sSaveGameName == pModule.Name:
			fValue = 1
		pButton = pGUICreator.ButtonCreator.CreateYesNoButton(sSaveGameName, ET_PRESS, None, fValue, pContentPanel, ButtonDict, ButtonDict)
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
			sOldGameSelected = pModule.Name
			pOldButton = pGUICreator.ButtonCreator.GetButtonByName(sOldGameSelected)
			if pOldButton != None:
				pOldButton.SetChosen(0)
		pName = App.TGString("")
		pButton.GetName(pName)
		sSelectedGame = pName.GetCString()
		SaveSelectionConfig(sSelectedGame)
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def SaveSelectionConfig(sSelectedGame):
	debug(__name__ + ", SaveSelectionConfig")
	ConfigPath  = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\SelectedSaveGame.py"
	file = nt.open(ConfigPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
	nt.write(file, "# Saved Configuration File for the selected save game,   by USS Frontier" + "\n")
	nt.write(file, "Name = \"" + str(sSelectedGame) + "\"\n")
	nt.close(file)

	pModule.Name = sSelectedGame