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
	ppromMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	ppromMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	ppromMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(ppromMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromMiguel)

	# Setup the character configuration
	ppromMiguel.SetSize(App.CharacterClass.SMALL)
	ppromMiguel.SetGender(App.CharacterClass.MALE)
	ppromMiguel.SetRandomAnimationChance(.75)
	ppromMiguel.SetBlinkChance(0.1)
	ppromMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	ppromMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	ppromMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	ppromMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	ppromMiguel.SetBlinkStages(3)

	ppromMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	ppromMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	ppromMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	ppromMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(ppromMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	ppromMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return ppromMiguel


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
	ppromMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (ppromMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(ppromMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	ppromMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(ppromMiguel):
#	kDebugObj.Print("Configuring Miguel for the prometheus bridge")

	# Clear out any old animations from another configuration
	ppromMiguel.ClearAnimations()

	# Register animation mappings
	ppromMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.promSmallAnimations.EBMoveFromL1ToS")
	ppromMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.promSmallAnimations.EBMoveFromSToL1")
	ppromMiguel.AddAnimation("promScienceTurnCaptain", "Bridge.Characters.promSmallAnimations.promTurnAtSTowardsCaptain")
	ppromMiguel.AddAnimation("promScienceBackCaptain", "Bridge.Characters.promSmallAnimations.promTurnBackAtSFromCaptain")

	ppromMiguel.AddAnimation("promScienceTurnC", "Bridge.Characters.promSmallAnimations.promTurnAtSTowardsCaptain")
	ppromMiguel.AddAnimation("promScienceBackC", "Bridge.Characters.CommonAnimations.SeatedL")
	ppromMiguel.AddAnimation("promScienceTurnH", "Bridge.Characters.promSmallAnimations.EBSTalkH")
	ppromMiguel.AddAnimation("promScienceBackH", "Bridge.Characters.CommonAnimations.SeatedL")
	ppromMiguel.AddAnimation("promScienceTurnE", "Bridge.Characters.promSmallAnimations.EBSTalkE")
	ppromMiguel.AddAnimation("promScienceBackE", "Bridge.Characters.CommonAnimations.SeatedL")
	ppromMiguel.AddAnimation("promScienceTurnT", "Bridge.Characters.promSmallAnimations.EBSTalkT")
	ppromMiguel.AddAnimation("promScienceBackT", "Bridge.Characters.CommonAnimations.SeatedL")

	ppromMiguel.AddAnimation("promScienceTurprom", "Bridge.Characters.promSmallAnimations.EBSTalkE")
	ppromMiguel.AddAnimation("promScienceBackX", "Bridge.Characters.CommonAnimations.SeatedL")

	ppromMiguel.AddAnimation("promScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	ppromMiguel.AddAnimation("promScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedS")

	ppromMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.promSmallAnimations.EBMoveFromSToS1")
	ppromMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.promSmallAnimations.EBMoveFromS1ToS")
	ppromMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.promSmallAnimations.EBMoveFromSToS2")
	ppromMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.promSmallAnimations.EBMoveFromS2ToS")
	ppromMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.promSmallAnimations.EBMoveFromS1ToS2")
	ppromMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.promSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	ppromMiguel.AddAnimation("promScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	ppromMiguel.AddAnimation("promScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	ppromMiguel.AddRandomAnimation("Bridge.Characters.promSmallAnimations.promSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	ppromMiguel.AddAnimation("PushingButtons", "Bridge.Characters.promSmallAnimations.promSConsoleInteraction")

	# Hit animations
	ppromMiguel.AddAnimation("promScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	ppromMiguel.AddAnimation("promScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	ppromMiguel.AddAnimation("promScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	ppromMiguel.AddAnimation("promScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(ppromMiguel)

	# Miguel stamds on the prom bridge
	ppromMiguel.SetLocation("promScience")
	ppromMiguel.SetStanding(0)
	ppromMiguel.SetLookAtAdj(-0.001, -10, 10)
	ppromMiguel.AddPositionZoom("promScience", 0.7, "Science")
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
#	Args:	ppromMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromMiguel):
	ppromMiguel.AddRandomAnimation("Bridge.Characters.promSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#ppromMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#ppromMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	ppromMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	ppromMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	ppromMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	ppromMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	ppromMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#ppromMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
