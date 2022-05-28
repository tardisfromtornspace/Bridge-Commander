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
	pExcMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pExcMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pExcMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pExcMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcMiguel)

	# Setup the character configuration
	pExcMiguel.SetSize(App.CharacterClass.SMALL)
	pExcMiguel.SetGender(App.CharacterClass.MALE)
	pExcMiguel.SetRandomAnimationChance(.75)
	pExcMiguel.SetBlinkChance(0.1)
	pExcMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pExcMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pExcMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pExcMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pExcMiguel.SetBlinkStages(3)

	pExcMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pExcMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pExcMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pExcMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pExcMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pExcMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pExcMiguel


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
	pExcMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pExcMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pExcMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForExcalibur()
#
#	Configure ourselves for the Excalibur bridge
#
#	Args:	pExcMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pExcMiguel):
#	kDebugObj.Print("Configuring Miguel for the Excalibur bridge")

	# Clear out any old animations from another configuration
	pExcMiguel.ClearAnimations()

	# Register animation mappings
	pExcMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.ExcSmallAnimations.EBMoveFromL1ToS")
	pExcMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.ExcSmallAnimations.EBMoveFromSToL1")
	pExcMiguel.AddAnimation("ExcScienceTurnCaptain", "Bridge.Characters.ExcSmallAnimations.ExcTurnAtSTowardsCaptain")
	pExcMiguel.AddAnimation("ExcScienceBackCaptain", "Bridge.Characters.ExcSmallAnimations.ExcTurnBackAtSFromCaptain")

	pExcMiguel.AddAnimation("ExcScienceTurnC", "Bridge.Characters.ExcSmallAnimations.ExcTurnAtSTowardsCaptain")
	pExcMiguel.AddAnimation("ExcScienceBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pExcMiguel.AddAnimation("ExcScienceTurnH", "Bridge.Characters.ExcSmallAnimations.EBSTalkH")
	pExcMiguel.AddAnimation("ExcScienceBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pExcMiguel.AddAnimation("ExcScienceTurnE", "Bridge.Characters.ExcSmallAnimations.EBSTalkE")
	pExcMiguel.AddAnimation("ExcScienceBackE", "Bridge.Characters.CommonAnimations.StandingConsole")
	pExcMiguel.AddAnimation("ExcScienceTurnT", "Bridge.Characters.ExcSmallAnimations.EBSTalkT")
	pExcMiguel.AddAnimation("ExcScienceBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pExcMiguel.AddAnimation("ExcScienceTurnX", "Bridge.Characters.ExcSmallAnimations.EBSTalkE")
	pExcMiguel.AddAnimation("ExcScienceBackX", "Bridge.Characters.CommonAnimations.StandingConsole")

	pExcMiguel.AddAnimation("ExcScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pExcMiguel.AddAnimation("ExcScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	pExcMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.ExcSmallAnimations.EBMoveFromSToS1")
	pExcMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.ExcSmallAnimations.EBMoveFromS1ToS")
	pExcMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.ExcSmallAnimations.EBMoveFromSToS2")
	pExcMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.ExcSmallAnimations.EBMoveFromS2ToS")
	pExcMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.ExcSmallAnimations.EBMoveFromS1ToS2")
	pExcMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.ExcSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pExcMiguel.AddAnimation("ExcScienceBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pExcMiguel.AddAnimation("ExcScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pExcMiguel.AddRandomAnimation("Bridge.Characters.ExcSmallAnimations.ExcEConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pExcMiguel.AddAnimation("PushingButtons", "Bridge.Characters.ExcSmallAnimations.ExcEConsoleInteraction")

	# Hit animations
	pExcMiguel.AddAnimation("ExcScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pExcMiguel.AddAnimation("ExcScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pExcMiguel.AddAnimation("ExcScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pExcMiguel.AddAnimation("ExcScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pExcMiguel)

	# Miguel stamds on the Excalibur bridge
	pExcMiguel.SetLocation("ExcScience")
	pExcMiguel.SetStanding(0)
	pExcMiguel.SetLookAtAdj(-110, 0, 50)
	pExcMiguel.AddPositionZoom("ExcScience", 0.5, "Science")
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
#	Args:	pExcMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcMiguel):
	pExcMiguel.AddRandomAnimation("Bridge.Characters.ExcSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pExcMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pExcMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pExcMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pExcMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pExcMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pExcMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pExcMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
