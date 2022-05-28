###############################################################################
#	Filename:	AmbSaffi.py
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
	pAmbSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pAmbSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pAmbSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbSaffi)

	# Setup the character configuration
	pAmbSaffi.SetSize(App.CharacterClass.MEDIUM)
	pAmbSaffi.SetGender(App.CharacterClass.FEMALE)
	pAmbSaffi.SetRandomAnimationChance(.75)
	pAmbSaffi.SetBlinkChance(0.1)
	pAmbSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pAmbSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pAmbSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pAmbSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pAmbSaffi.SetBlinkStages(3)

	pAmbSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pAmbSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pAmbSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pAmbSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pAmbSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pAmbSaffi


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
	pAmbSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pAmbSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pAmbSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pAmbSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pAmbSaffi):
#	debug("Configuring Saffi for the Ambassador bridge")

	# Clear out any old animations from another configuration
	pAmbSaffi.ClearAnimations()

	# Register animation mappings
	pAmbSaffi.AddAnimation("SeatedAmbCommander", "Bridge.Characters.AmbMediumAnimations.Amb_seated_C")
	pAmbSaffi.AddAnimation("StandingAmbCommander", "Bridge.Characters.AmbMediumAnimations.Amb_seated_C")
	pAmbSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.AmbMediumAnimations.EBMoveFromL1ToC")
	pAmbSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.AmbMediumAnimations.EBMoveFromCToL1")
	pAmbSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.AmbMediumAnimations.EBMoveFromCToC1")
	pAmbSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.AmbMediumAnimations.EBMoveFromC1ToC")
	pAmbSaffi.AddAnimation("AmbCommanderTurnCaptain", "Bridge.Characters.AmbMediumAnimations.AmbTNGTurnAtCTowardsCaptain")
	pAmbSaffi.AddAnimation("AmbCommanderBackCaptain", "Bridge.Characters.AmbMediumAnimations.AmbTNGTurnBackAtCFromCaptain")

	pAmbSaffi.AddAnimation("AmbCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pAmbSaffi.AddAnimation("AmbCommanderGlanceAwayCaptain", "Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")
	pAmbSaffi.AddAnimation("AmbCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pAmbSaffi.AddAnimation("AmbCommander1GlanceAwayCaptain", "Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")

	pAmbSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.AmbMediumAnimations.EBCTalkE")
	pAmbSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.AmbMediumAnimations.Amb_seated_C")
	pAmbSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.AmbMediumAnimations.EBCTalkH")
	pAmbSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.AmbMediumAnimations.Amb_seated_C")
	pAmbSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.AmbMediumAnimations.EBCTalkT")
	pAmbSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.AmbMediumAnimations.Amb_seated_C")
	pAmbSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.AmbMediumAnimations.EBCTalkS")
	pAmbSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.AmbMediumAnimations.Amb_seated_C")

	pAmbSaffi.AddAnimation("EBCommanderTurAmb", "Bridge.Characters.AmbMediumAnimations.EBCTalkE")
	pAmbSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.AmbMediumAnimations.Amb_seated_C")

	# Breathing
	pAmbSaffi.AddAnimation("AmbCommanderBreathe", "Bridge.Characters.AmbMediumAnimations.Amb_seated_C")
	pAmbSaffi.AddAnimation("AmbCommander1Breathe", "Bridge.Characters.AmbMediumAnimations.Amb_seated_C")
	pAmbSaffi.AddAnimation("AmbCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pAmbSaffi.AddAnimation("AmbCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	#pAmbSaffi.AddRandomAnimation("Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction", App.CharacterClass.STANDING_ONLY, 25, 1)
	#pAmbSaffi.AddAnimation("PushingButtons", "Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")

	# Hit animations
	pAmbSaffi.AddAnimation("AmbCommanderHit", "Bridge.Characters.AmbMediumAnimations.AmbCHit")
	pAmbSaffi.AddAnimation("AmbCommanderHitHard", "Bridge.Characters.AmbMediumAnimations.AmbCHitHard")
	#pAmbSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pAmbSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pAmbSaffi.AddAnimation("AmbCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pAmbSaffi.AddAnimation("AmbCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pAmbSaffi)
	pAmbSaffi.SetStanding(1)
	pAmbSaffi.SetLocation("AmbCommander")
	pAmbSaffi.AddPositionZoom("AmbCommander", 1.0)
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
#	Args:	pAmbSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbSaffi):
	pAmbSaffi.AddRandomAnimation("Bridge.Characters.AmbMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.STANDING_ONLY, 1, 1)

	pAmbSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	#pAmbSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.STANDING_ONLY)
	#pAmbSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.STANDING_ONLY)
	##pAmbSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.STANDING_ONLY)
	#pAmbSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.STANDING_ONLY)

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
