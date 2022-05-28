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
	pENBMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pENBMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pENBMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pENBMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBMiguel)

	# Setup the character configuration
	pENBMiguel.SetSize(App.CharacterClass.SMALL)
	pENBMiguel.SetGender(App.CharacterClass.MALE)
	pENBMiguel.SetRandomAnimationChance(.75)
	pENBMiguel.SetBlinkChance(0.1)
	pENBMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pENBMiguel.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pENBMiguel.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pENBMiguel.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pENBMiguel.SetBlinkStages(3)

	pENBMiguel.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pENBMiguel.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pENBMiguel.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pENBMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pENBMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENBMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pENBMiguel


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
	pENBMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pENBMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pENBMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pENBMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pENBMiguel):
#	kDebugObj.Print("Configuring Miguel for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	pENBMiguel.ClearAnimations()

	# Register animation mappings
	pENBMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.ENBSmallAnimations.EBMoveFromL1ToS")
	pENBMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.ENBSmallAnimations.EBMoveFromSToL1")
	pENBMiguel.AddAnimation("ENBScienceTurnCaptain", "Bridge.Characters.ENBSmallAnimations.ENBTurnAtSTowardsCaptain")
	pENBMiguel.AddAnimation("ENBScienceBackCaptain", "Bridge.Characters.ENBSmallAnimations.ENBTurnBackAtSFromCaptain")

	pENBMiguel.AddAnimation("ENBScienceTurnC", "Bridge.Characters.ENBSmallAnimations.ENBTurnAtSTowardsCaptain")
	pENBMiguel.AddAnimation("ENBScienceBackC", "Bridge.Characters.CommonAnimations.SeatedL")
	pENBMiguel.AddAnimation("ENBScienceTurnH", "Bridge.Characters.ENBSmallAnimations.EBSTalkH")
	pENBMiguel.AddAnimation("ENBScienceBackH", "Bridge.Characters.CommonAnimations.SeatedL")
	pENBMiguel.AddAnimation("ENBScienceTurnE", "Bridge.Characters.ENBSmallAnimations.EBSTalkE")
	pENBMiguel.AddAnimation("ENBScienceBackE", "Bridge.Characters.CommonAnimations.SeatedL")
	pENBMiguel.AddAnimation("ENBScienceTurnT", "Bridge.Characters.ENBSmallAnimations.EBSTalkT")
	pENBMiguel.AddAnimation("ENBScienceBackT", "Bridge.Characters.CommonAnimations.SeatedL")

	pENBMiguel.AddAnimation("ENBScienceTurnX", "Bridge.Characters.ENBSmallAnimations.EBSTalkE")
	pENBMiguel.AddAnimation("ENBScienceBackX", "Bridge.Characters.CommonAnimations.SeatedL")

	pENBMiguel.AddAnimation("ENBScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pENBMiguel.AddAnimation("ENBScienceGlanceAwayCaptain", "Bridge.Characters.ENBSmallAnimations.ENBSConsoleInteraction")

	pENBMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.ENBSmallAnimations.EBMoveFromSToS1")
	pENBMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.ENBSmallAnimations.EBMoveFromS1ToS")
	pENBMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.ENBSmallAnimations.EBMoveFromSToS2")
	pENBMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.ENBSmallAnimations.EBMoveFromS2ToS")
	pENBMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.ENBSmallAnimations.EBMoveFromS1ToS2")
	pENBMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.ENBSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pENBMiguel.AddAnimation("ENBScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pENBMiguel.AddAnimation("ENBScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pENBMiguel.AddRandomAnimation("Bridge.Characters.ENBSmallAnimations.ENBSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pENBMiguel.AddAnimation("PushingButtons", "Bridge.Characters.ENBSmallAnimations.ENBSConsoleInteraction")

	# Hit animations
	pENBMiguel.AddAnimation("ENBScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENBMiguel.AddAnimation("ENBScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENBMiguel.AddAnimation("ENBScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pENBMiguel.AddAnimation("ENBScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pENBMiguel)

	# Miguel stamds on the ENB bridge
	pENBMiguel.SetLocation("ENBScience")
	pENBMiguel.SetStanding(0)
#	pENBMiguel.SetLookAtAdj(30, -10, 8)
#	pENBMiguel.AddPositionZoom("ENBScience", 0.7, "Science")
	pENBMiguel.AddPositionZoom("ENBScience", 0.4)
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
#	Args:	pENBMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENBMiguel):
	pENBMiguel.AddRandomAnimation("Bridge.Characters.ENBSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pENBMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pENBMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pENBMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENBMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENBMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pENBMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pENBMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENBMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pENBMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
