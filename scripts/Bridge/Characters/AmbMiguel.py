###############################################################################
#	Filename:	AmbMiguel.py
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
	pAmbMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pAmbMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pAmbMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbMiguel)

	# Setup the character configuration
	pAmbMiguel.SetSize(App.CharacterClass.SMALL)
	pAmbMiguel.SetGender(App.CharacterClass.MALE)
	pAmbMiguel.SetRandomAnimationChance(.75)
	pAmbMiguel.SetBlinkChance(0.1)
	pAmbMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pAmbMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pAmbMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pAmbMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pAmbMiguel.SetBlinkStages(3)

	pAmbMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pAmbMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pAmbMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pAmbMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pAmbMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pAmbMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pAmbMiguel


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
	pAmbMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pAmbMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pAmbMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pAmbMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pAmbMiguel):
#	kDebugObj.Print("Configuring Miguel for the Ambassador bridge")

	# Clear out any old animations from another configuration
	pAmbMiguel.ClearAnimations()

	# Register animation mappings
	pAmbMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.AmbSmallAnimations.EBMoveFromL1ToS")
	pAmbMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.AmbSmallAnimations.EBMoveFromSToL1")
	pAmbMiguel.AddAnimation("AmbScienceTurnCaptain", "Bridge.Characters.AmbSmallAnimations.AmbTurnAtSTowardsCaptain")
	pAmbMiguel.AddAnimation("AmbScienceBackCaptain", "Bridge.Characters.AmbSmallAnimations.AmbTurnBackAtSFromCaptain")

	pAmbMiguel.AddAnimation("AmbScienceTurnC", "Bridge.Characters.AmbSmallAnimations.AmbTurnAtSTowardsCaptain")
	pAmbMiguel.AddAnimation("AmbScienceBackC", "Bridge.Characters.AmbSmallAnimations.Amb_stand_s")
	pAmbMiguel.AddAnimation("AmbScienceTurnH", "Bridge.Characters.AmbSmallAnimations.EBSTalkH")
	pAmbMiguel.AddAnimation("AmbScienceBackH", "Bridge.Characters.AmbSmallAnimations.Amb_stand_s")
	pAmbMiguel.AddAnimation("AmbScienceTurnE", "Bridge.Characters.AmbSmallAnimations.EBSTalkE")
	pAmbMiguel.AddAnimation("AmbScienceBackE", "Bridge.Characters.AmbSmallAnimations.Amb_stand_s")
	pAmbMiguel.AddAnimation("AmbScienceTurnT", "Bridge.Characters.AmbSmallAnimations.EBSTalkT")
	pAmbMiguel.AddAnimation("AmbScienceBackT", "Bridge.Characters.AmbSmallAnimations.Amb_stand_s")

	pAmbMiguel.AddAnimation("AmbScienceTurAmb", "Bridge.Characters.AmbSmallAnimations.EBSTalkE")
	pAmbMiguel.AddAnimation("AmbScienceBackX", "Bridge.Characters.AmbSmallAnimations.Amb_stand_s")

	pAmbMiguel.AddAnimation("AmbScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pAmbMiguel.AddAnimation("AmbScienceGlanceAwayCaptain", "Bridge.Characters.AmbSmallAnimations.AmbSConsoleInteraction")

	pAmbMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.AmbSmallAnimations.EBMoveFromSToS1")
	pAmbMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.AmbSmallAnimations.EBMoveFromS1ToS")
	pAmbMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.AmbSmallAnimations.EBMoveFromSToS2")
	pAmbMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.AmbSmallAnimations.EBMoveFromS2ToS")
	pAmbMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.AmbSmallAnimations.EBMoveFromS1ToS2")
	pAmbMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.AmbSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pAmbMiguel.AddAnimation("AmbScienceBreathe", "Bridge.Characters.AmbSmallAnimations.Amb_stand_s")
	pAmbMiguel.AddAnimation("AmbScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pAmbMiguel.AddRandomAnimation("Bridge.Characters.AmbSmallAnimations.AmbSConsoleInteraction", App.CharacterClass.STANDING_ONLY, 25, 1)

	# So the mission builders can force the call
	pAmbMiguel.AddAnimation("PushingButtons", "Bridge.Characters.AmbSmallAnimations.AmbSConsoleInteraction")

	# Hit animations
	pAmbMiguel.AddAnimation("AmbScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pAmbMiguel.AddAnimation("AmbScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pAmbMiguel.AddAnimation("AmbScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pAmbMiguel.AddAnimation("AmbScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pAmbMiguel)

	# Miguel stamds on the Amb bridge
	pAmbMiguel.SetLocation("AmbScience")
	pAmbMiguel.SetStanding(1)
	#pAmbMiguel.SetLookAtAdj(30, -10, 8)
	pAmbMiguel.AddPositionZoom("AmbScience", 0.9)
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
#	Args:	pAmbMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbMiguel):
	pAmbMiguel.AddRandomAnimation("Bridge.Characters.AmbSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.STANDING_ONLY, 1, 1)

	#pAmbMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pAmbMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pAmbMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pAmbMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pAmbMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pAmbMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pAmbMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
