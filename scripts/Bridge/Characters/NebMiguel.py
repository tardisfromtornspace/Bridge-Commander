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
	pNebMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pNebMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedTeal_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/miguel_head.tga")

	pNebMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pNebMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebMiguel)

	# Setup the character configuration
	pNebMiguel.SetSize(App.CharacterClass.SMALL)
	pNebMiguel.SetGender(App.CharacterClass.MALE)
	pNebMiguel.SetRandomAnimationChance(.75)
	pNebMiguel.SetBlinkChance(0.1)
	pNebMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pNebMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_blink1.tga")
	pNebMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_blink2.tga")
	pNebMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_eyesclosed.tga")
	pNebMiguel.SetBlinkStages(3)

	pNebMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_a.tga")
	pNebMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_e.tga")
	pNebMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_u.tga")
	pNebMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pNebMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pNebMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pNebMiguel


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
	pNebMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pNebMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pNebMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForNebula()
#
#	Configure ourselves for the Nebula bridge
#
#	Args:	pNebMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pNebMiguel):
#	kDebugObj.Print("Configuring Miguel for the Nebula bridge")

	# Clear out any old animations from another configuration
	pNebMiguel.ClearAnimations()

	# Register animation mappings
	pNebMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.NebSmallAnimations.EBMoveFromL1ToS")
	pNebMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.NebSmallAnimations.EBMoveFromSToL1")
	pNebMiguel.AddAnimation("NebScienceTurnCaptain", "Bridge.Characters.NebSmallAnimations.NebTurnAtSTowardsCaptain")
	pNebMiguel.AddAnimation("NebScienceBackCaptain", "Bridge.Characters.NebSmallAnimations.NebTurnBackAtSFromCaptain")

	pNebMiguel.AddAnimation("NebScienceTurnC", "Bridge.Characters.NebSmallAnimations.NebSTalkC")
	pNebMiguel.AddAnimation("NebScienceBackC", "Bridge.Characters.CommonAnimations.SeatedS")
	pNebMiguel.AddAnimation("NebScienceTurnH", "Bridge.Characters.NebSmallAnimations.EBSTalkH")
	pNebMiguel.AddAnimation("NebScienceBackH", "Bridge.Characters.CommonAnimations.SeatedS")
	pNebMiguel.AddAnimation("NebScienceTurnE", "Bridge.Characters.NebSmallAnimations.EBSTalkE")
	pNebMiguel.AddAnimation("NebScienceBackE", "Bridge.Characters.CommonAnimations.SeatedS")
	pNebMiguel.AddAnimation("NebScienceTurnT", "Bridge.Characters.NebSmallAnimations.EBSTalkT")
	pNebMiguel.AddAnimation("NebScienceBackT", "Bridge.Characters.CommonAnimations.SeatedS")

	pNebMiguel.AddAnimation("NebScienceTurnX", "Bridge.Characters.NebSmallAnimations.EBSTalkE")
	pNebMiguel.AddAnimation("NebScienceBackX", "Bridge.Characters.CommonAnimations.SeatedS")

	pNebMiguel.AddAnimation("NebScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pNebMiguel.AddAnimation("NebScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pNebMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.NebSmallAnimations.EBMoveFromSToS1")
	pNebMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.NebSmallAnimations.EBMoveFromS1ToS")
	pNebMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.NebSmallAnimations.EBMoveFromSToS2")
	pNebMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.NebSmallAnimations.EBMoveFromS2ToS")
	pNebMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.NebSmallAnimations.EBMoveFromS1ToS2")
	pNebMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.NebSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pNebMiguel.AddAnimation("NebScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pNebMiguel.AddAnimation("NebScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pNebMiguel.AddRandomAnimation("Bridge.Characters.NebSmallAnimations.NebSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pNebMiguel.AddAnimation("PushingButtons", "Bridge.Characters.NebSmallAnimations.NebSConsoleInteraction")

	# Hit animations
	pNebMiguel.AddAnimation("NebScienceHitStanding", "Bridge.Characters.CommonAnimations.NebHitStanding")
	pNebMiguel.AddAnimation("NebScienceHitHardStanding", "Bridge.Characters.CommonAnimations.NebHitHardStanding")
	pNebMiguel.AddAnimation("NebScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pNebMiguel.AddAnimation("NebScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pNebMiguel)

	# Miguel sits on the Nebula bridge
	pNebMiguel.SetStanding(0)
	pNebMiguel.SetLocation("NebScience")
	pNebMiguel.AddPositionZoom("NebScience", 0.7)
	pNebMiguel.AddPositionZoom("NebScience1", 0.7)
	pNebMiguel.AddPositionZoom("NebScience2", 0.8)
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
#	Args:	pNebMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebMiguel):
	pNebMiguel.AddRandomAnimation("Bridge.Characters.NebSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pNebMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pNebMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pNebMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pNebMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pNebMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pNebMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
						"TargetFrontShieldFailed",
						"TargetFrontShieldDraining",
						"TargetRearShieldFailed",
						"TargetRearShieldDraining",
						"TargetLeftShieldFailed",
						"TargetLeftShieldDraining",
						"TargetRightShieldFailed",
						"TargetRightShieldDraining",
						"TargetTopShieldFailed",
						"TargetTopShieldDraining",
						"TargetBottomShieldFailed",
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
