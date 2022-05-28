###############################################################################
#	Filename:	Brex.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Brex, the Engineer, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
#           Modified: 2/06/05                Blackrook32
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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head.nif", None)
	pBrex = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadBrex/brex_head_no_mouth.nif")
	pBrex.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadBrex/brex_head.tga")

	pRunBrex.SetCharacterName("Brex")

	# Add the character to the set
	pSet.AddObjectToSet(pRunBrex, "Engineer")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRunBrex)

	# Setup the character configuration
	pRunBrex.SetSize(App.CharacterClass.SMALL)
	pRunBrex.SetGender(App.CharacterClass.MALE)
	pRunBrex.SetRandomAnimationChance(.75)
	pRunBrex.SetBlinkChance(0.1)
	pRunBrex.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Engineering officer generic sounds
	LoadSounds()

	pRunBrex.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_blink1.tga")
	pRunBrex.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_blink2.tga")
	pRunBrex.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_eyes_close.tga")
	pRunBrex.SetBlinkStages(3)

	pRunBrex.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_head_a.tga")
	pRunBrex.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_head_e.tga")
	pRunBrex.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadBrex/Brex_head_u.tga")
	pRunBrex.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pRunBrex.GetDatabase(), "BrexNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRunBrex.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Engineering")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	return pRunBrex


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
	pRunBrex = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
	if (pRunBrex == None):
#		kDebugObj.Print("******* Engineering officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Engineer..")
	import Bridge.EngineerCharacterHandlers
	Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pRunBrex)

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


def ConfigureForType11(pRunBrex):
	pRunBrex.ClearAnimations()

	# Register animation mappings
	pRunBrex.AddAnimation("SeatedEBEngineer", "Bridge.Characters.CommonAnimations.SeatedS")
	pRunBrex.AddAnimation("EBL1SToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pRunBrex.AddAnimation("SovereignEngSeatedToE", "Bridge.Characters.Brex.EBMoveFromL1ToE")
	pRunBrex.AddAnimation("EBEngineerToL1", "Bridge.Characters.Brex.EBMoveFromEToL1")
	pRunBrex.AddAnimation("EBEngineerTurnCaptain", "Bridge.Characters.SmallAnimations.EBTurnAtETowardsCaptain")
	pRunBrex.AddAnimation("EBEngineerBackCaptain", "Bridge.Characters.SmallAnimations.EBTurnBackAtEFromCaptain")
	pRunBrex.AddAnimation("EBEngineer1ToE", "Bridge.Characters.SmallAnimations.EBMoveFromE1ToE")
	pRunBrex.AddAnimation("EBEngineerToE1", "Bridge.Characters.SmallAnimations.EBMoveFromEToE1")
	pRunBrex.AddAnimation("EBEngineer2ToE", "Bridge.Characters.SmallAnimations.EBMoveFromE2ToE")
	pRunBrex.AddAnimation("EBEngineerToE2", "Bridge.Characters.SmallAnimations.EBMoveFromEToE2")
	pRunBrex.AddAnimation("EBEngineer1ToE2", "Bridge.Characters.SmallAnimations.EBMoveFromE1ToE2")
	pRunBrex.AddAnimation("EBEngineer2ToE1", "Bridge.Characters.SmallAnimations.EBMoveFromE2ToE1")

	pRunBrex.AddAnimation("EBEngineerGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pRunBrex.AddAnimation("EBEngineerGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pRunBrex.AddAnimation("EBEngineerTurnC", "Bridge.Characters.SmallAnimations.EBETalkC")
	pRunBrex.AddAnimation("EBEngineerBackC", "Bridge.Characters.CommonAnimations.SeatedS")
	pRunBrex.AddAnimation("EBEngineerTurnH", "Bridge.Characters.SmallAnimations.EBETalkH")
	pRunBrex.AddAnimation("EBEngineerBackH", "Bridge.Characters.CommonAnimations.SeatedS")
	pRunBrex.AddAnimation("EBEngineerTurnS", "Bridge.Characters.SmallAnimations.EBETalkS")
	pRunBrex.AddAnimation("EBEngineerBackS", "Bridge.Characters.CommonAnimations.SeatedS")
	pRunBrex.AddAnimation("EBEngineerTurnT", "Bridge.Characters.SmallAnimations.EBETalkT")
	pRunBrex.AddAnimation("EBEngineerBackT", "Bridge.Characters.CommonAnimations.SeatedS")

	pRunBrex.AddAnimation("EBEngineerTurnX", "Bridge.Characters.SmallAnimations.EBTurnAtETowardsCaptain")
	pRunBrex.AddAnimation("EBEngineerBackX", "Bridge.Characters.SmallAnimations.EBTurnBackAtEFromCaptain")

	# Breathing
	pRunBrex.AddAnimation("EBEngineerBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pRunBrex.AddAnimation("EBEngineerBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	#pRunBrex.AddRandomAnimation("Bridge.Characters.AmbLargeAnimations.AmbTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	#pRunBrex.AddAnimation("PushingButtons", "Bridge.Characters.AmbLargeAnimations.AmbTConsoleInteraction")

	

	# Hit animations
	pRunBrex.AddAnimation("EBEngineerHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pRunBrex.AddAnimation("EBEngineerHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pRunBrex.AddAnimation("EBEngineerReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pRunBrex.AddAnimation("EBEngineerReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pRunBrex)

	pRunBrex.SetLocation("RunEngineer")
	


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pRunBrex	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pRunBrex):
	pRunBrex.AddRandomAnimation("Bridge.Characters.SmallAnimations.ELookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pRunBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pRunBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pRunBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRunBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRunBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pRunBrex.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pRunBrex.AddRandomAnimation("Bridge.Characters.galMediumAnimations.gal_interaction_XT01")

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
