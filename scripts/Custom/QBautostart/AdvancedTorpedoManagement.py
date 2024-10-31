from bcdebug import debug
import App
import MissionLib
import Lib.LibEngineering
#import Libs.LibEngineering
import Foundation
import string
import math
import loadspacehelper
import nt
import Lib.Ambiguity
TransferEnabled = 0
pPane = None
pInfoPane = None
pDetailsWindow = None
pTTPane = None
ammountbox = None
pPTPane = None
pSTPane = None
pInfoWindow = None
EnabledShips = []
pTargetShip = None
Storage = []
ammount = 5000
StarbaseStore = []
autogetenabled = 0
defaultscript = None
defaultslot = None
pwindowButton = None
pTrToggleButton = None
pDetailsWindowWin = None
pAutogetButton = None
ChanceFriendlyShipAllowBeam = 20
ET_TOGGLEAUTOGET = App.UtopiaModule_GetNextEventType()
ET_CLOSE = App.UtopiaModule_GetNextEventType()
ET_SCAN = App.UtopiaModule_GetNextEventType()
ET_NOTHING = App.UtopiaModule_GetNextEventType()
ET_INFO = App.UtopiaModule_GetNextEventType()
ET_TARGETINFO = App.UtopiaModule_GetNextEventType()
ET_GET = App.UtopiaModule_GetNextEventType()
ET_USE = App.UtopiaModule_GetNextEventType()
ET_TRANSFERTOGGLE = App.UtopiaModule_GetNextEventType()
paste = []
pDatabase = None
transporteractive = 0
pSound = App.TGSound_Create("sfx/Interface/new_game3.wav", "Beam_Sound", 0) # the Beam Sound
pSound.SetSFX(0)
pSound.SetInterface(1)
LastPlayerShip = None

def init():
        if not Lib.LibEngineering.CheckActiveMutator("Advanced Torpedo Management"):
                return
	firstcheck()
	start()
	myEvent = Lib.LibEngineering.GetEngineeringNextEventType()
	MissionLib.CreateTimer(myEvent, __name__ + ".TimerLoop", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
	
def Restart():
	debug(__name__ + ", Restart")
	global pwindowButton
	windowclose(None, None)
	TransferEnabled = 0
	Storage = []
	ammount = 5000
	autogetenabled = 0
	defaultscript = None
	defaultslot = None
	if pwindowButton:
		pwindowButton.SetDisabled()
	firstcheck()

def TimerLoop(pObject, pEvent):
	debug(__name__ + ", TimerLoop")
	global autogetenabled, pPane, pTargetShip, LastPlayerShip, Storage
	myEvent = Lib.LibEngineering.GetEngineeringNextEventType()
	MissionLib.CreateTimer(myEvent, __name__ + ".TimerLoop", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
	firstcheck()
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
		return
	pTargetShip = App.ShipClass_Cast(pPlayer.GetTarget())
	if pTargetShip:
		if autogetenabled == 1:
			if testgetabillity() == 1:
				autoget()
	if pPane:
		ScanTarget(None, None)
	if not LastPlayerShip == pPlayer.GetObjID():
		NewPlayerShip(pPlayer)
	LastPlayerShip = pPlayer.GetObjID()
	Torps = []
	Torps[len(Torps) : len(Torps)] = Storage
	pTorpedoSystem = pPlayer.GetTorpedoSystem()
	iNumTypes = pTorpedoSystem.GetNumAmmoTypes()
	pTorpedoType = pTorpedoSystem.GetAmmoType(iNumTypes -1)
	pTorpedoTypeName = pTorpedoType.GetAmmoName()
	pTorpedoTypeScript = pTorpedoType.GetTorpedoScript()
	pTorpedoTypeAvailable = pTorpedoSystem.GetNumAvailableTorpsToType(iNumTypes -1)
	if not pTorpedoTypeName == 'Stored Torpedoes' and pTorpedoTypeAvailable > 0 :
		if pTorpedoTypeScript in Torps:
			for i in range(len(Torps)):
				if Torps[i] == pTorpedoTypeScript:
					Torps[i + 2] = Torps[i + 2] + pTorpedoTypeAvailable
		else:
			Torps[len(Torps) : len(Torps)] = [pTorpedoTypeScript, pTorpedoTypeName, pTorpedoTypeAvailable]
	if not Torps == []:
		WriteShipSetup("player_" + string.split(pPlayer.GetScript(),".")[1], Torps)
	Torps = None

def NewPlayerShip(pPlayer=None):
	global Storage
	if not pPlayer:
		pPlayer = MissionLib.GetPlayer()
	Storage = LoadShipSetup("player_" + string.split(pPlayer.GetScript(),".")[1])
	Storage = Clean(Storage)

def testgetabillity():
	debug(__name__ + ", testgetabillity")
	global pTargetShip
	if not pTargetShip:
		return 0
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
		return
	if pPlayer.IsCloaked():
		Felixsay("cloaked")
		return 0
	if (Distance(pTargetShip) > 300 ):
		Felixsay("out_of_range")
		return 0

	if checkaffliction(pTargetShip) == 'friendly':
		RandomTypeNum = App.g_kSystemWrapper.GetRandomNumber(100)
		if RandomTypeNum <= ChanceFriendlyShipAllowBeam:
			return 1
		else:
			return 0
	else:
		tShields = pTargetShip.GetShields()
		Lowestshieldperc = 100
		if (tShields != None):
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				if tShields.GetMaxShields(ShieldDir) > 0:
					shield = (tShields.GetCurShields(ShieldDir) / tShields.GetMaxShields(ShieldDir)) * 100
				else: 
					shield = 0
				if shield < Lowestshieldperc:
					Lowestshieldperc = shield
		ms = int(11)
		if int(Lowestshieldperc) > ms and pTargetShip.GetShields().IsOn() == 1:
			Felixsay("no_offline_shield")
			return 0
		return 1

def checkaffliction(pTargetShip):
	debug(__name__ + ", checkaffliction")
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
	pFriendlies = pMission.GetFriendlyGroup()
        pEnemies = pMission.GetEnemyGroup()
        #pNeutrals = pMission.GetNeutralGroup()
        if pFriendlies.IsNameInGroup(pTargetShip.GetName()):
                return 'friendly'
        if pEnemies.IsNameInGroup(pTargetShip.GetName()):
                return 'enemy'
        #if pNeutrals.IsNameInGroup(pTargetShip.GetName()):
         #       return 'neutral'
        


def firstcheck():
	debug(__name__ + ", firstcheck")
	global defaultscript, defaultslot, pwindowButton, EnabledShips
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
		return
	pTorpedoSystem = pPlayer.GetTorpedoSystem()
	if not pTorpedoSystem:
		return	
	iNumTypes = pTorpedoSystem.GetNumAmmoTypes()
	if not iNumTypes:
		return
	pTorpedoType = pTorpedoSystem.GetAmmoType(iNumTypes -1)
	pTorpedoTypeName = pTorpedoType.GetAmmoName()
	pTorpedoTypeScript = pTorpedoType.GetTorpedoScript()
	pPlayerScript = pPlayer.GetScript()
	if pTorpedoTypeName == 'Stored Torpedoes':
		defaultscript = pTorpedoTypeScript
		defaultslot = iNumTypes - 1
		alreadyexists = 0
		if len(EnabledShips) > 0:
			for i in range(len(EnabledShips)):
				if EnabledShips[i] == pPlayerScript:
					alreadyexists = 1
		if alreadyexists == 0:
			EnabledShips[len(EnabledShips) : len(EnabledShips)] = [pPlayerScript]
		if pwindowButton:
			pwindowButton.SetEnabled()
	else:
		alreadyexists = 0
		if len(EnabledShips) > 0:
			for i in range(len(EnabledShips)):
				if EnabledShips[i] == pPlayerScript:
					alreadyexists = 1
		if alreadyexists == 0:
			if pwindowButton:
				pwindowButton.SetDisabled()
				windowbutton(None, 'close')
		else:
			if pwindowButton:
				pwindowButton.SetEnabled()
			
def start():
	debug(__name__ + ", start")
	global pwindowButton, pDatabase
        pPlayer = MissionLib.GetPlayer()
        pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
        pwindowButton = Lib.LibEngineering.CreateMenuButton("stored Torpedoes", "Tactical", __name__ + ".windowbutton", 0)
	firstcheck()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/TorpedoStore.tgl")

def Distance(pObject):
	debug(__name__ + ", Distance")
	pPlayer = App.Game_GetCurrentPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()

def Felixsay(SayString):
	debug(__name__ + ", Felixsay")
	global pDatabase
	pBridge = App.g_kSetManager.GetSet('bridge')
	g_pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
        pSequence = App.TGSequence_Create()
        pSequence.AppendAction(App.CharacterAction_Create(g_pFelix, App.CharacterAction.AT_SAY_LINE, SayString, None, 0, pDatabase))
        pSequence.Play()    

def windowbutton(pObject, pEvent):
	debug(__name__ + ", windowbutton")
	global pPane, pwindowButton
	if pEvent == 'close':
		windowclose(None, None)
		pwindowButton.SetName(App.TGString("stored Torpedoes"))
		return
	if pEvent == 'open':
		window(None, None)
		pwindowButton.SetName(App.TGString("close Window"))
		return
	if not pPane is None:
		windowclose(None, None)
		pwindowButton.SetName(App.TGString("stored Torpedoes"))
		return
	if pPane is None:
		window(None, None)
		pwindowButton.SetName(App.TGString("close Window"))

def window(pObject, pEvent):
	debug(__name__ + ", window")
	global pPane, pDetailsWindow, pDetailsWindowWin, autogetenabled, pAutogetButton, pTrToggleButton, TransferEnabled, ammount, ammountbox
	if pPane is None:
		pGame = App.Game_GetCurrentGame()
		pEpisode = pGame.GetCurrentEpisode()
		pMission = pEpisode.GetCurrentMission()
		pPane = App.TGPane_Create(2.0, 2.0) 
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		pTCW.AddChild(pPane, 0, 0) 
		pDetailsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Torpedo Inventory"), 0.0, 0.0, None, 1, 0.845, 0.8, App.g_kMainMenuBorderMainColor)
        	pPane.AddChild(pDetailsWindow, 0.155, 0)

		pDetailsWindowWin = App.STSubPane_Create(1.0, 2.0, 0)
		pDetailsWindowWin.Layout()
		pDetailsWindow.AddChild(pDetailsWindowWin)

		App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_TRANSFERTOGGLE, pMission, __name__ + ".TransferEnabledToggle")
		pEvent = App.TGStringEvent_Create()
	        pEvent.SetEventType(ET_TRANSFERTOGGLE)
        	pEvent.SetString("SovClose")
		if TransferEnabled == 1:
			pTrToggleButton = App.STRoundedButton_CreateW(App.TGString("Transfer-mode enabled"), pEvent, 0.16125, 0.034583)
		if TransferEnabled == 0:
			pTrToggleButton = App.STRoundedButton_CreateW(App.TGString("Use-Mode (standart)"), pEvent, 0.16125, 0.034583)
		pDetailsWindow.AddChild(pTrToggleButton, 0.330, 0.3)
		pEvent = None
		ammountbox = Lib.Ambiguity.createEditBox(pDetailsWindow, 0.330, 0.35, "Ammount", str(ammount), 0.10, 0.05, 256)
        	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SCAN, pMission, __name__ + ".ScanTarget")
		pEvent = App.TGStringEvent_Create()
	        pEvent.SetEventType(ET_SCAN)
        	pEvent.SetString("SovSCAN")
		pButton = App.STRoundedButton_CreateW(App.TGString("Scan Target"), pEvent, 0.13125, 0.034583)
		pDetailsWindow.AddChild(pButton, 0.345, 0.08)
		pEvent = None
        	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_NOTHING, pMission, __name__ + ".DoNothing")
		pEvent = App.TGStringEvent_Create()
	        pEvent.SetEventType(ET_NOTHING)
        	pEvent.SetString("NOTHING")
		pButton = App.STRoundedButton_CreateW(App.TGString("Targets Inventory"), pEvent, 0.325, 0.03)
		pDetailsWindow.AddChild(pButton, 0.48625, 0.13)
		pButton = App.STRoundedButton_CreateW(App.TGString("Your Inventory"), pEvent, 0.325, 0.03)
		pDetailsWindow.AddChild(pButton, 0.01, 0.13)
		pEvent = None
		App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_TOGGLEAUTOGET, pMission, __name__ + ".toggleautoget")
		pEvent = App.TGStringEvent_Create()
	        pEvent.SetEventType(ET_TOGGLEAUTOGET)
        	pEvent.SetString("SovClose")
		pAutogetButton = App.STRoundedButton_CreateW(App.TGString("Autoget : " + str(autogetenabled)), pEvent, 0.13125, 0.034583)
		pDetailsWindow.AddChild(pAutogetButton, 0.345, 0.03)
		pEvent = None
		ScanMe(None, None)
	ScanTarget(None, None)

def toggleautoget(pObject, pEvent):
	debug(__name__ + ", autoget")
	global autogetenabled
	if autogetenabled == 0:
		autogetenabled = 1
		pAutogetButton.SetName(App.TGString("Autoget : " + str(autogetenabled)))
		return
	if autogetenabled == 1:
		autogetenabled = 0
		pAutogetButton.SetName(App.TGString("Autoget : " + str(autogetenabled)))
		return

def autoget():
	debug(__name__ + ", autoget")
##########################################################################################################################
#Beta version: autoget sometimes crashes the game so i've disabled it for now:
#	return
##########################################################################################################################
	global pTargetShip
	try:
		pPlayer = MissionLib.GetPlayer()
		if not pPlayer:
	 		return
		pTargetShip = App.ShipClass_Cast(pPlayer.GetTarget())
		if not pTargetShip:
	 		return
		pTargetShip = App.ShipClass_GetObjectByID(None, pTargetShip.GetObjID())
		if not pTargetShip:
	 		return
		tTorpedoSystem = pTargetShip.GetTorpedoSystem()
		if (tTorpedoSystem):
 			iNumTypes = tTorpedoSystem.GetNumAmmoTypes()
 			for iType in range(iNumTypes):
				GetTorps(None, iType)
	except:
		return

def windowclose(pObject, pEvent):
	debug(__name__ + ", windowclose")
	global pPane
        if not pPane is None:
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		App.g_kFocusManager.RemoveAllObjectsUnder(pPane)
		pTCW.DeleteChild(pPane)
		pPane = None

def scanstarbase():
	debug(__name__ + ", scanstarbase")
	global pDetailsWindow, pTTPane, pDetailsWindow, StarbaseStore
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
		return
	pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
	if not pTarget:
	 	return
	pTarget = App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
	if not pTarget:
	 	return
	TargetName = pTarget.GetName()
	line = 1
	LoadSetup(TargetName)
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
        if not pTTPane is None:
            App.g_kFocusManager.RemoveAllObjectsUnder(pTTPane)
            pDetailsWindow.DeleteChild(pTTPane)
            pTTPane = None

	pTTPane = App.TGPane_Create(2.0, 2.0)
	pDetailsWindow.AddChild(pTTPane, 0, 0)

	#getting StarbaseStore
	items = len(StarbaseStore) / 3
	if items > 0:
		for i in range(items):
			pTorpedoTypeName = StarbaseStore[(i * 3) + 1]
			pTorpedoTypeScript = StarbaseStore[i * 3]
			pTorpedoTypeAvailable = int(StarbaseStore[(i * 3) + 2])
			text = pTorpedoTypeName
			text = text + " :  " + str(pTorpedoTypeAvailable)
			CreateStarbaseTorpButton(line, text)
			line = line + 1


def ScanTarget(pObject, pEvent):
	debug(__name__ + ", ScanTarget")
	global pDetailsWindow, pTTPane, pTargetShip
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
		return
	line = 1
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
        if not pTTPane is None:
            App.g_kFocusManager.RemoveAllObjectsUnder(pTTPane)
            pDetailsWindow.DeleteChild(pTTPane)
            pTTPane = None

	pTTPane = App.TGPane_Create(2.0, 2.0)
	pDetailsWindow.AddChild(pTTPane, 0, 0)

	#getting the Targets TorpedoSystem
	pTargetShip = App.ShipClass_Cast(pPlayer.GetTarget())
	if not pTargetShip:
 		return
	pTargetShip = App.ShipClass_GetObjectByID(None, pTargetShip.GetObjID())
	if not pTargetShip:
	 	return
	
	if pTargetShip.GetShipProperty().IsStationary() and checkaffliction(pTargetShip) == 'friendly':
		scanstarbase()
		return

	tTorpedoSystem = pTargetShip.GetTorpedoSystem()
	if (tTorpedoSystem):
 		iNumTypes = tTorpedoSystem.GetNumAmmoTypes()
 		for iType in range(iNumTypes):
			pTorpedoType = tTorpedoSystem.GetAmmoType(iType)
			pTorpedoTypeName = pTorpedoType.GetAmmoName()
			pTorpedoTypeScript = pTorpedoType.GetTorpedoScript()
			pTorpedoTypeAvailable = tTorpedoSystem.GetNumAvailableTorpsToType(iType)
			pTorpedoTypeMaxAvailable = pTorpedoType.GetMaxTorpedoes()
			text = pTorpedoTypeName
			text = text + " :  " + str(pTorpedoTypeAvailable) + "/" + str(pTorpedoTypeMaxAvailable)
			CreateTargetTorpButton(line, text)
			line = line + 1


def CreateTargetTorpButton(line, text):
	debug(__name__ + ", CreateTargetTorpButton")

	global pPane, pDetailsWindow, pTTPane

	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	ET_TARGETINFO = App.UtopiaModule_GetNextEventType()
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_TARGETINFO, pMission, __name__ + ".GetTorps")
	pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_TARGETINFO)
       	pEvent.SetInt(line - 1)
	pButton = App.STRoundedButton_CreateW(App.TGString(text), pEvent, 0.3, 0.03)
	ypos = line * 0.05
	ypos = ypos + 0.13
	pTTPane.AddChild(pButton, 0.5, ypos)
	pEvent = None


def CreateStarbaseTorpButton(line, text):
	debug(__name__ + ", CreateTargetTorpButton")

	global pPane, pDetailsWindow, pTTPane
	
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	ET_TARGETINFO = App.UtopiaModule_GetNextEventType()
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_TARGETINFO, pMission, __name__ + ".GetStarbaseTorps")
	pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_TARGETINFO)
       	pEvent.SetInt(line - 1)
	pButton = App.STRoundedButton_CreateW(App.TGString(text), pEvent, 0.3, 0.03)
	ypos = line * 0.05
	ypos = ypos + 0.13
	pTTPane.AddChild(pButton, 0.5, ypos)
	pEvent = None


def CreatePlayerTorpButton(line, text):
	debug(__name__ + ", CreatePlayerTorpButton")

	global pPane, pDetailsWindow, pPTPane

	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	ET_INFO = App.UtopiaModule_GetNextEventType()
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_INFO, pMission, __name__ + ".DoNothing")
	pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_INFO)
       	pEvent.SetInt(line - 1)
	pButton = App.STRoundedButton_CreateW(App.TGString(text), pEvent, 0.3, 0.03)
	ypos = line * 0.05
	ypos = ypos + 0.13
	pPTPane.AddChild(pButton, 0.02375, ypos)
	pEvent = None

def CreateStorageTorpButton(line, slot, text):
	debug(__name__ + ", CreateStorageTorpButton")

	global pPane, pDetailsWindow, pSTPane
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	ET_INFO = App.UtopiaModule_GetNextEventType()
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_INFO, pMission, __name__ + ".UseTorps")
	pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_INFO)
       	pEvent.SetInt(slot)
	pButton = App.STRoundedButton_CreateW(App.TGString(text), pEvent, 0.3, 0.03)
	ypos = line * 0.05
	ypos = ypos + 0.13 + 0.25
	pPTPane.AddChild(pButton, 0.02375, ypos)
	pEvent = None


def ScanMe(pObject, pEvent):
	debug(__name__ + ", ScanMe")
	global pDetailsWindow, pPTPane
	pPlayer = MissionLib.GetPlayer()
	line = 1
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
        if not pPTPane is None:
            App.g_kFocusManager.RemoveAllObjectsUnder(pPTPane)
            pDetailsWindow.DeleteChild(pPTPane)
            pPTPane = None

	pPTPane = App.TGPane_Create(2.0, 2.0)
	pDetailsWindow.AddChild(pPTPane, 0, 0)

	if pPlayer:
		#getting My TorpedoSystem
		pTorpedoSystem = pPlayer.GetTorpedoSystem()
		if (pTorpedoSystem):
 			iNumTypes = pTorpedoSystem.GetNumAmmoTypes()
 			for iType in range(iNumTypes):
				pTorpedoType = pTorpedoSystem.GetAmmoType(iType)
				pTorpedoTypeName = pTorpedoType.GetAmmoName()
				pTorpedoTypeScript = pTorpedoType.GetTorpedoScript()
				pTorpedoTypeAvailable = pTorpedoSystem.GetNumAvailableTorpsToType(iType)
				pTorpedoTypeMaxAvailable = pTorpedoType.GetMaxTorpedoes()
				text = pTorpedoTypeName
				text = text + " :  " + str(pTorpedoTypeAvailable) + "/" + str(pTorpedoTypeMaxAvailable)
				CreatePlayerTorpButton(line, text)
				line = line + 1
	ScanStore()

def GetStarbaseTorps(pObject, pEvent):
	debug(__name__ + ", GetStarbaseTorps")
	global ammountbox, pTargetShip, Storage, StarbaseStore
	getcount = 0
	if not pTargetShip:
 		return
	pTargetShip = App.ShipClass_GetObjectByID(None, pTargetShip.GetObjID())
	if not pTargetShip:
	 	return
	if (Distance(pTargetShip) > 300):
		return

	slot = pEvent.GetInt()
	pTorpedoTypeScript = StarbaseStore[slot * 3]
	pTorpedoTypeAvailable = int(StarbaseStore[(slot * 3) + 2])
	ammount = int(ammountbox.GetCString())
	if pTorpedoTypeAvailable > 0:
		if ammount < pTorpedoTypeAvailable:
			getcount = ammount
		else:
			getcount = pTorpedoTypeAvailable
		StarbaseStore[(slot * 3) + 2] = int(StarbaseStore[(slot * 3) + 2]) - getcount
		pTorpedoTypeName = StarbaseStore[(slot * 3) + 1]
		pTorpedoTypeScript = StarbaseStore[(slot * 3)]
		
		items = len(Storage) / 3
		Torp = [pTorpedoTypeScript, pTorpedoTypeName, getcount]
		if items > 0:
			for i in range(items):
				if Storage[i * 3] == Torp[0]:
					if Storage[(i * 3) + 1] == Torp[1]:
						Storage[(i * 3) + 2] = Storage[(i * 3) + 2] + Torp[2]
						ScanTarget(None, None)
						ScanMe(None, None)
						WriteSetup(pTargetShip.GetName())
						return
		Storage[len(Storage) : len(Storage)] = Torp
		WriteSetup(pTargetShip.GetName())
	ScanTarget(None, None)
	ScanMe(None, None)
	return

def GetTorps(pObject, pEvent):
	debug(__name__ + ", GetTorps")
	global ammountbox, pTargetShip, Storage, pPane, paste, transporteractive
	if transporteractive == 1:
		return
	ammount = int(ammountbox.GetCString())
	getcount = 0
	if not pTargetShip:
 		return
	pTargetShip = App.ShipClass_GetObjectByID(None, pTargetShip.GetObjID())
	if not pTargetShip:
	 	return
	if testgetabillity() == 0:
		return
	try:
		slot = int(pEvent)
	except:
		slot = pEvent.GetInt()
	paste = [slot]
	myEvent = Lib.LibEngineering.GetEngineeringNextEventType()
	MissionLib.CreateTimer(myEvent, __name__ + ".GetTorpsEV", App.g_kUtopiaModule.GetGameTime() + 1.5, 0, 0)
	transporteractive = 1
	App.g_kSoundManager.PlaySound("Beam_Sound")
#	GetTorpsEV(pObject, pEvent)


def GetTorpsEV(pObject, pEvent):
	debug(__name__ + ", GetTorpsEV")
	global ammountbox, pTargetShip, Storage, pPane, paste, transporteractive
	transporteractive = 0
	ammount = int(ammountbox.GetCString())
	getcount = 0
	if not pTargetShip:
 		return
	pTargetShip = App.ShipClass_GetObjectByID(None, pTargetShip.GetObjID())
	if not pTargetShip:
	 	return
	testgetabillityresult = testgetabillity()
	if testgetabillityresult == 0:
		return
	tTorpedoSystem = pTargetShip.GetTorpedoSystem()
	slot = paste[0]
	pTorpedoTypeAvailable = tTorpedoSystem.GetNumAvailableTorpsToType(slot)
	if pTorpedoTypeAvailable > 0:
		if ammount < pTorpedoTypeAvailable:
			getcount = ammount
		else:
			getcount = pTorpedoTypeAvailable
		tTorpedoSystem.LoadAmmoType(slot, - getcount)
		pTorpedoType = tTorpedoSystem.GetAmmoType(slot)
		pTorpedoTypeName = pTorpedoType.GetAmmoName()
		pTorpedoTypeScript = pTorpedoType.GetTorpedoScript()
	
		items = len(Storage) / 3
		Torp = [pTorpedoTypeScript, pTorpedoTypeName, getcount]
		if items > 0:
			for i in range(items):
				if Storage[i * 3] == Torp[0]:
					if Storage[(i * 3) + 1] == Torp[1]:
						Storage[(i * 3) + 2] = Storage[(i * 3) + 2] + Torp[2]
						ScanTarget(None, None)
						ScanMe(None, None)
						return
		Storage[len(Storage) : len(Storage)] = Torp
	if pPane:
		ScanTarget(None, None)
		ScanMe(None, None)
	return



def GetTorpName(pScript):
	debug(__name__ + ", GetTorpName")
	s = __import__(pScript)
	if(s):
		if(hasattr(s, "GetName")):
			return str(s.GetName())
	return str("Do not fire!")

def TransferEnabledToggle(pObject, pEvent):
	debug(__name__ + ", DoNothing")
	global TransferEnabled, pTrToggleButton
	if TransferEnabled == 0:
		TransferEnabled = 1
		pTrToggleButton.SetName(App.TGString("Transfer-mode enabled"))
		return
	if TransferEnabled == 1:
		TransferEnabled = 0
		pTrToggleButton.SetName(App.TGString("Use-Mode (standart)"))
		return

def Transfer(slot):
	debug(__name__ + ", Transfer")
	global ammountbox, pTargetShip, Storage, StarbaseStore
	ammount = int(ammountbox.GetCString())
	getcount = 0
	if not pTargetShip:
 		return
	pTargetShip = App.ShipClass_GetObjectByID(None, pTargetShip.GetObjID())
	if not pTargetShip:
	 	return
	if (Distance(pTargetShip) > 300):
		return

	pTorpedoTypeScript = Storage[slot * 3]
	pTorpedoTypeAvailable = int(Storage[(slot * 3) + 2])
	if ammount < pTorpedoTypeAvailable:
		getcount = ammount
	else:
		getcount = pTorpedoTypeAvailable
	Storage[(slot * 3) + 2] = int(Storage[(slot * 3) + 2]) - getcount
	pTorpedoTypeName = Storage[(slot * 3) + 1]
	pTorpedoTypeScript = Storage[(slot * 3)]
	
	items = len(StarbaseStore) / 3
	Torp = [pTorpedoTypeScript, pTorpedoTypeName, getcount]
	if items > 0:
		for i in range(items):
			if StarbaseStore[i * 3] == Torp[0]:
				if StarbaseStore[(i * 3) + 1] == Torp[1]:
					StarbaseStore[(i * 3) + 2] = StarbaseStore[(i * 3) + 2] + Torp[2]
					ScanTarget(None, None)
					ScanMe(None, None)
					WriteSetup(pTargetShip.GetName())
					return
	StarbaseStore[len(StarbaseStore) : len(StarbaseStore)] = Torp
	WriteSetup(pTargetShip.GetName())
	ScanTarget(None, None)
	ScanMe(None, None)
	return



def UseTorps(pObject, pEvent):
	debug(__name__ + ", UseTorps")
	global pDetailsWindow, pInfoPane, Storage, defaultslot, pTargetShip, TransferEnabled
        #if not pInfoPane is None:
        #    App.g_kFocusManager.RemoveAllObjectsUnder(pInfoPane)
        #    pDetailsWindow.DeleteChild(pInfoPane)
        #    pInfoPane = None
	slot = pEvent.GetInt()
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
	 	return
	if pTargetShip:
		pTargetShip = App.ShipClass_GetObjectByID(None, pTargetShip.GetObjID())
		if pTargetShip and pTargetShip.GetShipProperty().IsStationary():
			if TransferEnabled == 1:
				Transfer(slot)				
				return
	pTorpedoSystem = pPlayer.GetTorpedoSystem()
	pTorpedoType = pTorpedoSystem.GetAmmoType(defaultslot)
	avail = pTorpedoSystem.GetNumAvailableTorpsToType(defaultslot)
	added = 0
	if avail > 0:
		items = len(Storage) / 3
		for i in range(items):
			if Storage[i * 3] == pTorpedoType.GetTorpedoScript() and added == 0:
				Storage[(i * 3) + 2] = Storage[(i * 3) + 2] + avail
				added = 1

	if added == 0:
		pTorpedoTypeName = pTorpedoType.GetAmmoName()
		pTorpedoTypeScript = pTorpedoType.GetTorpedoScript()
		Storage[len(Storage) : len(Storage)] = [pTorpedoTypeScript, pTorpedoTypeName, avail]

	pTorpedoTypeScript = Storage[slot * 3]
	pTorpedoTypeAvailable = Storage[(slot * 3) + 2]
	Storage[(slot * 3) + 2] = 0
	hugo = pTorpedoType.SetTorpedoScript(pTorpedoTypeScript)
	hansi = pTorpedoType.SetMaxTorpedoes(int(pTorpedoTypeAvailable))
	pTorpedoSystem.LoadAmmoType(defaultslot, int(pTorpedoTypeAvailable))
	pPlayer = App.Game_GetCurrentPlayer()
	pTorp = pPlayer.GetTorpedoSystem()
	pTacWindow = App.TacWeaponsCtrl_GetTacWeaponsCtrl()
	pTorpTypeToggle = pTacWindow.GetTorpTypeToggle()
	pName = GetTorpName(pTorp.GetAmmoType(defaultslot).GetTorpedoScript())
	pTorpTypeToggle.SetName(App.TGString("Type: " + pName))
	pTorp.SetAmmoType(defaultslot)
	windowbutton(None, None)
	#ScanMe(None, None)

def Clean(Store):
	Torp = []
	Torps = []
	Done = []
	items = len(Store) / 3
	if items > 0:
		for i in range(items):
			pTorpedoTypeName = Store[(i * 3) + 1]
			pTorpedoTypeScript = Store[i * 3]
			pTorpedoTypeAvailable = int(Store[(i * 3) + 2])
			pPlayer = MissionLib.GetPlayer()
			if pPlayer:
				currscr = pPlayer.GetTorpedoSystem().GetAmmoType(pPlayer.GetTorpedoSystem().GetNumAmmoTypes()-1).GetTorpedoScript()
				if pTorpedoTypeAvailable > 0:
					if not pTorpedoTypeScript in Done:
						if not pTorpedoTypeScript == currscr:
							Torp = [pTorpedoTypeScript, pTorpedoTypeName, pTorpedoTypeAvailable]
							Torps[len(Torps) : len(Torps)] = Torp
							Done[len(Done) : len(Done)] = [pTorpedoTypeScript]
	
	Done = None
	Torp = None
	return Torps


def DoNothing(pObject, pEvent):
	debug(__name__ + ", DoNothing")
	global pDetailsWindow, pInfoPane

def ScanStore():
	debug(__name__ + ", ScanStore")
	global pDetailsWindow, pSTPane, pDetailsWindowWin
	#pPlayer = MissionLib.GetPlayer()
	line = 1
	slot = 0

	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
        if not pSTPane is None:
            App.g_kFocusManager.RemoveAllObjectsUnder(pSTPane)
            pDetailsWindowWin.DeleteChild(pSTPane)
            pSTPane = None

	pSTPane = App.TGPane_Create(2.0, 2.0)
	pDetailsWindowWin.AddChild(pSTPane, 0, 0)

	#getting Storage
	items = len(Storage) / 3
	if items > 0:
		for i in range(items):
			pTorpedoTypeName = Storage[(i * 3) + 1]
			pTorpedoTypeScript = Storage[i * 3]
			pTorpedoTypeAvailable = int(Storage[(i * 3) + 2])
			if pTorpedoTypeAvailable > 0:
				text = pTorpedoTypeName
				text = text + " :  " + str(pTorpedoTypeAvailable)
				CreateStorageTorpButton(line, slot, text)
				line = line + 1
			slot = slot + 1

#################################################LOAD & SAVE################################################

def LoadSetup(sModule):
	try:
		pModule = __import__('Custom.test.'+sModule)
	except ImportError:
		return
	
	global StarbaseStore
	StarbaseStore		=  pModule.StarbaseStore	
	
def LoadShipSetup(sModule):
	try:
		pModule = __import__('Custom.test.'+sModule)
	except ImportError:
		return []
	
	return pModule.Store	

def WriteSetup(filename):
	debug(__name__ + ", WriteSetup")
	global StarbaseStore
	Torp = []
	Torps = []
	items = len(StarbaseStore) / 3
	if items > 0:
		for i in range(items):
			pTorpedoTypeName = StarbaseStore[(i * 3) + 1]
			pTorpedoTypeScript = StarbaseStore[i * 3]
			pTorpedoTypeAvailable = int(StarbaseStore[(i * 3) + 2])
			if pTorpedoTypeAvailable > 0:
				Torp = [pTorpedoTypeScript, pTorpedoTypeName, pTorpedoTypeAvailable]
				Torps[len(Torps) : len(Torps)] = Torp
	
	StarbaseStore = Torps
	try: 
		nt.remove("scripts\\Custom\\test\\" + filename + ".py")
	except OSError:
		pass
		
	try:
		file = nt.open('scripts\\Custom\\test\\' + filename + '.py', nt.O_CREAT | nt.O_RDWR)
		nt.write(file, 'StarbaseStore = ')
		nt.write(file, repr(Torps))
		nt.close(file)
		
	except:
		return 0
		
	return -1

def WriteShipSetup(filename, Store):
	debug(__name__ + ", WriteSetup")
	Torp = []
	Torps = []
	items = len(Store) / 3
	if items > 0:
		for i in range(items):
			pTorpedoTypeName = Store[(i * 3) + 1]
			pTorpedoTypeScript = Store[i * 3]
			pTorpedoTypeAvailable = int(Store[(i * 3) + 2])
			if pTorpedoTypeAvailable > 0:
				Torp = [pTorpedoTypeScript, pTorpedoTypeName, pTorpedoTypeAvailable]
				Torps[len(Torps) : len(Torps)] = Torp
	
	try: 
		nt.remove("scripts\\Custom\\test\\" + filename + ".py")
	except OSError:
		pass
		
	try:
		file = nt.open('scripts\\Custom\\test\\' + filename + '.py', nt.O_CREAT | nt.O_RDWR)
		nt.write(file, 'Store = ')
		nt.write(file, repr(Torps))
		nt.close(file)
		
	except:
		return 0
		
	return -1

