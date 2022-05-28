from bcdebug import debug
###############################################################################
#	Filename:	Brex.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Brex, the Engineer, and configures animations.
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
#	Create Brex by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating Brex")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("Engineer") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Engineer")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif", None)
	pEXLBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pEXLBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Brex/brex_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/brex_head.tga")

	pEXLBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLBrex)

	# Setup the character configuration
	pEXLBrex.SetSize(App.CharacterClass.SMALL)
	pEXLBrex.SetGender(App.CharacterClass.MALE)
	pEXLBrex.SetRandomAnimationChance(.75)
	pEXLBrex.SetBlinkChance(0.1)

	pEXLBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pEXLBrex.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink1.tga")
	pEXLBrex.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink2.tga")
	pEXLBrex.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_eyes_close.tga")
	pEXLBrex.SetBlinkStages(3)

	pEXLBrex.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_a.tga")
	pEXLBrex.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_e.tga")
	pEXLBrex.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_u.tga")
	pEXLBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pEXLBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pEXLBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pEXLBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pEXLBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pEXLBrex


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
	debug(__name__ + ", ConfigureForShip")
	pEXLBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pEXLBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pEXLBrex)

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
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pEXLBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pEXLBrex):
#	kDebugObj.Print("Configuring Brex for the Excelsior bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcelsior")
	pEXLBrex.ClearAnimations()

	# Register animation mappings
	pEXLBrex.AddAnimation("SeatedEXLEngineer", "Bridge.Characters.CommonAnimations.StandingConsole")
	pEXLBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pEXLBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pEXLBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pEXLBrex.AddAnimation("EXLEngineerTurnCaptain", "Bridge.Characters.EXLSmallAnimations.EXLTurnAtETowardsCaptain")
	pEXLBrex.AddAnimation("EXLEngineerBackCaptain", "Bridge.Characters.EXLSmallAnimations.EXLTurnBackAtEFromCaptain")
	pEXLBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.EXLSmallAnimations.EBMoveFromE1ToE")
	pEXLBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.EXLSmallAnimations.EBMoveFromEToE1")
	pEXLBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.EXLSmallAnimations.EBMoveFromE2ToE")
	pEXLBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.EXLSmallAnimations.EBMoveFromEToE2")
	pEXLBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.EXLSmallAnimations.EBMoveFromE1ToE2")
	pEXLBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.EXLSmallAnimations.EBMoveFromE2ToE1")

	pEXLBrex.AddAnimation("EXLEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pEXLBrex.AddAnimation("EXLEngineerGlanceAwayCaptain", "Bridge.Characters.EXLSmallAnimations.EXLEConsoleInteraction")

	pEXLBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.EXLSmallAnimations.EBETalkC")
	pEXLBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pEXLBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.EXLSmallAnimations.EBETalkH")
	pEXLBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pEXLBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.EXLSmallAnimations.EBETalkS")
	pEXLBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.StandingConsole")
	pEXLBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.EXLSmallAnimations.EBETalkT")
	pEXLBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pEXLBrex.AddAnimation("EXLEngineerTurnX", "Bridge.Characters.EXLSmallAnimations.EXLTurnAtETowardsCaptain")
	pEXLBrex.AddAnimation("EXLEngineerBackX", "Bridge.Characters.EXLSmallAnimations.EXLTurnBackAtEFromCaptain")

	# Breathing
	pEXLBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pEXLBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pEXLBrex.AddRandomAnimation("Bridge.Characters.EXLSmallAnimations.EXLEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pEXLBrex.AddAnimation("PushingButtons", "Bridge.Characters.EXLSmallAnimations.EXLEConsoleInteraction")

	# Hit animations
	pEXLBrex.AddAnimation("EXLEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pEXLBrex.AddAnimation("EXLEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pEXLBrex.AddAnimation("EXLEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pEXLBrex.AddAnimation("EXLEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pEXLBrex)

	# Brex sits on the EXL bridge
	pEXLBrex.SetStanding(0)
	pEXLBrex.SetLocation("EXLEngineer")
	pEXLBrex.AddPositionZoom("EXLEngineer", 0.4)
	pEXLBrex.AddPositionZoom("EXLEngineer1", 0.4)
	pEXLBrex.AddPositionZoom("EXLEngineer2", 0.4)
#	kDebugObj.Print("Finished configuring Brex")
	pEXLBrex.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pEXLBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLBrex):
	debug(__name__ + ", AddCommonAnimations")
	pEXLBrex.AddRandomAnimation("Bridge.Characters.EXLSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pEXLBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pEXLBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pEXLBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pEXLBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


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
	debug(__name__ + ", LoadSounds")
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
						"FrontShieldfailed",
						"RearShieldDraining",
						"RearShieldfailed",
						"TopShieldDraining",
						"TopShieldfailed",
						"BottomShieldDraining",
						"BottomShieldfailed",
						"LeftShieldDraining",
						"LeftShieldfailed",
						"RightShieldDraining",
						"RightShieldfailed",
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
	debug(__name__ + ", MoveFromEToL1")
	import Bridge.Characters.EXLSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.EXLSmallAnimations.MoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "enableContactEngineeringButton"), 15.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "GalaxyEngSeated"))
	return pSequence

def MoveToEngineeringSet(pAction):
#	kDebugObj.Print("Moving Brex to the Engineering set")

	debug(__name__ + ", MoveToEngineeringSet")
	pBridge = App.g_kSetManager.GetSet("bridge")
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet()
	pEXLBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pEXLBrex
	bSuccess = pEngineering.AddObjectToSet(pEXLBrex, "Engineer")
	assert bSuccess

#	kDebugObj.Print("Done in MoveToEngineeringSet()")

	return 0

def enableContactEngineeringButton(pAction):
	debug(__name__ + ", enableContactEngineeringButton")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringenabled(1)

	return 0
	
def MoveFromL1ToE(self):
	debug(__name__ + ", MoveFromL1ToE")
	import Bridge.Characters.EXLSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.EXLSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	debug(__name__ + ", MoveToDBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringenabled(0)
	import Bridge.Characters.EXLSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pEXLBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pEXLBrex
	bSuccess = pBridge.AddObjectToSet(pEXLBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	debug(__name__ + ", EBMoveFromEToL1")
	import Bridge.Characters.EXLSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.EXLSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "enableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	debug(__name__ + ", EBMoveFromL1ToE")
	import Bridge.Characters.EXLSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.EXLSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	debug(__name__ + ", MoveToEBridgeSet")
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringenabled(0)
	import Bridge.Characters.EXLSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pEXLBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pEXLBrex
	bSuccess = pBridge.AddObjectToSet(pEXLBrex, "Engineer")
	assert bSuccess

	return 0
