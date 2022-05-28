###############################################################################
#	Filename:	RomBrex.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads RomBrex, the Engineer, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import Bridge.BridgeUtils
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create RomBrex by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating RomBrex")

	if (pSet.GetObject("Engineer") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Engineer")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "B5/HeadBrex/brex_head_no_mouth.NIF", None)
	pRomBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.NIF", CharacterPaths.g_pcHeadNIFPath + "B5/HeadBrex/brex_head_no_mouth.NIF")
	pRomBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "B5/BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "B5/HeadBrex/brex_head.tga")

	pRomBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pRomBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRomBrex)

	# Setup the character configuration
	pRomBrex.SetSize(App.CharacterClass.SMALL)
	pRomBrex.SetGender(App.CharacterClass.MALE)
	pRomBrex.SetRandomAnimationChance(.75)
	pRomBrex.SetBlinkChance(0.1)

	pRomBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pRomBrex.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "B5/HeadBrex/brex_blink1.tga")
	pRomBrex.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "B5/HeadBrex/brex_blink2.tga")
	pRomBrex.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "B5/HeadBrex/brex_eyes_close.tga")
	pRomBrex.SetBlinkStages(3)

	pRomBrex.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "B5/HeadBrex/brex_head_a.tga")
	pRomBrex.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "B5/HeadBrex/brex_head_e.tga")
	pRomBrex.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "B5/HeadBrex/brex_head_u.tga")
	pRomBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pRomBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRomBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pRomBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pRomBrex.SetLocation("")

#	kDebugObj.Print("Finished creating RomBrex")
	return pRomBrex


###############################################################################
#	ConfigureForShip()
#
#	Configure ourselves for the particular ship object.  This involves setting
#	up range watchers that tell us how to report.
#
#	Args:	pSet	- the Set object
#			pShip	- the player's ship (ShipClass object)
#
#	Return:	none
###############################################################################
def ConfigureForShip(pSet, pShip):
	pRomBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pRomBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pRomBrex)

	# Set up the status events that we need - Shield and Hull
	# Other events (repairs, subsystem reports) are generated elsewhere
	pShieldWatcher = pShip.GetShields().GetShieldWatcher(6)
	pHullWatcher = pShip.GetHull().GetCombinedPercentageWatcher()

	lWatchers = (
		( pShieldWatcher,	App.ET_TACTICAL_SHIELD_LEVEL_CHANGE ),
		( pHullWatcher,		App.ET_TACTICAL_HULL_LEVEL_CHANGE ) )

	lRanges = ( 0.05, 0.1, 0.15, 0.2, 0.25, 0.5, 0.75 )

	for pWatcher, eEventType in lWatchers:
		for fRange in lRanges:
			# Need an event for this range check..
			pEvent = App.TGFloatEvent_Create()
			pEvent.SetEventType(eEventType)
			pEvent.SetDestination(pShip)

			pWatcher.AddRangeCheck(fRange, App.FloatRangeWatcher.FRW_BELOW, pEvent)

	lWatchers = (
		( pShip.GetShields().GetShieldWatcher(0), App.ET_TACTICAL_SHIELD_0_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(1), App.ET_TACTICAL_SHIELD_1_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(2), App.ET_TACTICAL_SHIELD_2_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(3), App.ET_TACTICAL_SHIELD_3_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(4), App.ET_TACTICAL_SHIELD_4_LEVEL_CHANGE ),
		( pShip.GetShields().GetShieldWatcher(5), App.ET_TACTICAL_SHIELD_5_LEVEL_CHANGE ) )

	lRanges = ( 0.05, 0.5)

	for pWatcher, eEventType in lWatchers:
		for fRange in lRanges:
			# Need an event for this range check..
			pEvent = App.TGFloatEvent_Create()
			pEvent.SetEventType(eEventType)
			pEvent.SetDestination(pShip)

			pWatcher.AddRangeCheck(fRange, App.FloatRangeWatcher.FRW_BELOW, pEvent)


###############################################################################
#	ConfigureForWarbird()
#
#	Configure ourselves for the Warbird bridge
#
#	Args:	pRomBrex	- our Character object
#
#	Return:	none
###############################################################################

def ConfigureForWarbird(pRomBrex):
#	kDebugObj.Print("Configuring RomBrex for the Romulan bridge")

	# Clear out any old animations from another configuration
	pRomBrex.ClearAnimations()

	# Register animation mappings
	pRomBrex.AddAnimation("StandingWarbirdEngineer", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomBrex.AddAnimation("DBL1SToE", "Bridge.Characters.Brex.MoveFromL1ToE")
	pRomBrex.AddAnimation("WarbirdEngSeatedToE", "Bridge.Characters.Brex.MoveFromL1ToE")
	pRomBrex.AddAnimation("DBEngineerToL1", "Bridge.Characters.Brex.MoveFromEToL1")
	pRomBrex.AddAnimation("DBEngineerTurnCaptain", "Bridge.Characters.SmallAnimations.TurnAtETowardsCaptain")
	pRomBrex.AddAnimation("DBEngineerBackCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomBrex.AddAnimation("RomEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pRomBrex.AddAnimation("RomEngineerGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")

	pRomBrex.AddAnimation("DBEngineerTurnC", "Bridge.Characters.SmallAnimations.DBETalkC")
	pRomBrex.AddAnimation("DBEngineerBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomBrex.AddAnimation("DBEngineerTurnH", "Bridge.Characters.SmallAnimations.DBETalkH")
	pRomBrex.AddAnimation("DBEngineerBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomBrex.AddAnimation("DBEngineerTurnS", "Bridge.Characters.SmallAnimations.DBETalkS")
	pRomBrex.AddAnimation("DBEngineerBackS", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomBrex.AddAnimation("DBEngineerTurnT", "Bridge.Characters.SmallAnimations.DBETalkT")
	pRomBrex.AddAnimation("DBEngineerBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pRomBrex.AddAnimation("DBEngineerTurnX", "Bridge.Characters.SmallAnimations.DBETalkX")
	pRomBrex.AddAnimation("DBEngineerBackX", "Bridge.Characters.CommonAnimations.StandingConsole")

	# Breathing	
	pRomBrex.AddAnimation("DBEngineerBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomBrex.AddAnimation("DBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pRomBrex.AddRandomAnimation("Bridge.Characters.SmallAnimations.DBEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pRomBrex.AddAnimation("PushingButtons", "Bridge.Characters.SmallAnimations.DBEConsoleInteraction")

	# Hit animations
	pRomBrex.AddAnimation("DBEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pRomBrex.AddAnimation("DBEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pRomBrex.AddAnimation("DBEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pRomBrex.AddAnimation("DBEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pRomBrex)

	# Brex stands on the Warbird bridge
	pRomBrex.SetStanding(1)
	pRomBrex.SetLocation("RomEngineer")
#	kDebugObj.Print("Finished configuring Brex")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pRomBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pRomBrex):
	pRomBrex.AddRandomAnimation("Bridge.Characters.SmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pRomBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pRomBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pRomBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRomBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRomBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pRomBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pRomBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


###############################################################################
#	LoadSounds()
#
#	Load generic bridge sounds for this character
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")

	#
	# Build a list of sound to load
	#
	kSoundList =	[	"BrexSir1",		# Click Response
						"BrexSir2",
						"BrexSir3",
						"BrexSir4",
						"BrexSir5",

						"BrexYes1",		# Order Confirmation
						"BrexYes2",
						"BrexYes3",
						"BrexYes4",

						"BrexTransfer",	# Transferring Power
						"MainPowerDraining",

						"FrontShieldDraining",
						"FrontShieldFailed",
						"RearShieldDraining",
						"RearShieldFailed",
						"TopShieldDraining",
						"TopShieldFailed",
						"BottomShieldDraining",
						"BottomShieldFailed",
						"LeftShieldDraining",
						"LeftShieldFailed",
						"RightShieldDraining",
						"RightShieldFailed",
						"PhasersDisabled",
						"PhasersDestroyed",
						"ShieldsDisabled",
						"ShieldsDestroyed",
						"SensorsDisabled",
						"SensorsDestroyed",
						"TorpedoesDisabled",
						"TorpedoesDestroyed",
						"TractorDisabled",
						"TractorDestroyed",
						"ImpulseDisabled",
						"ImpulseDestroyed",
						"WarpDisabled",
						"WarpDestroyed",
						"PowerDisabled",
						"OutOfTorpedoes",
						"Hull05",
						"Hull10",
						"Hull15",
						"Hull20",
						"Hull25",
						"Hull50",
						"Hull75",
						"MultipleShieldsOffline",
						"Shields05",
						"Shields10",
						"Shields15",
						"Shields20",
						"Shields25",
						"Shields50",
						"Shields75",
						"ShieldsFailed"
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for i in range(len(kSoundList)):
		pGame.LoadDatabaseSoundInGroup(pDatabase, kSoundList[i], "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)

###############################################################################
#	MoveFromEToL1 & MoveFromL1ToE
#	
#	Functions that turn the "Contact Engineering" button on and off
#	
#	Args:	self		- the character that called these
#	
#	Return:	pSequence	- returned by the real functions
###############################################################################
def MoveFromEToL1(self):
	import Bridge.Characters.SmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.SmallAnimations.MoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 15.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "GalaxyEngSeated"))
	return pSequence

def MoveToEngineeringSet(pAction):
#	kDebugObj.Print("Moving RomBrex to the Engineering set")

	pBridge = App.g_kSetManager.GetSet("bridge")
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet()
	pRomBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pRomBrex
	bSuccess = pEngineering.AddObjectToSet(pRomBrex, "Engineer")
	assert bSuccess

#	kDebugObj.Print("Done in MoveToEngineeringSet()")

	return 0

def EnableContactEngineeringButton(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(1)

	return 0
	
def MoveFromL1ToE(self):
	import Bridge.Characters.SmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.SmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.SmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pRomBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pRomBrex
	bSuccess = pBridge.AddObjectToSet(pRomBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	import Bridge.Characters.SmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.SmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	import Bridge.Characters.SmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.SmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.SmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pRomBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pRomBrex
	bSuccess = pBridge.AddObjectToSet(pRomBrex, "Engineer")
	assert bSuccess

	return 0
