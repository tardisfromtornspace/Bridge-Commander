###############################################################################
#	Filename:	Saffi.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Saffi Larsen, XO, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print

###############################################################################
#	CreateCharacter()
#
#	Create Saffi by building her character and placing her on the passed in set.
#	Create her menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	debug("Creating Saffi")

	if (pSet.GetObject("XO") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("XO")))
	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", None)
	pnovaSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pnovaSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pnovaSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaSaffi)

	# Setup the character configuration
	pnovaSaffi.SetSize(App.CharacterClass.MEDIUM)
	pnovaSaffi.SetGender(App.CharacterClass.FEMALE)
	pnovaSaffi.SetRandomAnimationChance(.75)
	pnovaSaffi.SetBlinkChance(0.1)
	pnovaSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pnovaSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pnovaSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pnovaSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pnovaSaffi.SetBlinkStages(3)

	pnovaSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pnovaSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pnovaSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pnovaSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pnovaSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pnovaSaffi


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
	pnovaSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pnovaSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pnovaSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pnovaSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pnovaSaffi):
#	debug("Configuring Saffi for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pnovaSaffi.ClearAnimations()

	# Register animation mappings
	pnovaSaffi.AddAnimation("SeatedIntCommander", "Bridge.Characters.CommonAnimations.SeatedM")
	pnovaSaffi.AddAnimation("StandingIntCommander", "Bridge.Characters.CommonAnimations.Standing")
	pnovaSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.IntMediumAnimations.EBMoveFromL1ToC")
	pnovaSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.IntMediumAnimations.EBMoveFromCToL1")
	pnovaSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.IntMediumAnimations.EBMoveFromCToC1")
	pnovaSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.IntMediumAnimations.EBMoveFromC1ToC")
	pnovaSaffi.AddAnimation("IntCommanderTurnCaptain", "Bridge.Characters.IntMediumAnimations.IntTurnAtCTowardsCaptain")
	pnovaSaffi.AddAnimation("IntCommanderBackCaptain", "Bridge.Characters.IntMediumAnimations.IntTurnBackAtCFromCaptain")

	pnovaSaffi.AddAnimation("IntCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pnovaSaffi.AddAnimation("IntCommanderGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")
	pnovaSaffi.AddAnimation("IntCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pnovaSaffi.AddAnimation("IntCommander1GlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	pnovaSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.IntMediumAnimations.EBCTalkE")
	pnovaSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.CommonAnimations.SeatedM")
	pnovaSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.IntMediumAnimations.EBCTalkH")
	pnovaSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.CommonAnimations.SeatedM")
	pnovaSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.IntMediumAnimations.EBCTalkT")
	pnovaSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.CommonAnimations.SeatedM")
	pnovaSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.IntMediumAnimations.EBCTalkS")
	pnovaSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.CommonAnimations.SeatedM")

	pnovaSaffi.AddAnimation("EBCommanderTurnX", "Bridge.Characters.IntMediumAnimations.EBCTalkE")
	pnovaSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pnovaSaffi.AddAnimation("IntCommanderBreathe", "Bridge.Characters.CommonAnimations.SeatedM")
	pnovaSaffi.AddAnimation("IntCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pnovaSaffi.AddAnimation("IntCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pnovaSaffi.AddAnimation("IntCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pnovaSaffi.AddRandomAnimation("Bridge.Characters.IntMediumAnimations.IntCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# Hit animations
	pnovaSaffi.AddAnimation("IntCommanderHit", "Bridge.Characters.IntMediumAnimations.IntCHit")
	pnovaSaffi.AddAnimation("IntCommanderHitHard", "Bridge.Characters.IntMediumAnimations.IntCHitHard")
	#pnovaSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pnovaSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pnovaSaffi.AddAnimation("IntCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pnovaSaffi.AddAnimation("IntCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pnovaSaffi)
	pnovaSaffi.SetStanding(0)
	pnovaSaffi.SetLocation("novaCommander")
	pnovaSaffi.SetTranslateXYZ(0.000000, 30.000000, -53.000000)
	pnovaSaffi.AddPositionZoom("novaCommander", 0.55)
#	debug("Finished configuring Saffi")

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pnovaSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaSaffi):
	pnovaSaffi.AddRandomAnimation("Bridge.Characters.novaMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pnovaSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pnovaSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pnovaSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pnovaSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pnovaSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

###############################################################################
#	LoadSounds
#	
#	Load any of Saffi's general or spontaneous sounds, so they don't
#	hitch the game when they're played.
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
	
	#
	# Build a list of sound to load
	#
	lSoundList =	[
		# Yes?
		"gf001",
		"gf002",

		# Report.
		"gf020",

		# Alert lines.
		"GreenAlert",
		"GreenAlert2",
		"GreenAlert3",
		"YellowAlert",
		"YellowAlert3",
		"YellowAlert2",
		"RedAlert",
		"RedAlert2",

		# Contacting starfleet.
		"gl004",
		"gl005",
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for sLine in lSoundList:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)
