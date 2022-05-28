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
	pENAMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pENAMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pENAMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pENAMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAMiguel)

	# Setup the character configuration
	pENAMiguel.SetSize(App.CharacterClass.SMALL)
	pENAMiguel.SetGender(App.CharacterClass.MALE)
	pENAMiguel.SetRandomAnimationChance(.75)
	pENAMiguel.SetBlinkChance(0.1)
	pENAMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pENAMiguel.AdENAacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pENAMiguel.AdENAacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pENAMiguel.AdENAacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pENAMiguel.SetBlinkStages(3)

	pENAMiguel.AdENAacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pENAMiguel.AdENAacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pENAMiguel.AdENAacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pENAMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pENAMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENAMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pENAMiguel


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
	pENAMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pENAMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pENAMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pENAMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pENAMiguel):
#	kDebugObj.Print("Configuring Miguel for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	pENAMiguel.ClearAnimations()

	# Register animation mappings
	pENAMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.ENASmallAnimations.EBMoveFromL1ToS")
	pENAMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.ENASmallAnimations.EBMoveFromSToL1")
	pENAMiguel.AddAnimation("ENAScienceTurnCaptain", "Bridge.Characters.ENASmallAnimations.ENATurnAtSTowardsCaptain")
	pENAMiguel.AddAnimation("ENAScienceBackCaptain", "Bridge.Characters.ENASmallAnimations.ENATurnBackAtSFromCaptain")

	pENAMiguel.AddAnimation("ENAScienceTurnC", "Bridge.Characters.ENASmallAnimations.ENATurnAtSTowardsCaptain")
	pENAMiguel.AddAnimation("ENAScienceBackC", "Bridge.Characters.CommonAnimations.SeatedL")
	pENAMiguel.AddAnimation("ENAScienceTurnH", "Bridge.Characters.ENASmallAnimations.EBSTalkH")
	pENAMiguel.AddAnimation("ENAScienceBackH", "Bridge.Characters.CommonAnimations.SeatedL")
	pENAMiguel.AddAnimation("ENAScienceTurnE", "Bridge.Characters.ENASmallAnimations.EBSTalkE")
	pENAMiguel.AddAnimation("ENAScienceBackE", "Bridge.Characters.CommonAnimations.SeatedL")
	pENAMiguel.AddAnimation("ENAScienceTurnT", "Bridge.Characters.ENASmallAnimations.EBSTalkT")
	pENAMiguel.AddAnimation("ENAScienceBackT", "Bridge.Characters.CommonAnimations.SeatedL")

	pENAMiguel.AddAnimation("ENAScienceTurENA", "Bridge.Characters.ENASmallAnimations.EBSTalkE")
	pENAMiguel.AddAnimation("ENAScienceBackX", "Bridge.Characters.CommonAnimations.SeatedL")

	pENAMiguel.AddAnimation("ENAScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pENAMiguel.AddAnimation("ENAScienceGlanceAwayCaptain", "Bridge.Characters.ENASmallAnimations.ENASConsoleInteraction")

	pENAMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.ENASmallAnimations.EBMoveFromSToS1")
	pENAMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.ENASmallAnimations.EBMoveFromS1ToS")
	pENAMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.ENASmallAnimations.EBMoveFromSToS2")
	pENAMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.ENASmallAnimations.EBMoveFromS2ToS")
	pENAMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.ENASmallAnimations.EBMoveFromS1ToS2")
	pENAMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.ENASmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pENAMiguel.AddAnimation("ENAScienceBreathe", "Bridge.Characters.CommonAnimations.SeatedS")
	pENAMiguel.AddAnimation("ENAScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pENAMiguel.AddRandomAnimation("Bridge.Characters.ENASmallAnimations.ENASConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pENAMiguel.AddAnimation("PushingButtons", "Bridge.Characters.ENASmallAnimations.ENASConsoleInteraction")

	# Hit animations
	pENAMiguel.AddAnimation("ENAScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENAMiguel.AddAnimation("ENAScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENAMiguel.AddAnimation("ENAScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pENAMiguel.AddAnimation("ENAScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pENAMiguel)

	# Miguel stamds on the ENA bridge
	pENAMiguel.SetLocation("ENAScience")
	pENAMiguel.SetStanding(0)
#	pENAMiguel.SetLookAtAdj(30, -10, 8)
#	pENAMiguel.AddPositionZoom("ENAScience", 0.7, "Science")
	pENAMiguel.AddPositionZoom("ENAScience", 0.4)
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
#	Args:	pENAMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENAMiguel):
	pENAMiguel.AddRandomAnimation("Bridge.Characters.ENASmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pENAMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pENAMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pENAMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENAMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENAMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pENAMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pENAMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENAMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pENAMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
						"TargetFrontShielENAailed",
						"TargetFrontShieldDraining",
						"TargetRearShielENAailed",
						"TargetRearShieldDraining",
						"TargetLeftShielENAailed",
						"TargetLeftShieldDraining",
						"TargetRightShielENAailed",
						"TargetRightShieldDraining",
						"TargetTopShielENAailed",
						"TargetTopShieldDraining",
						"TargetBottomShielENAailed",
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
