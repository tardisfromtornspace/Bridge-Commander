from bcdebug import debug
###############################################################################################################
#   ChronoInfoGUI.py                 by Fernando Aluani
############
# This script is the one that contains the code which sets up and handled the Chronological Info GUI
# in the Science Menu
###############################################################################################################
import App
import MissionLib
import string
from Custom.GravityFX.GravityFXguilib import *
import Custom.Eras

pGUICreator = None
ET_CHRONO_INFO = None
bIsOpened = 0

#####################################################################
def CreateCIGUI():
	debug(__name__ + ", CreateCIGUI")
	global ET_CHRONO_INFO, pGUICreator

	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
	pBridge = App.g_kSetManager.GetSet("bridge")
	pScience = App.CharacterClass_GetObject(pBridge, "Science")
	if pScience == None:
		return
	pScienceMenu = pScience.GetMenu()
	if pScienceMenu == None:
		return

	pGUICreator = GUICreator()

	ET_CHRONO_INFO = GetNextEventType()
	
	pGUICreator.ButtonCreator.CreateButton("Chronological Info", ET_CHRONO_INFO, None, 1, pScienceMenu)
	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CHRONO_INFO, pMission, __name__ + ".CIOpenClose")
	pScience.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CIClose")



def CIOpenClose(pObject = None, pEvent = None):
	debug(__name__ + ", CIOpenClose")
	global bIsOpened
	pCI = pGUICreator.GetElement("Chronological Info")
	if not pCI:
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		pGUICreator.SetInfoForName("Chronological Info", 0.3, 0.1, 0.5, 0.6, 0)
		pCI = pGUICreator.CreateWindow("Chronological Info", pTCW)
		pCI.SetUseScrolling(1)
		pCI.SetScrollViewHeight(25.0)
		pCI.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pCI.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		pGUICreator.SetInfoForName("Actions Menu", 0.3, 0.7, 0.5, 0.15, 0)
		pAM = pGUICreator.CreateWindow("Actions Menu", pTCW)
		pAM.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pAM.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		CreateCIStaticContents(pCI, pAM)
	if pCI.IsVisible():
		pGUICreator.CloseElement("Chronological Info")
		pGUICreator.CloseElement("Actions Menu")
		bIsOpened = 0
	else:
		pGUICreator.ShowElement("Chronological Info")
		pGUICreator.ShowElement("Actions Menu")
		bIsOpened = 1
		UpdateChronologicalInfo()
	
		
def CIClose(pObject = None, pEvent = None):
	debug(__name__ + ", CIClose")
	global bIsOpened 
	if pGUICreator != None:
		pGUICreator.CloseElement("Chronological Info")
		pGUICreator.CloseElement("Actions Menu")
	bIsOpened = 0
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def CreateCIStaticContents(pCI, pAM):
	# Create static GUI contents.
	debug(__name__ + ", CreateCIStaticContents")
	ButtonDict = {'X': 0.01, 'Y': 0.05, 'WIDTH': 0.18, 'HEIGTH': 0.03}
	pGUICreator.ButtonCreator.CreateButton("Close", None, __name__ + ".CIClose", 1, pAM, ButtonDict, ButtonDict)


# Create dynamic GUI contents.
def UpdateChronologicalInfo():
	debug(__name__ + ", UpdateChronologicalInfo")
	global bIsOpened
	if bIsOpened == 0 or pGUICreator == None:
		return
	
	pCI = pGUICreator.GetElement("Chronological Info")

	sList = []
	
	pEraPlugin = Custom.Eras.GetSelectedEraPlugin()
	if pEraPlugin != None:
		sList.append(">>> Displaying information about current era.")
		sList.append("")
		sList.append("")
		sList.append("Era Name: "+pEraPlugin.GetName())
		sList.append("")
		sList.append("Stardate Range: from "+str(pEraPlugin.GetInitialStardate())+" to "+str(pEraPlugin.GetEndingStardate()))
		sList.append("")
		sList.append("Description:")
		for sDescLine in pEraPlugin.GetDescriptionLines():
			sList.append("   "+sDescLine)
	else:
		sList.append("         *****  ERROR  *****")
		sList.append("")
		sList.append(" > Couldn't get information from the Selected Era")
		sList.append("")
		sList.append("         *****  ERROR  *****")

	#####
	# Create/update the era description paragraph
	pPara = pGUICreator.GetElement("ChronoInfoParag")
	if pPara == None:
		pGUICreator.SetInfoForName("ChronoInfoParag", 0, 0, 0.45, 25.0)
		pPara = pGUICreator.CreateParagraph("ChronoInfoParag", sList, pCI)
		pPara.SetWrapWidth(0.47)
	else:
		pGUICreator.UpdateParagraph("ChronoInfoParag", sList)
		pPara.SetPosition(0, 0)

	pCI.SetUseScrolling(1)
	pCI.SetScrollViewHeight(25.0)
	return

def MouseHandler(pObject, pEvent):
	debug(__name__ + ", MouseHandler")
	pObject.CallNextHandler(pEvent)
	if pEvent.EventHandled() == 0:
		pEvent.SetHandled()


def KeyHandler(pObject, pEvent):
	debug(__name__ + ", KeyHandler")
	pObject.CallNextHandler(pEvent)
	if pEvent.EventHandled() == 0:
		pEvent.SetHandled()