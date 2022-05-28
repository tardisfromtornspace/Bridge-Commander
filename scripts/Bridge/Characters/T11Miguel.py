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
	pT11Miguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pT11Miguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedTeal_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/miguel_head.tga")


	pT11Miguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pT11Miguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pT11Miguel)

	# Setup the character configuration
	pT11Miguel.SetSize(App.CharacterClass.LARGE)
	pT11Miguel.SetGender(App.CharacterClass.MALE)
	pT11Miguel.SetRandomAnimationChance(.75)
	pT11Miguel.SetBlinkChance(0.1)
	pT11Miguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pT11Miguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_blink1.tga")
	pT11Miguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_blink2.tga")
	pT11Miguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_eyesclosed.tga")
	pT11Miguel.SetBlinkStages(3)

	pT11Miguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_a.tga")
	pT11Miguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_e.tga")
	pT11Miguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/Miguel_head_u.tga")
	pT11Miguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pT11Miguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pT11Miguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	return pT11Miguel


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
        
	pT11Miguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pT11Miguel == None):
		return
	
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pT11Miguel)



def ConfigureForType11(pT11Miguel):
	pT11Miguel.ClearAnimations()

	# Register animation mappings
	pT11Miguel.AddAnimation("EBL1SToS", "Bridge.Characters.SmallAnimations.EBMoveFromL1ToS")
	pT11Miguel.AddAnimation("EBScienceToL1", "Bridge.Characters.SmallAnimations.EBMoveFromSToL1")
	pT11Miguel.AddAnimation("EBScienceTurnCaptain", "Bridge.Characters.SmallAnimations.EBTurnAtSTowardsCaptain")
	pT11Miguel.AddAnimation("EBScienceBackCaptain", "Bridge.Characters.SmallAnimations.EBTurnBackAtSFromCaptain")

	pT11Miguel.AddAnimation("EBScienceTurnC", "Bridge.Characters.SmallAnimations.EBSTalkC")
	pT11Miguel.AddAnimation("EBScienceBackC", "Bridge.Characters.CommonAnimations.SeatedS")
	pT11Miguel.AddAnimation("EBScienceTurnH", "Bridge.Characters.SmallAnimations.EBSTalkH")
	pT11Miguel.AddAnimation("EBScienceBackH", "Bridge.Characters.CommonAnimations.SeatedS")
	pT11Miguel.AddAnimation("EBScienceTurnE", "Bridge.Characters.SmallAnimations.EBSTalkE")
	pT11Miguel.AddAnimation("EBScienceBackE", "Bridge.Characters.CommonAnimations.SeatedS")
	pT11Miguel.AddAnimation("EBScienceTurnT", "Bridge.Characters.SmallAnimations.EBSTalkT")
	pT11Miguel.AddAnimation("EBScienceBackT", "Bridge.Characters.CommonAnimations.SeatedS")

	pT11Miguel.AddAnimation("EBScienceTurnX", "Bridge.Characters.SmallAnimations.EBSTalkE")
	pT11Miguel.AddAnimation("EBScienceBackX", "Bridge.Characters.CommonAnimations.SeatedS")

	pT11Miguel.AddAnimation("EBScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pT11Miguel.AddAnimation("EBScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pT11Miguel.AddAnimation("EBScienceToS1", "Bridge.Characters.SmallAnimations.EBMoveFromSToS1")
	pT11Miguel.AddAnimation("EBScience1ToS", "Bridge.Characters.SmallAnimations.EBMoveFromS1ToS")
	pT11Miguel.AddAnimation("EBScienceToS2", "Bridge.Characters.SmallAnimations.EBMoveFromSToS2")
	pT11Miguel.AddAnimation("EBScience2ToS", "Bridge.Characters.SmallAnimations.EBMoveFromS2ToS")
	pT11Miguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.SmallAnimations.EBMoveFromS1ToS2")
	pT11Miguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.SmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pT11Miguel.AddAnimation("EBScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pT11Miguel.AddAnimation("EBScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pT11Miguel.AddRandomAnimation("Bridge.Characters.SmallAnimations.EBSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pT11Miguel.AddAnimation("PushingButtons", "Bridge.Characters.SmallAnimations.EBSConsoleInteraction")

	# Hit animations
	pT11Miguel.AddAnimation("EBScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pT11Miguel.AddAnimation("EBScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pT11Miguel.AddAnimation("EBScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pT11Miguel.AddAnimation("EBScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	pT11Miguel.SetStanding(0)
	AddCommonAnimations(pT11Miguel)

	pT11Miguel.SetLocation("T11Science")
	pT11Miguel.SetTranslateXYZ(-45.000000, 58.000000, 7.000000)


def AddCommonAnimations(pT11Miguel):

	# Just random stuff
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Yawn")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Sigh")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Neck_Rub")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Hair_Wipe")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleLookDownForeLeft")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleLookUpForeRight")
	pT11Miguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")

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
