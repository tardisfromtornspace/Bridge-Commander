###############################################################################
#	Filename:	Miguel.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Miguel Diaz, science, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create Miguel by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating Miguel")

	if (pSet.GetObject("Science") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Science")))


	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif", None)
	pTOSMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pTOSMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pTOSMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSMiguel)

	# Setup the character configuration
	pTOSMiguel.SetSize(App.CharacterClass.SMALL)
	pTOSMiguel.SetGender(App.CharacterClass.MALE)
	pTOSMiguel.SetRandomAnimationChance(.75)
	pTOSMiguel.SetBlinkChance(0.1)
	pTOSMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pTOSMiguel.AdTOSacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pTOSMiguel.AdTOSacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pTOSMiguel.AdTOSacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pTOSMiguel.SetBlinkStages(3)

	pTOSMiguel.AdTOSacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pTOSMiguel.AdTOSacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pTOSMiguel.AdTOSacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pTOSMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pTOSMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pTOSMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pTOSMiguel


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
	# Get our character object
	pTOSMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pTOSMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pTOSMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pTOSMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pTOSMiguel):
#	kDebugObj.Print("Configuring Miguel for the Constitution bridge")

	# Clear out any old animations from another configuration
	pTOSMiguel.ClearAnimations()

	# Register animation mappings
	pTOSMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.TOSSmallAnimations.EBMoveFromL1ToS")
	pTOSMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.TOSSmallAnimations.EBMoveFromSToL1")
	pTOSMiguel.AddAnimation("TOSScienceTurnCaptain", "Bridge.Characters.TOSSmallAnimations.TOSTurnAtSTowardsCaptain")
	pTOSMiguel.AddAnimation("TOSScienceBackCaptain", "Bridge.Characters.TOSSmallAnimations.TOSTurnBackAtSFromCaptain")

	pTOSMiguel.AddAnimation("TOSScienceTurnC", "Bridge.Characters.TOSSmallAnimations.TOSTurnAtSTowardsCaptain")
	pTOSMiguel.AddAnimation("TOSScienceBackC", "Bridge.Characters.CommonAnimations.seateds")
	pTOSMiguel.AddAnimation("TOSScienceTurnH", "Bridge.Characters.TOSSmallAnimations.EBSTalkH")
	pTOSMiguel.AddAnimation("TOSScienceBackH", "Bridge.Characters.CommonAnimations.seateds")
	pTOSMiguel.AddAnimation("TOSScienceTurnE", "Bridge.Characters.TOSSmallAnimations.EBSTalkE")
	pTOSMiguel.AddAnimation("TOSScienceBackE", "Bridge.Characters.CommonAnimations.seateds")
	pTOSMiguel.AddAnimation("TOSScienceTurnT", "Bridge.Characters.TOSSmallAnimations.EBSTalkT")
	pTOSMiguel.AddAnimation("TOSScienceBackT", "Bridge.Characters.CommonAnimations.seateds")

	pTOSMiguel.AddAnimation("TOSScienceTurTOS", "Bridge.Characters.TOSSmallAnimations.EBSTalkE")
	pTOSMiguel.AddAnimation("TOSScienceBackX", "Bridge.Characters.CommonAnimations.seateds")

	pTOSMiguel.AddAnimation("TOSScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pTOSMiguel.AddAnimation("TOSScienceGlanceAwayCaptain", "Bridge.Characters.TOSSmallAnimations.TOSSConsoleInteraction")

	pTOSMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.TOSSmallAnimations.EBMoveFromSToS1")
	pTOSMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.TOSSmallAnimations.EBMoveFromS1ToS")
	pTOSMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.TOSSmallAnimations.EBMoveFromSToS2")
	pTOSMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.TOSSmallAnimations.EBMoveFromS2ToS")
	pTOSMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.TOSSmallAnimations.EBMoveFromS1ToS2")
	pTOSMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.TOSSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pTOSMiguel.AddAnimation("TOSScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pTOSMiguel.AddAnimation("TOSScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pTOSMiguel.AddRandomAnimation("Bridge.Characters.TOSSmallAnimations.TOSSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pTOSMiguel.AddAnimation("PushingButtons", "Bridge.Characters.TOSSmallAnimations.TOSSConsoleInteraction")

	# Hit animations
	#pTOSMiguel.AddAnimation("TOSScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pTOSMiguel.AddAnimation("TOSScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pTOSMiguel.AddAnimation("TOSScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	#pTOSMiguel.AddAnimation("TOSScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pTOSMiguel)

	# Miguel stamds on the TOS bridge
	pTOSMiguel.SetLocation("TOSScience")
	pTOSMiguel.SetStanding(0)
#	pTOSMiguel.SetLookAtAdj(0, 0, 0)
#	pTOSMiguel.AddPositionZoom("TOSScience", 0.7, "Science")
	pTOSMiguel.AddPositionZoom("TOSScience", 0.7)
#	kDebugObj.Print("Finished configuring Miguel")



###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSMiguel):
	pTOSMiguel.AddRandomAnimation("Bridge.Characters.TOSSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pTOSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pTOSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pTOSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pTOSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pTOSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pTOSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pTOSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pTOSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pTOSMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
	# Like a function pointer (GetFile() is the same as pDatabase.GetFilename())
	GetFile = pDatabase.GetFilename	# do this for horizontal space savings

	#
	# Build a list of sound to load
	#
	kSoundList =	[	"MiguelSir1",		# Click Response
						"MiguelSir2",
						"MiguelSir3",
						"MiguelSir4",
						"MiguelSir5",

						"MiguelYes1",		# Order Confirmation
						"MiguelYes2",
						"MiguelYes3",
						"MiguelYes4",

						# Scanning lines.
						"MiguelScan",
						"gs038",
						"gs039",
						"gs040",
						"gs041",

						# Launching a probe.
						"gs030",

						# Spontaneous shield callouts.
						"TargetFrontShielTOSailed",
						"TargetFrontShieldDraining",
						"TargetRearShielTOSailed",
						"TargetRearShieldDraining",
						"TargetLeftShielTOSailed",
						"TargetLeftShieldDraining",
						"TargetRightShielTOSailed",
						"TargetRightShieldDraining",
						"TargetTopShielTOSailed",
						"TargetTopShieldDraining",
						"TargetBottomShielTOSailed",
						"TargetBottomShieldDraining",

						# Spontaneous target system callouts..
						"TargetHull05",
						"TargetHull10",
						"TargetHull15",
						"TargetHull20",
						"TargetHull25",
						"TargetHull50",
						"TargetHull75",

						"TargetPhasersDisabled",
						"TargetShieldsDisabled",
						"TargetSensorsDisabled",
						"TargetTorpedoesDisabled",
						"TargetTractorDisabled",
						"TargetImpulseDisabled",
						"TargetWarpDisabled",

						"TargetPhasersDestroyed",
						"TargetShieldsDestroyed",
						"TargetSensorsDestroyed",
						"TargetTorpedoesDestroyed",
						"TargetTractorDestroyed",
						"TargetImpulseDestroyed",
						"TargetWarpDestroyed",
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for i in range(len(kSoundList)):
		pGame.LoadDatabaseSoundInGroup(pDatabase, kSoundList[i], "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)
