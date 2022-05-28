###############################################################################
#	Filename:	Miguel.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Miguel Diaz, science, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
#           Modified: 2/06/05                Blackrook32
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
	if (pSet.GetObject("Science") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Science")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif", None)
	pMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedTeal_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/miguel_head.tga")


	pRunMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pRunMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRunMiguel)

	# Setup the character configuration
	pRunMiguel.SetSize(App.CharacterClass.SMALL)
	pRunMiguel.SetGender(App.CharacterClass.MALE)
	pRunMiguel.SetRandomAnimationChance(0.65)
	pRunMiguel.SetBlinkChance(0.1)
	pRunMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pRunMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_blink1.tga")
	pRunMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_blink2.tga")
	pRunMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_eyesclosed.tga")
	pRunMiguel.SetBlinkStages(3)

	pRunMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_a.tga")
	pRunMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_e.tga")
	pRunMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_u.tga")
	pRunMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pRunMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRunMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	return pRunMiguel


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
        
	pRunMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pRunMiguel == None):
		return
	
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pRunMiguel)



def ConfigureForType11(pRunMiguel):
	pRunMiguel.ClearAnimations()

	# Register animation mappings
	pRunMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.SmallAnimations.EBMoveFromL1ToS")
	pRunMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.SmallAnimations.EBMoveFromSToL1")
	pRunMiguel.AddAnimation("EBScienceTurnCaptain", "Bridge.Characters.SmallAnimations.EBTurnAtSTowardsCaptain")
	pRunMiguel.AddAnimation("EBScienceBackCaptain", "Bridge.Characters.SmallAnimations.EBTurnBackAtSFromCaptain")

	pRunMiguel.AddAnimation("EBScienceTurnC", "Bridge.Characters.SmallAnimations.EBSTalkC")
	pRunMiguel.AddAnimation("EBScienceBackC", "Bridge.Characters.CommonAnimations.SeatedS")
	pRunMiguel.AddAnimation("EBScienceTurnH", "Bridge.Characters.SmallAnimations.EBSTalkH")
	pRunMiguel.AddAnimation("EBScienceBackH", "Bridge.Characters.CommonAnimations.SeatedS")
	pRunMiguel.AddAnimation("EBScienceTurnE", "Bridge.Characters.SmallAnimations.EBSTalkE")
	pRunMiguel.AddAnimation("EBScienceBackE", "Bridge.Characters.CommonAnimations.SeatedS")
	pRunMiguel.AddAnimation("EBScienceTurnT", "Bridge.Characters.SmallAnimations.EBSTalkT")
	pRunMiguel.AddAnimation("EBScienceBackT", "Bridge.Characters.CommonAnimations.SeatedS")

	pRunMiguel.AddAnimation("EBScienceTurnX", "Bridge.Characters.SmallAnimations.EBSTalkE")
	pRunMiguel.AddAnimation("EBScienceBackX", "Bridge.Characters.CommonAnimations.SeatedS")

	pRunMiguel.AddAnimation("EBScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pRunMiguel.AddAnimation("EBScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pRunMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.SmallAnimations.EBMoveFromSToS1")
	pRunMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.SmallAnimations.EBMoveFromS1ToS")
	pRunMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.SmallAnimations.EBMoveFromSToS2")
	pRunMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.SmallAnimations.EBMoveFromS2ToS")
	pRunMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.SmallAnimations.EBMoveFromS1ToS2")
	pRunMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.SmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pRunMiguel.AddAnimation("EBScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pRunMiguel.AddAnimation("EBScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	#pRunMiguel.AddRandomAnimation("Bridge.Characters.AmbLargeAnimations.AmbTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	#pRunMiguel.AddAnimation("PushingButtons", "Bridge.Characters.AmbLargeAnimations.AmbTConsoleInteraction")


	# Hit animations
	pRunMiguel.AddAnimation("EBScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pRunMiguel.AddAnimation("EBScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pRunMiguel.AddAnimation("EBScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pRunMiguel.AddAnimation("EBScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	pRunMiguel.SetStanding(0)
	AddCommonAnimations(pRunMiguel)

	pRunMiguel.SetLocation("RunScience")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pRunMiguel):

	# Just random stuff
	pRunMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRunMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRunMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pRunMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pRunMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleLookDownForeLeft")
	pRunMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleLookUpForeRight")
	pRunMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")

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
