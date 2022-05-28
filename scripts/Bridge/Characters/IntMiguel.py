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
	pIntMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pIntMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Miguel/miguel_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/miguel_head.tga")

	pIntMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pIntMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntMiguel)

	# Setup the character configuration
	pIntMiguel.SetSize(App.CharacterClass.SMALL)
	pIntMiguel.SetGender(App.CharacterClass.MALE)
	pIntMiguel.SetRandomAnimationChance(.75)
	pIntMiguel.SetBlinkChance(0.1)
	pIntMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pIntMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink1.tga")
	pIntMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_blink2.tga")
	pIntMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_eyesclosed.tga")
	pIntMiguel.SetBlinkStages(3)

	pIntMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_a.tga")
	pIntMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_e.tga")
	pIntMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Miguel/Miguel_head_u.tga")
	pIntMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pIntMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pIntMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Miguel")
	return pIntMiguel


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
	pIntMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pIntMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pIntMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#

###############################################################################
#	ConfigureForIntrepid()
#
#	Configure ourselves for the Intrepid bridge
#
#	Args:	pIntMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pIntMiguel):
#	kDebugObj.Print("Configuring Miguel for the Intrepid bridge")

	# Clear out any old animations from another configuration
	pIntMiguel.ClearAnimations()

	# Register animation mappings
	pIntMiguel.AddAnimation("EBL1SToS", "Bridge.Characters.IntSmallAnimations.EBMoveFromL1ToS")
	pIntMiguel.AddAnimation("EBScienceToL1", "Bridge.Characters.IntSmallAnimations.EBMoveFromSToL1")
	pIntMiguel.AddAnimation("IntScienceTurnCaptain", "Bridge.Characters.IntSmallAnimations.IntTurnAtSTowardsCaptain")
	pIntMiguel.AddAnimation("IntScienceBackCaptain", "Bridge.Characters.IntSmallAnimations.IntTurnBackAtSFromCaptain")

	pIntMiguel.AddAnimation("IntScienceTurnC", "Bridge.Characters.IntSmallAnimations.IntTurnAtSTowardsCaptain")
	pIntMiguel.AddAnimation("IntScienceBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntMiguel.AddAnimation("IntScienceTurnH", "Bridge.Characters.IntSmallAnimations.EBSTalkH")
	pIntMiguel.AddAnimation("IntScienceBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntMiguel.AddAnimation("IntScienceTurnE", "Bridge.Characters.IntSmallAnimations.EBSTalkE")
	pIntMiguel.AddAnimation("IntScienceBackE", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntMiguel.AddAnimation("IntScienceTurnT", "Bridge.Characters.IntSmallAnimations.EBSTalkT")
	pIntMiguel.AddAnimation("IntScienceBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pIntMiguel.AddAnimation("IntScienceTurnX", "Bridge.Characters.IntSmallAnimations.EBSTalkE")
	pIntMiguel.AddAnimation("IntScienceBackX", "Bridge.Characters.CommonAnimations.StandingConsole")

	pIntMiguel.AddAnimation("IntScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pIntMiguel.AddAnimation("IntScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")

	pIntMiguel.AddAnimation("EBScienceToS1", "Bridge.Characters.IntSmallAnimations.EBMoveFromSToS1")
	pIntMiguel.AddAnimation("EBScience1ToS", "Bridge.Characters.IntSmallAnimations.EBMoveFromS1ToS")
	pIntMiguel.AddAnimation("EBScienceToS2", "Bridge.Characters.IntSmallAnimations.EBMoveFromSToS2")
	pIntMiguel.AddAnimation("EBScience2ToS", "Bridge.Characters.IntSmallAnimations.EBMoveFromS2ToS")
	pIntMiguel.AddAnimation("EBScience1ToS2", "Bridge.Characters.IntSmallAnimations.EBMoveFromS1ToS2")
	pIntMiguel.AddAnimation("EBScience2ToS1", "Bridge.Characters.IntSmallAnimations.EBMoveFromS2ToS1")

	# Breathing	
	pIntMiguel.AddAnimation("IntScienceBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntMiguel.AddAnimation("IntScienceBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pIntMiguel.AddRandomAnimation("Bridge.Characters.IntSmallAnimations.IntSConsoleInteraction", App.CharacterClass.STANDING_ONLY, 25, 1)

	# So the mission builders can force the call
	pIntMiguel.AddAnimation("PushingButtons", "Bridge.Characters.IntSmallAnimations.IntSConsoleInteraction")

	# Hit animations
	pIntMiguel.AddAnimation("IntScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pIntMiguel.AddAnimation("IntScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pIntMiguel.AddAnimation("IntScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pIntMiguel.AddAnimation("IntScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pIntMiguel)

	# Miguel stamds on the Intrepid bridge
	pIntMiguel.SetLocation("IntScience")
	pIntMiguel.SetStanding(1)
	pIntMiguel.SetLookAtAdj(90, 60, 60)
	pIntMiguel.AddPositionZoom("IntScience", 0.3, "Science")
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
#	Args:	pIntMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntMiguel):
	pIntMiguel.AddRandomAnimation("Bridge.Characters.IntSmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pIntMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pIntMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pIntMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pIntMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pIntMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pIntMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pIntMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
