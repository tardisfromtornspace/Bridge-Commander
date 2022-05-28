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

	if (pSet.GetObject("Engineer") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Engineer")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif", None)
	pTOSBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pTOSBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Brex/brex_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/brex_head.tga")

	pTOSBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSBrex)

	# Setup the character configuration
	pTOSBrex.SetSize(App.CharacterClass.SMALL)
	pTOSBrex.SetGender(App.CharacterClass.MALE)
	pTOSBrex.SetRandomAnimationChance(.75)
	pTOSBrex.SetBlinkChance(0.1)

	pTOSBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pTOSBrex.AdTOSacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink1.tga")
	pTOSBrex.AdTOSacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_blink2.tga")
	pTOSBrex.AdTOSacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_eyes_close.tga")
	pTOSBrex.SetBlinkStages(3)

	pTOSBrex.AdTOSacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_a.tga")
	pTOSBrex.AdTOSacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_e.tga")
	pTOSBrex.AdTOSacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Brex/Brex_head_u.tga")
	pTOSBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pTOSBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pTOSBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pTOSBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pTOSBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Brex")
	return pTOSBrex


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
	pTOSBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pTOSBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pTOSBrex)

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
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pTOSBrex	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pTOSBrex):
#	kDebugObj.Print("Configuring Brex for the Constitution bridge")

	# Clear out any old animations from another configuration
	pTOSBrex.ClearAnimations()

	# Register animation mappings
	pTOSBrex.AddAnimation("SeatedTOSEngineer", "Bridge.Characters.CommonAnimations.seateds")
	pTOSBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pTOSBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pTOSBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pTOSBrex.AddAnimation("TOSEngineerTurnCaptain", "Bridge.Characters.TOSSmallAnimations.TOSTurnAtETowardsCaptain")
	pTOSBrex.AddAnimation("TOSEngineerBackCaptain", "Bridge.Characters.TOSSmallAnimations.TOSTurnBackAtEFromCaptain")
	pTOSBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.TOSSmallAnimations.EBMoveFromE1ToE")
	pTOSBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.TOSSmallAnimations.EBMoveFromEToE1")
	pTOSBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.TOSSmallAnimations.EBMoveFromE2ToE")
	pTOSBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.TOSSmallAnimations.EBMoveFromEToE2")
	pTOSBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.TOSSmallAnimations.EBMoveFromE1ToE2")
	pTOSBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.TOSSmallAnimations.EBMoveFromE2ToE1")

	pTOSBrex.AddAnimation("TOSEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pTOSBrex.AddAnimation("TOSEngineerGlanceAwayCaptain", "Bridge.Characters.TOSSmallAnimations.TOSEConsoleInteraction")

	pTOSBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.TOSSmallAnimations.EBETalkC")
	pTOSBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.CommonAnimations.seateds")
	pTOSBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.TOSSmallAnimations.EBETalkH")
	pTOSBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.seateds")
	pTOSBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.TOSSmallAnimations.EBETalkS")
	pTOSBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.seateds")
	pTOSBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.TOSSmallAnimations.EBETalkT")
	pTOSBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.seateds")

	pTOSBrex.AddAnimation("TOSEngineerTurnX", "Bridge.Characters.TOSSmallAnimations.TOSTurnAtETowardsCaptain")
	pTOSBrex.AddAnimation("TOSEngineerBackX", "Bridge.Characters.TOSSmallAnimations.TOSTurnBackAtEFromCaptain")

	# Breathing
	pTOSBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.CommonAnimations.seateds")
	pTOSBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pTOSBrex.AddRandomAnimation("Bridge.Characters.TOSSmallAnimations.TOSEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pTOSBrex.AddAnimation("PushingButtons", "Bridge.Characters.TOSSmallAnimations.TOSEConsoleInteraction")

	# Hit animations
	#pTOSBrex.AddAnimation("TOSEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pTOSBrex.AddAnimation("TOSEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pTOSBrex.AddAnimation("TOSEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	#pTOSBrex.AddAnimation("TOSEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pTOSBrex)

	# Brex sits on the TOS bridge
	pTOSBrex.SetStanding(0)
	pTOSBrex.SetLocation("TOSEngineer")
	pTOSBrex.AddPositionZoom("TOSEngineer", 0.7)
	pTOSBrex.AddPositionZoom("TOSEngineer1", 0.7)
	pTOSBrex.AddPositionZoom("TOSEngineer2", 0.7)
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
#	Args:	pTOSBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSBrex):
	pTOSBrex.AddRandomAnimation("Bridge.Characters.TOSSmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pTOSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pTOSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pTOSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pTOSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pTOSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pTOSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pTOSBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)


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
						"FrontShielTOSailed",
						"RearShieldDraining",
						"RearShielTOSailed",
						"TopShieldDraining",
						"TopShielTOSailed",
						"BottomShieldDraining",
						"BottomShielTOSailed",
						"LeftShieldDraining",
						"LeftShielTOSailed",
						"RightShieldDraining",
						"RightShielTOSailed",
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
	import Bridge.Characters.TOSSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")

	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.TOSSmallAnimations.MoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 15.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "GalaxyEngSeated"))
	return pSequence

def MoveToEngineeringSet(pAction):
#	kDebugObj.Print("Moving Brex to the Engineering set")

	pBridge = App.g_kSetManager.GetSet("bridge")
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet()
	pTOSBrex = pBridge.RemoveObjectFromSet("Engineer")
	assert pTOSBrex
	bSuccess = pEngineering.AddObjectToSet(pTOSBrex, "Engineer")
	assert bSuccess

#	kDebugObj.Print("Done in MoveToEngineeringSet()")

	return 0

def EnableContactEngineeringButton(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(1)

	return 0
	
def MoveFromL1ToE(self):
	import Bridge.Characters.TOSSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "DBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToDBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.TOSSmallAnimations.MoveFromL1ToE(self))
	return pSequence

def MoveToDBridgeSet(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.TOSSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Galaxy")
	pTOSBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pTOSBrex
	bSuccess = pBridge.AddObjectToSet(pTOSBrex, "Engineer")
	assert bSuccess

	return 0

def EBMoveFromEToL1(self):
	import Bridge.Characters.TOSSmallAnimations
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(Bridge.Characters.TOSSmallAnimations.EBMoveFromEToL1(self))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EnableContactEngineeringButton"), 5.0)
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEngineeringSet"), 0.1)
	pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "SovereignEngSeated"))
	return pSequence

def EBMoveFromL1ToE(self):
	import Bridge.Characters.TOSSmallAnimations
	pSequence = App.TGSequence_Create()
	#pSequence.AppendAction(App.CharacterAction_Create(self, App.CharacterAction.AT_SET_LOCATION, "EBL1S"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "MoveToEBridgeSet"))
	pSequence.AppendAction(Bridge.Characters.TOSSmallAnimations.EBMoveFromL1ToE(self))
	return pSequence

def MoveToEBridgeSet(pAction):
	import Bridge.XOMenuHandlers
	Bridge.XOMenuHandlers.SetContactEngineeringEnabled(0)
	import Bridge.Characters.TOSSmallAnimations

	pBridge = Bridge.BridgeUtils.GetBridge()
	import Bridge.EngineerCharacterHandlers
	pEngineering = Bridge.EngineerCharacterHandlers.GetEngineeringSet("Sovereign")
	pTOSBrex = pEngineering.RemoveObjectFromSet("Engineer")
	assert pTOSBrex
	bSuccess = pBridge.AddObjectToSet(pTOSBrex, "Engineer")
	assert bSuccess

	return 0
