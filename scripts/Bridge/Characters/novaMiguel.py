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
	pnovaMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pnovaMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pnovaMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaMiguel)

	# Setup the character configuration
	pnovaMiguel.SetSize(App.CharacterClass.SMALL)
	pnovaMiguel.SetGender(App.CharacterClass.MALE)
	pnovaMiguel.SetRandomAnimationChance(.75)
	pnovaMiguel.SetBlinkChance(0.1)
	pnovaMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pnovaMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pnovaMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pnovaMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pnovaMiguel.SetBlinkStages(3)

	pnovaMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pnovaMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pnovaMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pnovaMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pnovaMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pnovaMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pnovaMiguel


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
	pnovaMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pnovaMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pnovaMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pnovaMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pnovaMiguel):
#	kDebugObj.Print("Configuring Miguel for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pnovaMiguel.ClearAnimations()

	# Register animation mappings
	pnovaMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.novaSmallAnimations.EBMoveFromL1ToS")
	pnovaMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.novaSmallAnimations.EBMoveFromSToL1")
	pnovaMiguel.AddAnimation("novaScienceTurnCaptain", "Bridge.Characters.novaSmallAnimations.novaTurnAtSTowardsCaptain")
	pnovaMiguel.AddAnimation("novaScienceBackCaptain", "Bridge.Characters.novaSmallAnimations.novaTurnBackAtSFromCaptain")

	pnovaMiguel.AddAnimation("novaScienceTurnC", "Bridge.Characters.novaSmallAnimations.novaTurnAtSTowardsCaptain")
	pnovaMiguel.AddAnimation("novaScienceBackC", "Bridge.Characters.CommonAnimations.SeatedL")
	pnovaMiguel.AddAnimation("novaScienceTurnH", "Bridge.Characters.novaSmallAnimations.EBSTalkH")
	pnovaMiguel.AddAnimation("novaScienceBackH", "Bridge.Characters.CommonAnimations.SeatedL")
	pnovaMiguel.AddAnimation("novaScienceTurnE", "Bridge.Characters.novaSmallAnimations.EBSTalkE")
	pnovaMiguel.AddAnimation("novaScienceBackE", "Bridge.Characters.CommonAnimations.SeatedL")
	pnovaMiguel.AddAnimation("novaScienceTurnT", "Bridge.Characters.novaSmallAnimations.EBSTalkT")
	pnovaMiguel.AddAnimation("novaScienceBackT", "Bridge.Characters.CommonAnimations.SeatedL")

	pnovaMiguel.AddAnimation("novaScienceTurnova", "Bridge.Characters.novaSmallAnimations.EBSTalkE")
	pnovaMiguel.AddAnimation("novaScienceBackX", "Bridge.Characters.CommonAnimations.SeatedL")

	pnovaMiguel.AddAnimation("novaScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pnovaMiguel.AddAnimation("novaScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pnovaMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.novaSmallAnimations.EBMoveFromSToS1")
	pnovaMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.novaSmallAnimations.EBMoveFromS1ToS")
	pnovaMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.novaSmallAnimations.EBMoveFromSToS2")
	pnovaMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.novaSmallAnimations.EBMoveFromS2ToS")
	pnovaMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.novaSmallAnimations.EBMoveFromS1ToS2")
	pnovaMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.novaSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pnovaMiguel.AddAnimation("novaScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pnovaMiguel.AddAnimation("novaScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pnovaMiguel.AddRandomAnimation("Bridge.Characters.novaSmallAnimations.novaSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pnovaMiguel.AddAnimation("PushingButtons", "Bridge.Characters.novaSmallAnimations.novaSConsoleInteraction")

	# Hit animations
	pnovaMiguel.AddAnimation("novaScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pnovaMiguel.AddAnimation("novaScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pnovaMiguel.AddAnimation("novaScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pnovaMiguel.AddAnimation("novaScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pnovaMiguel)

	# Miguel stamds on the nova bridge
	pnovaMiguel.SetLocation("novaScience")
	pnovaMiguel.SetStanding(0)

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
#	Args:	pnovaMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaMiguel):
	pnovaMiguel.AddRandomAnimation("Bridge.Characters.novaSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pnovaMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pnovaMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pnovaMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pnovaMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pnovaMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pnovaMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pnovaMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pnovaMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
