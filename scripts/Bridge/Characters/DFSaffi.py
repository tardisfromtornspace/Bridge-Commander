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
	pDFSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pDFSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pDFSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pDFSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFSaffi)

	# Setup the character configuration
	pDFSaffi.SetSize(App.CharacterClass.MEDIUM)
	pDFSaffi.SetGender(App.CharacterClass.FEMALE)
	pDFSaffi.SetRandomAnimationChance(.75)
	pDFSaffi.SetBlinkChance(0.1)
	pDFSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pDFSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pDFSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pDFSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pDFSaffi.SetBlinkStages(3)

	pDFSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pDFSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pDFSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pDFSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDFSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pDFSaffi


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
	pDFSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pDFSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pDFSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pDFSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pDFSaffi):
#	debug("Configuring Saffi for the Defiant bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForDefiant")
	pDFSaffi.ClearAnimations()

	# Register animation mappings
	pDFSaffi.AddAnimation("SeatedDFCommander", "Bridge.Characters.DFMediumAnimations.DFPlaceAtC")
	pDFSaffi.AddAnimation("StandingDFCommander", "Bridge.Characters.CommonAnimations.Standing")
	pDFSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.DFMediumAnimations.EBMoveFromL1ToC")
	pDFSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.DFMediumAnimations.EBMoveFromCToL1")
	pDFSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.DFMediumAnimations.EBMoveFromCToC1")
	pDFSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.DFMediumAnimations.EBMoveFromC1ToC")
	pDFSaffi.AddAnimation("DFCommanderTurnCaptain", "Bridge.Characters.DFMediumAnimations.DFTurnAtCTowardsCaptain")
	pDFSaffi.AddAnimation("DFCommanderBackCaptain", "Bridge.Characters.DFMediumAnimations.DFTurnBackAtCFromCaptain")

	pDFSaffi.AddAnimation("DFCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pDFSaffi.AddAnimation("DFCommanderGlanceAwayCaptain", "Bridge.Characters.DFMediumAnimations.DFseatedm")
	pDFSaffi.AddAnimation("DFCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pDFSaffi.AddAnimation("DFCommander1GlanceAwayCaptain", "Bridge.Characters.DFMediumAnimations.DFseatedm")

	pDFSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.DFMediumAnimations.EBCTalkE")
	pDFSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.DFMediumAnimations.DFseatedm")
	pDFSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.DFMediumAnimations.EBCTalkH")
	pDFSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.DFMediumAnimations.DFseatedm")
	pDFSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.DFMediumAnimations.EBCTalkT")
	pDFSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.DFMediumAnimations.DFseatedm")
	pDFSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.DFMediumAnimations.EBCTalkS")
	pDFSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.DFMediumAnimations.DFseatedm")

	pDFSaffi.AddAnimation("EBCommanderTurDF", "Bridge.Characters.DFMediumAnimations.EBCTalkE")
	pDFSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.DFMediumAnimations.DFseatedm")

	# Breathing
	pDFSaffi.AddAnimation("DFCommanderBreathe", "Bridge.Characters.DFMediumAnimations.DFseatedm")
	pDFSaffi.AddAnimation("DFCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pDFSaffi.AddAnimation("DFCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pDFSaffi.AddAnimation("DFCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pDFSaffi.AddRandomAnimation("Bridge.Characters.DFMediumAnimations.DFCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)
	pDFSaffi.AddAnimation("PushingButtons", "Bridge.Characters.DFMediumAnimations.DFCConsoleInteraction")

	# Hit animations
	pDFSaffi.AddAnimation("DFCommanderHit", "Bridge.Characters.DFMediumAnimations.DFCHit")
	pDFSaffi.AddAnimation("DFCommanderHitHard", "Bridge.Characters.DFMediumAnimations.DFCHitHard")
	#pDFSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pDFSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pDFSaffi.AddAnimation("DFCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pDFSaffi.AddAnimation("DFCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pDFSaffi)
	pDFSaffi.SetStanding(0)
	pDFSaffi.SetLocation("DFCommander")
	pDFSaffi.AddPositionZoom("DFCommander", 0.55)
#	debug("Finished configuring Saffi")
	pDFSaffi.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pDFSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFSaffi):
	debug(__name__ + ", AddCommonAnimations")
	pDFSaffi.AddRandomAnimation("Bridge.Characters.DFMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pDFSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pDFSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pDFSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pDFSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

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
