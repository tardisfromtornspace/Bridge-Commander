from bcdebug import debug
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

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("XO") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("XO")))
	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", None)
	pEXLSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pEXLSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pEXLSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLSaffi)

	# Setup the character configuration
	pEXLSaffi.SetSize(App.CharacterClass.MEDIUM)
	pEXLSaffi.SetGender(App.CharacterClass.FEMALE)
	pEXLSaffi.SetRandomAnimationChance(.75)
	pEXLSaffi.SetBlinkChance(0.1)
	pEXLSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pEXLSaffi.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pEXLSaffi.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pEXLSaffi.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pEXLSaffi.SetBlinkStages(3)

	pEXLSaffi.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pEXLSaffi.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pEXLSaffi.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pEXLSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pEXLSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pEXLSaffi


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
	debug(__name__ + ", ConfigureForShip")
	pEXLSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pEXLSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pEXLSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pEXLSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pEXLSaffi):
#	debug("Configuring Saffi for the Excelsior bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcelsior")
	pEXLSaffi.ClearAnimations()

	# Register animation mappings
	pEXLSaffi.AddAnimation("SeatedEXLCommander", "Bridge.Characters.EXLMediumAnimations.EXLPlaceAtC")
	pEXLSaffi.AddAnimation("StandingEXLCommander", "Bridge.Characters.CommonAnimations.Standing")
	pEXLSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.EXLMediumAnimations.EBMoveFromL1ToC")
	pEXLSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.EXLMediumAnimations.EBMoveFromCToL1")
	pEXLSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.EXLMediumAnimations.EBMoveFromCToC1")
	pEXLSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.EXLMediumAnimations.EBMoveFromC1ToC")
	pEXLSaffi.AddAnimation("EXLCommanderTurnCaptain", "Bridge.Characters.EXLMediumAnimations.EXLTurnAtCTowardsCaptain")
	pEXLSaffi.AddAnimation("EXLCommanderBackCaptain", "Bridge.Characters.EXLMediumAnimations.EXLTurnBackAtCFromCaptain")

	pEXLSaffi.AddAnimation("EXLCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pEXLSaffi.AddAnimation("EXLCommanderGlanceAwayCaptain", "Bridge.Characters.EXLMediumAnimations.EXLCConsoleInteraction")
	pEXLSaffi.AddAnimation("EXLCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pEXLSaffi.AddAnimation("EXLCommander1GlanceAwayCaptain", "Bridge.Characters.EXLMediumAnimations.EXLCConsoleInteraction")

	pEXLSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.EXLMediumAnimations.EBCTalkE")
	pEXLSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.EXLMediumAnimations.EXLseatedm")
	pEXLSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.EXLMediumAnimations.EBCTalkH")
	pEXLSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.EXLMediumAnimations.EXLseatedm")
	pEXLSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.EXLMediumAnimations.EBCTalkT")
	pEXLSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.EXLMediumAnimations.EXLseatedm")
	pEXLSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.EXLMediumAnimations.EBCTalkS")
	pEXLSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.EXLMediumAnimations.EXLseatedm")

	pEXLSaffi.AddAnimation("EBCommanderTurnX", "Bridge.Characters.EXLMediumAnimations.EBCTalkE")
	pEXLSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.EXLMediumAnimations.EXLseatedm")

	# Breathing
	pEXLSaffi.AddAnimation("EXLCommanderBreathe", "Bridge.Characters.EXLMediumAnimations.EXLseatedm")
	pEXLSaffi.AddAnimation("EXLCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pEXLSaffi.AddAnimation("EXLCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pEXLSaffi.AddAnimation("EXLCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pEXLSaffi.AddRandomAnimation("Bridge.Characters.EXLMediumAnimations.EXLCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)
	pEXLSaffi.AddAnimation("PushingButtons", "Bridge.Characters.EXLMediumAnimations.EXLCConsoleInteraction")

	# Hit animations
	pEXLSaffi.AddAnimation("EXLCommanderHit", "Bridge.Characters.EXLMediumAnimations.EXLCHit")
	pEXLSaffi.AddAnimation("EXLCommanderHitHard", "Bridge.Characters.EXLMediumAnimations.EXLCHitHard")
	#pEXLSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pEXLSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pEXLSaffi.AddAnimation("EXLCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pEXLSaffi.AddAnimation("EXLCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pEXLSaffi)
	pEXLSaffi.SetStanding(0)
	pEXLSaffi.SetLocation("EXLCommander")
	pEXLSaffi.AddPositionZoom("EXLCommander", 0.4)
#	debug("Finished configuring Saffi")
	pEXLSaffi.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pEXLSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLSaffi):
	debug(__name__ + ", AddCommonAnimations")
	pEXLSaffi.AddRandomAnimation("Bridge.Characters.EXLMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pEXLSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pEXLSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pEXLSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pEXLSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

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
	debug(__name__ + ", LoadSounds")
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
