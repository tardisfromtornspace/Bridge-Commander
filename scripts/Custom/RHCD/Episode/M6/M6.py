###############################################################################
#	Filename:	M6.py
#	
#	Confidential and Proprietary, Copyright 2002 by Totally Games
#	
#	TNG Romulan Overrun Defense Mission.
#	
#	Created:	4/26/2002	- Brian Moler (RedHotChiliDog)							  has good style :P )
###############################################################################
import App
import loadspacehelper
import MissionLib

# Mission state enumeration. This helps make it easier to keep track of where
# the user is in the mission.
MS_MISSION_START			= 0
MS_ARRIVED_VOLTAIR2			= 1
MS_MISSION_WIN				= 2
MS_MISSION_LOSE				= 3

ET_SECOND_WAVE				= App.Mission_GetNextEventType()
ET_THIRD_WAVE				= App.Mission_GetNextEventType()
ET_FOURTH_WAVE				= App.Mission_GetNextEventType()
ET_FIFTH_WAVE				= App.Mission_GetNextEventType()
ET_SIXTH_WAVE				= App.Mission_GetNextEventType()
ET_SEVENTH_WAVE				= App.Mission_GetNextEventType()
ET_EIGHTH_WAVE				= App.Mission_GetNextEventType()
ET_NINTH_WAVE				= App.Mission_GetNextEventType()
ET_TENTH_WAVE				= App.Mission_GetNextEventType()

g_eMissionState				= MS_MISSION_START
g_pMissionTGL 				= None		# string database for the mission
g_eMissionBriefingComplete		= 0		# indicates mission briefing is complete

fStartTime				= 0
g_eWavesComplete			= 0

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
	loadspacehelper.PreloadShip("Galaxy", 1)
	loadspacehelper.PreloadShip("Akira", 1)
	loadspacehelper.PreloadShip("Nebula", 1)
	loadspacehelper.PreloadShip("FedStarbase", 1)
	loadspacehelper.PreloadShip("Warbird", 30)
	
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
	g_pMissionTGL = App.g_kLocalizationManager.Load("data/TGL/RHCD/Episode/M6.tgl")

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
	# Poseidon
	import Systems.Poseidon.Poseidon
	pPoseidonMenu = Systems.Poseidon.Poseidon.CreateMenus()
	pPoseidon1Set = MissionLib.SetupSpaceSet("Systems.Poseidon.Poseidon1")
	pPoseidon2Set = MissionLib.SetupSpaceSet("Systems.Poseidon.Poseidon2")
	
	# Add our custom placement objects for this mission.
	import M6Poseidon2_P
	M6Poseidon2_P.LoadPlacements(pPoseidon2Set.GetName())

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
	pPoseidon1Set = App.g_kSetManager.GetSet("Poseidon1")

	# Create the ships that exist at mission start.
	pPlayer	= MissionLib.CreatePlayerShip("Sovereign", pPoseidon1Set, "player", "Player Start")
	
	# Setup ship affiliations.
	pFriendlies = MissionLib.GetFriendlyGroup()
	pFriendlies.AddName(pPlayer.GetName())
	pFriendlies.AddName("Galaxy")
	pFriendlies.AddName("Akira")
	pFriendlies.AddName("Nebula")
	pFriendlies.AddName("FedStarbase")
	
	pNeutrals = pMission.GetNeutralGroup()
	
	pEnemies = MissionLib.GetEnemyGroup()
	for i in range(30):
		pEnemies.AddName("Warbird " + str(i + 1))

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
	
	# Viewscreen Off.
	pSequence.AddAction(pViewOff, pLineDown4, 1.0)

	pLine5 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing5")
	pSequence.AddAction(pLine5, pLine4, 1.0)
	pLineDown5 = App.TGScriptAction_Create(__name__, "EndAction", pLine5.GetObjID())
	pSequence.AddAction(pLineDown5, pLineDown4, 10.0)

	pLine6 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing6")
	pSequence.AddAction(pLine6, pLine5, 1.0)
	pLineDown6 = App.TGScriptAction_Create(__name__, "EndAction", pLine6.GetObjID())
	pSequence.AddAction(pLineDown6, pLineDown5, 5.0)

	# Go to Red Alert status.
	pSequence.AddAction(App.TGScriptAction_Create(__name__, "GoToRedAlert"), pLineDown6, 1.0)
	
	pLine7 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing7")
	pSequence.AddAction(pLine7, pLine6, 1.0)
	pLineDown7 = App.TGScriptAction_Create(__name__, "EndAction", pLine7.GetObjID())
	pSequence.AddAction(pLineDown7, pLineDown6, 5.0)
	
	# Mission briefing complete.  This will permit the player to warp after the entire
	# initial briefing has been played out.  I had to add this, as the initial briefing sequence 
	# could still be playing well into the action of the next set, which we do not want.
	pSequence.AddAction(App.TGScriptAction_Create(__name__, "MissionBriefingComplete"), pLineDown7, 1.0)

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

	fStartTime = App.g_kUtopiaModule.GetGameTime()

	# Create a Timer that triggers the CreateSecondWave Function
	MissionLib.CreateTimer(ET_SECOND_WAVE, __name__ + ".CreateSecondWave", fStartTime + 240, 0, 0)

	# Create a Timer that triggers the CreateThirdWave Function
	MissionLib.CreateTimer(ET_THIRD_WAVE, __name__ + ".CreateThirdWave", fStartTime + 480, 0, 0)

	# Create a Timer that triggers the CreateFourthWave Function
	MissionLib.CreateTimer(ET_FOURTH_WAVE, __name__ + ".CreateFourthWave", fStartTime + 720, 0, 0)
	
	# Create a Timer that triggers the CreateFifthWave Function
	MissionLib.CreateTimer(ET_FIFTH_WAVE, __name__ + ".CreateFifthWave", fStartTime + 960, 0, 0)
	
	# Create a Timer that triggers the CreateSixthWave Function
	MissionLib.CreateTimer(ET_SIXTH_WAVE, __name__ + ".CreateSixthWave", fStartTime + 1200, 0, 0)

	# Create a Timer that triggers the CreateSeventhWave Function
	MissionLib.CreateTimer(ET_SEVENTH_WAVE, __name__ + ".CreateSeventhWave", fStartTime + 1440, 0, 0)
	
	# Create a Timer that triggers the CreateEighthWave Function
	MissionLib.CreateTimer(ET_EIGHTH_WAVE, __name__ + ".CreateEighthWave", fStartTime + 1680, 0, 0)

	# Create a Timer that triggers the CreateNinthWave Function
	MissionLib.CreateTimer(ET_NINTH_WAVE, __name__ + ".CreateNinthWave", fStartTime + 1920, 0, 0)

	# Create a Timer that triggers the CreateTenthWave Function
	MissionLib.CreateTimer(ET_TENTH_WAVE, __name__ + ".CreateTenthWave", fStartTime + 2160, 0, 0)
	
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
		pSet = pShip.GetContainingSet()
		if not pSet:
			pMission.CallNextHandler(pEvent)
			return

		# If the player is in the MS_MISSION_START state and they
		# are entering Poseidon 2, proceed to the next state of the mission.
		if (g_eMissionState == MS_MISSION_START) and (pSet.GetName() == "Poseidon2"):
			# Move to the next state in the mission.
			g_eMissionState = MS_ARRIVED_VOLTAIR2

			# Play the cutscene showing the ships warping in.
			Poseidon2Cutscene()

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
	# If the player is in Poseidon 2, check if it was the last enemy ship
	# exploding.
	pPlayer = App.Game_GetCurrentPlayer()
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	
	if (pPlayer != None) and (g_eMissionState == MS_ARRIVED_VOLTAIR2):
		pSet = pPlayer.GetContainingSet()
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		pEnemies = MissionLib.GetEnemyGroup()

		# Make sure all waves have entered game
		if (g_eWavesComplete == 0):
			pMission.CallNextHandler(pEvent)
			return
			
		# Make sure it was an enemy that was blowing up.
		if (pShip != None) and (pEnemies.IsNameInGroup(pShip.GetName()) == 0):
			pMission.CallNextHandler(pEvent)
			return
			
		for i in range(30):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "Warbird " + str(i + 1)))
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
	# If we're in Poseidon 2, and there are still enemies around, don't let the
	# player warp.
	pPlayer = App.Game_GetCurrentPlayer()
	if not pPlayer:
		pWarpButton.CallNextHandler(pEvent)
		return

	pSet = pPlayer.GetContainingSet()
	if not pSet:
		pWarpButton.CallNextHandler(pEvent)
		return
		
	# If mission briefing is not complete, then do not allow warp to Poseidon2.
	if (pSet.GetName() == "Poseidon1") and (g_eMissionBriefingComplete == 0):
		return

	if (pSet.GetName() == "Poseidon2") and (g_eMissionState == MS_ARRIVED_VOLTAIR2):
		# Check if there are still enemies in Poseidon 2. If so, then don't let
		# the player warp. Otherwise, it's OK.
		for i in range(30):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "Warbird " + str(i + 1)))
			if (pShip != None) and (not pShip.IsDying()) and (not pShip.IsDead()):
				# There's an enemy still here. The player can't warp.
				pBridge = App.g_kSetManager.GetSet("bridge")
				pSaffi = App.CharacterClass_GetObject(pBridge, "XO")
				pAction = App.CharacterAction_Create(pSaffi, 
					App.CharacterAction.AT_SAY_LINE, "WarpStop2", "Captain", 1, pSaffi.GetDatabase())
				pAction.Play()
				return


	pWarpButton.CallNextHandler(pEvent)

###############################################################################
#	Poseidon2Cutscene()
#	
#	Creates the sequence for when the player first enters Poseidon 2. Shows
#	three Warbirds warping in to attack the player.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def Poseidon2Cutscene():
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")

	# Create the Warbirds, and have them warp in. The extra parameter at the end
	# indicates that they should warp in (from nowhere). We won't assign their
	# AI just yet, because having them attack the player during the cutscene
	# would be unfair.
	pWarbird1 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 1", "Warbird 1 Start", 1)
	pWarbird2 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 2", "Warbird 2 Start", 1)
	pWarbird3 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 3", "Warbird 3 Start", 1)

	# Create the Federation Starbase.
	pStarbase = loadspacehelper.CreateShip("FedStarbase", pPoseidon2Set, "FedStarbase", "Starbase Start")
	
	# Create the player's fleet.
	pGalaxy	= loadspacehelper.CreateShip("Galaxy", pPoseidon2Set, "Galaxy", "Galaxy Start")
	pAkira	= loadspacehelper.CreateShip("Akira", pPoseidon2Set, "Akira", "Akira Start")
	pNebula	= loadspacehelper.CreateShip("Nebula", pPoseidon2Set, "Nebula", "Nebula Start")

	# Make player fleet commandable.
	MissionLib.AddCommandableShip("Galaxy")
	MissionLib.AddCommandableShip("Akira")
	MissionLib.AddCommandableShip("Nebula")
	
	pSeq = App.TGSequence_Create()

	# Start the cutscene.
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
	# Create a cutscene camera for Poseidon 2.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", "Poseidon2"))
	# Make the cutscene camera watch the Warbirds warping in.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "PlacementWatch", "Poseidon2", 
					  "Warbird 3 Start", "Cutscene Camera Placement"))
	# Change us so we're rendering Poseidon 2 instead of whatever else.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "Poseidon2"))
	# Have Felix announce the incoming enemies.
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))

	# Kill the cutscene camera.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", "Poseidon2"), 4.0)
	# Move back to the bridge.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
	# End the cutscene.
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
	# Assign the AIs for the Warbirds.
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AssignWarbirdAI"))
	# Assign the AIs for the player's friends.
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AssignFriendAI"))
	# Assign the AIs for the player's starbase.
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AssignStarbaseAI"))
	
	# Add Objectives.  This will initiate timers for additional waves of enemy ships.
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AddObjectives"))

	pSeq.Play()

###############################################################################
#	AssignWarbirdAI(pAction)
#	
#	Script action that assigns the attack AI for the Enemies that warp into
#	Poseidon 2.
#	
#	Args:	pAction		- this action
#	
#	Return:	zero, to indicate normal action termination
###############################################################################
def AssignWarbirdAI(pAction):
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")
	pWarbird1 = App.ShipClass_GetObject(pPoseidon2Set, "Warbird 1")
	pWarbird2 = App.ShipClass_GetObject(pPoseidon2Set, "Warbird 2")
	pWarbird3 = App.ShipClass_GetObject(pPoseidon2Set, "Warbird 3")

	import WarbirdAI
	pWarbird1.SetAI(WarbirdAI.CreateAI(pWarbird1))
	pWarbird2.SetAI(WarbirdAI.CreateAI(pWarbird2))
	pWarbird3.SetAI(WarbirdAI.CreateAI(pWarbird3))
	
	return 0

###############################################################################
#	AssignFriendAI(pAction)
#	
#	Script action that assigns the attack AI for the player's wingmen
#	
#	Args:	pAction		- this action
#	
#	Return:	zero, to indicate normal action termination
###############################################################################
def AssignFriendAI(pAction):
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")
	pGalaxy = App.ShipClass_GetObject(pPoseidon2Set, "Galaxy")
	pAkira = App.ShipClass_GetObject(pPoseidon2Set, "Akira")
	pNebula = App.ShipClass_GetObject(pPoseidon2Set, "Nebula")

	import FriendAI
	pGalaxy.SetAI(FriendAI.CreateAI(pGalaxy))
	pAkira.SetAI(FriendAI.CreateAI(pAkira))
	pNebula.SetAI(FriendAI.CreateAI(pNebula))
	
	return 0

###############################################################################
#	AssignStarbaseAI(pAction)
#	
#	Script action that assigns the attack AI for the player's Starbase
#	
#	Args:	pAction		- this action
#	
#	Return:	zero, to indicate normal action termination
###############################################################################
def AssignStarbaseAI(pAction):
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")
	pFedStarbase = App.ShipClass_GetObject(pPoseidon2Set, "FedStarbase")

	import StarbaseAI
	pFedStarbase.SetAI(StarbaseAI.CreateAI(pFedStarbase))
	
	return 0
	
###############################################################################
#	CreateSecondWave()
#
#	Create the second wave of Warbirds
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def CreateSecondWave(pObject, pEvent):

	# Have Felix announce the incoming enemies.
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")
	pSeq = App.TGSequence_Create()	
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))
	pSeq.Play()
	
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")
	
	# Create ships
	pWarbird4 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 4", "Warbird 4 Start", 1)
	pWarbird5 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 5", "Warbird 5 Start", 1)
	pWarbird6 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 6", "Warbird 6 Start", 1)	

	# Assign AI
	import WarbirdAI
	pWarbird4.SetAI(WarbirdAI.CreateAI(pWarbird4))
	pWarbird5.SetAI(WarbirdAI.CreateAI(pWarbird5))
	pWarbird6.SetAI(WarbirdAI.CreateAI(pWarbird6))

###############################################################################
#	CreateThirdWave()
#
#	Create the third wave of Warbirds
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def CreateThirdWave(pObject, pEvent):

	# Have Felix announce the incoming enemies.
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")	
	pSeq = App.TGSequence_Create()	
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))
	pSeq.Play()
	
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")	
	
	# Create ships
	pWarbird7 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 7", "Warbird 7 Start", 1)
	pWarbird8 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 8", "Warbird 8 Start", 1)
	pWarbird9 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 9", "Warbird 9 Start", 1)	

	# Assign AI
	import WarbirdAI
	pWarbird7.SetAI(WarbirdAI.CreateAI(pWarbird7))
	pWarbird8.SetAI(WarbirdAI.CreateAI(pWarbird8))
	pWarbird9.SetAI(WarbirdAI.CreateAI(pWarbird9))

###############################################################################
#	CreateFourthWave()
#
#	Create the fourth wave of Warbirds
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def CreateFourthWave(pObject, pEvent):

	# Have Felix announce the incoming enemies.
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")	
	pSeq = App.TGSequence_Create()	
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))
	pSeq.Play()
	
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")	
	
	# Create ships
	pWarbird10 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 10", "Warbird 10 Start", 1)
	pWarbird11 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 11", "Warbird 11 Start", 1)
	pWarbird12 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 12", "Warbird 12 Start", 1)	

	# Assign AI
	import WarbirdAI
	pWarbird10.SetAI(WarbirdAI.CreateAI(pWarbird10))
	pWarbird11.SetAI(WarbirdAI.CreateAI(pWarbird11))
	pWarbird12.SetAI(WarbirdAI.CreateAI(pWarbird12))

###############################################################################
#	CreateFifthWave()
#
#	Create the fifth wave of Warbirds
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def CreateFifthWave(pObject, pEvent):

	# Have Felix announce the incoming enemies.
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")	
	pSeq = App.TGSequence_Create()	
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))
	pSeq.Play()
	
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")	
	
	# Create ships
	pWarbird13 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 13", "Warbird 13 Start", 1)
	pWarbird14 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 14", "Warbird 14 Start", 1)
	pWarbird15 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 15", "Warbird 15 Start", 1)	

	# Assign AI
	import WarbirdAI
	pWarbird13.SetAI(WarbirdAI.CreateAI(pWarbird13))
	pWarbird14.SetAI(WarbirdAI.CreateAI(pWarbird14))
	pWarbird15.SetAI(WarbirdAI.CreateAI(pWarbird15))

###############################################################################
#	CreateSixthWave()
#
#	Create the sixth wave of Warbirds
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def CreateSixthWave(pObject, pEvent):

	# Have Felix announce the incoming enemies.
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")	
	pSeq = App.TGSequence_Create()	
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))
	pSeq.Play()
	
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")	
	
	# Create ships
	pWarbird16 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 16", "Warbird 16 Start", 1)
	pWarbird17 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 17", "Warbird 17 Start", 1)
	pWarbird18 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 18", "Warbird 18 Start", 1)	

	# Assign AI
	import WarbirdAI
	pWarbird16.SetAI(WarbirdAI.CreateAI(pWarbird16))
	pWarbird17.SetAI(WarbirdAI.CreateAI(pWarbird17))
	pWarbird18.SetAI(WarbirdAI.CreateAI(pWarbird18))

###############################################################################
#	CreateSeventhWave()
#
#	Create the seventh wave of Warbirds
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def CreateSeventhWave(pObject, pEvent):

	# Have Felix announce the incoming enemies.
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")	
	pSeq = App.TGSequence_Create()	
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))
	pSeq.Play()
	
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")	
	
	# Create ships
	pWarbird19 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 19", "Warbird 19 Start", 1)
	pWarbird20 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 20", "Warbird 20 Start", 1)
	pWarbird21 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 21", "Warbird 21 Start", 1)	

	# Assign AI
	import WarbirdAI
	pWarbird19.SetAI(WarbirdAI.CreateAI(pWarbird19))
	pWarbird20.SetAI(WarbirdAI.CreateAI(pWarbird20))
	pWarbird21.SetAI(WarbirdAI.CreateAI(pWarbird21))

###############################################################################
#	CreateEighthWave()
#
#	Create the eighth wave of Warbirds
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def CreateEighthWave(pObject, pEvent):

	# Have Felix announce the incoming enemies.
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")	
	pSeq = App.TGSequence_Create()	
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))
	pSeq.Play()
	
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")	
	
	# Create ships
	pWarbird22 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 22", "Warbird 22 Start", 1)
	pWarbird23 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 23", "Warbird 23 Start", 1)
	pWarbird24 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 24", "Warbird 24 Start", 1)	

	# Assign AI
	import WarbirdAI
	pWarbird22.SetAI(WarbirdAI.CreateAI(pWarbird22))
	pWarbird23.SetAI(WarbirdAI.CreateAI(pWarbird23))
	pWarbird24.SetAI(WarbirdAI.CreateAI(pWarbird24))

###############################################################################
#	CreateNinthWave()
#
#	Create the ninth wave of Warbirds
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def CreateNinthWave(pObject, pEvent):

	# Have Felix announce the incoming enemies.
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")	
	pSeq = App.TGSequence_Create()	
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))
	pSeq.Play()
	
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")	
	
	# Create ships
	pWarbird25 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 25", "Warbird 25 Start", 1)
	pWarbird26 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 26", "Warbird 26 Start", 1)
	pWarbird27 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 27", "Warbird 27 Start", 1)	

	# Assign AI
	import WarbirdAI
	pWarbird25.SetAI(WarbirdAI.CreateAI(pWarbird25))
	pWarbird26.SetAI(WarbirdAI.CreateAI(pWarbird26))
	pWarbird27.SetAI(WarbirdAI.CreateAI(pWarbird27))

###############################################################################
#	CreateTenthWave()
#
#	Create the tenth wave of Warbirds
#
#	Args:	pObject	- TGObject object
#		pEvent	- TGEvent object
#
#	Return:	none
###############################################################################
def CreateTenthWave(pObject, pEvent):

	# Have Felix announce the incoming enemies.
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")	
	pSeq = App.TGSequence_Create()	
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))
	pSeq.Play()
	
	pPoseidon2Set = App.g_kSetManager.GetSet("Poseidon2")	
	
	# Create ships
	pWarbird28 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 28", "Warbird 28 Start", 1)
	pWarbird29 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 29", "Warbird 29 Start", 1)
	pWarbird30 = loadspacehelper.CreateShip("Warbird", pPoseidon2Set, "Warbird 30", "Warbird 30 Start", 1)	

	# Assign AI
	import WarbirdAI
	pWarbird28.SetAI(WarbirdAI.CreateAI(pWarbird28))
	pWarbird29.SetAI(WarbirdAI.CreateAI(pWarbird29))
	pWarbird30.SetAI(WarbirdAI.CreateAI(pWarbird30))

	global g_eWavesComplete
	g_eWavesComplete = 1
	
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
