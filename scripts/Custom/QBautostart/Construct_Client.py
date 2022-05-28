import App
import MissionLib
import Libs.LibEngineering
from Libs.LibQBautostart import *
from Construct import *


sButtonName = "Construct Control"
pPlayer = None
pConstructWindow = None
ET_CLOSE = Libs.LibEngineering.GetEngineeringNextEventType()
ET_MODE = Libs.LibEngineering.GetEngineeringNextEventType()
ET_SELECT_DOCK = Libs.LibEngineering.GetEngineeringNextEventType()
ET_FORCE_START = Libs.LibEngineering.GetEngineeringNextEventType()
ET_SELECT_SHIP_TYPE = Libs.LibEngineering.GetEngineeringNextEventType()
ET_SELECT_SHIP_IN_CONSTRUCT_QUEUE = Libs.LibEngineering.GetEngineeringNextEventType()
ET_ADD_SHIP = Libs.LibEngineering.GetEngineeringNextEventType()
ET_DEL_SHIP = Libs.LibEngineering.GetEngineeringNextEventType()
CLOSE_X_POS                             = 0.3
CLOSE_Y_POS                             = 0
MODE_X_POS                             = 0.3
MODE_Y_POS                             = 0.1
SELECT_DOCK_X_POS			= 0.3
SELECT_DOCK_Y_POS			= 0.05
FORCE_START_X_POS			= 0.3
FORCE_START_Y_POS			= 0.15
SHIPS_SUBPANE_WIDTH			= 0.22
QUEUE_X_POS			= 0.5390625
QUEUE_Y_POS			= 0.0083333
ADD_X_POS			= 0.250025
ADD_Y_POS			= 0.52
ADD_WIDTH		= 0.2515625
ADD_HEIGHT		= 0.0354167
DEL_X_POS			= 0.250025
DEL_Y_POS			= 0.64
DEL_WIDTH			= 0.2515625
DEL_HEIGHT			= 0.0354167
iSelectedSpecies = 0
iSelectedShipInQueue = 0
pModeButton = None
pSelectDockButton = None
pForceStartButton = None
pConstructQueueButton = None
pSubPane = None
iSelectedDock = 1
iNumDocks = 1

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de & \"cnotsch\" c.notsch@gmx.at (patch)",
                "needBridge": 0
            }


NonSerializedObjects = (
"pPlayer",
"pConstructWindow",
"ET_CLOSE",
"ET_MODE",
"ET_SELECT_SHIP_TYPE",
"pModeButton",
"pSelectDockButton",
"pForceStartButton",
"ET_SELECT_DOCK",
"pConstructQueueButton",
"ET_SELECT_SHIP_IN_CONSTRUCT_QUEUE",
"ET_ADD_SHIP",
"ET_DEL_SHIP",
"pSubPane",
)


def RebuildConstructQueue():
	global iSelectedDock
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip, iSelectedDock)
	if not pConstructor:
		return
		
	pConstructQueueButton.KillChildren()
	i = 0
	for sShipType in pConstructor.GetConstructQueue():
		FdtnShip = Foundation.shipList[sShipType]
		sShipLongName = FdtnShip.name
		
		pEvent = App.TGIntEvent_Create()
        	pEvent.SetEventType(ET_SELECT_SHIP_IN_CONSTRUCT_QUEUE)
        	pEvent.SetInt(i)
        	pEvent.SetDestination(pConstructWindow)
                
        	pButton = App.STButton_CreateW(App.TGString(sShipLongName), pEvent)
        	pConstructQueueButton.AddChild(pButton)
		i = i+1
	pConstructQueueButton.Open()
	

def GenerateConstructQueue():
	global pConstructQueueButton	
	pConstructQueueButton = App.STCharacterMenu_Create("Construct Queue")
	pConstructWindow.AddChild(pConstructQueueButton, QUEUE_X_POS, QUEUE_Y_POS)


def ConstructControl(pObject, pEvent):
	if not pConstructWindow:
		CreateConstructWindow()
		CreateWindowInterieur()
	else:
		if pConstructWindow.IsVisible():
			pConstructWindow.SetNotVisible()
			DestroyWindowInterieur()
		else:
			pConstructWindow.SetVisible()
			CreateWindowInterieur()
	
	
def DestroyWindowInterieur():
	if pConstructWindow:
		pSubPane.KillChildren()
		pConstructQueueButton.KillChildren()
		pConstructWindow.KillChildren()


def CreateWindowInterieur():
	global pModeButton, iSelectedDock
	
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip, iSelectedDock)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetDestination(pConstructWindow)
        pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pButton, CLOSE_X_POS, CLOSE_Y_POS, 0)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_FORCE_START)
        pEvent.SetDestination(pConstructWindow)
	Text = App.TGString('Force Start')
        pButton = App.STRoundedButton_CreateW(Text, pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pButton, FORCE_START_X_POS, FORCE_START_Y_POS, 0)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_SELECT_DOCK)
        pEvent.SetDestination(pConstructWindow)
	SelectDockText = App.TGString('Dock' + str(iSelectedDock) + ' selected')
        pButton = App.STRoundedButton_CreateW(SelectDockText, pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pButton, SELECT_DOCK_X_POS, SELECT_DOCK_Y_POS, 0)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MODE)
        pEvent.SetDestination(pConstructWindow)
        pEvent.SetInt(0)
	if pConstructor.GetMode() == "Construct":
		s = "Mode Construct"
	else:
		s = "Mode Repair"
        pModeButton = App.STRoundedButton_CreateW(App.TGString(s), pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pModeButton, MODE_X_POS, MODE_Y_POS, 0)
	
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_ADD_SHIP)
        pEvent.SetDestination(pConstructWindow)
        pButton = App.STRoundedButton_CreateW(App.TGString("Add To Queue"), pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pButton, ADD_X_POS, ADD_Y_POS, 0)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_DEL_SHIP)
        pEvent.SetDestination(pConstructWindow)
        pButton = App.STRoundedButton_CreateW(App.TGString("Del From Queue"), pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pButton, DEL_X_POS, DEL_Y_POS, 0)
	
	BuildShipSelectWindow(pConstructor)
	GenerateConstructQueue()
	RebuildConstructQueue()


def ToggleMode(pObject, pEvent):	
	global iSelectedDock
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip, iSelectedDock)
	if not pConstructor:
		return
	if pConstructor.GetMode() == "Construct":
		pConstructor.SetMode("Repair")
		s = "Mode Repair"
	else:
		pConstructor.SetMode("Construct")
		s = "Mode Construct"
	if pModeButton:
		pModeButton.SetName(App.TGString(s))

def SelectDock(pObject, pEvent):	
	global iSelectedDock, iNumDocks, pSelectDockButton
	iNumDocks = GetNumDocks(App.ShipClass_Cast(pPlayer.GetTarget()))
	iSelectedDock = iSelectedDock + 1
	if iSelectedDock > iNumDocks:
		iSelectedDock = 1
	if pSelectDockButton:
		pSelectDockButton.SetName(App.TGString('Dock' + str(iSelectedDock) + ' selected'))
	DestroyWindowInterieur()
	CreateWindowInterieur()
def ForceStart(pObject, pEvent):
	global iSelectedDock
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip, iSelectedDock)
	if not pConstructor:
		return
	pConstructor.ForceStart()

def CreateConstructWindow():
	global pConstructWindow
	
	pConstructWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Add ships Window"), 0.0, 0.0, None, 1, 0.8, 0.8, App.g_kMainMenuBorderMainColor)
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pTacticalControlWindow.AddChild(pConstructWindow, 0.15, 0)
        pConstructWindow.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".PassMouse")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_CLOSE, __name__ + ".ConstructControl")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_MODE, __name__ + ".ToggleMode")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_TYPE, __name__ + ".SelectShipType")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_IN_CONSTRUCT_QUEUE, __name__ + ".SelectShipInQueue")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_ADD_SHIP, __name__ + ".AddShipToQueue")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_DEL_SHIP, __name__ + ".DelShipFromQueue")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_SELECT_DOCK, __name__ + ".SelectDock")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_FORCE_START, __name__ + ".ForceStart")

        pConstructWindow.SetVisible()
	pTacticalControlWindow.MoveToFront(pConstructWindow)
	pTacticalControlWindow.MoveTowardsBack(pConstructWindow) # one step back


def AddShipToQueue(pObject, pEvent):
	global iSelectedDock
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip, iSelectedDock)
	if not pConstructor:
		return
	
	sShipType = pConstructor.lShipsToConstruct[iSelectedSpecies]
	pConstructor.AddShipToConstructQueue(sShipType)
	RebuildConstructQueue()


def DelShipFromQueue(pObject, pEvent):
	global iSelectedShipInQueue, iSelectedDock
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip, iSelectedDock)
	if not pConstructor:
		return
	
	lQueue = pConstructor.GetConstructQueue()
	if iSelectedShipInQueue > len(lQueue)-1:
		iSelectedShipInQueue = len(lQueue)-1
	pConstructor.RemoveShipFromQueue(iSelectedShipInQueue)
	RebuildConstructQueue()

def SelectShipType(pObject, pEvent):
	global iSelectedSpecies
	iSelectedSpecies = pEvent.GetInt()


def SelectShipInQueue(pObject, pEvent):
	global iSelectedShipInQueue
	iSelectedShipInQueue = pEvent.GetInt()


def BuildShipSelectWindow(pConstructor):
	global pSubPane
	pSubPane = App.STSubPane_Create(SHIPS_SUBPANE_WIDTH, 500.0, 0)
	
	for iIndex in range(len(pConstructor.lShipsToConstruct)):
		Ship = pConstructor.lShipsToConstruct[iIndex]
		FdtnShip = Foundation.shipList[Ship]
		ShipLongName = FdtnShip.name
		
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_SELECT_SHIP_TYPE)
                pEvent.SetInt(iIndex)		# store the index so we know which button was clicked.
                pEvent.SetDestination(pConstructWindow)
		
		pButton = App.STButton_CreateW(App.TGString(ShipLongName), pEvent)
		pEvent.SetSource(pButton)
		
		pSubPane.AddChild(pButton, 0, 0, 0)
        pSubPane.Layout()
        pConstructWindow.AddChild(pSubPane)
	

def IsTargetAFriendlyConstructShip(pPlayer, pShip):
	global iSelectedDock
	if not pShip:
		return 0
	return GetConstructInstanceFor(pShip, iSelectedDock) and IsSameGroup(pPlayer, pShip)


def TargetChanged(pObject, pEvent):
	global iNumDocks
	pPlayer = MissionLib.GetPlayer()
	pTarget = pPlayer.GetTarget()
	pMenu = Libs.LibEngineering.GetBridgeMenu("Helm")

	if pMenu:
		pButton = Libs.LibEngineering.GetButton(sButtonName, pMenu)
		if not pTarget or not IsTargetAFriendlyConstructShip(pPlayer, App.ShipClass_Cast(pTarget)) and pButton:
			pMenu.DeleteChild(pButton)
		elif IsTargetAFriendlyConstructShip(pPlayer, App.ShipClass_Cast(pTarget)) and not pButton:
			pButton = Libs.LibEngineering.CreateMenuButton(sButtonName, "Helm", __name__ + ".ConstructControl")
			iNumDocks = GetNumDocks(App.ShipClass_Cast(pTarget))
	
	pObject.CallNextHandler(pEvent)
	

def init():
	global pPlayer
	
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
	
	pPlayer = MissionLib.GetPlayer()
	pPlayer.AddPythonFuncHandlerForInstance(App.ET_TARGET_WAS_CHANGED, __name__+ ".TargetChanged")
	

def exit():
	global pConstructWindow
	
	if not pPlayer:
		return
	
	pPlayer.RemoveHandlerForInstance(App.ET_TARGET_WAS_CHANGED, __name__+ ".TargetChanged")
	if pConstructWindow:
		pConstructWindow.KillChildren()
		pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
		pTacticalControlWindow.DeleteChild(pConstructWindow)
		pConstructWindow = None
	
	
def NewPlayerShip():
	global pPlayer
	if pPlayer:
		pPlayer.RemoveHandlerForInstance(App.ET_TARGET_WAS_CHANGED, __name__+ ".TargetChanged")
	pPlayer = MissionLib.GetPlayer()
	if pPlayer:
		pPlayer.AddPythonFuncHandlerForInstance(App.ET_TARGET_WAS_CHANGED, __name__+ ".TargetChanged")


def Restart():
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
	NewPlayerShip()


# handle mouse clicks in empty space
def PassMouse(pWindow, pEvent):
        pWindow.CallNextHandler(pEvent)

        if pEvent.EventHandled() == 0:
                pEvent.SetHandled()
