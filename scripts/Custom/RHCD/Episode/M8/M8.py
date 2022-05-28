###############################################################################
#	Filename:	M8.py
#	
#	Confidential and Proprietary, Copyright 2002 by Totally Games
#	
#	Target of Opportunity (Klingon).
#	
#	Created:	5/15/2002	- Brian Moler (RedHotChiliDog)							  has good style :P )
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

ET_ACTIVATE_1				= App.Mission_GetNextEventType()
ET_ACTIVATE_2				= App.Mission_GetNextEventType()
ET_ACTIVATE_3				= App.Mission_GetNextEventType()
ET_ACTIVATE_4				= App.Mission_GetNextEventType()
ET_ACTIVATE_5				= App.Mission_GetNextEventType()

g_eMissionState				= MS_MISSION_START
g_pMissionTGL 				= None		# string database for the mission
g_eMissionBriefingComplete		= 0		# indicates mission briefing is complete
g_ePlayerVictory			= 0		# indicates player win or loss

g_idActivate1Timer			= App.NULL_ID
g_idActivate2Timer			= App.NULL_ID
g_idActivate3Timer			= App.NULL_ID
g_idActivate4Timer			= App.NULL_ID
g_idActivate5Timer			= App.NULL_ID

fRandomTime				= 0
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
	# Pre-create ships for this mission.
	loadspacehelper.PreloadShip("Sovereign", 1)
	loadspacehelper.PreloadShip("Vorcha", 3)
	loadspacehelper.PreloadShip("BirdOfPrey", 2)
	
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
	global g_pMissionTGL
	g_pMissionTGL = App.g_kLocalizationManager.Load("data/TGL/RHCD/Episode/M8.tgl")

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
	import Systems.Yiles.Yiles
	pYilesMenu = CreateYilesMenus()
	pYiles1Set = MissionLib.SetupSpaceSet("Systems.Yiles.Yiles1")
	pYiles2Set = MissionLib.SetupSpaceSet("Systems.Yiles.Yiles2")
	
	# Add our custom placement objects for this mission.
	import M8Yiles2_P
	M8Yiles2_P.LoadPlacements(pYiles2Set.GetName())

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
	# get the sets we need
	pYiles1Set = App.g_kSetManager.GetSet("Yiles1")

	# Create the ships that exist at mission start.
	pPlayer	= MissionLib.CreatePlayerShip("Sovereign", pYiles1Set, "player", "Player Start")
	
	# Setup ship affiliations.
	pFriendlies = MissionLib.GetFriendlyGroup()
	pFriendlies.AddName(pPlayer.GetName())
	
	pNeutrals = pMission.GetNeutralGroup()
	
	pEnemies = MissionLib.GetEnemyGroup()
	for i in range(3):
		pEnemies.AddName("Vorcha " + str(i + 1))
	for i in range(2):
		pEnemies.AddName("BirdOfPrey " + str(i + 1))
		

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

	ClearTimers()
	
	# Create a Timer that triggers the release of Vorcha #1
	fStartTime = App.g_kUtopiaModule.GetGameTime()
	fRandomTime = App.g_kSystemWrapper.GetRandomNumber(180) + 180
	pActivate1 = MissionLib.CreateTimer(ET_ACTIVATE_1, __name__ + ".Activate1", fStartTime + fRandomTime, 0, 0)
	global g_idActivate1Timer
	g_idActivate1Timer = pActivate1.GetObjID()

	# Create a Timer that triggers the release of Vorcha #2
	fStartTime = App.g_kUtopiaModule.GetGameTime()
	fRandomTime = App.g_kSystemWrapper.GetRandomNumber(180) + 180
	pActivate2 = MissionLib.CreateTimer(ET_ACTIVATE_2, __name__ + ".Activate2", fStartTime + fRandomTime, 0, 0)
	global g_idActivate2Timer
	g_idActivate2Timer = pActivate2.GetObjID()
	
	# Create a Timer that triggers the release of Vorcha #3
	fStartTime = App.g_kUtopiaModule.GetGameTime()
	fRandomTime = App.g_kSystemWrapper.GetRandomNumber(180) + 180
	pActivate3 = MissionLib.CreateTimer(ET_ACTIVATE_3, __name__ + ".Activate3", fStartTime + fRandomTime, 0, 0)
	global g_idActivate3Timer
	g_idActivate3Timer = pActivate3.GetObjID()
	
	# Create a Timer that triggers the release of BirdOfPrey #1
	fStartTime = App.g_kUtopiaModule.GetGameTime()
	fRandomTime = App.g_kSystemWrapper.GetRandomNumber(180) + 180
	pActivate4 = MissionLib.CreateTimer(ET_ACTIVATE_4, __name__ + ".Activate4", fStartTime + fRandomTime, 0, 0)
	global g_idActivate4Timer
	g_idActivate4Timer = pActivate4.GetObjID()
	
	# Create a Timer that triggers the release of BirdOfPrey #2
	fStartTime = App.g_kUtopiaModule.GetGameTime()
	fRandomTime = App.g_kSystemWrapper.GetRandomNumber(180) + 180
	pActivate5 = MissionLib.CreateTimer(ET_ACTIVATE_5, __name__ + ".Activate5", fStartTime + fRandomTime, 0, 0)
	global g_idActivate5Timer
	g_idActivate5Timer = pActivate5.GetObjID()
	
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
			
		for i in range(3):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "Vorcha " + str(i + 1)))
			if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):
				pMission.CallNextHandler(pEvent)
				return
				
		for i in range(2):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "BirdOfPrey " + str(i + 1)))
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
		for i in range(3):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "Vorcha " + str(i + 1)))
			if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):
				# There's an enemy still here. The player loses.
				g_ePlayerVictory = 0

		for i in range(2):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "BirdOfPrey " + str(i + 1)))
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
	pYiles2Set = App.g_kSetManager.GetSet("Yiles2")
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")

	# Create the Klingons We won't assign their AI just yet, because we don't 
	# want them to activate until their random timer has expired.
	pVorcha1 = loadspacehelper.CreateShip("Vorcha", pYiles2Set, "Vorcha 1", "Vorcha 1 Start")
	pVorcha2 = loadspacehelper.CreateShip("Vorcha", pYiles2Set, "Vorcha 2", "Vorcha 2 Start")
	pVorcha3 = loadspacehelper.CreateShip("Vorcha", pYiles2Set, "Vorcha 3", "Vorcha 3 Start")
	pBirdOfPrey1 = loadspacehelper.CreateShip("BirdOfPrey", pYiles2Set, "BirdOfPrey 1", "BirdOfPrey 1 Start")
	pBirdOfPrey2 = loadspacehelper.CreateShip("BirdOfPrey", pYiles2Set, "BirdOfPrey 2", "BirdOfPrey 2 Start")

	# Enemy ships are at Green Alert status.
	pVorcha1.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	pVorcha2.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	pVorcha3.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	pBirdOfPrey1.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	pBirdOfPrey2.SetAlertLevel(App.ShipClass.GREEN_ALERT)
	
	pSeq = App.TGSequence_Create()

	# Start the cutscene.
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
	# Create a cutscene camera for Yiles 2.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", "Yiles2"))
	# Make the cutscene camera watch the Vorchas warping in.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "PlacementWatch", "Yiles2", 
					  "Vorcha 3 Start", "Cutscene Camera Placement"))
	# Change us so we're rendering Yiles 2 instead of whatever else.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "Yiles2"))

	# Kill the cutscene camera.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", "Yiles2"), 4.0)
	# Move back to the bridge.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
	# End the cutscene.
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
	
	# Add Objectives.  This will initiate timers for activating the enemy ships.
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AddObjectives"))

	pSeq.Play()

###############################################################################
#	Activate1()
#
#	Activate AI for Vorcha #1
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def Activate1(pObject, pEvent):

	# Have Felix announce the activating enemy.
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = pPlayer.GetContainingSet()
	pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "Vorcha 1"))
	if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):
		pBridge = App.g_kSetManager.GetSet("bridge")
		pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
		pSeq = App.TGSequence_Create()	
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt032", None, 0, pFelix.GetDatabase()))
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt036", None, 0, pFelix.GetDatabase()))
		pSeq.Play()
	
		pYiles2Set = App.g_kSetManager.GetSet("Yiles2")
	
		# Assign AI
		import KlingonAI
		pVorcha1 = App.ShipClass_GetObject(pYiles2Set, "Vorcha 1")
		pVorcha1.SetAI(KlingonAI.CreateAI(pVorcha1))

###############################################################################
#	Activate2()
#
#	Activate AI for Vorcha #2
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def Activate2(pObject, pEvent):

	# Have Felix announce the activating enemy.
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = pPlayer.GetContainingSet()
	pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "Vorcha 2"))
	if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):	
		pBridge = App.g_kSetManager.GetSet("bridge")
		pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
		pSeq = App.TGSequence_Create()	
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt032", None, 0, pFelix.GetDatabase()))
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt036", None, 0, pFelix.GetDatabase()))
		pSeq.Play()
	
		pYiles2Set = App.g_kSetManager.GetSet("Yiles2")
	
		# Assign AI
		import KlingonAI
		pVorcha2 = App.ShipClass_GetObject(pYiles2Set, "Vorcha 2")
		pVorcha2.SetAI(KlingonAI.CreateAI(pVorcha2))

###############################################################################
#	Activate3()
#
#	Activate AI for Vorcha #3
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def Activate3(pObject, pEvent):

	# Have Felix announce the activating enemy.
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = pPlayer.GetContainingSet()
	pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "Vorcha 3"))
	if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):	
		pBridge = App.g_kSetManager.GetSet("bridge")
		pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
		pSeq = App.TGSequence_Create()	
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt032", None, 0, pFelix.GetDatabase()))
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt036", None, 0, pFelix.GetDatabase()))
		pSeq.Play()
	
		pYiles2Set = App.g_kSetManager.GetSet("Yiles2")
	
		# Assign AI
		import KlingonAI
		pVorcha3 = App.ShipClass_GetObject(pYiles2Set, "Vorcha 3")
		pVorcha3.SetAI(KlingonAI.CreateAI(pVorcha3))
	
###############################################################################
#	Activate4()
#
#	Activate AI for BirdOfPrey #1
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def Activate4(pObject, pEvent):

	# Have Felix announce the activating enemy.
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = pPlayer.GetContainingSet()
	pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "BirdOfPrey 1"))
	if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):	
		pBridge = App.g_kSetManager.GetSet("bridge")
		pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
		pSeq = App.TGSequence_Create()	
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt032", None, 0, pFelix.GetDatabase()))
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt036", None, 0, pFelix.GetDatabase()))
		pSeq.Play()
	
		pYiles2Set = App.g_kSetManager.GetSet("Yiles2")
		
		# Assign AI
		import KlingonAI
		pBirdOfPrey1 = App.ShipClass_GetObject(pYiles2Set, "BirdOfPrey 1")
		pBirdOfPrey1.SetAI(KlingonAI.CreateAI(pBirdOfPrey1))	

###############################################################################
#	Activate5()
#
#	Activate AI for BirdOfPrey #2
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def Activate5(pObject, pEvent):

	# Have Felix announce the activating enemy.
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = pPlayer.GetContainingSet()
	pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "BirdOfPrey 2"))
	if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):	
		pBridge = App.g_kSetManager.GetSet("bridge")
		pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
		pSeq = App.TGSequence_Create()	
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt032", None, 0, pFelix.GetDatabase()))
		pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt036", None, 0, pFelix.GetDatabase()))
		pSeq.Play()
	
		pYiles2Set = App.g_kSetManager.GetSet("Yiles2")
	
		# Assign AI
		import KlingonAI
		pBirdOfPrey2 = App.ShipClass_GetObject(pYiles2Set, "BirdOfPrey 2")
		pBirdOfPrey2.SetAI(KlingonAI.CreateAI(pBirdOfPrey2))

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

	pLine4 = App.SubtitleAction_Create(g_pMissionTGL, "Victory4")
	pSequence.AddAction(pLine4, pLine3, 1.0)
	pLineDown4 = App.TGScriptAction_Create(__name__, "EndAction", pLine4.GetObjID())
	pSequence.AddAction(pLineDown4, pLineDown3, 10.0)
	
	pLine5 = App.SubtitleAction_Create(g_pMissionTGL, "Victory5")
	pSequence.AddAction(pLine5, pLine4, 1.0)
	pLineDown5 = App.TGScriptAction_Create(__name__, "EndAction", pLine5.GetObjID())
	pSequence.AddAction(pLineDown5, pLineDown4, 10.0)

	# Viewscreen Off.
	pSequence.AddAction(pViewOff, pLineDown5, 1.0)
	
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

	pLine4 = App.SubtitleAction_Create(g_pMissionTGL, "Loss4")
	pSequence.AddAction(pLine4, pLine3, 1.0)
	pLineDown4 = App.TGScriptAction_Create(__name__, "EndAction", pLine4.GetObjID())
	pSequence.AddAction(pLineDown4, pLineDown3, 10.0)
	
	pLine5 = App.SubtitleAction_Create(g_pMissionTGL, "Loss5")
	pSequence.AddAction(pLine5, pLine4, 1.0)
	pLineDown5 = App.TGScriptAction_Create(__name__, "EndAction", pLine5.GetObjID())
	pSequence.AddAction(pLineDown5, pLineDown4, 10.0)

	# Viewscreen Off.
	pSequence.AddAction(pViewOff, pLineDown5, 1.0)
	
	# Play the sequence.
	pEndGame = App.TGScriptAction_Create("MissionLib", "GameOver", pSequence)
	pEndGame.Play()	

################################################################################
#	ClearTimers()
#	
#	Called to delete remaining timers
#	
#	Args: None
#	
#	Return: None
################################################################################
def ClearTimers():
	# Clear the activate 1 timer, if it's still there.
	global g_idActivate1Timer
	if g_idActivate1Timer != App.NULL_ID:
		App.g_kTimerManager.DeleteTimer(g_idActivate1Timer)
		g_idActivate1Timer = App.NULL_ID	

	# Clear the activate 2 timer, if it's still there.
	global g_idActivate2Timer
	if g_idActivate2Timer != App.NULL_ID:
		App.g_kTimerManager.DeleteTimer(g_idActivate2Timer)
		g_idActivate2Timer = App.NULL_ID

	# Clear the activate 3 timer, if it's still there.
	global g_idActivate3Timer
	if g_idActivate3Timer != App.NULL_ID:
		App.g_kTimerManager.DeleteTimer(g_idActivate3Timer)
		g_idActivate3Timer = App.NULL_ID

	# Clear the activate 4 timer, if it's still there.
	global g_idActivate4Timer
	if g_idActivate4Timer != App.NULL_ID:
		App.g_kTimerManager.DeleteTimer(g_idActivate4Timer)
		g_idActivate4Timer = App.NULL_ID
		
	# Clear the activate 5 timer, if it's still there.
	global g_idActivate5Timer
	if g_idActivate5Timer != App.NULL_ID:
		App.g_kTimerManager.DeleteTimer(g_idActivate5Timer)
		g_idActivate5Timer = App.NULL_ID

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
	App.SortedRegionMenu_ClearSetCourseMenu()
	
	global g_pMissionTGL
	if g_pMissionTGL:
		App.g_kLocalizationManager.Unload(g_pMissionTGL)
		g_pMissionTGL = None

	ClearTimers()