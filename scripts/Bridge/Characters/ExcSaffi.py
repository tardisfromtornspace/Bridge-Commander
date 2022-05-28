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
	pExcSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pExcSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pExcSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pExcSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcSaffi)

	# Setup the character configuration
	pExcSaffi.SetSize(App.CharacterClass.MEDIUM)
	pExcSaffi.SetGender(App.CharacterClass.FEMALE)
	pExcSaffi.SetRandomAnimationChance(.75)
	pExcSaffi.SetBlinkChance(0.1)
	pExcSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pExcSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pExcSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pExcSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pExcSaffi.SetBlinkStages(3)

	pExcSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pExcSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pExcSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pExcSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pExcSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pExcSaffi


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
	pExcSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pExcSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pExcSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForExcalibur()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pExcSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pExcSaffi):
#	debug("Configuring Saffi for the Excalibur bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcalibur")
	pExcSaffi.ClearAnimations()

	# Register animation mappings
	pExcSaffi.AddAnimation("SeatedExcCommander", "Bridge.Characters.CommonAnimations.SeatedM")
	pExcSaffi.AddAnimation("StandingExcCommander", "Bridge.Characters.CommonAnimations.Standing")
	pExcSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.ExcMediumAnimations.EBMoveFromL1ToC")
	pExcSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.ExcMediumAnimations.EBMoveFromCToL1")
	pExcSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.ExcMediumAnimations.EBMoveFromCToC1")
	pExcSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.ExcMediumAnimations.EBMoveFromC1ToC")
	pExcSaffi.AddAnimation("ExcCommanderTurnCaptain", "Bridge.Characters.ExcMediumAnimations.ExcTurnAtCTowardsCaptain")
	pExcSaffi.AddAnimation("ExcCommanderBackCaptain", "Bridge.Characters.ExcMediumAnimations.ExcTurnBackAtCFromCaptain")

	pExcSaffi.AddAnimation("ExcCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pExcSaffi.AddAnimation("ExcCommanderGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")
	pExcSaffi.AddAnimation("ExcCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pExcSaffi.AddAnimation("ExcCommander1GlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	pExcSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.ExcMediumAnimations.EBCTalkE")
	pExcSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.CommonAnimations.SeatedM")
	pExcSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.ExcMediumAnimations.EBCTalkH")
	pExcSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.CommonAnimations.SeatedM")
	pExcSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.ExcMediumAnimations.EBCTalkT")
	pExcSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.CommonAnimations.SeatedM")
	pExcSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.ExcMediumAnimations.EBCTalkS")
	pExcSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.CommonAnimations.SeatedM")

	pExcSaffi.AddAnimation("EBCommanderTurnX", "Bridge.Characters.ExcMediumAnimations.EBCTalkE")
	pExcSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pExcSaffi.AddAnimation("ExcCommanderBreathe", "Bridge.Characters.CommonAnimations.SeatedM")
	pExcSaffi.AddAnimation("ExcCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pExcSaffi.AddAnimation("ExcCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pExcSaffi.AddAnimation("ExcCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pExcSaffi.AddRandomAnimation("Bridge.Characters.ExcMediumAnimations.ExcCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)
	pExcSaffi.AddAnimation("PushingButtons", "Bridge.Characters.ExcMediumAnimations.ExcCConsoleInteraction")

	# Hit animations
	pExcSaffi.AddAnimation("ExcCommanderHit", "Bridge.Characters.ExcMediumAnimations.ExcCHit")
	pExcSaffi.AddAnimation("ExcCommanderHitHard", "Bridge.Characters.ExcMediumAnimations.ExcCHitHard")
	#pExcSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pExcSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pExcSaffi.AddAnimation("ExcCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pExcSaffi.AddAnimation("ExcCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pExcSaffi)
	pExcSaffi.SetStanding(0)
	pExcSaffi.SetLocation("ExcCommander")
	pExcSaffi.AddPositionZoom("ExcCommander", 0.9)
#	debug("Finished configuring Saffi")
	pExcSaffi.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pExcSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcSaffi):
	debug(__name__ + ", AddCommonAnimations")
	pExcSaffi.AddRandomAnimation("Bridge.Characters.ExcExcMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pExcSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pExcSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pExcSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pExcSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

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
