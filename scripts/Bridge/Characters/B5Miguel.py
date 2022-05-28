###############################################################################
#	Filename:	RomMiguel.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads RomMiguel Diaz, science, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create RomMiguel by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating RomMiguel")

	if (pSet.GetObject("Science") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Science")))
	

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "B5/HeadMiguel/miguel_head.NIF", None)
	pRomMiguel = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.NIF", CharacterPaths.g_pcHeadNIFPath + "B5/HeadMiguel/miguel_head.NIF")
	pRomMiguel.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "B5/BodyMaleM/FedTeal_body.tga", CharacterPaths.g_pcHeadTexPath + "B5/HeadMiguel/miguel_head.tga")

	pRomMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pRomMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRomMiguel)

	# Setup the character configuration
	pRomMiguel.SetSize(App.CharacterClass.SMALL)
	pRomMiguel.SetGender(App.CharacterClass.MALE)
	pRomMiguel.SetRandomAnimationChance(.75)
	pRomMiguel.SetBlinkChance(0.1)
	pRomMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	LoadSounds()

	pRomMiguel.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "B5/HeadMiguel/miguel_head_blink1.tga")
	pRomMiguel.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "B5/HeadMiguel/miguel_head_blink2.tga")
	pRomMiguel.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "B5/HeadMiguel/miguel_head_eyesclosed.tga")
	pRomMiguel.SetBlinkStages(3)

	pRomMiguel.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "B5/HeadMiguel/miguel_head_a.tga")
	pRomMiguel.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "B5/HeadMiguel/miguel_head_e.tga")
	pRomMiguel.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "B5/HeadMiguel/miguel_head_u.tga")
	pRomMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pRomMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRomMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating RomMiguel")
	return pRomMiguel


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
	pRomMiguel = App.CharacterClass_Cast(pSet.GetObject("Science"))
	if (pRomMiguel == None):
#		kDebugObj.Print("******* Science officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Science..")
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pRomMiguel)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Receiving probe data"
	#



###############################################################################
#	ConfigureForWarbird()
#
#	Configure ourselves for the Warbird bridge
#
#	Args:	pRomMiguel	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForWarbird(pRomMiguel):
#	kDebugObj.Print("Configuring RomMiguel for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pRomMiguel.ClearAnimations()

	# Register animation mappings
	pRomMiguel.AddAnimation("DBL1SToS", "Bridge.Characters.SmallAnimations.MoveFromL1ToS")
	pRomMiguel.AddAnimation("DBScienceToL1", "Bridge.Characters.SmallAnimations.MoveFromSToL1")
	pRomMiguel.AddAnimation("DBScienceTurnCaptain", "Bridge.Characters.SmallAnimations.TurnAtSTowardsCaptain")
	pRomMiguel.AddAnimation("DBScienceBackCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")

	pRomMiguel.AddAnimation("DBScienceTurnC", "Bridge.Characters.SmallAnimations.DBSTalkC")
	pRomMiguel.AddAnimation("DBScienceBackC", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomMiguel.AddAnimation("DBScienceTurnH", "Bridge.Characters.SmallAnimations.DBSTalkH")
	pRomMiguel.AddAnimation("DBScienceBackH", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomMiguel.AddAnimation("DBScienceTurnE", "Bridge.Characters.SmallAnimations.DBSTalkE")
	pRomMiguel.AddAnimation("DBScienceBackE", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomMiguel.AddAnimation("DBScienceTurnT", "Bridge.Characters.SmallAnimations.DBSTalkT")
	pRomMiguel.AddAnimation("DBScienceBackT", "Bridge.Characters.CommonAnimations.StandingConsole")

	pRomMiguel.AddAnimation("DBScienceTurnX", "Bridge.Characters.SmallAnimations.DBSTalkX")
	pRomMiguel.AddAnimation("DBScienceBackX", "Bridge.Characters.CommonAnimations.StandingConsole")

	pRomMiguel.AddAnimation("DBScienceGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pRomMiguel.AddAnimation("DBScienceGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.Standing")

	pRomMiguel.AddAnimation("LookAroundConsole", "Bridge.Characters.CommonAnimations.LookAroundConsoleDown")

	# Breathing	
	pRomMiguel.AddAnimation("DBScienceBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomMiguel.AddAnimation("DBScienceSBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pRomMiguel.AddRandomAnimation("Bridge.Characters.SmallAnimations.DBSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pRomMiguel.AddAnimation("PushingButtons", "Bridge.Characters.SmallAnimations.DBSConsoleInteraction")

	# Hit animations
	pRomMiguel.AddAnimation("DBScienceHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pRomMiguel.AddAnimation("DBScienceHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pRomMiguel.AddAnimation("DBScienceReactLeftStanding", "Bridge.Characters.CommonAnimations.ReactLeft");
	pRomMiguel.AddAnimation("DBScienceReactRightStanding", "Bridge.Characters.CommonAnimations.ReactRight");
	pRomMiguel.AddAnimation("DBScienceHitHardStandingTest", "Bridge.Characters.CommonAnimations.HitHardStanding")

	# Add common animations.
	AddCommonAnimations(pRomMiguel)

	# RomMiguel stands on the Galaxy bridge
	pRomMiguel.SetStanding(1)
	pRomMiguel.SetLocation("RomScience")
#	kDebugObj.Print("Finished configuring RomMiguel")



###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pRomMiguel	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pRomMiguel):
	pRomMiguel.AddRandomAnimation("Bridge.Characters.SmallAnimations.SLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	#pRomMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pRomMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	pRomMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRomMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRomMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pRomMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pRomMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pRomMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pRomMiguel.AddRandomAnimation("Bridge.Characters.CommonAnimations.Nod", App.CharacterClass.STANDING_ONLY)


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
