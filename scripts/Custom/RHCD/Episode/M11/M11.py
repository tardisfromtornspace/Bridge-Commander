from bcdebug import debug
###############################################################################
#	Filename:	M11.py
#	
#	Confidential and Proprietary, Copyright 2002 by Totally Games
#	
#	Random Skirmish Mission.
#	
#	Created:	4/27/2003	- Brian Moler (RedHotChiliDog)							  has good style :P )
###############################################################################
import App
import loadspacehelper
import MissionLib

# Mission state enumeration. This helps make it easier to keep track of where
# the user is in the mission.
MS_MISSION_START			= 0
MS_ARRIVED_YILES2			= 1
MS_LEAVE_YILES2				= 2
MS_MISSION_WIN				= 3
MS_MISSION_LOSE				= 4

g_eMissionState				= MS_MISSION_START
g_pMissionTGL 				= None		# string database for the mission
g_eMissionBriefingComplete		= 0		# indicates mission briefing is complete
g_ePlayerVictory			= 0		# indicates player win or loss

g_PlayerShipClassList = ["Akira", "Ambassador", "BirdOfPrey", "CardHybrid", "Galaxy", "Galor", "Keldon", "KessokHeavy", "KessokLight", "Marauder", "Nebula", "Sovereign", "Vorcha", "Warbird"]
g_EnemyShipClassList  = ["Akira", "Ambassador", "BirdOfPrey", "CardHybrid", "Galaxy", "Galor", "Keldon", "KessokHeavy", "KessokLight", "Marauder", "Nebula", "Sovereign", "Vorcha", "Warbird"]

g_PlayerShipClass			= ""
g_EnemyShipClass			= ""
g_PlayerCount				= 0
g_EnemyCount				= 0

fRandomTime				= 0
fRandomPlayer				= 0
fRandomEnemy				= 0
fStartTime				= 0

###############################################################################
#	PreLoadAssets()
#	
#	This is called once, at the beginning of the mission before Initialize()
#	to allow us to add instances of ships we'll use. This is not mandatory,
#	but will prevent hitching when ships are created.
#	
#	Args:	pMission	- the Mission object
#	
#	Return:	none
###############################################################################
def PreLoadAssets(pMission):

	debug(__name__ + ", PreLoadAssets")
	global g_PlayerShipClassList
	global g_EnemyShipClassList
	global g_PlayerShipClass
	global g_EnemyShipClass
	global g_PlayerCount
	global g_EnemyCount

	# Count the entries in the player ship class list
	for sName in g_PlayerShipClassList:
		g_PlayerCount = g_PlayerCount + 1

	# Count the entries in the enemy ship class list
	for sName in g_EnemyShipClassList:
		g_EnemyCount = g_EnemyCount + 1
		
	# Pre-create player ship for this mission.
	if g_PlayerCount:
		fRandomPlayer = App.g_kSystemWrapper.GetRandomNumber(g_PlayerCount)
		g_PlayerShipClass = g_PlayerShipClassList [fRandomPlayer]
		loadspacehelper.PreloadShip(g_PlayerShipClass, 1)

	# Pre-create enemy ship for this mission.
	if g_EnemyCount:
		fRandomEnemy = App.g_kSystemWrapper.GetRandomNumber(g_EnemyCount)
		g_EnemyShipClass = g_EnemyShipClassList [fRandomEnemy]
		loadspacehelper.PreloadShip(g_EnemyShipClass, 1)
		
################################################################################
#	Initialize()
#	
#	Called once when mission loads to initialize mission.
#	
#	Args: 	pMission	- the mission object
#	
#	Return: None
################################################################################
def Initialize(pMission):
	debug(__name__ + ", Initialize")
	global g_pMissionTGL
	g_pMissionTGL = App.g_kLocalizationManager.Load("data/TGL/RHCD/Episode/M11.tgl")

	global g_eMissionState
	g_eMissionState = MS_MISSION_START
	
	global g_eMissionBriefingComplete
	g_eMissionBriefingComplete = 0

	# Specify (and load if necessary) the player's bridge. This is only
	# necessary for the first mission in the game, unless you're switching
	# bridges.
	import LoadBridge
	LoadBridge.Load("SovereignBridge")

	# Create the regions for this mission
	CreateRegions()

	# Create the starting objects
	CreateStartingObjects(pMission)

	# Setup event handlers.
	SetupEventHandlers()

	# Mission briefing()
	MissionBriefing()
	
################################################################################
#	CreateRegions()
#
#	Creates the regions we'll be using in this mission.  Also loads in any
#	mission placement files we need.
#
#	Args:	None
#
#	Return:	None
################################################################################
def CreateRegions():
	# Yiles
	debug(__name__ + ", CreateRegions")
	import Systems.Yiles.Yiles
	pYilesMenu = CreateYilesMenus()
	pYiles1Set = MissionLib.SetupSpaceSet("Systems.Yiles.Yiles1")
	pYiles2Set = MissionLib.SetupSpaceSet("Systems.Yiles.Yiles2")
	
	# Add our custom placement objects for this mission.
	import M11Yiles2_P
	M11Yiles2_P.LoadPlacements(pYiles2Set.GetName())

################################################################################
#	CreateYilesMenus()
#
#	Use this instead of the standard CreateMenus function from the Yiles
#	system.  This only puts Yiles1 and Yiles2 on the menu.
#
#	Args:	None
#
#	Return:	None
################################################################################
def CreateYilesMenus():
	debug(__name__ + ", CreateYilesMenus")
	import Systems.Utils
	return Systems.Utils.CreateSystemMenu("Yiles", "Systems.Yiles.Yiles2",
							 "Systems.Yiles.Yiles1",
							 "Systems.Yiles.Yiles2")

################################################################################
#	CreateStartingObjects()
#
#	Creates all the objects that exist at the beginning of the mission and sets
# 	up the affiliations for all objects that will occur in the mission.
#
#	Args:	pMission	- The mission object.
#
#	Return:	None
################################################################################
def CreateStartingObjects(pMission):

	debug(__name__ + ", CreateStartingObjects")
	global g_PlayerShipClass
	global g_EnemyShipClass
	
	# get the sets we need
	pYiles1Set = App.g_kSetManager.GetSet("Yiles1")

	# Create the ships that exist at mission start.
	pPlayer	= MissionLib.CreatePlayerShip(g_PlayerShipClass, pYiles1Set, "player", "Player Start")
	
	# Setup ship affiliations.
	pFriendlies = MissionLib.GetFriendlyGroup()
	pFriendlies.AddName(pPlayer.GetName())
	
	pNeutrals = pMission.GetNeutralGroup()
	
	pEnemies = MissionLib.GetEnemyGroup()
	for i in range(1):
		pEnemies.AddName(g_EnemyShipClass + " " + str(i + 1))

###############################################################################
#	SetupEventHandlers()
#	
#	Sets up event handlers for this mission.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def SetupEventHandlers():
	debug(__name__ + ", SetupEventHandlers")
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXITED_WARP,
		pMission, __name__ + ".HandleExitedWarp")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING,
		pMission, __name__ + ".HandleObjectExploding")

	# Special handlers for menu buttons
	# Helm buttons
	import Bridge.BridgeUtils
	pKiskaMenu = Bridge.BridgeUtils.GetBridgeMenu("Helm")
	if (pKiskaMenu != None):
		# Instance handler for warp button
		pWarpButton = Bridge.BridgeUtils.GetWarpButton()
		if (pWarpButton != None):
			pWarpButton.AddPythonFuncHandlerForInstance(App.ET_WARP_BUTTON_PRESSED, __name__ + ".HandleWarpButton")

###############################################################################
#	MissionBriefing()
#	
#	Does the mission briefing.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def MissionBriefing():
	debug(__name__ + ", MissionBriefing")
	pLiuSet = MissionLib.SetupBridgeSet("LiuSet", "data/Models/Sets/StarbaseControl/starbasecontrolRM.nif", -40, 65, -1.55)
	pLiu = App.CharacterClass_GetObject(pLiuSet, "Liu")
	if not (pLiu):
		pLiu = MissionLib.SetupCharacter("Bridge.Characters.Admiral_Liu", "LiuSet", 0, 0, 5)
		
	pViewOn	= App.TGScriptAction_Create("MissionLib", "ViewscreenOn", "LiuSet", "Liu")	
	pViewOff = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
	
	pSequence = App.TGSequence_Create()

	pLine1 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing1")
	pSequence.AddAction(pLine1)
	pLineDown1 = App.TGScriptAction_Create(__name__, "EndAction", pLine1.GetObjID())
	pSequence.AddAction(pLineDown1, App.TGAction_CreateNull(), 15.0)

	pLine2 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing2")
	pSequence.AddAction(pLine2, pLine1, 1.0)
	pLineDown2 = App.TGScriptAction_Create(__name__, "EndAction", pLine2.GetObjID())
	pSequence.AddAction(pLineDown2, pLineDown1, 5.0)
	
	# Viewscreen On.
	pSequence.AddAction(pViewOn, pLineDown2, 1.0)

	pLine3 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing3")
	pSequence.AddAction(pLine3, pLine2, 1.0)
	pLineDown3 = App.TGScriptAction_Create(__name__, "EndAction", pLine3.GetObjID())
	pSequence.AddAction(pLineDown3, pLineDown2, 5.0)

	pLine4 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing4")
	pSequence.AddAction(pLine4, pLine3, 1.0)
	pLineDown4 = App.TGScriptAction_Create(__name__, "EndAction", pLine4.GetObjID())
	pSequence.AddAction(pLineDown4, pLineDown3, 10.0)
	
	pLine5 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing5")
	pSequence.AddAction(pLine5, pLine4, 1.0)
	pLineDown5 = App.TGScriptAction_Create(__name__, "EndAction", pLine5.GetObjID())
	pSequence.AddAction(pLineDown5, pLineDown4, 10.0)

	pLine6 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing6")
	pSequence.AddAction(pLine6, pLine5, 1.0)
	pLineDown6 = App.TGScriptAction_Create(__name__, "EndAction", pLine6.GetObjID())
	pSequence.AddAction(pLineDown6, pLineDown5, 5.0)

	# Viewscreen Off.
	pSequence.AddAction(pViewOff, pLineDown6, 1.0)
	
	pLine7 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing7")
	pSequence.AddAction(pLine7, pLine6, 1.0)
	pLineDown7 = App.TGScriptAction_Create(__name__, "EndAction", pLine7.GetObjID())
	pSequence.AddAction(pLineDown7, pLineDown6, 5.0)

	# Go to Red Alert status.
	pSequence.AddAction(App.TGScriptAction_Create(__name__, "GoToRedAlert"), pLineDown7, 1.0)

	pLine8 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing8")
	pSequence.AddAction(pLine8, pLine7, 1.0)
	pLineDown8 = App.TGScriptAction_Create(__name__, "EndAction", pLine8.GetObjID())
	pSequence.AddAction(pLineDown8, pLineDown7, 5.0)
	
	# Mission briefing complete.  This will permit the player to warp after the entire
	# initial briefing has been played out.  I had to add this, as the initial briefing sequence 
	# could still be playing well into the action of the next set, which we do not want.
	pSequence.AddAction(App.TGScriptAction_Create(__name__, "MissionBriefingComplete"), pLineDown8, 1.0)

	# Play the sequence.
	pSequence.Play()

###############################################################################
#	MissionBriefingComplete(pAction)
#	
#	Tells script that mission briefing is complete.
#	
#	Args:	pAction		- this action
#	
#	Return:	zero, to indicate normal action termination
###############################################################################
def MissionBriefingComplete(pAction):

	debug(__name__ + ", MissionBriefingComplete")
	global g_eMissionBriefingComplete
	g_eMissionBriefingComplete = 1
	
	return 0

###############################################################################
#	AddObjectives()
#
#	Adds goals and timers after briefing
#
#	Args:	none
#			
#	Return:	none
###############################################################################
def AddObjectives(pAction):

	debug(__name__ + ", AddObjectives")
	return 0
	
###############################################################################
#	GoToRedAlert(pAction)
#	
#	Red alert status.
#	
#	Args:	pAction		- this action
#	
#	Return:	zero, to indicate normal action termination
###############################################################################
def GoToRedAlert(pAction):
	# Switch to red alert
	debug(__name__ + ", GoToRedAlert")
	App.TGSoundAction_Create("RedAlertSound").Play()
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(App.Game_GetCurrentGame().GetPlayer())
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(App.Game_GetCurrentGame().GetPlayer().RED_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	
	return 0
	
###############################################################################
#	EndAction(pAction, idActionToEnd)
#	
#	Ends the action with the specified ID. Used above to remove subtitle-only
#	lines.
#	
#	Args:	pAction		- this action, passed in automatically
#		idActionToEnd	- the object ID of the action to end
#	
#	Return:	zero, for normal action end
###############################################################################
def EndAction(pAction, idActionToEnd):
	debug(__name__ + ", EndAction")
	pAction = App.TGAction_Cast(App.TGObject_GetTGObjectPtr(idActionToEnd))

	if pAction:
		pAction.Completed()	# Finish the action.

	return 0

###############################################################################
#	HandleExitedWarp(pMission, pEvent)
#	
#	Event handler for when an object is done warping.
#	
#	Args:	pMission	- the mission (the object specified in the event
#						  handler)
#		pEvent		- the event
#	
#	Return:	none
###############################################################################
def HandleExitedWarp(pMission, pEvent):
	# Check if the object is the player.
	debug(__name__ + ", HandleExitedWarp")
	pShip = App.ShipClass_Cast(pEvent.GetSource())
	pPlayer = App.Game_GetCurrentPlayer()

	if (pShip != None) and (pPlayer != None) and (pShip.GetObjID() == pPlayer.GetObjID()):
		# It's the player.
		global g_eMissionState
		global g_ePlayerVictory
		pSet = pShip.GetContainingSet()
		if not pSet:
			pMission.CallNextHandler(pEvent)
			return

		# If the player is in the MS_MISSION_START state and they
		# are entering Yiles 2, proceed to the next state of the mission.
		if (g_eMissionState == MS_MISSION_START) and (pSet.GetName() == "Yiles2"):
			# Move to the next state in the mission.
			g_eMissionState = MS_ARRIVED_YILES2

			# Play the cutscene showing the ships warping in.
			Yiles2Cutscene()

		# If the player is in the MS_LEAVE_YILES2 state and they
		# are entering Yiles 1, play the victory/loss sequence.
		if (g_eMissionState == MS_LEAVE_YILES2) and (pSet.GetName() == "Yiles1"):
			# Play victory or loss sequence.
			if g_ePlayerVictory:
				g_eMissionState = MS_MISSION_WIN
				VictorySequence()
			else:
				g_eMissionState = MS_MISSION_LOSE
				LossSequence()

	pMission.CallNextHandler(pEvent)

###############################################################################
#	HandleObjectExploding(pMission, pEvent)
#	
#	Handler called whenever something is dying.
#	
#	Args:	pMission	- the mission (the object specified in the event
#						  handler)
#		pEvent		- the event
#	
#	Return:	none
###############################################################################
def HandleObjectExploding(pMission, pEvent):

	debug(__name__ + ", HandleObjectExploding")
	global g_PlayerShipClass
	global g_EnemyShipClass
	
	# If the player is in Yiles 2, check if it was the last enemy ship
	# exploding.
	pPlayer = App.Game_GetCurrentPlayer()
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	
	if (pPlayer != None) and (g_eMissionState == MS_ARRIVED_YILES2):
		pSet = pPlayer.GetContainingSet()
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		pEnemies = MissionLib.GetEnemyGroup()

		# Make sure it was an enemy that was blowing up.
		if (pShip != None) and (pEnemies.IsNameInGroup(pShip.GetName()) == 0):
			pMission.CallNextHandler(pEvent)
			return
			
		for i in range(1):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, g_EnemyShipClass + " " + str(i + 1)))
			if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):
				pMission.CallNextHandler(pEvent)
				return

		# No live enemies left. Play a little sequence.
		pBridge = App.g_kSetManager.GetSet("bridge")
		pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
		pMiguel = App.CharacterClass_GetObject(pBridge, "Science")

		pSequence = App.TGSequence_Create()
		pSequence.AppendAction(App.CharacterAction_Create(pFelix, 
			App.CharacterAction.AT_SAY_LINE, "FelixEnDes", None, 1, pFelix.GetDatabase()))
		pSequence.AppendAction(App.CharacterAction_Create(pMiguel, 
			App.CharacterAction.AT_SAY_LINE, "gs038", "Captain", 1, pMiguel.GetDatabase()))
		pSequence.Play()
		global g_eMissionState
		g_eMissionState = MS_MISSION_WIN
		VictorySequence()

	pMission.CallNextHandler(pEvent)

###############################################################################
#	HandleWarpButton(pWarpButton, pEvent)
#	
#	Handler called when the user clicks on the warp button. To prevent warping,
#	don't call the next handler.
#	
#	Args:	pWarpButton	- the warp button
#		pEvent		- the event
#	
#	Return:	none
###############################################################################
def HandleWarpButton(pWarpButton, pEvent):

	debug(__name__ + ", HandleWarpButton")
	global g_PlayerShipClass
	global g_EnemyShipClass
	
	pPlayer = App.Game_GetCurrentPlayer()
	if not pPlayer:
		pWarpButton.CallNextHandler(pEvent)
		return

	pSet = pPlayer.GetContainingSet()
	if not pSet:
		pWarpButton.CallNextHandler(pEvent)
		return
		
	# If mission briefing is not complete, then do not allow warping.
	if (pSet.GetName() == "Yiles1") and (g_eMissionBriefingComplete == 0):
		return

	# If player retreated back to Yiles1, then do not allow warping.
	if (pSet.GetName() == "Yiles1") and (g_eMissionState == MS_MISSION_LOSE):
		return
		
	if (pSet.GetName() == "Yiles2") and (g_eMissionState == MS_ARRIVED_YILES2):
		global g_ePlayerVictory
		global g_eMissionState		
		g_ePlayerVictory = 1
		g_eMissionState = MS_LEAVE_YILES2
		# Check if there are still enemies in Yiles 2. If so, then player loses.
		for i in range(1):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, g_EnemyShipClass + " " + str(i + 1)))
			if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):
				# There's an enemy still here. The player loses.
				g_ePlayerVictory = 0

	pWarpButton.CallNextHandler(pEvent)

###############################################################################
#	Yiles2Cutscene()
#	
#	Creates the sequence for when the player first enters Yiles 2. Shows
#	three Vorchas warping in to attack the player.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def Yiles2Cutscene():

	debug(__name__ + ", Yiles2Cutscene")
	global g_PlayerShipClass
	global g_EnemyShipClass
	
	pYiles2Set = App.g_kSetManager.GetSet("Yiles2")
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")

	# Create the enemy ship, and have them warp in. The extra parameter at the end
	# indicates that they should warp in (from nowhere). We won't assign their
	# AI just yet, because having them attack the player during the cutscene
	# would be unfair.
	pEnemy1 = loadspacehelper.CreateShip(g_EnemyShipClass, pYiles2Set, g_EnemyShipClass + " " + str(1), "Enemy 1 Start", 1)

	pSeq = App.TGSequence_Create()

	# Start the cutscene.
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
	# Create a cutscene camera for Yiles 2.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", "Yiles2"))
	# Make the cutscene camera watch the enemy warping in.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "PlacementWatch", "Yiles2", 
					  "Enemy 1 Start", "Cutscene Camera Placement"))
	# Change us so we're rendering Yiles 2 instead of whatever else.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "Yiles2"))
	# Have Felix announce the incoming enemies.
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming1", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))

	# Kill the cutscene camera.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", "Yiles2"), 4.0)
	# Move back to the bridge.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
	# End the cutscene.
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
	# Assign the AIs for the enemy.
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AssignEnemyAI"))

	pSeq.Play()

###############################################################################
#	AssignEnemyAI(pAction)
#	
#	Script action that assigns the attack AI for the enemy that warp into
#	Yiles 2.
#	
#	Args:	pAction		- this action
#	
#	Return:	zero, to indicate normal action termination
###############################################################################
def AssignEnemyAI(pAction):

	debug(__name__ + ", AssignEnemyAI")
	global g_PlayerShipClass
	global g_EnemyShipClass
	
	pYiles2Set = App.g_kSetManager.GetSet("Yiles2")
	pEnemy1 = App.ShipClass_GetObject(pYiles2Set, g_EnemyShipClass + " " + str(1))

	import EnemyAI
	pEnemy1.SetAI(EnemyAI.CreateAI(pEnemy1))
	
	return 0
	
###############################################################################
#	VictorySequence()
#	
#	Plays the sequence to celebrate player victory.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def VictorySequence():
	debug(__name__ + ", VictorySequence")
	pLiuSet = MissionLib.SetupBridgeSet("LiuSet", "data/Models/Sets/StarbaseControl/starbasecontrolRM.nif", -40, 65, -1.55)
	pLiu = App.CharacterClass_GetObject(pLiuSet, "Liu")
	if not (pLiu):
		pLiu = MissionLib.SetupCharacter("Bridge.Characters.Admiral_Liu", "LiuSet", 0, 0, 5)
		
	pViewOn	= App.TGScriptAction_Create("MissionLib", "ViewscreenOn", "LiuSet", "Liu")	
	pViewOff = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
	
	pSequence = App.TGSequence_Create()

	pLine1 = App.SubtitleAction_Create(g_pMissionTGL, "Victory1")
	pSequence.AddAction(pLine1)
	pLineDown1 = App.TGScriptAction_Create(__name__, "EndAction", pLine1.GetObjID())
	pSequence.AddAction(pLineDown1, App.TGAction_CreateNull(), 15.0)

	pLine2 = App.SubtitleAction_Create(g_pMissionTGL, "Victory2")
	pSequence.AddAction(pLine2, pLine1, 1.0)
	pLineDown2 = App.TGScriptAction_Create(__name__, "EndAction", pLine2.GetObjID())
	pSequence.AddAction(pLineDown2, pLineDown1, 5.0)
	
	# Viewscreen On.
	pSequence.AddAction(pViewOn, pLineDown2, 1.0)

	pLine3 = App.SubtitleAction_Create(g_pMissionTGL, "Victory3")
	pSequence.AddAction(pLine3, pLine2, 1.0)
	pLineDown3 = App.TGScriptAction_Create(__name__, "EndAction", pLine3.GetObjID())
	pSequence.AddAction(pLineDown3, pLineDown2, 5.0)

	# Viewscreen Off.
	pSequence.AddAction(pViewOff, pLineDown3, 1.0)
	
	# Play the sequence.
	pEndGame = App.TGScriptAction_Create("MissionLib", "GameOver", pSequence)
	pEndGame.Play()		

###############################################################################
#	LossSequence()
#	
#	Plays the sequence for player loss.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def LossSequence():
	debug(__name__ + ", LossSequence")
	pLiuSet = MissionLib.SetupBridgeSet("LiuSet", "data/Models/Sets/StarbaseControl/starbasecontrolRM.nif", -40, 65, -1.55)
	pLiu = App.CharacterClass_GetObject(pLiuSet, "Liu")
	if not (pLiu):
		pLiu = MissionLib.SetupCharacter("Bridge.Characters.Admiral_Liu", "LiuSet", 0, 0, 5)
		
	pViewOn	= App.TGScriptAction_Create("MissionLib", "ViewscreenOn", "LiuSet", "Liu")	
	pViewOff = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
	
	pSequence = App.TGSequence_Create()

	pLine1 = App.SubtitleAction_Create(g_pMissionTGL, "Loss1")
	pSequence.AddAction(pLine1)
	pLineDown1 = App.TGScriptAction_Create(__name__, "EndAction", pLine1.GetObjID())
	pSequence.AddAction(pLineDown1, App.TGAction_CreateNull(), 15.0)

	pLine2 = App.SubtitleAction_Create(g_pMissionTGL, "Loss2")
	pSequence.AddAction(pLine2, pLine1, 1.0)
	pLineDown2 = App.TGScriptAction_Create(__name__, "EndAction", pLine2.GetObjID())
	pSequence.AddAction(pLineDown2, pLineDown1, 5.0)
	
	# Viewscreen On.
	pSequence.AddAction(pViewOn, pLineDown2, 1.0)

	pLine3 = App.SubtitleAction_Create(g_pMissionTGL, "Loss3")
	pSequence.AddAction(pLine3, pLine2, 1.0)
	pLineDown3 = App.TGScriptAction_Create(__name__, "EndAction", pLine3.GetObjID())
	pSequence.AddAction(pLineDown3, pLineDown2, 5.0)

	# Viewscreen Off.
	pSequence.AddAction(pViewOff, pLineDown3, 1.0)
	
	# Play the sequence.
	pEndGame = App.TGScriptAction_Create("MissionLib", "GameOver", pSequence)
	pEndGame.Play()	

################################################################################
#	Terminate()
#	
#	Called when mission ends to free resources
#	
#	Args: pMission - the mission object
#	
#	Return: None
################################################################################
def Terminate(pMission):
	# Clear out all the systems in the set course menu.
	debug(__name__ + ", Terminate")
	App.SortedRegionMenu_ClearSetCourseMenu()
	
	global g_pMissionTGL
	if g_pMissionTGL:
		App.g_kLocalizationManager.Unload(g_pMissionTGL)
		g_pMissionTGL = None