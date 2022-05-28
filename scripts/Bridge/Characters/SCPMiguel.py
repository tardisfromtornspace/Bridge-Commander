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
	pSCPMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pSCPMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pSCPMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPMiguel)

	# Setup the character configuration
	pSCPMiguel.SetSize(App.CharacterClass.SMALL)
	pSCPMiguel.SetGender(App.CharacterClass.MALE)
	pSCPMiguel.SetRandomAnimationChance(.75)
	pSCPMiguel.SetBlinkChance(0.1)
	pSCPMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pSCPMiguel.AdSCPacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pSCPMiguel.AdSCPacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pSCPMiguel.AdSCPacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pSCPMiguel.SetBlinkStages(3)

	pSCPMiguel.AdSCPacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pSCPMiguel.AdSCPacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pSCPMiguel.AdSCPacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pSCPMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pSCPMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pSCPMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pSCPMiguel


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
	pSCPMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pSCPMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pSCPMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pSCPMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pSCPMiguel):
#	kDebugObj.Print("Configuring Miguel for the Galor bridge")

	# Clear out any old animations from another configuration
	pSCPMiguel.ClearAnimations()

	# Register animation mappings
	pSCPMiguel.AddAnimation("SeatedSCPScience", "Bridge.Characters.CommonAnimations.StandingConsole")
	pSCPMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.CommonAnimations.StandingConsole")
	pSCPMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.CommonAnimations.StandingConsole")
	pSCPMiguel.AddAnimation("SCPScienceTurnCaptain", "Bridge.Characters.SCPSmallAnimations.SCPTurnAtSTowardsCaptain")
	pSCPMiguel.AddAnimation("SCPScienceBackCaptain", "Bridge.Characters.SCPSmallAnimations.SCPTurnBackAtSFromCaptain")

	pSCPMiguel.AddAnimation("SCPScienceTurnC", "Bridge.Characters.SCPSmallAnimations.SCPTurnAtSTowardsCaptain")
	pSCPMiguel.AddAnimation("SCPScienceBackC", "Bridge.Characters.SCPSmallAnimations.SCPTurnBackAtSFromCaptain")
	pSCPMiguel.AddAnimation("SCPScienceTurnH", "Bridge.Characters.SCPSmallAnimations.EBSTalkH")
	pSCPMiguel.AddAnimation("SCPScienceBackH", "Bridge.Characters.SCPSmallAnimations.SCPSConsoleInteraction")
	pSCPMiguel.AddAnimation("SCPScienceTurnE", "Bridge.Characters.SCPSmallAnimations.EBSTalkE")
	pSCPMiguel.AddAnimation("SCPScienceBackE", "Bridge.Characters.SCPSmallAnimations.SCPSConsoleInteraction")
	pSCPMiguel.AddAnimation("SCPScienceTurnT", "Bridge.Characters.SCPSmallAnimations.EBSTalkT")
	pSCPMiguel.AddAnimation("SCPScienceBackT", "Bridge.Characters.SCPSmallAnimations.SCPSConsoleInteraction")

	pSCPMiguel.AddAnimation("SCPScienceTurnX", "Bridge.Characters.SCPSmallAnimations.EBSTalkE")
	pSCPMiguel.AddAnimation("SCPScienceBackX", "Bridge.Characters.SCPSmallAnimations.SCPSConsoleInteraction")

	pSCPMiguel.AddAnimation("SCPScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pSCPMiguel.AddAnimation("SCPScienceGlanceAwayCaptain", "Bridge.Characters.SCPSmallAnimations.SCPSConsoleInteraction")

	pSCPMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.SCPSmallAnimations.EBMoveFromSToS1")
	pSCPMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.SCPSmallAnimations.EBMoveFromS1ToS")
	pSCPMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.SCPSmallAnimations.EBMoveFromSToS2")
	pSCPMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.SCPSmallAnimations.EBMoveFromS2ToS")
	pSCPMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.SCPSmallAnimations.EBMoveFromS1ToS2")
	pSCPMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.SCPSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pSCPMiguel.AddAnimation("SCPScienceBreathe", "Bridge.Characters.SCPSmallAnimations.SCPSConsoleInteraction")
	pSCPMiguel.AddAnimation("SCPScienceBreatheTurned", "Bridge.Characters.SCPSmallAnimations.SCPSConsoleInteraction")

	# Interaction
	pSCPMiguel.AddRandomAnimation("Bridge.Characters.SCPSmallAnimations.SCPSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pSCPMiguel.AddAnimation("PushingButtons", "Bridge.Characters.SCPSmallAnimations.SCPSConsoleInteraction")

	# Hit animations
	pSCPMiguel.AddAnimation("SCPScienceHit", "Bridge.Characters.SCPMediumAnimations.SCPsHit")
	pSCPMiguel.AddAnimation("SCPScienceHitHard", "Bridge.Characters.SCPMediumAnimations.SCPsHitHard")
	pSCPMiguel.AddAnimation("SCPScienceReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft");
	pSCPMiguel.AddAnimation("SCPScienceReactRight", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pSCPMiguel)

	# Miguel stamds on the SCP bridge
	pSCPMiguel.SetLocation("SCPScience")
	pSCPMiguel.SetStanding(0)
#	pSCPMiguel.SetLookAtAdj(30, -10, 8)
#	pSCPMiguel.AddPositionZoom("SCPScience", 0.7, "Science")
	pSCPMiguel.AddPositionZoom("SCPScience", 0.4)
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
#	Args:	pSCPMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPMiguel):
	pSCPMiguel.AddRandomAnimation("Bridge.Characters.SCPSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1,1)
	#pSCPMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pSCPMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pSCPMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pSCPMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	#pSCPMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pSCPMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pSCPMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pSCPMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
						"TargetFrontShielSCPailed",
						"TargetFrontShieldDraining",
						"TargetRearShielSCPailed",
						"TargetRearShieldDraining",
						"TargetLeftShielSCPailed",
						"TargetLeftShieldDraining",
						"TargetRightShielSCPailed",
						"TargetRightShieldDraining",
						"TargetTopShielSCPailed",
						"TargetTopShieldDraining",
						"TargetBottomShielSCPailed",
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
