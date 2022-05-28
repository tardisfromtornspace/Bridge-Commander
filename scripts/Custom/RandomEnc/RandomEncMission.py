from bcdebug import debug
import App
import loadspacehelper
import MissionLib

import Foundation

import Encounter

g_version = "1.0"

qbGameMode = None 

g_pEnemies = None
g_pFriendlies = None
g_pNeutrals = None

g_pDatabase = None
g_pMission = None

g_pKiska = None
g_pFelix = None
g_pSaffi = None
g_pMiguel = None
g_pBrex = None

g_sPlayerRace = ""

def PreLoadAssets(pMission):
	#loadspacehelper.PreloadShip("Galaxy", 1)
	debug(__name__ + ", PreLoadAssets")
	loadspacehelper.PreloadShip("FedStarbase", 1)
	
def Initialize(pMission):
	debug(__name__ + ", Initialize")
	global g_pEnemies
	g_pEnemies = MissionLib.GetEnemyGroup()
	global g_pFriendlies
	g_pFriendlies = MissionLib.GetFriendlyGroup()
	global g_pNeutrals
	g_pNeutrals = pMission.GetNeutralGroup()

	global g_pDatabase
	g_pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')

	global g_pMission
	g_pMission = pMission

	global qbGameMode 
	qbGameMode = Foundation.BuildGameMode()
	qbGameMode.Activate()
	
	initBridge()
	initRegions()
	initHelmMenu()
	initShips()
	initEvents()

def Terminate(pMission):
	debug(__name__ + ", Terminate")
	global qbGameMode
	qbGameMode.Deactivate()
	qbGameMode = None

	App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, g_pMission, __name__+".EnterSet")
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_DESTROYED, g_pMission, __name__ + ".ShipDestroyed")
	
	if (g_pDatabase != None):
		App.g_kLocalizationManager.Unload(g_pDatabase)

def initBridge():
	debug(__name__ + ", initBridge")
	import LoadBridge
	LoadBridge.Load("GalaxyBridge")

def initRegions():
	debug(__name__ + ", initRegions")
	pStarbaseSet = MissionLib.SetupSpaceSet("Systems.Starbase12.Starbase12")
	MissionLib.SetupSpaceSet("Systems.Riha.Riha1")
	MissionLib.SetupSpaceSet("Systems.Artrus.Artrus1")
	MissionLib.SetupSpaceSet("Systems.OmegaDraconis.OmegaDraconis1")

def initHelmMenu():
	debug(__name__ + ", initHelmMenu")
	import Systems.Starbase12.Starbase
	Systems.Starbase12.Starbase.CreateMenus()
	import Systems.Riha.Riha
	Systems.Riha.Riha.CreateMenus()
	import Systems.Artrus.Artrus
	Systems.Artrus.Artrus.CreateMenus()
	import Systems.OmegaDraconis.OmegaDraconis
	Systems.OmegaDraconis.OmegaDraconis.CreateMenus()
	
def initShips():
	debug(__name__ + ", initShips")
	pStarbaseSet = App.g_kSetManager.GetSet("Starbase12")
	
	global g_sPlayerRace
	g_sPlayerRace, playerShipName = Encounter.createRandomPlayerShip()
	pPlayer	= MissionLib.CreatePlayerShip(playerShipName, pStarbaseSet, "player", "Player Start")
	pStarbase = loadspacehelper.CreateShip("FedStarbase", pStarbaseSet, "Starbase 12", "Starbase12 Location")

	g_pFriendlies.AddName("player")
	g_pFriendlies.AddName("Starbase 12")
	
	fleet = Encounter.createPlayerFleet(g_sPlayerRace)
	n = 1
	for s in fleet:
		name = s+'(' + repr(n) + ')'
		pShip = loadspacehelper.CreateShip(s, pStarbaseSet, name, "")
		import ai.FollowAI
		pShip.SetAI(ai.FollowAI.CreateAI(pShip))
		g_pFriendlies.AddName(name)
		MissionLib.AddCommandableShip(name)
		PlaceShipRandomly(pShip)
		n = n+1
		
def initEvents():
	debug(__name__ + ", initEvents")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, g_pMission, __name__+".EnterSet")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_DESTROYED, g_pMission, __name__ + ".ShipDestroyed")

def EnterSet(pObject, pEvent):
	debug(__name__ + ", EnterSet")
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	
	if (pShip == None):
		return
	if (pShip.IsDead()):
		return
		
	pSet = pShip.GetContainingSet()
	lpEnemies = g_pEnemies.GetActiveObjectTuple()
	lpFriends = g_pFriendlies.GetActiveObjectTuple()
	
	if ((pShip.GetName() == "player") and (pSet.GetName() != "Starbase12") and ((pSet.GetName() != "warp")) and (len(lpEnemies) == 0)):
		fleet = Encounter.createEnemyFleet(g_sPlayerRace, g_pFriendlies.GetNumActiveObjects()-1)
		n = 1
		for s in fleet:
			name = s+'(' + repr(n) + ')'
			pShip = loadspacehelper.CreateShip(s, pSet, name, "")
			import ai.QuickBattleAI
			pShip.SetAI(ai.QuickBattleAI.CreateAI(pShip, 2, 1))
			g_pEnemies.AddName(name)
			PlaceShipRandomly(pShip)
			n = n+1
		
		for pObject in lpFriends:
			pShip = App.ShipClass_Cast(pObject)
			if ((pShip.GetWarpEngineSubsystem() != None) and (pShip.GetName() != "player")):
				import ai.FleetAI
				pShip.SetAI(ai.FleetAI.CreateAI(pShip))

	if (pObject):
		pObject.CallNextHandler(pEvent)
		
def ShipDestroyed(pObject, pEvent):
	debug(__name__ + ", ShipDestroyed")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()

	# Get the ship that was destroyed.
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip != None):
		if (pPlayer and pShip.GetName() == pPlayer.GetName()):
			pSequence = App.TGSequence_Create()
			pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeOut"))
			pSequence.AppendAction(App.TGScriptAction_Create(__name__, "ShutdownGame"))
			pSequence.Play()
			
	if (pObject):
		pObject.CallNextHandler(pEvent)

def ShutdownGame(pAction = None):
	debug(__name__ + ", ShutdownGame")
	return MissionLib.ExitGame(pAction, bDisplayRestart=0)

	pTop = App.TopWindow_GetTopWindow()
	if (pTop):
		pTop.AbortFade()

	App.Game_GetCurrentGame().Terminate()
	return 0

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
