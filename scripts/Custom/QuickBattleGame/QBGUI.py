import App

import Foundation
import FoundationMenu

import QBFile
import Lib.Ambiguity

systemMenuBuilder = None
shipMenuBuilder = None
bridgeMenuBuilder = None
qbGameMode = None
g_pMissionDatabase = None

TRUE = 1
FALSE = 0

ET_START_BUTTON = None

g_pMainMenu = None
g_pMainPanel = None
g_pActivePanel = None

g_pShipList = None
g_pShipListWindow = None
g_pRegionListWindow = None
g_pRegionList = None
g_pEdName = None
g_pEdX = None
g_pEdY = None
g_pEdZ = None
g_pEdAI = None
g_pEdMinDamage = None
g_pEdMaxDamage = None
g_pEdMinETA = None
g_pEdMaxETA = None
g_pAIMenu = None
g_pGroupMenu = None
g_pShipSystemMenu = None
g_pSelShipSystem = None
g_pShipsIcon = None
g_pShipsTextWindow = None
g_pStarbaseButton = None
g_pWarpButton = None
g_pBridgeList = None
g_pLoadMenu = None
g_pLoadWindow = None
g_pCriticalButton = None

g_pSelectedShip = None
g_pSelectedRegion = None
g_iSelectedAILevel = None
g_iSelectedGroup = None
g_sSelectedFile = 'QBSetup'
g_pEdSelectedFile = None

BAR_HEIGHT				= 0.0291666

AI_MENU_Y_POS				= 0.54583
AI_MENU_WIDTH				= 0.12
AI_MENU_HEIGHT				= 0.19125

MAINFRAME_X=0.05
MAINFRAME_Y=0.025
MAINFRAME_W=0.9
MAINFRAME_H=0.95

PANEL1_X=0.025
PANEL1_Y=0.075
PANEL1_W=0.175
PANEL1_H=0.825

CLOSEBUTTON_X=0
CLOSEBUTTON_Y=0
CLOSEBUTTON_W=0.125
CLOSEBUTTON_H=0.041

STARTBUTTON_X=0
STARTBUTTON_Y=0.048
STARTBUTTON_W=0.125
STARTBUTTON_H=0.041

MAINMENU_X=0
MAINMENU_Y=0.125
MAINMENU_W=0.175
MAINMENU_H=0.7

DETAILPANEL_X=0.225
DETAILPANEL_Y=0.075
DETAILPANEL_W=0.65
DETAILPANEL_H=0.825

SHIPMENU_X=0.018
SHIPMENU_Y=0.03
SHIPMENU_W=0.175
SHIPMENU_H=0.55

SELECTEDSHIPSMENU_X=0.475
SELECTEDSHIPSMENU_Y=0.03
SELECTEDSHIPSMENU_W=0.175
SELECTEDSHIPSMENU_H=0.55

BRIDGEMENU_X=0.019
BRIDGEMENU_Y=0.6
BRIDGEMENU_W=0.174
BRIDGEMENU_H=0.205

SHIPICON_X=0.475
SHIPICON_Y=0.6
SHIPICON_W=0.174
SHIPICON_H=0.205

UPDATEBUTTON_X=0.201
UPDATEBUTTON_Y=0.752
UPDATEBUTTON_W=0.125
UPDATEBUTTON_H=0.041

DELETEBUTTON_X=0.339
DELETEBUTTON_Y=0.75
DELETEBUTTON_W=0.125
DELETEBUTTON_H=0.04


def Init(pMission):
	InitGlobals(pMission)
	InitDialog()
	
def Remove():
	global g_pShipList
	global g_pShipListWindow
	global g_pEdName
	global g_pRegionListWindow
	global g_pRegionList

	g_pShipList = None
	g_pShipListWindow = None
	g_pRegionListWindow = None
	g_pRegionList = None
	g_pEdName = None
	
	global qbGameMode
	qbGameMode.Deactivate()
	qbGameMode = None

def InitGlobals(pMission):
	global g_pMissionDatabase
	g_pMissionDatabase = pMission.SetDatabase("data/TGL/QuickBattle/QuickBattle.tgl")

	global systemMenuBuilder, shipMenuBuilder, bridgeMenuBuilder
	systemMenuBuilder = FoundationMenu.SystemMenuBuilderDef(g_pMissionDatabase)
	shipMenuBuilder = FoundationMenu.ShipMenuBuilderDef(g_pMissionDatabase)
	bridgeMenuBuilder = FoundationMenu.BridgeMenuBuilderDef(g_pMissionDatabase)

	global qbGameMode
	qbGameMode = Foundation.BuildGameMode()
	qbGameMode.Activate()

def InitDialog():
	Lib.Ambiguity.addEventHandler("XO", "ET_CLOSE_DIALOG", __name__ + ".CloseDialog")
	Lib.Ambiguity.addEventHandler("XO", "ET_SELECT_SHIP", __name__ + ".SelectShip")
	Lib.Ambiguity.addEventHandler("XO", "ET_SELECT_SHIPLIST", __name__ + ".SelectShipList")
	Lib.Ambiguity.addEventHandler("XO", "ET_START_BUTTON", __name__ + ".StartSimulation")
	Lib.Ambiguity.addEventHandler("XO", "ET_SELECT_AI", __name__ + ".SelectAI")
	Lib.Ambiguity.addEventHandler("XO", "ET_SELECT_GROUP", __name__ + ".SelectGroup")
	Lib.Ambiguity.addEventHandler("XO", "ET_SELECT_SYSTEM", __name__ + ".SelectSystem")
	Lib.Ambiguity.addEventHandler("XO", "ET_SELECT_REGIONLIST", __name__ + ".SelectRegionList")
	Lib.Ambiguity.addEventHandler("XO", "ET_SELECT_SHIPSYSTEM", __name__ + ".SelectShipSystem")
	Lib.Ambiguity.addEventHandler("XO", "ET_SELECT_BRIDGE", __name__ + ".SelectBridge")
	Lib.Ambiguity.addEventHandler("XO", "ET_SELECT_FILE", __name__ + ".SelectGame")
	
	global ET_START_BUTTON
	ET_START_BUTTON = Lib.Ambiguity.getEvent("ET_START_BUTTON")

	pForm = Lib.Ambiguity.createForm("MainForm", 1.0, 1.0, FALSE)
	pMainPanel = Lib.Ambiguity.createPanel(pForm, "MainPanel", MAINFRAME_X, MAINFRAME_Y, MAINFRAME_W, MAINFRAME_H)
	global g_pMainPanel
	g_pMainPanel = pMainPanel
	
	pFrame = Lib.Ambiguity.createFrame(pMainPanel, "QuickBattle Configuration", 0.0, 0.0, MAINFRAME_W, MAINFRAME_H, "NoMinimize", App.g_kMainMenuBorderMainColor)
	pFrame.SetUseScrolling(0)

	pPanel = Lib.Ambiguity.createPanel(pMainPanel, "MenuPanel", PANEL1_X, PANEL1_Y, PANEL1_W, PANEL1_H)
	pMainPanel.MoveToFront(pPanel)

	Lib.Ambiguity.createMainMenuButton(pPanel, "Close", Lib.Ambiguity.getEvent("ET_CLOSE_DIALOG"), "Close", "XO", CLOSEBUTTON_X, CLOSEBUTTON_Y, CLOSEBUTTON_W, CLOSEBUTTON_H)
	Lib.Ambiguity.createMainMenuButton(pPanel, "Start", Lib.Ambiguity.getEvent("ET_START_BUTTON"), "Start", "XO", STARTBUTTON_X, STARTBUTTON_Y, STARTBUTTON_W, STARTBUTTON_H)
	
	menudef = [["Ships"], ["Systems"], ["File"]]
	
	event = Lib.Ambiguity.addEventHandler("XO", "ET_MENUBUTTON", __name__ + ".MenuButton")
	global g_pMainMenu
	g_pMainMenu = Lib.Ambiguity.createMenu(pPanel, "Mainmenu", event, "XO", menudef, MAINMENU_X, MAINMENU_Y, MAINMENU_W, MAINMENU_H)
	
	# ShipPanel
	pShipPanel = Lib.Ambiguity.createPanel(pMainPanel, "ShipPanel", DETAILPANEL_X, DETAILPANEL_Y, DETAILPANEL_W, DETAILPANEL_H)
	pMainPanel.MoveToFront(pShipPanel)

	pMenu = GenerateShipMenu()
	pShipPanel.AddChild(pMenu, SHIPMENU_X, SHIPMENU_Y)
	pShipPanel.MoveToFront(pMenu)	
	
	pMenu = GenerateShipList()
	pShipPanel.AddChild(pMenu, SELECTEDSHIPSMENU_X, SELECTEDSHIPSMENU_Y)
	pShipPanel.MoveToFront(pMenu)	

	pMenu = GenerateBridgeList()
	pShipPanel.AddChild(pMenu, BRIDGEMENU_X, BRIDGEMENU_Y)
	pShipPanel.MoveToFront(pMenu)	

	pStylizedWindow = Lib.Ambiguity.createPanel(pShipPanel, "ShipIconPanel", SHIPICON_X, SHIPICON_Y, SHIPICON_W, SHIPICON_H)
	global g_pShipsTextWindow
	g_pShipsTextWindow = pStylizedWindow
	global g_pShipsIcon	
	g_pShipsIcon = Lib.Ambiguity.createIcon2(pStylizedWindow, "ShipIcons", App.SPECIES_UNKNOWN, SHIPICON_X, SHIPICON_Y, SHIPICON_W, SHIPICON_H)
	g_pShipsIcon.SetNotVisible ()	
	pFrame = Lib.Ambiguity.createFrame(pStylizedWindow, "Ship Icon", 0, 0, SHIPICON_W, SHIPICON_H, "NoMinimize", App.g_kMainMenuBorderMainColor)
	pShipPanel.MoveToFront(pStylizedWindow)

	x = SHIPMENU_X+SHIPMENU_W
	
	global g_pEdName
	g_pEdName = Lib.Ambiguity.createEditBox(pShipPanel, x+0.01, 0.035, "Name", "", 0.25, 0.05, 256)
	
	global g_pEdX
	g_pEdX = Lib.Ambiguity.createEditBox(pShipPanel, x+0.01, 0.07, "X", "0", 0.08, 0.01, 256)

	global g_pEdY
	g_pEdY = Lib.Ambiguity.createEditBox(pShipPanel, x+0.1, 0.07, "Y", "0", 0.08, 0.01, 256)

	global g_pEdZ
	g_pEdZ = Lib.Ambiguity.createEditBox(pShipPanel, x+0.19, 0.07, "Z", "0", 0.08, 0.01, 256)

	global g_pEdAI
	g_pEdAI = Lib.Ambiguity.createEditBox(pShipPanel, x+0.01, 0.105, "AI", "  ", 0.25, 0.04, 256)

	pPanel1 = Lib.Ambiguity.createPanel(pShipPanel, "ExtraPanel", x + 0.01, 0.145, 0.12, 0.2)
	pShipPanel.MoveToFront(pPanel1)
	
	pPanelr = Lib.Ambiguity.createPanel(pShipPanel, "ExtraPanel", x + 0.14, 0.18, 0.12, 0.2)
	pShipPanel.MoveToFront(pPanelr)

	global g_pCriticalButton
	event = Lib.Ambiguity.addEventHandler("XO", "ET_CRITICAL_BUTTON", __name__ + ".CriticalButton")
	g_pCriticalButton = Lib.Ambiguity.createButton(pPanel1, "Critical", event, "MissionCritical", "XO")
	g_pCriticalButton.SetPosition(0, 0)
	g_pCriticalButton.SetChoosable(1)
	g_pCriticalButton.SetAutoChoose(1)

	global g_pStarbaseButton
	event = Lib.Ambiguity.addEventHandler("XO", "ET_STARBASE_BUTTON", __name__ + ".StarbaseButton")
	g_pStarbaseButton = Lib.Ambiguity.createButton(pPanel1, "Starbase", event, "Starbase", "XO")
	g_pStarbaseButton.SetPosition(0, 0.035)
	g_pStarbaseButton.SetChoosable(1)
	g_pStarbaseButton.SetAutoChoose(1)

	global g_pWarpButton
	event = Lib.Ambiguity.addEventHandler("XO", "ET_WARP_BUTTON", __name__ + ".WarpButton")
	g_pWarpButton = Lib.Ambiguity.createButton(pPanelr, "Allow Warp", event, "AllowWarp", "XO")
	g_pWarpButton.SetPosition(0, 0)
	g_pWarpButton.SetChoosable(1)
	g_pWarpButton.SetAutoChoose(1)
	
	Lib.Ambiguity.createLabel(pShipPanel, "Damage", x + 0.14, 0.22)
	global g_pEdMinDamage
	g_pEdMinDamage = Lib.Ambiguity.createEditBox(pShipPanel, x+0.14, 0.26, "Min", "0", 0.12, 0.04, 256)
	global g_pEdMaxDamage
	g_pEdMaxDamage = Lib.Ambiguity.createEditBox(pShipPanel, x+0.14, 0.30, "Max", "0", 0.12, 0.04, 256)

	Lib.Ambiguity.createLabel(pShipPanel, "ETA", x, 0.22)
	global g_pEdMinETA
	g_pEdMinETA = Lib.Ambiguity.createEditBox(pShipPanel, x, 0.26, "Min", "0", 0.12, 0.04, 256)
	global g_pEdMaxETA
	g_pEdMaxETA = Lib.Ambiguity.createEditBox(pShipPanel, x, 0.30, "Max", "0", 0.12, 0.04, 256)

	pMenu = GenerateAIMenu()
	pShipPanel.AddChild(pMenu, x+0.01, AI_MENU_Y_POS)
	pShipPanel.MoveToFront(pMenu)

	pMenu = GenerateGroupMenu()
	pShipPanel.AddChild(pMenu, x+AI_MENU_WIDTH+0.03, AI_MENU_Y_POS)
	pShipPanel.MoveToFront(pMenu)

	pMenu = GenerateShipSystemMenu()
	pShipPanel.AddChild(pMenu, x+0.01, AI_MENU_Y_POS-AI_MENU_HEIGHT - 0.01)
	pShipPanel.MoveToFront(pMenu)

	event = Lib.Ambiguity.addEventHandler("XO", "ET_UPDATE_SHIPLIST", __name__ + ".UpdateShipList")
	Lib.Ambiguity.createMainMenuButton(pShipPanel, "Update", event, "Update", "XO", UPDATEBUTTON_X, UPDATEBUTTON_Y, UPDATEBUTTON_W, UPDATEBUTTON_H)
	
	event = Lib.Ambiguity.addEventHandler("XO", "ET_DELETE_SHIPLIST", __name__ + ".DeleteShipList")
	Lib.Ambiguity.createMainMenuButton(pShipPanel, "Delete", event, "Delete", "XO", DELETEBUTTON_X, DELETEBUTTON_Y, DELETEBUTTON_W, DELETEBUTTON_H)
	
	pShipFrame = Lib.Ambiguity.createFrame(pShipPanel, "Ships", 0.0, 0.0, DETAILPANEL_W, DETAILPANEL_H, "NoMinimize", App.g_kMainMenuBorderMainColor)
	pShipFrame.SetUseScrolling(0)

	global g_pActivePanel
	g_pActivePanel = pShipPanel

	# SystemPanel
	pSystemPanel = Lib.Ambiguity.createPanel(pMainPanel, "SystemPanel", DETAILPANEL_X, DETAILPANEL_Y, DETAILPANEL_W, DETAILPANEL_H)
	pMainPanel.MoveToFront(pSystemPanel)
	pSystemPanel.SetNotVisible()
	
	pMenu = GenerateRegionMenu()
	pSystemPanel.AddChild(pMenu, 0.01, 0.1)

	pMenu = GenerateRegionList()
	pSystemPanel.AddChild(pMenu, 0.32, 0.1)

	pSystemFrame = Lib.Ambiguity.createFrame(pSystemPanel, "Systems", 0.0, 0.0, DETAILPANEL_W, DETAILPANEL_H, "NoMinimize", App.g_kMainMenuBorderMainColor)
	pSystemFrame.SetUseScrolling(0)
	
	# FilePanel
	pFilePanel = Lib.Ambiguity.createPanel(pMainPanel, "FilePanel", DETAILPANEL_X, DETAILPANEL_Y, DETAILPANEL_W, DETAILPANEL_H)
	pMainPanel.MoveToFront(pFilePanel)
	pFilePanel.SetNotVisible()

	pMenu = GenerateLoadMenu()
	pFilePanel.AddChild(pMenu, 0.01, 0.15)	

	global g_pEdSelectedFile
	g_pEdSelectedFile = Lib.Ambiguity.createEditBox(pFilePanel, 0.01, 0.1, "File", "", 0.3, 0.05, 256)

	event = Lib.Ambiguity.addEventHandler("XO", "ET_LOAD_BUTTON", __name__ + ".LoadGame")
	Lib.Ambiguity.createMainMenuButton(pFilePanel, "Load", event, "Load", "XO", 0.35, 0.1, UPDATEBUTTON_W, UPDATEBUTTON_H)

	event = Lib.Ambiguity.addEventHandler("XO", "ET_SAVE_BUTTON", __name__ + ".SaveGame")
	Lib.Ambiguity.createMainMenuButton(pFilePanel, "Save", event, "Save", "XO", 0.35, 0.15, UPDATEBUTTON_W, UPDATEBUTTON_H)
	
	event = Lib.Ambiguity.addEventHandler("XO", "ET_DEL_BUTTON", __name__ + ".DeleteGame")
	Lib.Ambiguity.createMainMenuButton(pFilePanel, "Delete", event, "Delete", "XO", 0.35, 0.29, UPDATEBUTTON_W, UPDATEBUTTON_H)

	pFileFrame = Lib.Ambiguity.createFrame(pFilePanel, "File", 0.0, 0.0, DETAILPANEL_W, DETAILPANEL_H, "NoMinimize", App.g_kMainMenuBorderMainColor)
	pFileFrame.SetUseScrolling(0)
	

def MenuButton(pObject, pEvent):
	s = Lib.Ambiguity.getEventString(pEvent)
	g_pActivePanel.SetNotVisible()
	
	global g_pActivePanel
	sPanel = ""
	if (s == "Ships"):
		sPanel = "ShipPanel"
		RebuildShipSystemMenu()
		RebuildShipList()
	elif (s == "Systems"):
		sPanel = "SystemPanel"
	elif (s == "File"):
		sPanel = "FilePanel"
		RebuildLoadMenu()
	elif (s == "Plugins"):
		sPanel = "PluginPanel"
		
	if (sPanel != ''):
		g_pActivePanel = Lib.Ambiguity.getPanel(sPanel)
		g_pActivePanel.SetVisible()

	if (pObject):
		pObject.CallNextHandler(pEvent)
		
	
def OpenDialog(pObject=None, pEvent=None):
	Lib.Ambiguity.showFormModal("MainForm")

	if (pObject):
		pObject.CallNextHandler(pEvent)

def CloseDialog(pObject, pEvent):
	Lib.Ambiguity.closeFormModal("MainForm")
	
	if (pObject):
		pObject.CallNextHandler(pEvent)
	
def SelectShip(pObject, pEvent):
	AddShip(Foundation.shipList[pEvent.GetInt()].shipFile)
	
	if (pObject):
		pObject.CallNextHandler(pEvent)

def SelectShipList(pObject, pEvent):
	key = (App.TGStringEvent_Cast(pEvent)).GetCString()
	ship = QBFile.g_pShipListData[key]
	global g_pSelectedShip
	g_pSelectedShip = key
	
	ChangeIcon(key)
	
	# Name
	g_pEdName.SetString(ship['name'])

	# X
	g_pEdX.SetString(repr(ship['pos'][0]))
	# Y
	g_pEdY.SetString(repr(ship['pos'][1]))
	# Z
	g_pEdZ.SetString(repr(ship['pos'][2]))

	# AI file
	if (ship['ai'] != ''):
		g_pEdAI.SetString(ship['ai'])
	else:
		g_pEdAI.SetString(' ')
	
	g_pEdMinDamage.SetString(repr(100-ship['mindamage']*100))
	g_pEdMaxDamage.SetString(repr(100-ship['maxdamage']*100))
	
	if ship.has_key('minETA'):
		g_pEdMinETA.SetString(str(ship['minETA']))
		g_pEdMaxETA.SetString(str(ship['maxETA']))
	else:
		g_pEdMinETA.SetString("0")
		g_pEdMaxETA.SetString("0")

	SetAI(ship['ailevel'])
	if (ship['group']=='neutral'):
		SetGroup(0.0)
	elif (ship['group']=='friend'):
		SetGroup(1.0)
	elif (ship['group']=='enemy'):
		SetGroup(2.0)
	elif (ship['group']=='player'):
		SetGroup(3.0)
	elif (ship['group']=='neutral2'):
		SetGroup(4.0)
		
	global g_pSelShipSystem
	g_pSelShipSystem = None
	for system in QBFile.g_pRegionListData:
		import strop
		s = strop.split(system, '.')
		if (s[-1] == ship['system']):
			g_pSelShipSystem = system
	SelectShipSystem(None, None)

	g_pStarbaseButton.SetChosen(ship['starbase'])	
	g_pWarpButton.SetChosen(ship['warp'])	
	g_pCriticalButton.SetChosen(ship['missioncritical'])

	if (pObject):
		pObject.CallNextHandler(pEvent)

def UpdateShipList(pObject, pEvent):
	if (not g_pSelectedShip is None):
		ship = QBFile.g_pShipListData[g_pSelectedShip]
		
		ship['name'] = g_pEdName.GetCString()
		
		del QBFile.g_pShipListData[g_pSelectedShip]
		global g_pSelectedShip
		g_pSelectedShip = ship['name']
		QBFile.g_pShipListData[g_pSelectedShip] = ship
		
		QBFile.g_pShipListData[g_pSelectedShip]
		ship['ailevel'] = g_iSelectedAILevel
		if (g_iSelectedGroup == 0.0):
			ship['group'] = 'neutral'
		elif (g_iSelectedGroup == 1.0):
			ship['group'] = 'friend'
		elif (g_iSelectedGroup == 2.0):
			ship['group'] = 'enemy'
		elif (g_iSelectedGroup == 3.0):
			ship['group'] = 'player'
			# The Player ship has to be named 'player' for some reason.
			# It's probably related to the AI.
			ship['name'] = 'player'
		elif (g_iSelectedGroup == 4.0):
			ship['group'] = 'neutral2'

		if (not g_pSelShipSystem is None):
			import strop
			s = strop.split(g_pSelShipSystem, '.')
			ship['system'] = s[-1]

		try:
			x = float(g_pEdX.GetCString())
			ship['pos'][0] = x
		except ValueError:
			print "'" + g_pEdX.GetCString() + "' is no float value"
		try:
			y = float(g_pEdY.GetCString())
			ship['pos'][1] = y
		except ValueError:
			print "'" + g_pEdY.GetCString() + "' is no float value"
		try:
			z = float(g_pEdZ.GetCString())
			ship['pos'][2] = z
		except ValueError:
			print "'" + g_pEdZ.GetCString() + "' is no float value"
			
		try:
			mindamage = (100-float(g_pEdMinDamage.GetCString())) / 100
			ship['mindamage'] = mindamage
		except ValueError:
			print "'" + g_pEdMinDamage.GetCString() + "' is no float value"

		try:
			maxdamage = (100-float(g_pEdMaxDamage.GetCString())) / 100
			ship['maxdamage'] = maxdamage
		except ValueError:
			print "'" + g_pEdMaxDamage.GetCString() + "' is no float value"

		minETA = g_pEdMinETA.GetCString()
		ship['minETA'] = minETA
		maxETA = g_pEdMaxETA.GetCString()
		ship['maxETA'] = maxETA

		import string
		ship['ai'] = string.strip(g_pEdAI.GetCString())

		ship['starbase'] = g_pStarbaseButton.IsChosen()
		ship['warp'] = g_pWarpButton.IsChosen()
		ship['missioncritical'] = g_pCriticalButton.IsChosen()

		RebuildShipList()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def DeleteShipList(pObject, pEvent):
	if (not g_pSelectedShip is None):
		del QBFile.g_pShipListData[g_pSelectedShip]
		global g_pSelectedShip
		g_pSelectedShip = None
		RebuildShipList()
	if (pObject):
		pObject.CallNextHandler(pEvent)

def TextEntryMouseHandler(pObject, pEvent):
	if (pObject):
		pObject.CallNextHandler(pEvent)

def SelectSystem(pObject, pEvent):
	import string
	
	region = (App.TGStringEvent_Cast(pEvent)).GetCString()
	sRegionName = region
	if  (string.lower(region) == "starbase12"):
		return # Starbase12 will only crash us
	if  (string.lower(region) != "starbase12") and (string.find(string.digits, region[-1]) != -1):
		sRegionName = region[:-1]
	if (QBFile.g_pRegionListData.count(sRegionName + "." + region) == 0):
		QBFile.g_pRegionListData.append(sRegionName + "." + region)
		RebuildRegionList()
	if (pObject):
		pObject.CallNextHandler(pEvent)

def SelectRegionList(pObject, pEvent):
	region = (App.TGStringEvent_Cast(pEvent)).GetCString()
	if (QBFile.g_pRegionListData.count(region) != 0):
		QBFile.g_pRegionListData.remove(region)
		RebuildRegionList()
		
	if (pObject):
		pObject.CallNextHandler(pEvent)
		
def SelectShipSystem(pObject, pEvent):
	if (not pEvent is None):
		selsystem = (App.TGStringEvent_Cast(pEvent)).GetCString()
		global g_pSelShipSystem
		g_pSelShipSystem = selsystem
	
	for system in QBFile.g_pRegionListData:
		import strop
		s = strop.split(system, '.')
		button = g_pShipSystemMenu.GetButtonW(App.TGString(s[-1]))
		if (not button is None):
			if (system == g_pSelShipSystem):
				button.SetChosen(1)
			else:
				button.SetChosen(0)

def CriticalButton(pObject, pEvent):
	if (pObject):
		pObject.CallNextHandler(pEvent)

def StarbaseButton(pObject, pEvent):
	if (pObject):
		pObject.CallNextHandler(pEvent)

def WarpButton(pObject, pEvent):
	if (pObject):
		pObject.CallNextHandler(pEvent)

def SelectBridge(pObject, pEvent):
	#button	= g_pBridgeList.GetButtonW(App.TGString(g_Bridge))
	#button.SetChosen(0)

	bridge = Foundation.bridgeList[pEvent.GetInt()].bridgeString
	global g_Bridge
	g_Bridge = bridge
	QBFile.g_sBridge = g_Bridge

	#button	= g_pBridgeList.GetButtonW(App.TGString(g_Bridge))
	#button.SetChosen(1)

	if (pObject):
		pObject.CallNextHandler(pEvent)

def StartSimulation(pObject, pEvent):
	Lib.Ambiguity.closeFormModal("MainForm")
	
	if (pObject):
		pObject.CallNextHandler(pEvent)
		
def CheckSetup():
	hasSystem = 1
	hasName = 1
	hasPlayer = 0
	keys = QBFile.g_pShipListData.keys()

	for key in keys:
		ship = QBFile.g_pShipListData[key]
		#print ship['name'], ship['system']
		if (ship['name'] == ''):
			hasName = 0
		if (ship['group'] == 'player'):
			hasPlayer = 1
		if (ship['system'] == ''):
			hasSystem = 0

	return hasSystem & hasName & hasPlayer

def LoadGame(pObject, pEvent):
	if (not pEvent is None):
		if (g_sSelectedFile != ''):
			LoadSetup(g_sSelectedFile)
	if (pObject):
		pObject.CallNextHandler(pEvent)

def SaveGame(pObject, pEvent):
	if (not pEvent is None):
		global g_sSelectedFile
		g_sSelectedFile = g_pEdSelectedFile.GetCString()
		
		if (g_sSelectedFile != ''):
			SaveSetup(g_sSelectedFile)
	if (pObject):
		pObject.CallNextHandler(pEvent)
		
def DeleteGame(pObject, pEvent):
	if (not pEvent is None):
		global g_sSelectedFile
		g_sSelectedFile = g_pEdSelectedFile.GetCString()

		if (g_sSelectedFile != '' and g_sSelectedFile != 'QBSetup'):
			QBFile.DeleteSetup(g_sSelectedFile)
		
		RebuildLoadMenu()

		if (pObject):
			pObject.CallNextHandler(pEvent)

def SelectGame(pObject, pEvent):
	if (not pEvent is None):
		selSetup = (App.TGStringEvent_Cast(pEvent)).GetCString()
		g_pEdSelectedFile.SetString(selSetup)
		global g_sSelectedFile
		g_sSelectedFile = selSetup
	if (pObject):
		pObject.CallNextHandler(pEvent)
###############################################################################
#	CreateBridgeMenuButton()
#
#	Create a menu button which sends an int event with the passed in event
#	type and int data, to a passed in character.
#
#	Args:	pName		- name of button (string)
#			eType		- event type
#			sSubType	- sub type to be passed in the string of the TGStringEvent
#			pCharacter	- character to which to send the event
#			fWidth		- the width of the button
#			fHeight		- the height of the button
#
#	Return:	none
###############################################################################
def CreateBridgeMenuButton(pName, eType, sSubType, pCharacter, fWidth = 0.0, fHeight = 0.0):
	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(pCharacter)
	pEvent.SetString(sSubType)
	if fWidth == 0.0:
		return (App.STButton_CreateW(pName, pEvent))
	else:
		return (App.STRoundedButton_CreateW(pName, pEvent, fWidth, fHeight))


###############################################################################
#	CreateFloatButton(pName, eType, fFloat, pCharacter, 
#					  fWidth = 0.0, fHeight = 0.0)
#	
#	Creates a button that sends a float event.
#	
#	Args:	pName		- name of button (string)
#			eType		- event type
#			fFloat		- float to be passed in event
#			pCharacter	- character to which the event will go
#			fWidth		- width
#			fHeight		- height
#	
#	Return:	
###############################################################################
def CreateFloatButton(pName, eType, fFloat, pCharacter, fWidth = 0.0, fHeight = 0.0):
	pEvent = App.TGFloatEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(pCharacter)
	pEvent.SetFloat(fFloat)
	if fWidth == 0.0:
		return (App.STButton_CreateW(pName, pEvent))
	else:
		return (App.STRoundedButton_CreateW(pName, pEvent, fWidth, fHeight))

def GenerateShipMenu():
	pSet =  App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pSet, 'XO')

	# Create menus for all the sorts of enemy ships
	pShipMenu = App.STSubPane_Create(SHIPMENU_W, SHIPMENU_H, 1)
	
	pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Available Ships"))
	pStylizedWindow.SetFixedSize(SHIPMENU_W, SHIPMENU_H);
	pStylizedWindow.SetTitleBarThickness(BAR_HEIGHT)
	pStylizedWindow.AddChild(pShipMenu)
	App.g_kFocusManager.AddObjectToTabOrder(pStylizedWindow)

	shipMenuBuilder(qbGameMode.shipMenu, pShipMenu, Lib.Ambiguity.getEvent("ET_SELECT_SHIP"), pSaffi)
	
	return pStylizedWindow
		
def GenerateShipList():
	global g_pShipListWindow
	global g_pShipList
	g_pShipList = App.STSubPane_Create(SELECTEDSHIPSMENU_W, SELECTEDSHIPSMENU_H, 1)

	g_pShipListWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Selected Ships"))

	g_pShipList.Resize(SELECTEDSHIPSMENU_W - g_pShipListWindow.GetBorderWidth(), SELECTEDSHIPSMENU_H - g_pShipListWindow.GetBorderHeight())

	g_pShipListWindow.SetFixedSize(SELECTEDSHIPSMENU_W, SELECTEDSHIPSMENU_H)
	g_pShipListWindow.AddChild(g_pShipList)

	g_pShipList.ResizeToContents()
	
	RebuildShipList()
	
	return g_pShipListWindow
	
def GenerateLoadMenu():
	global g_pLoadMenu
	global g_pLoadWindow
	
	g_pLoadMenu = App.STSubPane_Create(0.3, 0.55, 1)

	g_pLoadWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Load Setup"))

	g_pLoadMenu.Resize(0.3 - g_pLoadWindow.GetBorderWidth(), 0.55 - g_pLoadWindow.GetBorderHeight())

	g_pLoadWindow.SetFixedSize(0.3, 0.55)
	g_pLoadWindow.AddChild(g_pLoadMenu)

	g_pLoadMenu.ResizeToContents()
	
	RebuildLoadMenu()
	return g_pLoadWindow

def GetDefaultShipData(classname):
	pShipData = {
		'class': 	classname,
		'name':  	classname,
		'system':	'',
		'pos':		[0, 0, 0],
		'ailevel':	0.5,
		'ai':		'',
		'warp':		1,
		'group':	'neutral',
		'starbase':	0,
		'mindamage':	1,
		'maxdamage':	1,
		'missioncritical': 0
	}
	
	return pShipData
	
def SetBridge(sBridge):
	global g_Bridge
	g_Bridge = sBridge

def AddShip(classname, data = None):
	if (data is None):
		ship = GetDefaultShipData(classname)
	else:
		ship = data
	
	i = 1
	while (QBFile.g_pShipListData.has_key(ship['name']+" "+repr(i))):
		i = i + 1
	else:
		if (data is None):
			ship['name'] = ship['name']+" "+repr(i)
		QBFile.g_pShipListData[ship['name']] = ship
	RebuildShipList()
	
def AddSystem(system):
	if (QBFile.g_pRegionListData.count(system)==0):
		QBFile.g_pRegionListData.append(system)
	
	RebuildRegionList()
	RebuildShipSystemMenu()
	
def RebuildShipList():
	pSet =  App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pSet, 'XO')

	g_pShipList.KillChildren()
	
	keys = QBFile.g_pShipListData.keys()
	keys.sort()
	
	for key in keys:
		s = QBFile.g_pShipListData[key]['name']
		button = CreateBridgeMenuButton(App.TGString(s), Lib.Ambiguity.getEvent("ET_SELECT_SHIPLIST"), key, pSaffi)
		button.SetUseUIHeight(0)
		if (QBFile.g_pShipListData[key]['group'] == 'neutral'):
			button.SetNormalColor(App.g_kRadarNeutralColor)
		elif (QBFile.g_pShipListData[key]['group'] == 'friend'):
			button.SetNormalColor(App.g_kRadarFriendlyColor)
		elif (QBFile.g_pShipListData[key]['group'] == 'enemy'):
			button.SetNormalColor(App.g_kRadarEnemyColor)
		elif (QBFile.g_pShipListData[key]['group'] == 'player'):
			color = App.TGColorA()
			color.r = 0
			color.g = 1
			color.b = 0
			button.SetNormalColor(App.g_kTitleColor)
		elif (QBFile.g_pShipListData[key]['group'] == 'neutral2'):
			button.SetNormalColor(App.g_kRadarUnknownColor)
		button.SetColorBasedOnFlags()
		g_pShipList.AddChild(button)

	g_pShipList.ResizeToContents()
	#g_pShipListWindow.ScrollToBottom()
	g_pShipListWindow.Layout()

def RebuildLoadMenu():
	import nt
	import strop

	# load both directorys, where we can find Missions here.
	list = nt.listdir('scripts\Custom\QuickBattleGame') + nt.listdir('scripts\Custom\QuickBattleGame\Missions')
	files = []

	for file in list:
		s = strop.split(file, '.')
		if (len(s)>1) and ((s[-1] == 'pyc') or (s[-1] == 'py')):
			filename = s[0]
			try:
			        pModule = __import__('Custom.QuickBattleGame.Missions.'+filename)
			except:
			        pModule = __import__('Custom.QuickBattleGame.'+filename)
			
			if (hasattr(pModule, 'gVersion')):
				if (files.count(filename)==0):
					files.append(filename)
	
	pSet =  App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pSet, 'XO')

	g_pLoadMenu.KillChildren()
	for file in files:
		button = CreateBridgeMenuButton(App.TGString(file), Lib.Ambiguity.getEvent("ET_SELECT_FILE"), file, pSaffi)
		button.SetUseUIHeight(0)
		g_pLoadMenu.AddChild(button)

	g_pLoadMenu.ResizeToContents()
	g_pLoadWindow.Layout()
	
	
def GenerateAIMenu():
	pSet =  App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pSet, 'XO')

	global g_pAIMenu
	g_pAIMenu = App.STSubPane_Create(AI_MENU_WIDTH, AI_MENU_HEIGHT, 1)
	
	pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("AI Level"))
	pStylizedWindow.SetUseScrolling(0)
	pStylizedWindow.SetFixedSize(AI_MENU_WIDTH, AI_MENU_HEIGHT)
	pStylizedWindow.SetTitleBarThickness(BAR_HEIGHT)
	pStylizedWindow.AddChild(g_pAIMenu)

	pLow = CreateFloatButton(App.TGString("Low"), Lib.Ambiguity.getEvent("ET_SELECT_AI"), 0.0, pSaffi)
	pLow.SetChoosable(1)
	g_pAIMenu.AddChild(pLow)

	pMedium = CreateFloatButton(App.TGString("Medium"), Lib.Ambiguity.getEvent("ET_SELECT_AI"), 0.5, pSaffi)
	pMedium.SetChoosable(1)
	g_pAIMenu.AddChild(pMedium)
	pMedium.SetChosen(1)

	pHigh = CreateFloatButton(App.TGString("High"), Lib.Ambiguity.getEvent("ET_SELECT_AI"), 1.0, pSaffi)
	pHigh.SetChoosable(1)
	g_pAIMenu.AddChild(pHigh)
	
	return pStylizedWindow

def SelectAI(pObject, pEvent):
	SetAI(pEvent.GetFloat())

	pObject.CallNextHandler(pEvent)
	
def SetAI(fAI):
	# Update the appropriate global value
	global g_iSelectedAILevel
	g_iSelectedAILevel = fAI

	pLow	= g_pAIMenu.GetButtonW(App.TGString("Low"))
	pMedium	= g_pAIMenu.GetButtonW(App.TGString("Medium"))
	pHigh	= g_pAIMenu.GetButtonW(App.TGString("High"))
	
	# Even though it will usually be the AI Menu itself that's called us, it
	# won't *always* be -- so we update it to reflect the current level
	if fAI == 0.0:
		pLow.SetChosen(1)
		pMedium.SetChosen(0)
		pHigh.SetChosen(0)
	elif fAI == 0.5:
		pLow.SetChosen(0)
		pMedium.SetChosen(1)
		pHigh.SetChosen(0)
	else:
		pLow.SetChosen(0)
		pMedium.SetChosen(0)
		pHigh.SetChosen(1)

def GenerateGroupMenu():
	pSet =  App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pSet, 'XO')

	global g_pGroupMenu
	g_pGroupMenu = App.STSubPane_Create(AI_MENU_WIDTH, AI_MENU_HEIGHT, 1)
	
	pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Group"))
	pStylizedWindow.SetUseScrolling(1)
	pStylizedWindow.SetFixedSize(AI_MENU_WIDTH, AI_MENU_HEIGHT)
	pStylizedWindow.SetTitleBarThickness(BAR_HEIGHT)
	pStylizedWindow.AddChild(g_pGroupMenu)

	pLow = CreateFloatButton(App.TGString("Neutral"), Lib.Ambiguity.getEvent("ET_SELECT_GROUP"), 0.0, pSaffi)
	pLow.SetChoosable(1)
	g_pGroupMenu.AddChild(pLow)

	pMedium = CreateFloatButton(App.TGString("Friendly"), Lib.Ambiguity.getEvent("ET_SELECT_GROUP"), 1.0, pSaffi)
	pMedium.SetChoosable(1)
	g_pGroupMenu.AddChild(pMedium)
	pMedium.SetChosen(1)

	pHigh = CreateFloatButton(App.TGString("Enemy"), Lib.Ambiguity.getEvent("ET_SELECT_GROUP"), 2.0, pSaffi)
	pHigh.SetChoosable(1)
	g_pGroupMenu.AddChild(pHigh)

	pPlayer = CreateFloatButton(App.TGString("PLAYER"), Lib.Ambiguity.getEvent("ET_SELECT_GROUP"), 3.0, pSaffi)
	pPlayer.SetChoosable(1)
	g_pGroupMenu.AddChild(pPlayer)
	
	pPlayer = CreateFloatButton(App.TGString("Neutral2"), Lib.Ambiguity.getEvent("ET_SELECT_GROUP"), 4.0, pSaffi)
	pPlayer.SetChoosable(1)
	g_pGroupMenu.AddChild(pPlayer)

	return pStylizedWindow

def GenerateShipSystemMenu():

	global g_pShipSystemMenu	
	g_pShipSystemMenu = App.STSubPane_Create(AI_MENU_WIDTH*2+0.02, AI_MENU_HEIGHT, 1)

	pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("System"))
	pStylizedWindow.SetUseScrolling(1)
	pStylizedWindow.SetFixedSize(AI_MENU_WIDTH*2+0.02, AI_MENU_HEIGHT)
	pStylizedWindow.SetTitleBarThickness(BAR_HEIGHT)
	pStylizedWindow.AddChild(g_pShipSystemMenu)
	
	RebuildShipSystemMenu()
	return pStylizedWindow

def RebuildShipSystemMenu():
	pSet =  App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pSet, 'XO')
	
	g_pShipSystemMenu.KillChildren()
	
	for system in QBFile.g_pRegionListData:
		import strop
		s = strop.split(system, '.')
		button = CreateBridgeMenuButton(App.TGString(s[-1]), Lib.Ambiguity.getEvent("ET_SELECT_SHIPSYSTEM"), system, pSaffi)
		button.SetChoosable(1)
		if (system == g_pSelShipSystem):
			button.SetChosen(1)
		g_pShipSystemMenu.AddChild(button)

def SelectGroup(pObject, pEvent):
	SetGroup(pEvent.GetFloat())

	pObject.CallNextHandler(pEvent)

def SetGroup(fGroup):
	# Update the appropriate global value
	global g_iSelectedGroup
	g_iSelectedGroup = fGroup

	pNeutral	= g_pGroupMenu.GetButtonW(App.TGString("Neutral"))
	pFriendly	= g_pGroupMenu.GetButtonW(App.TGString("Friendly"))
	pEnemy		= g_pGroupMenu.GetButtonW(App.TGString("Enemy"))
	pPlayer		= g_pGroupMenu.GetButtonW(App.TGString("Player"))
	pNeutral2	= g_pGroupMenu.GetButtonW(App.TGString("Neutral2"))
	
	if fGroup == 0.0:
		pNeutral.SetChosen(1)
		pFriendly.SetChosen(0)
		pEnemy.SetChosen(0)
		pPlayer.SetChosen(0)
		pNeutral2.SetChosen(0)
	elif fGroup == 1.0:
		pNeutral.SetChosen(0)
		pFriendly.SetChosen(1)
		pEnemy.SetChosen(0)
		pPlayer.SetChosen(0)
		pNeutral2.SetChosen(0)
	elif fGroup == 2.0:
		pNeutral.SetChosen(0)
		pFriendly.SetChosen(0)
		pEnemy.SetChosen(1)
		pPlayer.SetChosen(0)
		pNeutral2.SetChosen(0)
	elif fGroup == 3.0:
		pNeutral.SetChosen(0)
		pFriendly.SetChosen(0)
		pEnemy.SetChosen(0)
		pPlayer.SetChosen(1)
		pNeutral2.SetChosen(0)
	elif fGroup == 4.0:
		pNeutral.SetChosen(0)
		pFriendly.SetChosen(0)
		pEnemy.SetChosen(0)
		pPlayer.SetChosen(0)
		pNeutral2.SetChosen(1)

def GenerateRegionMenu():
	pSet =  App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pSet, 'XO')

	pChangeRegionMenu = App.STSubPane_Create(0.3, 0.55, 1)

	pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Systems"))
	pStylizedWindow.SetFixedSize(0.3, 0.55)
	pStylizedWindow.SetTitleBarThickness(BAR_HEIGHT)
	pStylizedWindow.AddChild(pChangeRegionMenu)

	systemMenuBuilder(qbGameMode.systems, pChangeRegionMenu, Lib.Ambiguity.getEvent("ET_SELECT_SYSTEM"), pSaffi)

	App.g_kFocusManager.AddObjectToTabOrder(pChangeRegionMenu)
	return pStylizedWindow
	
def GenerateRegionList():
	global g_pRegionListWindow
	global g_pRegionList
	g_pRegionList = App.STSubPane_Create(0.3, 0.55, 1)

	g_pRegionListWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Selected Regions"))

	g_pRegionList.Resize(0.3 - g_pRegionListWindow.GetBorderWidth(), 0.55 - g_pRegionListWindow.GetBorderHeight())

	g_pRegionListWindow.SetFixedSize(0.3, 0.55)
	g_pRegionListWindow.AddChild(g_pRegionList)

	g_pRegionList.ResizeToContents()
	
	RebuildRegionList()
	return g_pRegionListWindow
	
def RebuildRegionList():
	pSet =  App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pSet, 'XO')

	g_pRegionList.KillChildren()
	QBFile.g_pRegionListData.sort()

	for region in QBFile.g_pRegionListData:
		import strop
		s = strop.split(region, '.')
		button = CreateBridgeMenuButton(App.TGString(s[-1]), Lib.Ambiguity.getEvent("ET_SELECT_REGIONLIST"), region, pSaffi)
		button.SetUseUIHeight(0)		
		g_pRegionList.AddChild(button)

	g_pRegionList.ResizeToContents()
	g_pRegionListWindow.Layout()

def GenerateBridgeList():
	pSet =  App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pSet, 'XO')

	global g_pBridgeList
	g_pBridgeList = App.STSubPane_Create(BRIDGEMENU_W, BRIDGEMENU_H, 1)
	
	bridgeMenuBuilder(qbGameMode.bridgeList, g_pBridgeList, Lib.Ambiguity.getEvent("ET_SELECT_BRIDGE"), pSaffi) 

	#button	= g_pBridgeList.GetButtonW(App.TGString(g_Bridge))
	#button.SetChosen(1)

	pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Bridge"))
	pStylizedWindow.SetUseScrolling(1)
	pStylizedWindow.SetFixedSize(BRIDGEMENU_W, BRIDGEMENU_H - 0.02)
	pStylizedWindow.SetTitleBarThickness(BAR_HEIGHT)
	pStylizedWindow.AddChild(g_pBridgeList)

	return pStylizedWindow

def ChangeIcon(shipKey):
	iIconNumber = 0
	try:
		import Foundation
	except ImportError:
		return
	else:
		sClass = QBFile.g_pShipListData[shipKey]['class']
		if Foundation.shipList._keyList.has_key(sClass):
			shipDef = Foundation.shipList._keyList[sClass]
			iIconNumber = shipDef.GetIconNum()
	UpdateIcon(iIconNumber, g_pShipsIcon, g_pShipsTextWindow)

def UpdateIcon(iIconNumber, pIcon, pPane):
	pIcon.SetVisible ()
	pIcon.SetIconNum(iIconNumber)
	pIcon.SizeToArtwork()

	# If we're too big, shrink us down
	if ((pIcon.GetHeight()+0.05) > pPane.GetHeight()):
		fRatio = pPane.GetHeight() / (pIcon.GetHeight()+0.05)
		pIcon.Resize(pIcon.GetWidth() * fRatio, pIcon.GetHeight() * fRatio)

	# Center us in our parent pane
	fXPos = (pPane.GetWidth() - pIcon.GetWidth()) / 2.0
	fYPos = ((pPane.GetHeight() - pIcon.GetHeight()) / 2.0) + 0.01
	pIcon.SetPosition(fXPos, fYPos)

def LoadSetup(sModule):
	if QBFile.LoadSetup(sModule):
		Lib.Ambiguity.showMessageBox("Load", "Setup loaded.")	
		RebuildRegionList()
		RebuildShipSystemMenu()
		RebuildShipList()
	else:
		Lib.Ambiguity.showMessageBox("Load", "Load failed.")	
		
def SaveSetup(filename):
	if (filename != ''):
		WriteSetup(filename)
	RebuildLoadMenu()

def WriteSetup(filename):
	if QBFile.WriteSetup(filename):
		Lib.Ambiguity.showMessageBox("Save", "Setup saved.")
	else:
		Lib.Ambiguity.showMessageBox("Save", "Save failed.")
