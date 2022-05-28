from bcdebug import debug
###############################################################################################################
#   SaveGameGUI.py                 by Fernando Aluani
############
# This script that contains the code that sets up and handles the Save Game window, and its sub components
###############################################################################################################
import App
import MissionLib
import Foundation
import string
import nt
import Galaxy
import GalacticWarSimulator
import SavingSystem
import Custom.QBautostart.Libs.Races
from GalaxyLIB import *
from Custom.GravityFX.GravityFXguilib import *

pGUICreator = None
eRefresh = None
ET_SAVE_GAME = None
#####################################################################
def CreateSaveGameGUI():
	debug(__name__ + ", CreateSaveGameGUI")
	global pGUICreator, ET_SAVE_GAME
	if GalacticWarSimulator.WarSimulator.IsInitialized() == 0:
		return
	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
	pBridge = App.g_kSetManager.GetSet("bridge")
	pXO = App.CharacterClass_GetObject(pBridge, "XO")
	if pXO == None:
		return
	pXOMenu = pXO.GetMenu()
	if pXOMenu == None:
		return

	if pGUICreator == None:
		pGUICreator = GUICreator()

	ET_SAVE_GAME = GetNextEventType()
	
	pButton = pGUICreator.ButtonCreator.CreateButton("Save Game...", ET_SAVE_GAME, None, 1, pXOMenu)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SAVE_GAME, pMission, __name__ + ".SGOpenClose")

	pXO.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".SGClose")
	#App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__ + ".TIHandler")


def SGOpenClose(pObject = None, pEvent = None):
	debug(__name__ + ", SGOpenClose")
	global pGUICreator
	pSG = pGUICreator.GetElement("Save War Simulator")
	if not pSG:
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		pGUICreator.SetInfoForName("Save War Simulator", 0.2, 0.2, 0.6, 0.6, 0)
		pSG = pGUICreator.CreateWindow("Save War Simulator", pTCW)
		pSG.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pSG.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		CreateSGStaticContents(pSG)
	if pSG.IsVisible():
		pGUICreator.CloseElement("Save War Simulator")
	else:
		pGUICreator.ShowElement("Save War Simulator")
	
		
def SGClose(pObject = None, pEvent = None):
	debug(__name__ + ", SGClose")
	if pGUICreator != None:
		pGUICreator.CloseElement("Save War Simulator")
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def CreateSGStaticContents(pSG):
	# Create static GUI contents.
	debug(__name__ + ", CreateSGStaticContents")
	dTICoords = {'X': 0.07, 'Y': 0.1}
	AddTextInput("Type here", 0.2, dTICoords)

	pGUICreator.SetInfoForName("TInfoPara", 0.07, 0.08)
	pGUICreator.CreateParagraph("TInfoPara", ["Type in the name of your save game file here."], pSG)

	pGUICreator.SetInfoForName("TInfoPara2", 0.10, 0.2)
	pPara = pGUICreator.CreateParagraph("TInfoPara2", ["After selecting the name of your saved game, press the Save Game button below. Saving a game with an already existing name will overwrite the old save file. Also, it is advised to save the game when there is little 'action' happening."], pSG)
	pPara.SetWrapWidth(0.22)

	pGUICreator.SetInfoForName("Saved Games List", 0.4, 0.0, 0.2, 0.55, 1)
	pSGL = pGUICreator.CreateWindow("Saved Games List", pSG)
	pSGL.SetUseScrolling(1)
	pSGL.SetScrollViewHeight(25.0)

	pGUICreator.SetInfoForName("SaveGamesPara", 0.0, 0.0)
	pPara = pGUICreator.CreateParagraph("SaveGamesPara", [], pSGL)
	pPara.SetWrapWidth(0.19)
	UpdateSaveGameFileNames()

	ButtonDict = {'X': 0.02, 'Y': 0.45, 'WIDTH': 0.16, 'HEIGTH': 0.04}
	pGUICreator.ButtonCreator.CreateButton("Save Game", None, __name__ + ".SaveGameClick", 1, pSG, ButtonDict, ButtonDict)

	ButtonDict = {'X': 0.2, 'Y': 0.45, 'WIDTH': 0.16, 'HEIGTH': 0.04}
	pGUICreator.ButtonCreator.CreateButton("Close", None, __name__ + ".SGClose", 1, pSG, ButtonDict, ButtonDict)

	return

def UpdateSaveGameFileNames():
	debug(__name__ + ", UpdateSaveGameFileNames")
	if pGUICreator == None:
		return
	NamesList = nt.listdir('scripts/Custom/GalaxyCharts/GameSaves')

	lToBeRemoved = ['__init__.py', '__init__.pyc']
	for sRemovee in lToBeRemoved:
		if sRemovee in NamesList:
			NamesList.remove(sRemovee)

	lNamesChecked = []
	lStrList = []

	for sFile in NamesList:
		sFileStrings = string.split(sFile, '.')
		sSaveName = sFileStrings[0]
		sExt = sFileStrings[-1]
		if (sExt == "py" or sExt == "pyc") and (not sSaveName in lNamesChecked):
			lNamesChecked.append(sSaveName)
			lStrList.append("-"+str(sSaveName))
	
	if len(lStrList) <= 0:
		lStrList.append("> NO SAVE GAME FILES DETECTED.")

	pPara = pGUICreator.GetElement("SaveGamesPara")
	pGUICreator.UpdateParagraph("SaveGamesPara", lStrList)
	pPara.SetPosition(0.0, 0.0)

#######################

def SaveGameClick(pObject = None, pEvent = None):
	debug(__name__ + ", SaveGameClick")
	if pGUICreator == None:
		return
	sSaveGameName = pTI[1].GetCString()
	sMessageBoxName = "Save Game Message"
	if len(sSaveGameName) < 4:
		pGUICreator.CreateMessageBox(sMessageBoxName, "The name of your save game file should have 4 or more letters.")
		return
	if SavingSystem.IsLoading() == 1:
		pGUICreator.CreateMessageBox(sMessageBoxName, "Can't save game, Saving System is busy.")
		return
	bOK = SavingSystem.Save(sSaveGameName)
	if bOK == 0:
		pGUICreator.CreateMessageBox(sMessageBoxName, "ERROR: Couldn't save game. Possibly due to an ERROR or because a ship is travelling.")
	if bOK == 1:
		pGUICreator.CreateMessageBox(sMessageBoxName, "Game saved succesfully!")
	UpdateSaveGameFileNames()
	return

pTI = []
def AddTextInput(sDefaultValue, fMaxWidth, Coords):
	debug(__name__ + ", AddTextInput")
	if pGUICreator == None:
		return
	global pTI
	pDefault = App.TGString(sDefaultValue)
	sName = "SaveGame Text Input"
	sConfigName = "SaveGame Text InputC"
	pParent = pGUICreator.GetElement("Save War Simulator")
	iMaxCharNum = 30
	fLongestLength = 0.0
	pTI = pGUICreator.ButtonCreator.CreateTextInput(sName, pParent, pDefault, fMaxWidth, fLongestLength, sConfigName, iMaxCharNum, 1, None, Coords)
	#pTI[0].AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".TIHandler")
	pTI[1].SetIgnoreString("1234567890!@#$%¨&*()¹²³£¢¬§-_=+|\\´`[{~^]},<.>;:/?°ºª\"\'\n\r")
	pTI[0].SetVisible()
	pTI[1].SetVisible()

def TIHandler(pObject, pEvent):
	debug(__name__ + ", TIHandler")
	global bTIselected
	if len(pTI) >= 2:
		if bTIselected == 1:
			iUnicode = pEvent.GetUnicode()
			kDisplayString = App.g_kInputManager.GetDisplayStringFromUnicode(iUnicode)
			sKey = kDisplayString.GetCString()
			#print "TIH: ok -", sKey
			pTI[1].AppendString(sKey)
		else:
			#print "TIH: nope"
			pObject.CallNextHandler(pEvent)
	else:
		#print "TIH: ..."
		pObject.CallNextHandler(pEvent)
		#if pEvent.EventHandled() == 0:
		#	pEvent.SetHandled()

bTIselected = 0
def MouseHandler(pObject, pEvent):
	debug(__name__ + ", MouseHandler")
	global bTIselected
	pObject.CallNextHandler(pEvent)
	if pEvent.EventHandled() == 0:
		pEvent.SetHandled()
	MouseX = pEvent.GetX()
	MouseY = pEvent.GetY()
	if pEvent.IsButtonEvent():
		nNum = pEvent.GetButtonNum()
		if nNum == App.TGMouseEvent.MEF_BUTTON_LEFT:
			pPOS = App.NiPoint2(0,0)
			pTI[0].GetPosition(pPOS)
			X, Y = pPOS.x, pPOS.y
			EndX, EndY = X+pTI[0].GetWidth(), Y+pTI[0].GetHeight()
			if X <= MouseX <= EndX and Y <= MouseY <= EndY:
				bTIselected = 1
				#isolateWindow()
			else:
				bTIselected = 0
				#normalizeWindow()
		elif nNum == App.TGMouseEvent.MEF_BUTTON_RIGHT:
			bTIselected = 0
			#normalizeWindow()

pOldFocus = None
def isolateWindow():
	debug(__name__ + ", isolateWindow")
	global pOldFocus
	pParent = pGUICreator.GetElement("Save War Simulator")
	pOldFocus = pTopWindow.GetFocus()
	pTopWindow.MoveToFront(pParent)
	pTopWindow.SetFocus(pParent)
	pParent.SetAlwaysHandleEvents()

def normalizeWindow():
	debug(__name__ + ", normalizeWindow")
	global pOldFocus
	pParent = pGUICreator.GetElement("Save War Simulator")
	pTopWindow = App.TopWindow_GetTopWindow()
	pTopWindow.MoveToBack(pParent)
	pTopWindow.SetFocus(pOldFocus)
	pParent.SetNotAlwaysHandleEvents()


def KeyHandler(pObject, pEvent):
	debug(__name__ + ", KeyHandler")
	pObject.CallNextHandler(pEvent)
	if pEvent.EventHandled() == 0:
		pEvent.SetHandled()