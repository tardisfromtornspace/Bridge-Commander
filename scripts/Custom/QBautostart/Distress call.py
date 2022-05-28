from bcdebug import debug
# 'Distress call.py' by Defiant
# erik@defiant.homedns.org


import App
import MissionLib
import Libs.LibEngineering
import Foundation
import string
import math
from Custom.QBautostart.Libs.Races import Races
import loadspacehelper


MODINFO = { "Author": "\"Defiant\" erik@defiant.homedns.org",
            "Download": "http://defiant.homedns.org/~erik/STBC/Distress/",
            "Version": "0.4",
            "License": "GPL",
            "Description": "Send out an distress call.",
            "needBridge": 0
            }

MAX_NUM_SHIPS = 20
min_time = 30
max_time = 270
incoming_mult = 4
dict_Timer = {}
dict_Notify = {}
ShipInd = 1
ET_ADD = None
ET_NOTIFY = None
pButton = None
i_Ship = 0

def GetShipType(pShip):
	# thanks to mldaalder for the idea of using -1 instead of 1
        debug(__name__ + ", GetShipType")
        return string.split(pShip.GetScript(), '.')[-1]


def GetFreeName(Name):
        debug(__name__ + ", GetFreeName")
        global i_Ship
	while(MissionLib.GetShip(Name + str(i_Ship))):
		i_Ship = i_Ship + 1
	return Name + str(i_Ship)
	

# Species of the Ship
def GetShipSpecies(pShip):
	debug(__name__ + ", GetShipSpecies")
	ShipType = GetShipType(pShip)
        if not ShipType:
		return
	if not hasattr(Foundation.shipList, 'has_key'):
		print("Error, bad Foundation!")
                print("Try to update your Shuttle Launching Framework!")
		return
        if not Foundation.shipList.has_key(ShipType):
		print("Cannot get Race for ", ShipType, " - No Foundation entry!")
		return
        FdtnShip = Foundation.shipList[ShipType]
        if not FdtnShip:
		return
        if FdtnShip.GetRace():
                RaceName = FdtnShip.GetRace().name
        else:
                RaceName = None
	
	return RaceName


def IsGodShip(ShipType):
	debug(__name__ + ", IsGodShip")
	return Races["GodShips"].IsOurRace(ShipType)


def IsGodRace(myRace):
	debug(__name__ + ", IsGodRace")
	if (myRace == "Borg"):
                return 1
	if (myRace == "8472"):
                return 1
        return 0
        

def getMVAMShip(ShipType):
        debug(__name__ + ", getMVAMShip")
        if ShipType in ["MvamGalaxySaucer", "MvamGalaxyStardrive"]:
                return "MvamGalaxy"
        elif ShipType in ["MvamPrometheusSaucer", "MvamPrometheusDorsal", "MvamPrometheusVentral"]:
                return "MvamPrometheus"
        return None


# Finally adds a ship
def AddShip(pObject, pEvent):
	debug(__name__ + ", AddShip")
	global dict_Timer

	if not dict_Timer.has_key(str(pEvent)):
		return

	pPlayer		= MissionLib.GetPlayer()
	pEnemies	= MissionLib.GetEnemyGroup()
	pFriendlies	= MissionLib.GetFriendlyGroup()
	shipType	= dict_Timer[str(pEvent)][0]
	shipName	= dict_Timer[str(pEvent)][1]
	Position	= dict_Timer[str(pEvent)][2]
        pSet            = dict_Timer[str(pEvent)][3]
	
	if not pSet:
		return
	
	pShip = loadspacehelper.CreateShip(shipType, pSet, shipName, "", 1)
	if not pShip:
		print "Distress call: Update to create", shipType
		return
	pShip.UpdateNodeOnly()
	CreateAIPosition(pShip, pSet)

	FdtnShips = Foundation.shipList
        ship = FdtnShips[shipType]
	
	if (Position == "friendly"):
		pFriendlies.AddName(pShip.GetName())
		
		FdtnAI = ship.StrFriendlyAI()
		if FdtnAI == "QuickBattleFriendlyAI":
			pShip.SetAI(Libs.LibEngineering.CreateFriendlyAI(pShip))
		else:
			pAIModule = __import__("QuickBattle." + FdtnAI)
			pShip.SetAI(pAIModule.CreateAI(pShip))
	elif (Position == "enemy"):
		pEnemies.AddName(pShip.GetName())
		
		FdtnAI = ship.StrEnemyAI()
		if FdtnAI == "QuickBattleAI":
			pShip.SetAI(Libs.LibEngineering.CreateEnemyAI(pShip))
		else:
			pAIModule = __import__("QuickBattle." + FdtnAI)
			pShip.SetAI(pAIModule.CreateAI(pShip))
	
	del dict_Timer[str(pEvent)]


# Starts the Timer to add ships
def AddShipTimer(ShipRace, ToAdd, pSet = None):
	debug(__name__ + ", AddShipTimer")
	global dict_Timer, ShipInd, ET_ADD, ET_NOTIFY, dict_Notify, min_time, max_time, incoming_mult

	NotifyTime = 0
	AddShipRace = None
        EscortShips = None
	pPlayer = MissionLib.GetPlayer()
	
	if pPlayer and not pSet:
		pSet = pPlayer.GetContainingSet()

	# ok, thats what we have to do here:
	# 1. Get our enemys and friendlys
	if not Races.has_key(ShipRace):
		print("Error: No race info for", ShipRace)
		return
	
	# 2. Find out what to do:
	if (ToAdd == "friendly"):
		# Get a random shiptype:
		if (len(Races[ShipRace].GetShips()) == 0):
			print("Error: No Ships for Race", ShipRace)
			return
		RandTypeNum = App.g_kSystemWrapper.GetRandomNumber(len(Races[ShipRace].GetShips()))
		ShipType = Races[ShipRace].GetShips()[RandTypeNum]
		if getMVAMShip(ShipType):
			ShipType = getMVAMShip(ShipType)
		if IsGodShip(ShipType):
			return
		Position = "friendly"
		RealShipName = Races[ShipRace].GetRandomName()
		if not RealShipName:
			RealShipName = GetFreeName(ShipType)
		NotifyTime = 1
		AddShipRace = Races[ShipRace]
	elif (ToAdd == "friendlyRace"):
		# Get a random friendly ShipRace
		if (len(Races[ShipRace].GetFriendlys()) == 0):
			print("ERROR: No friendly Race for", ShipRace)
			return
		RandRaceNum = App.g_kSystemWrapper.GetRandomNumber(len(Races[ShipRace].GetFriendlys()))
		friendRace = Races[ShipRace].GetFriendlys()[RandRaceNum]
		if not Races.has_key(friendRace):
			print("Error: No race info for", friendRace)
			return
		if (len(Races[friendRace].GetShips()) == 0):
			print("Error: No Ships for Race", friendRace)
			return
		RandTypeNum = App.g_kSystemWrapper.GetRandomNumber(len(Races[friendRace].GetShips()))
		ShipType = Races[friendRace].GetShips()[RandTypeNum]
		if getMVAMShip(ShipType):
			ShipType = getMVAMShip(ShipType)
		if IsGodShip(ShipType) or IsGodRace(friendRace):
			return
		Position = "friendly"
		RealShipName = Races[friendRace].GetRandomName()
		if not RealShipName:
			RealShipName = GetFreeName(ShipType)
		NotifyTime = 1
		AddShipRace = Races[friendRace]
	elif (ToAdd == "enemy"):
		# Get a random enemy ShipRace
		if (len(Races[ShipRace].GetEnemys()) == 0):
			print("ERROR: No enemy Race for", ShipRace)
			return
		RandRaceNum = App.g_kSystemWrapper.GetRandomNumber(len(Races[ShipRace].GetEnemys()))
		enemyRace = Races[ShipRace].GetEnemys()[RandRaceNum]
		if not Races.has_key(enemyRace):
			print("Error: No race info for", enemyRace)
			return
		if (len(Races[enemyRace].GetShips()) == 0):
			print("Error: No Ships for Race", enemyRace)
			return
		RandTypeNum = App.g_kSystemWrapper.GetRandomNumber(len(Races[enemyRace].GetShips()))
		ShipType = Races[enemyRace].GetShips()[RandTypeNum]
		if getMVAMShip(ShipType):
			ShipType = getMVAMShip(ShipType)
		if IsGodShip(ShipType) or IsGodRace(enemyRace):
			return
		Position = "enemy"
		RealShipName = Races[enemyRace].GetRandomName()
		if not RealShipName:
			RealShipName = GetFreeName(ShipType)
		AddShipRace = Races[enemyRace]
	elif (ToAdd == "ferengi"):
		ShipType = "Marauder"
		Position = "neutral"
		RealShipName = "Ferengi"
	else:
		print("Error: Nothing todo")
		return

	# Preload
        try:
        	loadspacehelper.PreloadShip(ShipType, 1)
        except:
                print("Error: Cannot preload", ShipType)
                return

	ShipName = RealShipName + "-" + str(ShipInd)
	ShipInd = ShipInd + 1
	
	# Create an event - it's a thing that will call this function
	pTimerEvent = App.TGEvent_Create()
	pTimerEvent.SetEventType(ET_ADD)
	pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())

	# Add in 30 seconds up to 5 minutes
	RealAddTime = 0
	if max_time > 0:
		RealAddTime = App.g_kSystemWrapper.GetRandomNumber(max_time) + min_time
	AddTime = App.g_kUtopiaModule.GetGameTime() + RealAddTime
	
	# Create a timer - it's a thing that will wait for a given time,then do something
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(AddTime)
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pTimerEvent)
	App.g_kTimerManager.AddTimer(pTimer)

	print("Get: ", ShipType, ShipName, "as", Position, "in", RealAddTime)
	# or any other Idea how to get Informations together with a Timer?
	dict_Timer[str(pTimerEvent)] = ShipType, ShipName, Position, pSet
        
	# does this ship get an escort?
        if AddShipRace:
                EscortShips = AddShipRace.GetEscort(ShipType)
        if EscortShips:
                for EscortShip in EscortShips:
		        EscortName = AddShipRace.GetRandomName()
		        if not EscortName:
			        EscortName = GetFreeName(EscortShip)
                        # Preload
                        try:
        	                loadspacehelper.PreloadShip(ShipType, 1)
                        except:
                                print("Error: Cannot preload", ShipType)
                        return
                        # Create an event - it's a thing that will call this function
	                pTimerEvent = App.TGEvent_Create()
	                pTimerEvent.SetEventType(ET_ADD)
	                pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())
                        # Create a timer - it's a thing that will wait for a given time,then do something
	                pTimer = App.TGTimer_Create()
	                pTimer.SetTimerStart(AddTime)
	                pTimer.SetDelay(0)
                        pTimer.SetDuration(0)
	                pTimer.SetEvent(pTimerEvent)
	                App.g_kTimerManager.AddTimer(pTimer)
		        dict_Timer[str(pTimerEvent)] = EscortShip, EscortName, Position, pSet

	# if we add a friendly, we also Notify the Player
	if (NotifyTime == 1):
		RealNotifyTime = 0
		if incoming_mult > 0:
			RealNotifyTime = RealAddTime / (App.g_kSystemWrapper.GetRandomNumber(incoming_mult) + 2)
		NotifyTime = App.g_kUtopiaModule.GetGameTime() + RealNotifyTime
		
		pTimer2Event = App.TGEvent_Create()
		pTimer2Event.SetEventType(ET_NOTIFY)
		pTimer2Event.SetDestination(App.TopWindow_GetTopWindow())
		pTimer2 = App.TGTimer_Create()
		pTimer2.SetTimerStart(NotifyTime)
		pTimer2.SetDelay(0)
		pTimer2.SetDuration(0)
		pTimer2.SetEvent(pTimer2Event)
		App.g_kTimerManager.AddTimer(pTimer2)

		# variant the arrive time about +/-10 seconds
		varTime = math.pow(-1, App.g_kSystemWrapper.GetRandomNumber(3)) * App.g_kSystemWrapper.GetRandomNumber(10)
		approxTime = RealAddTime - RealNotifyTime + varTime
		dict_Notify[str(pTimer2Event)] = RealShipName, approxTime


def reacButton(pObject, pEvent):
        debug(__name__ + ", reacButton")
        global pButton
        
        if not pButton:
                pMenu = Libs.LibEngineering.GetBridgeMenu("Helm")
                pButton = Libs.LibEngineering.GetButton("Send distress call", pMenu)
	if pButton:
        	pButton.SetEnabled()


# Print Help arriving in...seconds
def NotifyHelp(pObject, pEvent):
	debug(__name__ + ", NotifyHelp")
	global dict_Notify
	
	if not dict_Notify.has_key(str(pEvent)):
		return
	
	shipName = dict_Notify[str(pEvent)][0]
	approxTime = dict_Notify[str(pEvent)][1]
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Distress call.tgl")

	pcETA = pDatabase.GetString("ETA").GetCString()
	pcString = pcETA % (shipName, str(approxTime))

        # from Multiplayer
        pSequence = App.TGSequence_Create()
        pSubtitleAction = App.SubtitleAction_CreateC(pcString)
        pSubtitleAction.SetDuration(5.0)
        pSequence.AddAction(pSubtitleAction)
        pSequence.Play()
        App.STMissionLog_GetMissionLog().AddLine(App.TGString(pcString))


def SendCall(pObject, pEvent):
        debug(__name__ + ", SendCall")
        global pButton
	pPlayer		= MissionLib.GetPlayer()
	
	if not pPlayer:
		return
	
	pEnemyGroup     = MissionLib.GetEnemyGroup()
	pSet		= pPlayer.GetContainingSet()
	lpEnemys        = pEnemyGroup.GetActiveObjectTupleInSet(pSet)
        pDatabase       = App.g_kLocalizationManager.Load("data/TGL/Distress call.tgl")
        pBridge         = App.g_kSetManager.GetSet("bridge")
        g_pKiska        = App.CharacterClass_GetObject(pBridge, "Helm")
	countEnemy	= 0
	ferengidone	= 0

	# Count enemy Ships in System.
	for pEnemy in lpEnemys:
		# If it is a god Ship or a Base, add 5 points
		ShipType = GetShipType(pEnemy)
		if IsGodShip(ShipType) or pEnemy.GetShipProperty().IsStationary():
			countEnemy = countEnemy + 5
		else:
			countEnemy = countEnemy + 1
	# GetRandomNumber() will crash if used with 0. Make sure it is at least 1:
	if countEnemy == 0:
		countEnemy = 1

	PlayerSpecies = GetShipSpecies(pPlayer)
        if not PlayerSpecies:
                return

	# Chances:
	# Get amount of Ships:
	ShipCount = App.g_kSystemWrapper.GetRandomNumber(countEnemy * (App.g_kSystemWrapper.GetRandomNumber(3) + 1))
	# If we are a Station then we can also expect more help
	if pPlayer.GetShipProperty().IsStationary():
		ShipCount = ShipCount + App.g_kSystemWrapper.GetRandomNumber(5)
	
	if ShipCount > MAX_NUM_SHIPS:
		ShipCount = MAX_NUM_SHIPS
	
	# if ShipCount == 0 --> no ships coming
	for i in range(ShipCount):
		Chance = App.g_kSystemWrapper.GetRandomNumber(100) + 1
		# 1. Help from Same Race = 60%
		# 2. Help from friendly Race = 45%
		# 3. More enemy coming = 15%
		# 4. Ferengi just watching the fight, wants to get your hulk: 5%
		if (Chance <= 65):
			AddShipTimer(PlayerSpecies, "friendly", pSet)
		if (Chance <= 20) or (Chance > 70):
			AddShipTimer(PlayerSpecies, "friendlyRace", pSet)
		if (Chance > 60) or (Chance <= 70):
			AddShipTimer(PlayerSpecies, "enemy")
		if (Chance % 10 == 0) and (ferengidone == 0):
			ferengidone = 1
			AddShipTimer(PlayerSpecies, "ferengi", pSet)

        # tell call
        pSequence = App.TGSequence_Create()
	pAction = App.CharacterAction_Create(g_pKiska, App.CharacterAction.AT_SAY_LINE, "Start call", None, 0, pDatabase)
        pSequence.AppendAction(pAction)
        pSequence.Play()
       
        # and finally the Timer to reactivate the Button.
	myEvent = Libs.LibEngineering.GetEngineeringNextEventType()
        MissionLib.CreateTimer(myEvent, __name__ + ".reacButton", App.g_kUtopiaModule.GetGameTime() + 300, 0, 0)
        if not pButton:
                pMenu = Libs.LibEngineering.GetBridgeMenu("Helm")
                pButton = Libs.LibEngineering.GetButton("Send distress call", pMenu)
        pButton.SetDisabled()


# returns -RandomMax...+RandomMax
def GetRandom(RandomMax):
        debug(__name__ + ", GetRandom")
	if RandomMax > 0:
        	return App.g_kSystemWrapper.GetRandomNumber(RandomMax) * (-1) ** App.g_kSystemWrapper.GetRandomNumber(2)
	return 0
        
        
def CreateAIPosition(g_pAIShip, pSet):
        debug(__name__ + ", CreateAIPosition")
        RandomMax = 1000
	kLocation = App.TGPoint3()
        X = GetRandom(RandomMax)
        Y = GetRandom(RandomMax)
        Z = GetRandom(RandomMax)
	kLocation.SetXYZ(X, Y, Z)
	
        i = 0
	while ( pSet.IsLocationEmptyTG(kLocation, g_pAIShip.GetRadius()*2, 1) == 0):
		X = GetRandom(RandomMax)
		Y = GetRandom(RandomMax)
                Z = GetRandom(RandomMax)
		kLocation.SetXYZ(X, Y, Z)
                i = i + 1
                if i == 10:
                        i = 0
                        RandomMax = RandomMax + 10000
	
	g_pAIShip.SetTranslate(kLocation)
	g_pAIShip.UpdateNodeOnly()
	

def init():
	# not configured for Multiplayer yet
        debug(__name__ + ", init")
        if App.g_kUtopiaModule.IsMultiplayer():
                return

	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return

	global pButton
	pButton = Libs.LibEngineering.CreateMenuButton("Send distress call", "Helm", __name__ + ".SendCall")


def Restart():
	debug(__name__ + ", Restart")
	global dict_Notify, dict_Notify, dict_Timer
	
	# not configured for Multiplayer yet
        if App.g_kUtopiaModule.IsMultiplayer():
                return

	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return

	reacButton(None, None)
	dict_Notify = {}
	dict_Timer = {}


# Set Timer
ET_ADD = Libs.LibEngineering.GetEngineeringNextEventType()
ET_NOTIFY = Libs.LibEngineering.GetEngineeringNextEventType()
App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(ET_ADD, __name__ + ".AddShip")
App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(ET_NOTIFY, __name__ + ".NotifyHelp")
