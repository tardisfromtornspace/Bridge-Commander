#from bcdebug import debug
# based on:
# 'Distress call.py' by Defiant
# erik@defiant.homedns.org
# modified to RandomBattle.py dy cnotsch
# c.notsch@gmx.at

import App
import MissionLib
import Libs.LibEngineering
import Lib.LibEngineering
import Foundation
import string
import math
from Custom.QBautostart.Libs.Races import Races
import loadspacehelper


MODINFO = { "Author": "\"cnotsch\" c.notsch@gmx.at",
            "Download": "",
            "Version": "0.2",
            "License": "GPL",
            "Description": "Setup a randomly created battle in QB.",
            "needBridge": 0
            }

min_time = 1
max_time = 600
ferengidone	= 0
maxships = max_time / 16
maxshipsonmap = 10
friendlypercent = 25
friendlyracepercent = 15
enemypercent =60
maxshipsonmaplimit = 50
time = 16
godsdisabled = 1
MAX_NUM_SHIPS = 50
incoming_mult = 4
dict_Timer = {}
dict_Notify = {}
ShipInd = 1
ET_ADD = None
ET_NOTIFY = None
pGodButton = None
pButton = None
i_Ship = 0
pDifficultyButton = None
pmaxshipsButton = None
pTimeButton = None
running = 0
count = 0
efp =  friendlypercent + enemypercent
effp = efp + friendlyracepercent


###############################################################################################

def GetShipType(pShip):
	# thanks to mldaalder for the idea of using -1 instead of 1
        #debug(__name__ + ", GetShipType")
        return string.split(pShip.GetScript(), '.')[-1]


###############################################################################################

def GetFreeName(Name):
        #debug(__name__ + ", GetFreeName")
        #global i_Ship
	i_Ship = 0
	
	while(MissionLib.GetShip(Name + str(i_Ship))):
		i_Ship = i_Ship + 1
	if i_Ship == 0:
		return Name
	return Name + str(i_Ship)
	

###############################################################################################

# Species of the Ship
def GetShipSpecies(pShip):
	#debug(__name__ + ", GetShipSpecies")
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


###############################################################################################

def IsGodShip(ShipType):
	#debug(__name__ + ", IsGodShip")
	return Races["GodShips"].IsOurRace(ShipType)


###############################################################################################

def IsGodRace(myRace):
	#debug(__name__ + ", IsGodRace")
	if (myRace == "Borg"):
                return 1
	if (myRace == "8472"):
                return 1
        return 0


###############################################################################################        

def getMVAMShip(ShipType):
        #debug(__name__ + ", getMVAMShip")
        if ShipType in ["MvamGalaxySaucer", "MvamGalaxyStardrive"]:
                return "MvamGalaxy"
        elif ShipType in ["MvamPrometheusSaucer", "MvamPrometheusDorsal", "MvamPrometheusVentral"]:
                return "MvamPrometheus"
        return None


###############################################################################################

# Finally adds a ship
def AddShip(pObject, pEvent):
	#debug(__name__ + ", AddShip")
	global dict_Timer, running
	pPlayer		= MissionLib.GetPlayer()
	
	if not pPlayer:
		return

	pEnemyGroup     = MissionLib.GetEnemyGroup()
	pFriendlyGroup     = MissionLib.GetFriendlyGroup()
	pSet		= pPlayer.GetContainingSet()
	lpEnemys        = pEnemyGroup.GetActiveObjectTupleInSet(pSet)
	lpFriendlys        = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)

	countEnemy	= 0
	countFriendly	= 0
	        
	# Count enemy Ships in System.
	for pEnemy in lpEnemys:
		# If it is a god Ship or a Base, add 5 points
		ShipType = GetShipType(pEnemy)
		if IsGodShip(ShipType) or pEnemy.GetShipProperty().IsStationary():
			countEnemy = countEnemy + 5
		else:
			countEnemy = countEnemy + 1
	# Count enemy Ships in System.
	for pFriendly in lpFriendlys:
		# If it is a god Ship or a Base, add 5 points
		ShipType = GetShipType(pFriendly)
		if IsGodShip(ShipType) or pFriendly.GetShipProperty().IsStationary():
			countFriendly = countFriendly + 5
		else:
			countFriendly = countFriendly + 1
	if countFriendly + countEnemy > maxshipsonmap:
		return


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


###############################################################################################

# Starts the Timer to add ships
def AddShipTimer(ShipRace, ToAdd, pSet = None):
	#debug(__name__ + ", AddShipTimer")
	global dict_Timer, ShipInd, ET_ADD, ET_NOTIFY, dict_Notify, min_time, max_time, incoming_mult, godsdisabled, time
	RealAddTime = time
	if time > 0:
		RealAddTime = App.g_kSystemWrapper.GetRandomNumber(time) + min_time
	AddTime = App.g_kUtopiaModule.GetGameTime() + RealAddTime
	myEvent = Libs.LibEngineering.GetEngineeringNextEventType()
	MissionLib.CreateTimer(myEvent, __name__ + ".loop", AddTime, 0, 0)

	NotifyTime = 0
	AddShipRace = None
        EscortShips = None
	pPlayer = MissionLib.GetPlayer()
	
	if pPlayer and not pSet:
		pSet = pPlayer.GetContainingSet()

	# ok, thats what we have to do here:
	# 1. Get our enemys and friendlys
	if not Races.has_key(ShipRace):
		#print("Error: No race info for", ShipRace)
		return
	
	# 2. Find out what to do:
	if (ToAdd == "friendly"):
		# Get a random shiptype:
		if (len(Races[ShipRace].GetShips()) == 0):
			print("Warning: No Ships for Race", ShipRace)
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
		if godsdisabled == 1:
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
		if godsdisabled == 1:
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

	
	# Create a timer - it's a thing that will wait for a given time,then do something
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(AddTime)
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pTimerEvent)
	App.g_kTimerManager.AddTimer(pTimer)

	#print("Get: ", ShipType, ShipName, "as", Position, "in", RealAddTime)
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



###############################################################################################

def reacButton(pObject, pEvent):
        #debug(__name__ + ", reacButton")
        global pButton
        if not pButton:
                pMenu = Libs.LibEngineering.GetBridgeMenu("Helm")
                pButton = Libs.LibEngineering.GetButton("Start...", pMenu)
	if pButton:
        	pButton.SetEnabled()

###############################################################################################
 
# Print Help arriving in...seconds
def NotifyHelp(pObject, pEvent):
	#debug(__name__ + ", NotifyHelp")
	global dict_Notify
	
	if not dict_Notify.has_key(str(pEvent)):
		return
	
	shipName = dict_Notify[str(pEvent)][0]
	approxTime = dict_Notify[str(pEvent)][1]
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Distress call2.tgl")

	pcETA = pDatabase.GetString("ETA").GetCString()
	pcString = pcETA % (shipName, str(approxTime))

        # from Multiplayer
        pSequence = App.TGSequence_Create()
        pSubtitleAction = App.SubtitleAction_CreateC(pcString)
        pSubtitleAction.SetDuration(5.0)
        pSequence.AddAction(pSubtitleAction)
        pSequence.Play()
        App.STMissionLog_GetMissionLog().AddLine(App.TGString(pcString))

###############################################################################################

def SendCall(pObject, pEvent):
        #debug(__name__ + ", SendCall")
	global count, running
	if running == 1:
	        print("Random Battle has been stopped")
		count = 0
		running = 0
		if pButton:
	        	pButton.SetName(App.TGString("Start..."))
		return

        print("Random Battle has been started")
	count = 0
	running = 1
        myEvent = Libs.LibEngineering.GetEngineeringNextEventType()
        MissionLib.CreateTimer(myEvent, __name__ + ".Count", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
	loop(None,None)
	if pButton:
        	pButton.SetName(App.TGString("Stop..."))
	return

###############################################################################################

def loop(pObject, pEvent):
        #debug(__name__ + ", loop")
        global pButton, diffic, pDifficultyButton, running, count, pTimeButton, ferengidone, enemypercent, friendlypercent, friendlyracepercent
	if not running == 1:
		return
	pPlayer		= MissionLib.GetPlayer()
	#print 'loop'
	efp =  friendlypercent + enemypercent
	effp = efp + friendlyracepercent

	if not pPlayer:
		print 'no player'
		return
	
	pSet		= pPlayer.GetContainingSet()
        PlayerSpecies = GetShipSpecies(pPlayer)
        if not PlayerSpecies:
		print 'no playerspecies'
                return

	Chance = App.g_kSystemWrapper.GetRandomNumber(effp) + 1
	if (Chance <= enemypercent):
		AddShipTimer(PlayerSpecies, "enemy", pSet)
	if (Chance > enemypercent) and (Chance <= efp):
		AddShipTimer(PlayerSpecies, "friendly", pSet)
	if (Chance > efp):
		AddShipTimer(PlayerSpecies, "friendlyRace")
#	if (Chance < effp / 20) and (ferengidone == 0):
#		ferengidone = 1
#		AddShipTimer(PlayerSpecies, "ferengi", pSet)
		

###############################################################################################

# returns -RandomMax...+RandomMax
def GetRandom(RandomMax):
        #debug(__name__ + ", GetRandom")
	if RandomMax > 0:
        	return App.g_kSystemWrapper.GetRandomNumber(RandomMax) * (-1) ** App.g_kSystemWrapper.GetRandomNumber(2)
	return 0


###############################################################################################        
        
def CreateAIPosition(g_pAIShip, pSet):
        #debug(__name__ + ", CreateAIPosition")
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
	

###############################################################################################

def init():
	# not configured for Multiplayer yet
        #debug(__name__ + ", init")
        if App.g_kUtopiaModule.IsMultiplayer():
                return

	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return

	global pButton, diffic, pDifficultyButton, pmaxshipsButton, maxshipsonmap, max_time, pTimeButton, godsdisabled, pGodButton
	pMasterButton = App.STMenu_CreateW(App.TGString("Random Battle Menue"))
	diffic=3
	pButton = Lib.LibEngineering.CreateMenuButton("Start...", "Helm", __name__ + ".SendCall", 0, pMasterButton)
	pDifficultyButton = Lib.LibEngineering.CreateMenuButton("Normal", "Helm", __name__ + ".Difficulty", 0, pMasterButton)
	pmaxshipsButton = Lib.LibEngineering.CreateMenuButton("max. ships on map: " + str(maxshipsonmap), "Helm", __name__ + ".maxshipsButton", 0, pMasterButton)
	pTimeButton = Lib.LibEngineering.CreateMenuButton("Battletime: " + str(0) + " min.", "Helm", __name__ + ".setmaxTime", 0, pMasterButton)
	pTimeButton.SetDisabled()
	if godsdisabled == 1:
		pGodButton = Lib.LibEngineering.CreateMenuButton("Enable GodShips", "Helm", __name__ + ".togglegods", 0, pMasterButton)
	if godsdisabled == 0:
		pGodButton = Lib.LibEngineering.CreateMenuButton("Disable GodShips", "Helm", __name__ + ".togglegods", 0, pMasterButton)
	Lib.LibEngineering.GetBridgeMenu("Helm").AddChild(pMasterButton)

###############################################################################################
	
def togglegods(pObject, pEvent):        
        #debug(__name__ + ", togglegods")
	global godsdisabled, pGodButton
	if godsdisabled == 0:
		godsdisabled = 1
		pGodButton.SetName(App.TGString("Enable GodShips"))
		return
	if godsdisabled == 1:
		godsdisabled = 0
		pGodButton.SetName(App.TGString("Disable GodShips"))
		return

###############################################################################################

def Restart():
	#debug(__name__ + ", Restart")
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
	

###############################################################################################

def Difficulty(pObject, pEvent):        
        #debug(__name__ + ", Difficulty")
        global diffic, pDifficultyButton, friendlypercent, friendlyracepercent, enemypercent, time
        
        diffic = diffic + 1
        
        if diffic > 5:
                diffic = 1
        if diffic == 1:
                pDifficultyButton.SetName(App.TGString("Very Easy"))
                friendlypercent = 35
                friendlyracepercent = 25
                enemypercent = 50
                time = 60
        if diffic == 2:
                pDifficultyButton.SetName(App.TGString("Easy"))
                friendlypercent = 35
                friendlyracepercent = 10
                enemypercent = 55
                time = 25
        if diffic == 3:
                pDifficultyButton.SetName(App.TGString("Normal"))
                friendlypercent = 30
                friendlyracepercent = 10
                enemypercent = 60
                time = 16
        if diffic == 4:
                pDifficultyButton.SetName(App.TGString("Hard"))
                friendlypercent = 16
                friendlyracepercent = 4
                enemypercent = 80
                time = 13
        if diffic == 5:
                pDifficultyButton.SetName(App.TGString("Extreme"))
                friendlypercent = 0
                friendlyracepercent = 0
                enemypercent = 100
                time = 10
        return


###############################################################################################

def maxshipsButton(pObject, pEvent):
        #debug(__name__ + ", maxshipsButton")
        global pmaxshipsButton, maxshipsonmap
        maxshipsonmap = maxshipsonmap + 2
        if maxshipsonmap >= maxshipsonmaplimit:
                maxshipsonmap = 2
        pmaxshipsButton.SetName(App.TGString("max. ships on map: " + str(maxshipsonmap)))
        return

###############################################################################################

def Count(pObject, pEvent):
        #debug(__name__ + ", Count")
        global max_time, count, pTimeButton, running
	if running == 1:
	        count = count + 1
		countmin = count / 60
		countsec = count - ( countmin * 60 )
		myEvent = Libs.LibEngineering.GetEngineeringNextEventType()
		MissionLib.CreateTimer(myEvent, __name__ + ".Count", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
		pTimeButton.SetName(App.TGString("Battletime: " + str(countmin) + " min. " + str(countsec) + " sec."))
		return
	pTimeButton.SetName(App.TGString("Battletime: " + str(0) + " min."))
	count = 0

###############################################################################################

def setmaxTime(pObject, pEvent):
        #debug(__name__ + ", setmaxTime")
        return

###############################################################################################

# Set Timer
ET_ADD = Libs.LibEngineering.GetEngineeringNextEventType()
ET_NOTIFY = Libs.LibEngineering.GetEngineeringNextEventType()
App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(ET_ADD, __name__ + ".AddShip")
App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(ET_NOTIFY, __name__ + ".NotifyHelp")

