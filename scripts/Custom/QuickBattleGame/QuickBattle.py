from bcdebug import debug
import App
import loadspacehelper
import MissionLib
import Actions.MissionScriptActions
import Bridge.PowerDisplay
import Bridge.TacticalMenuHandlers
import Bridge.HelmMenuHandlers
import Tactical.Interface.TacticalControlWindow
import Bridge.BridgeUtils
import Effects

import QBGUI
import QBFile
import Foundation
import Lib.Ambiguity

g_version = "2.3"

qbGameMode = None 

gShips = []

gSystem = []
gBridge = ''
gPlugins = []
gPluginsVer = []

TRUE = 1
FALSE = 0

pEnemies = None
pFriendlies = None
pNeutrals = None
pNeutrals2 = None

g_pCriticalFriendly = []
g_pCriticalEnemy = []

g_pDatabase = None
g_pDockButton = None
g_pMission = None

g_pSubPane = None

g_pKiska = None
g_pFelix = None
g_pSaffi = None
g_pMiguel = None
g_pBrex = None

ET_PRELOAD_DONE = None
ET_FLEETATTACK = None
ET_FLEETRESUME = None

ET_SHIP_TIMER = None
dict_Timer = {}

def PreLoadAssets(pMission):
	debug(__name__ + ", PreLoadAssets")
	InitLists()
		
	for ship in gShips:
		loadspacehelper.PreloadShip(ship["class"], 1)
		
def Initialize(pMission):
	debug(__name__ + ", Initialize")
	global pEnemies
	pEnemies = MissionLib.GetEnemyGroup()
	global pFriendlies
	pFriendlies = MissionLib.GetFriendlyGroup()
	global pNeutrals
	pNeutrals = MissionLib.GetNeutralGroup()
	
	global pNeutrals2
	pNeutrals2 = App.ObjectGroup()
	
	global g_pDatabase
	g_pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
	global g_pQBDatabase
	g_pQBDatabase = App.g_kLocalizationManager.Load('data/TGL/QuickBattle/QuickBattle.tgl')
	global g_pMission
	g_pMission = pMission
	global ET_PRELOAD_DONE
	ET_PRELOAD_DONE = App.Mission_GetNextEventType()
	global ET_FLEETATTACK
	ET_FLEETATTACK = App.Mission_GetNextEventType()
	global ET_FLEETRESUME
	ET_FLEETRESUME = App.Mission_GetNextEventType()

	global qbGameMode 
	qbGameMode = Foundation.BuildGameMode()
	qbGameMode.Activate()
	
	CreateStartingRegions()
	import LoadBridge
	LoadBridge.Load(gBridge)
	InitializeCrewPointers()
	AddSystemMenus()
	CreateFleetMenu()

	CreateStartingObjects(pMission)
	CreateObjectives()

	SetupEventHandlers(pMission)

	ConfigInit()

	executePlugins(pMission)
	
def executePlugins(pMission):
	debug(__name__ + ", executePlugins")
	import nt
	import string

	list = nt.listdir('scripts/Custom/QuickBattleGame/Plugins')
	list.sort()

	#dotPrefix = string.join(string.split(dir, '\\')[1:], '.') + '.'
	global gPlugins
	gPlugins = []

	for plugin in list:
		s = string.split(plugin, '.')
		if len(s) <= 1:
			continue
		extension = s[-1]
		fileName = string.join(s[:-1], '.')

		if (extension == 'pyc' or extension == 'py'):
			try:
				if (gPlugins.count(fileName) == 0):
					pModule = __import__("Custom.QuickBattleGame.plugins." + fileName)
					ver = ""
					if (dir(pModule).count('Version')>0):
						ver = pModule.Version()
					else:
						ver = fileName
					gPlugins.append(fileName)
					gPluginsVer.append(ver)
					if (dir(pModule).count('Initialize')>0):
						pModule.Initialize(pMission)
			except:
				import sys
				print sys.exc_info()[0]
				print sys.exc_info()[1]
				print sys.exc_info()[2]
	
def restartPlugins():
	debug(__name__ + ", restartPlugins")
	for plugin in gPlugins:
		pModule = __import__("Custom.QuickBattleGame.plugins." + plugin)
		if (dir(pModule).count('Restart')>0):
			pModule.Restart()

def terminatePlugins():
	debug(__name__ + ", terminatePlugins")
	for plugin in gPlugins:
		pModule = __import__("Custom.QuickBattleGame.plugins." + plugin)
		if (dir(pModule).count('Terminate')>0):
			pModule.Terminate()
	
def Terminate(pMission):
	debug(__name__ + ", Terminate")
	QBGUI.Remove()
	
	global qbGameMode
	qbGameMode.Deactivate()
	qbGameMode = None
	
	RemoveInstanceHandlers()

	if (g_pDatabase != None):
		App.g_kLocalizationManager.Unload(g_pDatabase)
		
	terminatePlugins()
	
	Lib.Ambiguity.terminate()

def InitLists():
	debug(__name__ + ", InitLists")
	global gSystem, gBridge, gShips

	QBFile.LoadSetup("QBSetup")

	gSystem                =  QBFile.g_pSystem           
	gBridge                =  QBFile.g_sBridge           
	gShips		       =  QBFile.g_pShips
	
	try:
		import plugin
		import QBSetup
		plugin.gPluginData = QBSetup.gPluginData
	except:
		plugin.gPluginData = {}

def InitializeCrewPointers():
	debug(__name__ + ", InitializeCrewPointers")
	pBridge = App.g_kSetManager.GetSet('bridge')
	global g_pKiska
	g_pKiska = App.CharacterClass_GetObject(pBridge, 'Helm')
	global g_pFelix
	g_pFelix = App.CharacterClass_GetObject(pBridge, 'Tactical')
	global g_pSaffi
	g_pSaffi = App.CharacterClass_GetObject(pBridge, 'XO')
	global g_pMiguel
	g_pMiguel = App.CharacterClass_GetObject(pBridge, 'Science')
	global g_pBrex
	g_pBrex = App.CharacterClass_GetObject(pBridge, 'Engineer')
	
def AddSystemMenus():
	debug(__name__ + ", AddSystemMenus")
	for system in gSystem:
		if (system[0] == 'Starbase12'):
			continue # Starbase12 will only crash us
			import Systems.Starbase12.Starbase
			pMenu = Systems.Starbase12.Starbase.CreateMenus()
		elif (system[0] == 'DryDock'):
			import Systems.DryDock.DryDockSystem
			pMenu = Systems.DryDock.DryDockSystem.CreateMenus()		
		elif (system[0] == 'QuickBattle'):
			import Systems.QuickBattle.QuickBattleSystem
			pMenu = Systems.QuickBattle.QuickBattleSystem.CreateMenus()		
		else:
			pModule = __import__('Systems.' + system[0] + '.' + system[0])
			if (hasattr(pModule, "CreateMenus")):
				pMenu = pModule.CreateMenus()
			else:
				import Systems.Utils
				Systems.Utils.CreateSystemMenu(system[0], 'Systems.' + system[0] + '.' + system[0])

		if (system[2] != ''):
			pMenu.SetEpisodeName(system[2])
		
def RemoveSystemMenus():
	debug(__name__ + ", RemoveSystemMenus")
	App.SortedRegionMenu_ClearSetCourseMenu()		

def CreateStartingObjects(pMission):
	debug(__name__ + ", CreateStartingObjects")
	AddShips()
	
	pPlayer = MissionLib.GetPlayer()
	if (pPlayer is None):
		return 

def AddShips():
	debug(__name__ + ", AddShips")
	import QuickBattleAI
	import QuickBattleFriendlyAI
	import StarbaseAI
	import StarbaseFriendlyAI
	import NeutralAI
	import Neutral2AI
	import StarbaseNeutralAI
	import StarbaseNeutral2AI

	pEnemies.RemoveAllNames()
	pFriendlies.RemoveAllNames()
	pNeutrals.RemoveAllNames()
	pNeutrals2.RemoveAllNames()

	# Player ship has to be created first, so move it to the start of the list
	playerShip = None
	for ship in gShips:
		if ship["group"] == 'player':
			playerShip = ship
	if playerShip != None:
		gShips.remove(ship)
		gShips.insert(0, ship)
	
	for pShip in gShips:
		pSet = App.g_kSetManager.GetSet(pShip["system"])
		
		if not pShip.has_key("minETA"):
			pShip["minETA"] = 0
			pShip["maxETA"] = 0
		
		if pShip["group"] == 'player':
			pLoadedShip = MissionLib.CreatePlayerShip(pShip["class"], pSet, pShip["name"], '')
		elif (pShip["minETA"] == 0 and pShip["maxETA"] == 0):
			pLoadedShip = loadspacehelper.CreateShip(pShip["class"], pSet, pShip["name"], '')
		else:
			TimerAddShip(pShip)
			continue
		
		TranslateShip(pLoadedShip, pShip["pos"][0], pShip["pos"][1], pShip["pos"][2])
		DamageShipRandomly(pLoadedShip, pShip["mindamage"], pShip["maxdamage"])			

		if pShip["group"] == "player":
			pFriendlies.AddName(pShip["name"])
		elif pShip["group"] == "friend":
			pFriendlies.AddName(pShip["name"])
			if pShip["starbase"] == 0:
				MissionLib.AddCommandableShip(pShip["name"])
		elif pShip["group"] == "enemy":
			pEnemies.AddName(pShip["name"])
		elif pShip["group"] == "neutral":
			pNeutrals.AddName(pShip["name"])
		elif pShip["group"] == "neutral2":
			pNeutrals2.AddName(pShip["name"])
			
	# If lists have no names in it, just make one up.
	if not pEnemies.GetNameTuple():
		pEnemies.AddName("butnowforsomethingcompletelydifferent")
	if not pFriendlies.GetNameTuple():
		pFriendlies.AddName("alwayslookatthebrightsideoflife")
	if not pNeutrals.GetNameTuple():
		pNeutrals.AddName("supercalifragilisticexpialigotious")
	if not pNeutrals2.GetNameTuple():
		pNeutrals2.AddName("itwasthebestoftimes")

	# AI has to be created after everything else
	for ship in gShips:
		pSet = App.g_kSetManager.GetSet(ship["system"])
		pShip = MissionLib.GetShip(ship["name"], pSet)

		if not pShip:
			continue

		if ship["ai"] != "":
			try:
				pModule = __import__(ship["ai"])
				ai = apply(pModule.CreateAI, (pShip,))
				pShip.SetAI(ai)
			except:
				print "AI file ", pShip["ai"], " is not valid."     	
		elif ship["group"] == "friend":
			if ship["starbase"] == 0:
				pShip.SetAI(QuickBattleFriendlyAI.CreateAI(pShip, ship["ailevel"], ship["warp"]))
			else:
				pShip.SetAI(StarbaseFriendlyAI.CreateAI(pShip))
		elif ship["group"] == "enemy":
			if ship["starbase"] == 0:
				pShip.SetAI(QuickBattleAI.CreateAI(pShip, ship["ailevel"], ship["warp"]))
			else:
				pShip.SetAI(StarbaseAI.CreateAI(pShip))
		elif ship["group"] == "neutral":
			if ship["starbase"] == 0:
				pShip.SetAI(NeutralAI.CreateAI(pShip, ship["ailevel"], ship["warp"]))
			else:
				pShip.SetAI(StarbaseNeutralAI.CreateAI(pShip))
		elif ship["group"] == "neutral2":
			if ship["starbase"] == 0:
				pShip.SetAI(Neutral2AI.CreateAI(pShip, ship["ailevel"], ship["warp"]))
			else:
				pShip.SetAI(StarbaseNeutral2AI.CreateAI(pShip))


def CreateObjectives():
	debug(__name__ + ", CreateObjectives")
	pBridgeSet = App.g_kSetManager.GetSet('bridge')
	pSaffi = App.CharacterClass_GetObject(pBridgeSet, 'XO')


	pSaffiMenu = g_pSaffi.GetMenu()
	if (pSaffiMenu == None):
		return 0
	pObjectivesMenu = pSaffiMenu.GetSubmenuW(g_pDatabase.GetString('Objectives'))
	if (pObjectivesMenu != None):
		pObjectivesMenu.KillChildren()
		import Lib.Ambiguity
		for ship in gShips:
			if ship["missioncritical"]:
				pButton = Lib.Ambiguity.createButton(pObjectivesMenu, "", None, "Objective", "XO")
				if ship["group"] == "enemy" or ship["group"] == "neutral2":
					g_pCriticalEnemy.append(ship)
					pButton.SetName(App.TGString(ship["name"] + " must be destroyed"))					
				else:
					g_pCriticalFriendly.append(ship)
					pButton.SetName(App.TGString(ship["name"] + " must survive"))					

def TranslateShip(pShip, x, y, z):
	debug(__name__ + ", TranslateShip")
	pPlayer = App.Game_GetCurrentPlayer()

	if (x == y == z == 0):
		if (pShip.GetName() != pPlayer.GetName()):
			PlaceShipRandomly(pShip)
	else:
		p = App.TGPoint3()
		p.SetX(x)
		p.SetY(y)
		p.SetZ(z)
		pShip.SetTranslate(p)


def CreateStartingRegions():
	debug(__name__ + ", CreateStartingRegions")
	for system in gSystem:
		if (App.g_kSetManager.GetSet(system[1]) is None):
			MissionLib.SetupSpaceSet('Systems.' + system[0] + '.' + system[1])
	
def CreateFleetMenu():
	debug(__name__ + ", CreateFleetMenu")
	pHailMenu = MissionLib.GetCharacterSubmenu("Helm", "Hail")

	pFleetMenu = App.STMenu_CreateW(App.TGString("Fleet")) 
	pHailMenu.AddChild(pFleetMenu)

	g_pKiska.AddPythonFuncHandlerForInstance(ET_FLEETATTACK, (__name__ + '.FleetAttack'))
	pFleetMenu.AddChild(CreateBridgeMenuButton(App.TGString('Attack Target'), ET_FLEETATTACK, 0, g_pKiska))
	g_pKiska.AddPythonFuncHandlerForInstance(ET_FLEETRESUME, (__name__ + '.FleetResume'))
	pFleetMenu.AddChild(CreateBridgeMenuButton(App.TGString('Resume Old Orders'), ET_FLEETRESUME, 0, g_pKiska))

def CreateBridgeMenuButton(pName, eType, iSubType, pCharacter):
	debug(__name__ + ", CreateBridgeMenuButton")
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(iSubType)
	BridgeMenuButton = App.STButton_CreateW(pName, pEvent)
	return BridgeMenuButton
	
def SetupEventHandlers(pMission):
	debug(__name__ + ", SetupEventHandlers")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_DESTROYED, pMission, __name__ + ".ShipDestroyed")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ShipExploding")

	pKiskaMenu = Bridge.BridgeUtils.GetBridgeMenu("Helm")
	if (pKiskaMenu != None):
		pKiskaMenu.AddPythonFuncHandlerForInstance(App.ET_DOCK,	__name__ + ".DockButtonClicked")
		pKiskaMenu.AddPythonFuncHandlerForInstance(App.ET_HAIL,	__name__ + ".HailHandler")

	pBrexMenu = Bridge.BridgeUtils.GetBridgeMenu('Engineer')
	if (pBrexMenu != None):
		event = Lib.Ambiguity.getEvent("ET_TRANSPORT")
		g_pBrex.AddPythonFuncHandlerForInstance(event, __name__ + ".Transport")
		pButton = CreateBridgeMenuButton(App.TGString('Evacuate'), event, 0, g_pBrex)
		pBrexMenu.PrependChild(pButton)				  

	
	event = Lib.Ambiguity.addEventHandler("XO", "ET_CONFIG", __name__ + ".Config")
	Lib.Ambiguity.createMenuButton("XO", "Configure", event, "Configure")
	event = Lib.Ambiguity.addEventHandler("XO", "ET_CREDITS", __name__ + ".Credits")
	Lib.Ambiguity.createMenuButton("XO", "Credits", event, "Credits")

	# Timer
	global ET_SHIP_TIMER
	ET_SHIP_TIMER = App.Mission_GetNextEventType()
	App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(ET_SHIP_TIMER, __name__ + ".TimerCreateShip")

def RemoveInstanceHandlers():
	debug(__name__ + ", RemoveInstanceHandlers")
	pBrexMenu = Bridge.BridgeUtils.GetBridgeMenu('Engineer')
	if (pBrexMenu != None):
		g_pBrex.RemoveHandlerForInstance(Lib.Ambiguity.getEvent("ET_TRANSPORT"), __name__ + ".Transport")
		
	pKiskaMenu = Bridge.BridgeUtils.GetBridgeMenu("Helm")
	if (not pKiskaMenu is None):
		pKiskaMenu.RemoveHandlerForInstance(App.ET_DOCK, __name__ + ".DockButtonClicked")
		pKiskaMenu.RemoveHandlerForInstance(App.ET_HAIL, __name__ + ".HailHandler")
		g_pKiska.RemoveHandlerForInstance(ET_FLEETATTACK, (__name__ + '.FleetAttack'))
		g_pKiska.RemoveHandlerForInstance(ET_FLEETRESUME, (__name__ + '.FleetResume'))

	# Timer
	global ET_SHIP_TIMER
	App.TopWindow_GetTopWindow().RemoveHandlerForInstance(ET_SHIP_TIMER, __name__ + ".TimerCreateShip")

def DockButtonClicked(pObject, pEvent):	
	debug(__name__ + ", DockButtonClicked")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer:
		DockStarbase()

	pObject.CallNextHandler(pEvent)
	import BridgeHandlers
	BridgeHandlers.DropMenusTurnBack()

def DockStarbase():
	# Get Player.
	debug(__name__ + ", DockStarbase")
	pPlayer = MissionLib.GetPlayer()
	pStarbase = FindStarbase(pPlayer)
	
	if (pStarbase is None):
		return

	MissionLib.SetTotalTorpsAtStarbase("Photon", -1)
	MissionLib.SetTotalTorpsAtStarbase("Quantum", -1)
	MissionLib.SetTotalTorpsAtStarbase("Adv. Photon", -1)
	MissionLib.SetTotalTorpsAtStarbase("Positron", -1)
	MissionLib.SetTotalTorpsAtStarbase("Phased", -1)

	pGraffAction = None
	# Set AI for docking/undocking.
	import AI.Compound.DockWithStarbase
	MissionLib.SetPlayerAI("Helm", AI.Compound.DockWithStarbase.CreateAI(pPlayer, pStarbase, pGraffAction, NoRepair = FALSE, FadeEnd = TRUE))

def FleetDock(pShip):	
	debug(__name__ + ", FleetDock")
	pStarbase = FindStarbase(pShip)
			
	if(pStarbase is None):
		return

	MissionLib.SetTotalTorpsAtStarbase("Photon", -1)
	MissionLib.SetTotalTorpsAtStarbase("Quantum", -1)
	MissionLib.SetTotalTorpsAtStarbase("Adv. Photon", -1)
	MissionLib.SetTotalTorpsAtStarbase("Positron", -1)
	MissionLib.SetTotalTorpsAtStarbase("Phased", -1)
	Bridge.HelmMenuHandlers.OverrideAI(pShip, "AI.Fleet.DockStarbase", pShip.GetObjID(), pStarbase.GetObjID(), None, NoRepair = FALSE, FadeEnd = TRUE)


def FindStarbase(pShip):
	debug(__name__ + ", FindStarbase")
	if pShip:
		pStarbaseSet = pShip.GetContainingSet()
		if(pStarbaseSet is None):
			return
	
		# Get Starbase.
		pStarbase = None
		for pShip in gShips:
			if pShip["group"] == "friend" and pShip["starbase"] != 0:
				pStarbase = pStarbaseSet.GetObject(pShip["name"])
				if ((not pStarbase is None) or (pShip["class"] == "FedStarbase")):
					break
		
		if(pStarbase is None):
			return
		
		return pStarbase

def FleetAttack(pObject, pEvent):
	debug(__name__ + ", FleetAttack")
	pPlayer = MissionLib.GetPlayer()
	pTarget = pPlayer.GetTarget()
	pSet = pPlayer.GetContainingSet()
	if pTarget:
		lpFriendlies = pFriendlies.GetActiveObjectTupleInSet(pSet)
		for pObject in lpFriendlies:
			pFriend = App.ShipClass_Cast(pObject)
			if (pFriend.GetName() != pPlayer.GetName()) and (pFriend.GetImpulseEngineSubsystem() != None):
				import Bridge.HelmMenuHandlers
				Bridge.HelmMenuHandlers.OverrideAI(pFriend, "AI.Fleet.DestroyTarget", pFriend.GetObjID(), pTarget.GetObjID())

	if (pObject):
		pObject.CallNextHandler(pEvent)

def FleetResume(pObject, pEvent):
	debug(__name__ + ", FleetResume")
	pPlayer = MissionLib.GetPlayer()
	pTarget = pPlayer.GetTarget()
	pSet = pPlayer.GetContainingSet()
	if pTarget:
		lpFriendlies = pFriendlies.GetActiveObjectTupleInSet(pSet)
		for pObject in lpFriendlies:
			pFriend = App.ShipClass_Cast(pObject)
			import Bridge.HelmMenuHandlers
			Bridge.HelmMenuHandlers.StopOverridingAI(pFriend)
	
	if (pObject):
		pObject.CallNextHandler(pEvent)

def HailHandler(TGObject, pEvent):
	# Get the player and their target
	debug(__name__ + ", HailHandler")
	pPlayer = MissionLib.GetPlayer()
	if (pPlayer is None):
		return
	pTarget	= App.ObjectClass_Cast(pEvent.GetSource())
	if (pTarget is None):
		return
		
	sTargetName = pTarget.GetName()

	pStarbase = FindStarbase(pPlayer)
	if (pStarbase is None):
		return
		
	sStarbaseName = pStarbase.GetName()
	
	if (sTargetName == sStarbaseName):
		DockStarbase()
	else:
		FleetDock(pTarget)

	
def Credits(pObject, pEvent):

	debug(__name__ + ", Credits")
	pPane = App.TGPane_Create(1.0, 1.0)
	App.g_kRootWindow.PrependChild(pPane)	# stick it in front

	MissionLib.LookForward(None, TRUE)

	pSequence = App.TGSequence_Create()
	pSequence.SetUseRealTime (1)
	pSequence.SetSkippable(1)

	pAction = LineAction("QuickBattle Replacement " + g_version, pPane, 15, 5, 16)
	pSequence.AddAction(pAction, None, 0)

	pAction = LineAction("Created 2002 by Banbury", pPane, 17, 5, 12)
	pSequence.AddAction(pAction, None, 1)
	
	pAction = LineAction("Tutorial and additional changes by", pPane, 15, 5, 14)
	pSequence.AddAction(pAction, None, 7)
	pAction = LineAction("Capt. Redbeard", pPane, 18, 6, 16)
	pSequence.AddAction(pAction, None, 7)

	pAction = LineAction("Additional coding by", pPane, 15, 5, 14)
	pSequence.AddAction(pAction, None, 16)
	pAction = LineAction("Defiant", pPane, 18, 6, 16)
	pSequence.AddAction(pAction, None, 16)

	pAction = LineAction("Greetings to", pPane, 12, 8, 14)
	pSequence.AddAction(pAction, None, 25)
	pAction = LineAction("all the nice people", pPane, 15, 8, 12)
	pSequence.AddAction(pAction, None, 25)
	pAction = LineAction("at Bridge Commander Universe", pPane, 17, 8, 12)
	pSequence.AddAction(pAction, None, 25)
	
	pAction = LineAction("Special Greetings to", pPane, 15, 5, 14)
	pSequence.AddAction(pAction, None, 34)
	pAction = LineAction("Dasher42", pPane, 18, 6, 16)
	pSequence.AddAction(pAction, None, 35)

	pSequence.Play()
	
	return 0

def LineAction(sLine, pPane, fPos, duration, fontSize):
	debug(__name__ + ", LineAction")
	fHeight = fPos * 0.0375
	pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
	return pAction
	
def ConfigInit():
	debug(__name__ + ", ConfigInit")
	QBGUI.SetBridge(gBridge)

	QBGUI.Init(g_pMission)
	QBGUI.RebuildShipList()
			
	g_pSaffi.AddPythonFuncHandlerForInstance(QBGUI.ET_START_BUTTON, (__name__ + '.StartSimulation'))



def Config(pObject, pEvent):
	debug(__name__ + ", Config")
	pTopWindow = App.TopWindow_GetTopWindow()
	if (not pTopWindow.IsBridgeVisible()):
		pTopWindow.ForceBridgeVisible()
	
#	pSequence = App.TGSequence_Create()
#	pTest = App.CharacterAction_Create(g_pSaffi, App.CharacterAction.AT_PLAY_ANIMATION_FILE, "skel1_3")
#	pTest = App.CharacterAction_Create(g_pSaffi, App.CharacterAction.AT_PLAY_ANIMATION_FILE, "pointing_left")
#	pSequence.AppendAction(pTest)
#	pSequence.Play()

	QBGUI.OpenDialog()
	
	if (pObject):
		pObject.CallNextHandler(pEvent)

def StartSimulation(pObject, pEvent):
	debug(__name__ + ", StartSimulation")
	if (QBGUI.CheckSetup() == 0):
		pTopWindow = App.TopWindow_GetTopWindow()
		pModalDialogWindow = App.ModalDialogWindow_Cast (pTopWindow.FindMainWindow (App.MWT_MODAL_DIALOG))
		pModalDialogWindow.Run(None, App.TGString("Not enough data. Please check that all your ships have a name and a starting system and that you have assigned a PLAYER ship."), App.TGString("OK"), None, None, None)
	else:
		ResetQB()
		if (pObject):
			pObject.CallNextHandler(pEvent)

def ChangeGlobals():
	debug(__name__ + ", ChangeGlobals")
	global gBridge
	gBridge = QBGUI.g_Bridge
	
	global gSystem
	gSystem = []
	for system in QBFile.g_pRegionListData:
		import strop
		s = strop.split(system, '.')
		gSystem.append([s[0], s[1], ''])		
	
	global gShips
	gShips = []
	
	keys = QBFile.g_pShipListData.keys()
	for key in keys:
		ship = QBFile.g_pShipListData[key]
		gShips.append(ship)

def ResetQB():
	debug(__name__ + ", ResetQB")
	pTopWindow = App.TopWindow_GetTopWindow()
	pTopWindow.AllowKeyboardInput(0)
	pTopWindow.AllowMouseInput(0)

	Bridge.TacticalMenuHandlers.ClearOrderMenus ()
	App.CharacterAction_Create(g_pSaffi, App.CharacterAction.AT_MENU_DOWN).Play()
	RemoveSystemMenus()

	for pSet in App.g_kSetManager.GetAllSets():	
		for kShip in pSet.GetClassObjectList(App.CT_DAMAGEABLE_OBJECT):
			if kShip.GetName() != MissionLib.GetPlayer().GetName():
				pSet.RemoveObjectFromSet(kShip.GetName())
				kShip.SetDeleteMe(1)
		for kTorp in pSet.GetClassObjectList(App.CT_TORPEDO):
				kTorp.SetDeleteMe(1)

	ChangeGlobals()
	CreateStartingRegions()
	RecreatePlayer()
	AddSystemMenus()
	AddShips()
	CreateObjectives()

	# Switch us to green alert
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(App.Game_GetCurrentGame().GetPlayer())
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(App.Game_GetCurrentGame().GetPlayer().GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)

	# dump the unused models
	App.g_kLODModelManager.Purge()

	pTopWindow.AllowKeyboardInput(1)
	pTopWindow.AllowMouseInput(1)
	
	restartPlugins()
		
def RecreatePlayer():
	debug(__name__ + ", RecreatePlayer")
	pPlayer = MissionLib.GetPlayer()
	pSet = None
	if pPlayer:
		pSet = pPlayer.GetContainingSet()
		pPlayer.SetDead()
		pSet.DeleteObjectFromSet(pPlayer.GetName())

#	ship = None
#	for s in QBFile.g_pShips:
#		if s["group"] == "player":
#			ship = s

#	pQBSet = App.g_kSetManager.GetSet(ship["system"])
#	pPlayer = MissionLib.CreatePlayerShip(ship["class"], pQBSet, ship["name"], '')
#	TranslateShip(pPlayer, ship["pos"][0], ship["pos"][1], ship["pos"][2])

#	# Update the ship with its new positional information...
#	pPlayer.UpdateNodeOnly()

#	# update the proximity manager with this object's new position.
#	pProximityManager = pQBSet.GetProximityManager()
#	if (pProximityManager):
#		pProximityManager.UpdateObject (pPlayer)

	# Reload our bridge, just in case
	import LoadBridge
	LoadBridge.Load(gBridge)

#	path = "data/Textures/Uniforms/voyager/"
#	import QBCharacter
#	global g_pMiguel
#	g_pMiguel = QBCharacter.LoadCrew(path, gBridge)


	# Reassign global pointers
	InitializeCrewPointers()

#	return pPlayer
	
def PlaceShipRandomly(pShip):
	debug(__name__ + ", PlaceShipRandomly")
	pSet = pShip.GetContainingSet()
	
	vLocation = pShip.GetWorldLocation()
	vForward = pShip.GetWorldForwardTG()
	vForward.Scale(pShip.GetRadius() + pShip.GetRadius() + 200.0)

	kPoint = App.TGPoint3()
	ChooseNewLocation(vLocation, vForward)
	kPoint.Set(vLocation)
	kPoint.Add(vForward)

	fRadius = pShip.GetRadius () * 2.0

	while pSet.IsLocationEmptyTG(kPoint, fRadius, 1) == 0:
		ChooseNewLocation(vLocation, vForward)
		kPoint.Set(vLocation)
		kPoint.Add(vForward)

	pShip.SetTranslate(kPoint)

def ChooseNewLocation(vOrigin, vOffset):
	# Add some random amount to vOffset
	debug(__name__ + ", ChooseNewLocation")
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber (1000) + 750)

	vOffset.SetX( vOffset.GetX() + fUnitRandom )


	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber (1000) + 750)

	vOffset.SetY( vOffset.GetY() + fUnitRandom )

	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber (1000) + 750)

	vOffset.SetZ( vOffset.GetZ() + fUnitRandom )

	return 0

def ShipDestroyed(pObject, pEvent):
	debug(__name__ + ", ShipDestroyed")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()

	# Get the ship that was destroyed.
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip != None):
		if (pPlayer and pShip.GetName() == pPlayer.GetName()):
			ResetQB()
			ResetView()
		else:
			bMissionState = 0
			name = pShip.GetName()
			
			import QBFile
                        if not QBFile.g_pShipListData.has_key(name):
                                if (pObject):
		                        pObject.CallNextHandler(pEvent)
                                return

			shipinfo = QBFile.g_pShipListData[name]
			bMissionState = shipinfo["missioncritical"]
			
			if (pEnemies.IsNameInGroup(name) or pNeutrals2.IsNameInGroup(name)):
				pLine1 = App.CharacterAction_Create(g_pFelix, App.CharacterAction.AT_SAY_LINE, "QBEnemyGenericShipDestroyed", "Captain", 1, g_pQBDatabase)
				if bMissionState:
					g_pCriticalEnemy.remove(shipinfo)
					if len(g_pCriticalEnemy) == 0:
						MissionWon()
					return
					
			elif (pFriendlies.IsNameInGroup(name) or pNeutrals.IsNameInGroup(name)):
				pLine1 = App.CharacterAction_Create(g_pFelix, App.CharacterAction.AT_SAY_LINE, "QBFriendlyGenericShipDestroyed", "Captain", 1, g_pQBDatabase)
				if bMissionState:
					g_pCriticalFriendly.remove(shipinfo)
					if len(g_pCriticalFriendly) == 0:
						MissionLost()
					return
	
			pSequence = App.TGSequence_Create()
			pSequence.AddAction(pLine1)
			pSequence.Play()
		
	if (pObject):
		pObject.CallNextHandler(pEvent)
		
def MissionWon():
	debug(__name__ + ", MissionWon")
	import DynamicMusic
	DynamicMusic.PlayFanfare("Win")

	pLine1 = App.CharacterAction_Create(g_pSaffi, App.CharacterAction.AT_SAY_LINE, "QBComputerWin", "Captain", 0, g_pQBDatabase)
	pReset = App.TGScriptAction_Create(__name__, "ResetQBAction")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(pLine1)
	pSequence.AppendAction(pReset, 5)
	pSequence.Play()
	
def MissionLost():
	debug(__name__ + ", MissionLost")
	import DynamicMusic
	DynamicMusic.PlayFanfare("Lose")

	pLine1 = App.CharacterAction_Create(g_pSaffi, App.CharacterAction.AT_SAY_LINE, "QBComputerLose", "Captain", 0, g_pQBDatabase)
	pReset = App.TGScriptAction_Create(__name__, "ResetQBAction")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(pLine1)
	pSequence.AppendAction(pReset, 5)
	pSequence.Play()
	
def ResetQBAction(pAction):
	debug(__name__ + ", ResetQBAction")
	ResetQB()
	ResetView()
	return 0
	
def ResetView():
	# Force back to the bridge
	debug(__name__ + ", ResetView")
	pTopWindow = App.TopWindow_GetTopWindow()
	pTopWindow.ForceBridgeVisible()

	# Need to reset interactive mode, otherwise you'll get stuck if you go
	# to this mode.
	pCinematic = App.CinematicWindow_Cast(pTopWindow.FindMainWindow(App.MWT_CINEMATIC))
	if pCinematic:
		pCinematic.SetInteractive(1)

	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	if pPlayer:
		pPlayer.SetTarget(None)

def ShipExploding(pObject, pEvent):
	debug(__name__ + ", ShipExploding")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()

	# Get the ship that was destroyed.
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip != None):
		if (pPlayer and pShip.GetName() == pPlayer.GetName()):
			import DynamicMusic
			DynamicMusic.PlayFanfare("PlayerBlewUp")
		else:
			import DynamicMusic
			DynamicMusic.PlayFanfare("EnemyBlewUp")
			
	if (pObject):
		pObject.CallNextHandler(pEvent)

def Distance(pObject):
	debug(__name__ + ", Distance")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()

def Transport(pObject, pEvent):
	debug(__name__ + ", Transport")
	pPlayer = MissionLib.GetPlayer()
	pTarget = pPlayer.GetTarget()
	pSet = pPlayer.GetContainingSet()
	dist = 300
	pClosest = None
	lpFriendlies = pFriendlies.GetActiveObjectTupleInSet(pSet)
	for pObject in lpFriendlies:
		pFriend = App.ShipClass_Cast(pTarget)
		d = Distance(pFriend)
		if (d<dist) and (pFriend.GetName() != pPlayer.GetName()) and pFriend.GetImpulseEngineSubsystem() != None:
			pClosest = pFriend
			dist = d
	
	if (pClosest != None):
		MissionLib.RemoveCommandableShip(pClosest.GetName())
		MissionLib.AddCommandableShip(pPlayer.GetName())
		ai = pClosest.GetAI()

		pGame = App.Game_GetCurrentGame()

		pSetPlayerAction = App.TGScriptAction_Create(__name__, "SetPlayerAction", pClosest)
		
		pSequence = App.TGSequence_Create()
		
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.MissionScriptActions", "ChangeToBridge"))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "SetTarget", pClosest.GetName()))
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName()), 2)
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", pSet.GetName()))
		pSequence.AppendAction(pSetPlayerAction)	
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "LockedView", pSet.GetName(), pClosest.GetName(), 30, 30, 15))
		
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pSet.GetName()), 6)	
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "SetTarget", pPlayer.GetName()))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))

		pSequence.Play()

		MissionLib.SetPlayerAI("Captain", None)
		pPlayer.ClearAI()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def SetPlayerAction(pAction, pShip):
	debug(__name__ + ", SetPlayerAction")
	pGame = App.Game_GetCurrentGame()
	pGame.SetPlayer(pShip)
	return 0
		
def ZoomTarget(pAction, pSource, pTarget):
	debug(__name__ + ", ZoomTarget")
	import Camera
	Camera.ZoomTarget(pSource.GetName(), pTarget.GetName())
	return 0	
	
def DamageSystemRandomly(pSystem, fMinPercent, fMaxPercent):
	debug(__name__ + ", DamageSystemRandomly")
	if (pSystem):
		r = App.g_kSystemWrapper.GetRandomNumber(100)
		r = r / 100.0
		r = r * (fMaxPercent - fMinPercent)
		r = r + fMinPercent
		pSystem.SetConditionPercentage (r)
	
def DamageShipRandomly(pShip, fMinPercent, fMaxPercent):
	debug(__name__ + ", DamageShipRandomly")
	if (pShip):
		DamageSystemRandomly(pShip.GetHull(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetShields(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetPowerSubsystem(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetSensorSubsystem(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetImpulseEngineSubsystem(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetWarpEngineSubsystem(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetTorpedoSystem(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetPhaserSystem(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetPulseWeaponSystem(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetTractorBeamSystem(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetRepairSubsystem(), fMinPercent, fMaxPercent)
		DamageSystemRandomly(pShip.GetCloakingSubsystem(), fMinPercent, fMaxPercent)
		
def TimerAddShip(pShip):
	debug(__name__ + ", TimerAddShip")
	global ET_SHIP_TIMER, dict_Timer
	
	# Create an event - it's a thing that will call this function
	pTimerEvent = App.TGEvent_Create()
	pTimerEvent.SetEventType(ET_SHIP_TIMER)
	pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())
	
	if (pShip["minETA"] >= pShip["maxETA"]):
		CounterTime = int(pShip["minETA"])
	elif int(pShip["maxETA"]) - int(pShip["minETA"]) > 0:
		CounterTime = int(pShip["minETA"]) + App.g_kSystemWrapper.GetRandomNumber(int(pShip["maxETA"]) - int(pShip["minETA"]))

	# Create a timer - it's a thing that will wait for a given time,then do something
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + CounterTime * 60)
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pTimerEvent)
	App.g_kTimerManager.AddTimer(pTimer)

	# or any other Idea how to get Informations together with a Timer?
	dict_Timer[str(pTimerEvent)] = pShip

def TimerCreateShip(pObject, pEvent):
	debug(__name__ + ", TimerCreateShip")
	import QuickBattleAI
	import QuickBattleFriendlyAI
	import StarbaseAI
	import StarbaseFriendlyAI
	import NeutralAI
	import Neutral2AI
	import StarbaseNeutralAI
	import StarbaseNeutral2AI

	global dict_Timer
	ship = dict_Timer[str(pEvent)]

	pSet = App.g_kSetManager.GetSet(ship["system"])
	pPlayerSet = MissionLib.GetPlayer().GetContainingSet()
	if (pSet.GetName() == pPlayerSet.GetName()):
		WarpSound = 1
	else:
		WarpSound = 0

	# Rest here	is from	AddShips()
	pLoadedShip	= loadspacehelper.CreateShip(ship["class"], pSet, ship["name"],	'', WarpSound)

	TranslateShip(pLoadedShip, ship["pos"][0], ship["pos"][1], ship["pos"][2])
	DamageShipRandomly(pLoadedShip, ship["mindamage"], ship["maxdamage"])			

	if ship["group"] ==	"player":
		pFriendlies.AddName(ship["name"])
	elif ship["group"] == "friend":
		pFriendlies.AddName(ship["name"])
		if ship["starbase"]	== 0:
			MissionLib.AddCommandableShip(ship["name"])
	elif ship["group"] == "enemy":
		pEnemies.AddName(ship["name"])
	elif ship["group"] == "neutral":
		pNeutrals.AddName(ship["name"])
	elif ship["group"] == "neutral2":
		pNeutrals2.AddName(ship["name"])

	# If lists have no names in	it, just make one up.
	if not pEnemies.GetNameTuple():
		pEnemies.AddName("butnowforsomethingcompletelydifferent")
	if not pFriendlies.GetNameTuple():
		pFriendlies.AddName("alwayslookatthebrightsideoflife")
	if not pNeutrals.GetNameTuple():
		pNeutrals.AddName("supercalifragilisticexpialigotious")
	if not pNeutrals2.GetNameTuple():
		pNeutrals2.AddName("itwasthebestoftimes")

	# AI has to	be created after everything else
	pSet = App.g_kSetManager.GetSet(ship["system"])

	if ship["ai"] != "":
		try:
			pModule = __import__(ship["ai"])
			ai = apply(pModule.CreateAI, (pLoadedShip,))
			pLoadedShip.SetAI(ai)
		except:
			print "AI file ", pLoadedShip["ai"], " is not valid."	
	elif ship["group"] == "friend":
		if ship["starbase"]	== 0:
			pLoadedShip.SetAI(QuickBattleFriendlyAI.CreateAI(pLoadedShip, ship["ailevel"], ship["warp"]))
		else:
			pLoadedShip.SetAI(StarbaseFriendlyAI.CreateAI(pLoadedShip))
	elif ship["group"] == "enemy":
		if ship["starbase"]	== 0:
			pLoadedShip.SetAI(QuickBattleAI.CreateAI(pLoadedShip, ship["ailevel"], ship["warp"]))
		else:
			pLoadedShip.SetAI(StarbaseAI.CreateAI(pLoadedShip))
	elif ship["group"] == "neutral":
		if ship["starbase"]	== 0:
			pLoadedShip.SetAI(NeutralAI.CreateAI(pLoadedShip, ship["ailevel"], ship["warp"]))
		else:
			pLoadedShip.SetAI(StarbaseNeutralAI.CreateAI(pLoadedShip))
	elif ship["group"] == "neutral2":
		if ship["starbase"]	== 0:
			pLoadedShip.SetAI(Neutral2AI.CreateAI(pLoadedShip, ship["ailevel"],	ship["warp"]))
		else:
			pLoadedShip.SetAI(StarbaseNeutral2AI.CreateAI(pLoadedShip))
