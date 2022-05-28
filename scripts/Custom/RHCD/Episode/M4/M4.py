###############################################################################
#	Filename:	M4.py
#	
#	Confidential and Proprietary, Copyright 2002 by Totally Games
#	
#	TNG Cardayashi Maru Mission.
#	
#	Created:	4/10/2002	- Brian Moler (RedHotChiliDog)							  has good style :P )
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
	# Pre-create one Sovereign, Freighter, and nine Keldons.
	loadspacehelper.PreloadShip("Sovereign", 1)
	loadspacehelper.PreloadShip("Keldon", 9)
	loadspacehelper.PreloadShip("Freighter", 1)
	
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
	g_pMissionTGL = App.g_kLocalizationManager.Load("data/TGL/RHCD/Episode/M4.tgl")

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
	# Voltair
	import Systems.Voltair.Voltair
	pVoltairMenu = Systems.Voltair.Voltair.CreateMenus()
	pVoltair1Set = MissionLib.SetupSpaceSet("Systems.Voltair.Voltair1")
	pVoltair2Set = MissionLib.SetupSpaceSet("Systems.Voltair.Voltair2")
	
	# Add our custom placement objects for this mission.
	import M4Voltair2_P
	M4Voltair2_P.LoadPlacements(pVoltair2Set.GetName())

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
	pVoltair1Set = App.g_kSetManager.GetSet("Voltair1")
	
	# Create the ships that exist at mission start.
	pPlayer	= MissionLib.CreatePlayerShip("Sovereign", pVoltair1Set, "player", "Player Start")
	
	# Setup ship affiliations.
	pFriendlies = MissionLib.GetFriendlyGroup()
	pFriendlies.AddName(pPlayer.GetName())
	pFriendlies.AddName("Kobayashi Maru")
	
	pNeutrals = pMission.GetNeutralGroup()
	
	pEnemies = MissionLib.GetEnemyGroup()
	for i in range(9):
		pEnemies.AddName("Keldon " + str(i + 1))

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
	pSequence = App.TGSequence_Create()

	pLine1 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing1")
	pSequence.AddAction(pLine1)
	pLineDown1 = App.TGScriptAction_Create(__name__, "EndAction", pLine1.GetObjID())
	pSequence.AddAction(pLineDown1, App.TGAction_CreateNull(), 15.0)

	pLine2 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing2")
	pSequence.AddAction(pLine2, pLine1, 1.0)
	pLineDown2 = App.TGScriptAction_Create(__name__, "EndAction", pLine2.GetObjID())
	pSequence.AddAction(pLineDown2, pLineDown1, 5.0)

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

	pLine7 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing7")
	pSequence.AddAction(pLine7, pLine6, 1.0)
	pLineDown7 = App.TGScriptAction_Create(__name__, "EndAction", pLine7.GetObjID())
	pSequence.AddAction(pLineDown7, pLineDown6, 5.0)
	
	pLine8 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing8")
	pSequence.AddAction(pLine8, pLine7, 1.0)
	pLineDown8 = App.TGScriptAction_Create(__name__, "EndAction", pLine8.GetObjID())
	pSequence.AddAction(pLineDown8, pLineDown7, 10.0)
	
	pLine9 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing9")
	pSequence.AddAction(pLine9, pLine8, 1.0)
	pLineDown9 = App.TGScriptAction_Create(__name__, "EndAction", pLine9.GetObjID())
	pSequence.AddAction(pLineDown9, pLineDown8, 5.0)
	
	pLine10 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing10")
	pSequence.AddAction(pLine10, pLine9, 1.0)
	pLineDown10 = App.TGScriptAction_Create(__name__, "EndAction", pLine10.GetObjID())
	pSequence.AddAction(pLineDown10, pLineDown9, 10.0)
	
	pLine11 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing11")
	pSequence.AddAction(pLine11, pLine10, 1.0)
	pLineDown11 = App.TGScriptAction_Create(__name__, "EndAction", pLine11.GetObjID())
	pSequence.AddAction(pLineDown11, pLineDown10, 5.0)

	# Go to Red Alert status.
	pSequence.AddAction(App.TGScriptAction_Create(__name__, "GoToRedAlert"), pLineDown11, 1.0)
	
	pLine12 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing12")
	pSequence.AddAction(pLine12, pLine11, 1.0)
	pLineDown12 = App.TGScriptAction_Create(__name__, "EndAction", pLine12.GetObjID())
	pSequence.AddAction(pLineDown12, pLineDown11, 5.0)
	
	pLine13 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing13")
	pSequence.AddAction(pLine13, pLine12, 1.0)
	pLineDown13 = App.TGScriptAction_Create(__name__, "EndAction", pLine13.GetObjID())
	pSequence.AddAction(pLineDown13, pLineDown12, 5.0)
	
	pLine14 = App.SubtitleAction_Create(g_pMissionTGL, "Briefing14")
	pSequence.AddAction(pLine14, pLine13, 1.0)
	pLineDown14 = App.TGScriptAction_Create(__name__, "EndAction", pLine14.GetObjID())
	pSequence.AddAction(pLineDown14, pLineDown13, 5.0)
	
	# Mission briefing complete.  This will permit the player to warp after the entire
	# initial briefing has been played out.  I had to add this, as the initial briefing sequence 
	# could still be playing well into the action of the next set, which we do not want.
	pSequence.AddAction(App.TGScriptAction_Create(__name__, "MissionBriefingComplete"), pLineDown14, 1.0)

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
	MissionLib.CreateTimer(ET_SECOND_WAVE, __name__ + ".CreateSecondWave", fStartTime + 90, 0, 0)

	# Create a Timer that triggers the CreateThirdWave Function
	MissionLib.CreateTimer(ET_THIRD_WAVE, __name__ + ".CreateThirdWave", fStartTime + 180, 0, 0)
	
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
		# are entering Voltair 2, proceed to the next state of the mission.
		if (g_eMissionState == MS_MISSION_START) and (pSet.GetName() == "Voltair2"):
			# Move to the next state in the mission.
			g_eMissionState = MS_ARRIVED_VOLTAIR2

			# Play the cutscene showing the ships warping in.
			Voltair2Cutscene()

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
	# If the player is in Voltair 2, check if it was the last enemy ship
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
			
		for i in range(9):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "Keldon " + str(i + 1)))
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
	# If we're in Voltair 2, and there are still enemies around, don't let the
	# player warp.
	pPlayer = App.Game_GetCurrentPlayer()
	if not pPlayer:
		pWarpButton.CallNextHandler(pEvent)
		return

	pSet = pPlayer.GetContainingSet()
	if not pSet:
		pWarpButton.CallNextHandler(pEvent)
		return
		
	# If mission briefing is not complete, then do not allow warp to Voltair2.
	if (pSet.GetName() == "Voltair1") and (g_eMissionBriefingComplete == 0):
		return

	if (pSet.GetName() == "Voltair2") and (g_eMissionState == MS_ARRIVED_VOLTAIR2):
		# Check if there are still enemies in Voltair 2. If so, then don't let
		# the player warp. Otherwise, it's OK.
		for i in range(9):
			pShip = App.ShipClass_Cast(App.ShipClass_GetObject(pSet, "Keldon " + str(i + 1)))
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
#	Voltair2Cutscene()
#	
#	Creates the sequence for when the player first enters Voltair 2. Shows
#	three Keldons warping in to attack the player.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def Voltair2Cutscene():
	pVoltair2Set = App.g_kSetManager.GetSet("Voltair2")
	pBridge = App.g_kSetManager.GetSet("bridge")
	pFelix = App.CharacterClass_GetObject(pBridge, "Tactical")

	# Create the Keldons, and have them warp in. The extra parameter at the end
	# indicates that they should warp in (from nowhere). We won't assign their
	# AI just yet, because having them attack the player during the cutscene
	# would be unfair.
	pKeldon1 = loadspacehelper.CreateShip("Keldon", pVoltair2Set, "Keldon 1", "Keldon 1 Start", 1)
	pKeldon2 = loadspacehelper.CreateShip("Keldon", pVoltair2Set, "Keldon 2", "Keldon 2 Start", 1)
	pKeldon3 = loadspacehelper.CreateShip("Keldon", pVoltair2Set, "Keldon 3", "Keldon 3 Start", 1)

	# Create the damaged freighter Kobayashi Maru
	pFreighter = loadspacehelper.CreateShip("Freighter", pVoltair2Set, "Kobayashi Maru", "Freighter Start")
	MissionLib.DamageShip("Kobayashi Maru", 0.6, 0.9)
	import FreighterDamage
	FreighterDamage.AddDamage(pFreighter)
	
	pSeq = App.TGSequence_Create()

	# Start the cutscene.
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
	# Create a cutscene camera for Voltair 2.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", "Voltair2"))
	# Make the cutscene camera watch the Keldons warping in.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "PlacementWatch", "Voltair2", 
					  "Keldon 3 Start", "Cutscene Camera Placement"))
	# Change us so we're rendering Voltair 2 instead of whatever else.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "Voltair2"))
	# Have Felix announce the incoming enemies.
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "Incoming3", None, 0, pFelix.GetDatabase()))
	pSeq.AppendAction(App.CharacterAction_Create(pFelix, App.CharacterAction.AT_SAY_LINE, "gt031", None, 0, pFelix.GetDatabase()))

	# Kill the cutscene camera.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", "Voltair2"), 4.0)
	# Move back to the bridge.
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
	# End the cutscene.
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
	# Assign the AIs for the Keldons.
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AssignKeldonAI"))
	
	# Add Objectives.  This will initiate timers for additional waves of enemy ships.
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AddObjectives"))

	pSeq.Play()

###############################################################################
#	AssignKeldonAI(pAction)
#	
#	Script action that assigns the attack AI for the Keldons that warp into
#	Voltair 2.
#	
#	Args:	pAction		- this action
#	
#	Return:	zero, to indicate normal action termination
###############################################################################
def AssignKeldonAI(pAction):
	pVoltair2Set = App.g_kSetManager.GetSet("Voltair2")
	pKeldon1 = App.ShipClass_GetObject(pVoltair2Set, "Keldon 1")
	pKeldon2 = App.ShipClass_GetObject(pVoltair2Set, "Keldon 2")
	pKeldon3 = App.ShipClass_GetObject(pVoltair2Set, "Keldon 3")

	import KeldonAI
	pKeldon1.SetAI(KeldonAI.CreateAI(pKeldon1))
	pKeldon2.SetAI(KeldonAI.CreateAI(pKeldon2))
	pKeldon3.SetAI(KeldonAI.CreateAI(pKeldon3))
	
	return 0

###############################################################################
#	CreateSecondWave()
#
#	Create the second wave of Keldons
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
	
	pVoltair2Set = App.g_kSetManager.GetSet("Voltair2")
	
	# Create ships
	pKeldon4 = loadspacehelper.CreateShip("Keldon", pVoltair2Set, "Keldon 4", "Keldon 4 Start", 1)
	pKeldon5 = loadspacehelper.CreateShip("Keldon", pVoltair2Set, "Keldon 5", "Keldon 5 Start", 1)
	pKeldon6 = loadspacehelper.CreateShip("Keldon", pVoltair2Set, "Keldon 6", "Keldon 6 Start", 1)	

	# Assign AI
	import KeldonAI
	pKeldon4.SetAI(KeldonAI.CreateAI(pKeldon4))
	pKeldon5.SetAI(KeldonAI.CreateAI(pKeldon5))
	pKeldon6.SetAI(KeldonAI.CreateAI(pKeldon6))

###############################################################################
#	CreateThirdWave()
#
#	Create the third wave of Keldons
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
	
	pVoltair2Set = App.g_kSetManager.GetSet("Voltair2")	
	
	# Create ships
	pKeldon7 = loadspacehelper.CreateShip("Keldon", pVoltair2Set, "Keldon 7", "Keldon 7 Start", 1)
	pKeldon8 = loadspacehelper.CreateShip("Keldon", pVoltair2Set, "Keldon 8", "Keldon 8 Start", 1)
	pKeldon9 = loadspacehelper.CreateShip("Keldon", pVoltair2Set, "Keldon 9", "Keldon 9 Start", 1)	

	# Assign AI
	import KeldonAI
	pKeldon7.SetAI(KeldonAI.CreateAI(pKeldon7))
	pKeldon8.SetAI(KeldonAI.CreateAI(pKeldon8))
	pKeldon9.SetAI(KeldonAI.CreateAI(pKeldon9))

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
