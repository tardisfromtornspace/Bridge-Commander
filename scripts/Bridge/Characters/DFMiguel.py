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
	pDFMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pDFMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pDFMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pDFMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFMiguel)

	# Setup the character configuration
	pDFMiguel.SetSize(App.CharacterClass.SMALL)
	pDFMiguel.SetGender(App.CharacterClass.MALE)
	pDFMiguel.SetRandomAnimationChance(.75)
	pDFMiguel.SetBlinkChance(0.1)
	pDFMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pDFMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pDFMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pDFMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pDFMiguel.SetBlinkStages(3)

	pDFMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pDFMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pDFMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pDFMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pDFMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDFMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pDFMiguel


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
	pDFMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pDFMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pDFMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pDFMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pDFMiguel):
#	kDebugObj.Print("Configuring Miguel for the Defiant bridge")

	# Clear out any old animations from another configuration
	pDFMiguel.ClearAnimations()

	# Register animation mappings
	pDFMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.DFSmallAnimations.EBMoveFromL1ToS")
	pDFMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.DFSmallAnimations.EBMoveFromSToL1")
	pDFMiguel.AddAnimation("DFScienceTurnCaptain", "Bridge.Characters.DFSmallAnimations.DFTurnAtSTowardsCaptain")
	pDFMiguel.AddAnimation("DFScienceBackCaptain", "Bridge.Characters.DFSmallAnimations.DFTurnBackAtSFromCaptain")

	pDFMiguel.AddAnimation("DFScienceTurnC", "Bridge.Characters.DFSmallAnimations.DFTurnAtSTowardsCaptain")
	pDFMiguel.AddAnimation("DFScienceBackC", "Bridge.Characters.CommonAnimations.SeatedL")
	pDFMiguel.AddAnimation("DFScienceTurnH", "Bridge.Characters.DFSmallAnimations.EBSTalkH")
	pDFMiguel.AddAnimation("DFScienceBackH", "Bridge.Characters.CommonAnimations.SeatedL")
	pDFMiguel.AddAnimation("DFScienceTurnE", "Bridge.Characters.DFSmallAnimations.EBSTalkE")
	pDFMiguel.AddAnimation("DFScienceBackE", "Bridge.Characters.CommonAnimations.SeatedL")
	pDFMiguel.AddAnimation("DFScienceTurnT", "Bridge.Characters.DFSmallAnimations.EBSTalkT")
	pDFMiguel.AddAnimation("DFScienceBackT", "Bridge.Characters.CommonAnimations.SeatedL")

	pDFMiguel.AddAnimation("DFScienceTurDF", "Bridge.Characters.DFSmallAnimations.EBSTalkE")
	pDFMiguel.AddAnimation("DFScienceBackX", "Bridge.Characters.CommonAnimations.SeatedL")

	pDFMiguel.AddAnimation("DFScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pDFMiguel.AddAnimation("DFScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pDFMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.DFSmallAnimations.EBMoveFromSToS1")
	pDFMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.DFSmallAnimations.EBMoveFromS1ToS")
	pDFMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.DFSmallAnimations.EBMoveFromSToS2")
	pDFMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.DFSmallAnimations.EBMoveFromS2ToS")
	pDFMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.DFSmallAnimations.EBMoveFromS1ToS2")
	pDFMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.DFSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pDFMiguel.AddAnimation("DFScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pDFMiguel.AddAnimation("DFScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pDFMiguel.AddRandomAnimation("Bridge.Characters.DFSmallAnimations.DFSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pDFMiguel.AddAnimation("PushingButtons", "Bridge.Characters.DFSmallAnimations.DFSConsoleInteraction")

	# Hit animations
	pDFMiguel.AddAnimation("DFScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pDFMiguel.AddAnimation("DFScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pDFMiguel.AddAnimation("DFScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pDFMiguel.AddAnimation("DFScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pDFMiguel)

	# Miguel stamds on the DF bridge
	pDFMiguel.SetLocation("DFScience")
	pDFMiguel.SetStanding(0)
	pDFMiguel.SetLookAtAdj(30, -10, 8)
	pDFMiguel.AddPositionZoom("DFScience", 0.7, "Science")
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
#	Args:	pDFMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFMiguel):
	pDFMiguel.AddRandomAnimation("Bridge.Characters.DFSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pDFMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pDFMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pDFMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pDFMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pDFMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pDFMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
