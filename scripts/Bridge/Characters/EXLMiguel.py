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
	pEXLMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pEXLMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pEXLMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLMiguel)

	# Setup the character configuration
	pEXLMiguel.SetSize(App.CharacterClass.SMALL)
	pEXLMiguel.SetGender(App.CharacterClass.MALE)
	pEXLMiguel.SetRandomAnimationChance(.75)
	pEXLMiguel.SetBlinkChance(0.1)
	pEXLMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pEXLMiguel.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pEXLMiguel.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pEXLMiguel.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pEXLMiguel.SetBlinkStages(3)

	pEXLMiguel.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pEXLMiguel.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pEXLMiguel.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pEXLMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pEXLMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pEXLMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pEXLMiguel


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
	pEXLMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pEXLMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pEXLMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pEXLMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pEXLMiguel):
#	kDebugObj.Print("Configuring Miguel for the Excelsior bridge")

	# Clear out any old animations from another configuration
	pEXLMiguel.ClearAnimations()

	# Register animation mappings
	pEXLMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.EXLSmallAnimations.EBMoveFromL1ToS")
	pEXLMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.EXLSmallAnimations.EBMoveFromSToL1")
	pEXLMiguel.AddAnimation("EXLScienceTurnCaptain", "Bridge.Characters.EXLSmallAnimations.EXLTurnAtSTowardsCaptain")
	pEXLMiguel.AddAnimation("EXLScienceBackCaptain", "Bridge.Characters.EXLSmallAnimations.EXLTurnBackAtSFromCaptain")

	pEXLMiguel.AddAnimation("EXLScienceTurnC", "Bridge.Characters.EXLSmallAnimations.EXLTurnAtSTowardsCaptain")
	pEXLMiguel.AddAnimation("EXLScienceBackC", "Bridge.Characters.CommonAnimations.SeatedL")
	pEXLMiguel.AddAnimation("EXLScienceTurnH", "Bridge.Characters.EXLSmallAnimations.EBSTalkH")
	pEXLMiguel.AddAnimation("EXLScienceBackH", "Bridge.Characters.CommonAnimations.SeatedL")
	pEXLMiguel.AddAnimation("EXLScienceTurnE", "Bridge.Characters.EXLSmallAnimations.EBSTalkE")
	pEXLMiguel.AddAnimation("EXLScienceBackE", "Bridge.Characters.CommonAnimations.SeatedL")
	pEXLMiguel.AddAnimation("EXLScienceTurnT", "Bridge.Characters.EXLSmallAnimations.EBSTalkT")
	pEXLMiguel.AddAnimation("EXLScienceBackT", "Bridge.Characters.CommonAnimations.SeatedL")

	pEXLMiguel.AddAnimation("EXLScienceTurnX", "Bridge.Characters.EXLSmallAnimations.EBSTalkE")
	pEXLMiguel.AddAnimation("EXLScienceBackX", "Bridge.Characters.CommonAnimations.SeatedL")

	pEXLMiguel.AddAnimation("EXLScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pEXLMiguel.AddAnimation("EXLScienceGlanceAwayCaptain", "Bridge.Characters.EXLSmallAnimations.EXLSConsoleInteraction")

	pEXLMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.EXLSmallAnimations.EBMoveFromSToS1")
	pEXLMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.EXLSmallAnimations.EBMoveFromS1ToS")
	pEXLMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.EXLSmallAnimations.EBMoveFromSToS2")
	pEXLMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.EXLSmallAnimations.EBMoveFromS2ToS")
	pEXLMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.EXLSmallAnimations.EBMoveFromS1ToS2")
	pEXLMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.EXLSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pEXLMiguel.AddAnimation("EXLScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pEXLMiguel.AddAnimation("EXLScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pEXLMiguel.AddRandomAnimation("Bridge.Characters.EXLSmallAnimations.EXLSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pEXLMiguel.AddAnimation("PushingButtons", "Bridge.Characters.EXLSmallAnimations.EXLSConsoleInteraction")

	# Hit animations
	pEXLMiguel.AddAnimation("EXLScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pEXLMiguel.AddAnimation("EXLScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pEXLMiguel.AddAnimation("EXLScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pEXLMiguel.AddAnimation("EXLScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pEXLMiguel)

	# Miguel stamds on the EXL bridge
	pEXLMiguel.SetLocation("EXLScience")
	pEXLMiguel.SetStanding(0)
#	pEXLMiguel.SetLookAtAdj(30, -10, 8)
#	pEXLMiguel.AddPositionZoom("EXLScience", 0.7, "Science")
	pEXLMiguel.AddPositionZoom("EXLScience", 0.4)
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
#	Args:	pEXLMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLMiguel):
	pEXLMiguel.AddRandomAnimation("Bridge.Characters.EXLSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pEXLMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pEXLMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pEXLMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pEXLMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pEXLMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pEXLMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
						"TargetFrontShieldfailed",
						"TargetFrontShieldDraining",
						"TargetRearShieldfailed",
						"TargetRearShieldDraining",
						"TargetLeftShieldfailed",
						"TargetLeftShieldDraining",
						"TargetRightShieldfailed",
						"TargetRightShieldDraining",
						"TargetTopShieldfailed",
						"TargetTopShieldDraining",
						"TargetBottomShieldfailed",
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
