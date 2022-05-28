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
	pTOSSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pTOSSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pTOSSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSSaffi)

	# Setup the character configuration
	pTOSSaffi.SetSize(App.CharacterClass.MEDIUM)
	pTOSSaffi.SetGender(App.CharacterClass.FEMALE)
	pTOSSaffi.SetRandomAnimationChance(.75)
	pTOSSaffi.SetBlinkChance(0.1)
	pTOSSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pTOSSaffi.AdTOSacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pTOSSaffi.AdTOSacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pTOSSaffi.AdTOSacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pTOSSaffi.SetBlinkStages(3)

	pTOSSaffi.AdTOSacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pTOSSaffi.AdTOSacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pTOSSaffi.AdTOSacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pTOSSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pTOSSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pTOSSaffi


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
	pTOSSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pTOSSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pTOSSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pTOSSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pTOSSaffi):
#	debug("Configuring Saffi for the Constitution bridge")

	# Clear out any old animations from another configuration
	pTOSSaffi.ClearAnimations()

	# Register animation mappings
	pTOSSaffi.AddAnimation("SeatedTOSCommander", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pTOSSaffi.AddAnimation("StandingTOSCommander", "Bridge.Characters.CommonAnimations.Standing")
	pTOSSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.TOSMediumAnimations.EBMoveFromL1ToC")
	pTOSSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.TOSMediumAnimations.EBMoveFromCToL1")
	pTOSSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.TOSMediumAnimations.EBMoveFromCToC1")
	pTOSSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.TOSMediumAnimations.EBMoveFromC1ToC")
	pTOSSaffi.AddAnimation("TOSCommanderTurnCaptain", "Bridge.Characters.TOSMediumAnimations.TOSTurnAtCTowardsCaptain")
	pTOSSaffi.AddAnimation("TOSCommanderBackCaptain", "Bridge.Characters.TOSMediumAnimations.TOSTurnBackAtCFromCaptain")

	pTOSSaffi.AddAnimation("TOSCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pTOSSaffi.AddAnimation("TOSCommanderGlanceAwayCaptain", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pTOSSaffi.AddAnimation("TOSCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pTOSSaffi.AddAnimation("TOSCommander1GlanceAwayCaptain", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")

	pTOSSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.TOSMediumAnimations.EBCTalkE")
	pTOSSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pTOSSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.TOSMediumAnimations.EBCTalkH")
	pTOSSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pTOSSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.TOSMediumAnimations.EBCTalkT")
	pTOSSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pTOSSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.TOSMediumAnimations.EBCTalkS")
	pTOSSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")

	pTOSSaffi.AddAnimation("EBCommanderTurTOS", "Bridge.Characters.TOSMediumAnimations.EBCTalkE")
	pTOSSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.TOSMediumAnimations.Seatedm")

	# Breathing
	pTOSSaffi.AddAnimation("TOSCommanderBreathe", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pTOSSaffi.AddAnimation("TOSCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pTOSSaffi.AddAnimation("TOSCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pTOSSaffi.AddAnimation("TOSCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pTOSSaffi.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction", App.CharacterClass.SITTING_ONLY, 25, 1)
	pTOSSaffi.AddAnimation("PushingButtons", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")

	# Hit animations
	#pTOSSaffi.AddAnimation("TOSCommanderHit", "Bridge.Characters.TOSMediumAnimations.TOSCHit")
	#pTOSSaffi.AddAnimation("TOSCommanderHitHard", "Bridge.Characters.TOSMediumAnimations.TOSCHitHard")
	#pTOSSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pTOSSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pTOSSaffi.AddAnimation("TOSCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pTOSSaffi.AddAnimation("TOSCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pTOSSaffi)
	pTOSSaffi.SetStanding(0)
	pTOSSaffi.SetLocation("TOSCommander")
	pTOSSaffi.AddPositionZoom("TOSCommander", 0.7)
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
#	Args:	pTOSSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSSaffi):
	pTOSSaffi.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction", App.CharacterClass.SITTING_ONLY, 1, 1)
	pTOSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pTOSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pTOSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pTOSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pTOSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pTOSSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

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
