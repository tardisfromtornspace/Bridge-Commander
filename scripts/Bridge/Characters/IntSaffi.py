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
	pIntSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pIntSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pIntSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pIntSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntSaffi)

	# Setup the character configuration
	pIntSaffi.SetSize(App.CharacterClass.MEDIUM)
	pIntSaffi.SetGender(App.CharacterClass.FEMALE)
	pIntSaffi.SetRandomAnimationChance(.75)
	pIntSaffi.SetBlinkChance(0.1)
	pIntSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pIntSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pIntSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pIntSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pIntSaffi.SetBlinkStages(3)

	pIntSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pIntSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pIntSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pIntSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pIntSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pIntSaffi


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
	pIntSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pIntSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pIntSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForIntrepid()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pIntSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pIntSaffi):
#	debug("Configuring Saffi for the Intrepid bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForIntrepid")
	pIntSaffi.ClearAnimations()

	# Register animation mappings
	pIntSaffi.AddAnimation("SeatedIntCommander", "Bridge.Characters.CommonAnimations.SeatedM")
	pIntSaffi.AddAnimation("StandingIntCommander", "Bridge.Characters.CommonAnimations.Standing")
	pIntSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.IntMediumAnimations.EBMoveFromL1ToC")
	pIntSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.IntMediumAnimations.EBMoveFromCToL1")
	pIntSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.IntMediumAnimations.EBMoveFromCToC1")
	pIntSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.IntMediumAnimations.EBMoveFromC1ToC")
	pIntSaffi.AddAnimation("IntCommanderTurnCaptain", "Bridge.Characters.IntMediumAnimations.IntTurnAtCTowardsCaptain")
	pIntSaffi.AddAnimation("IntCommanderBackCaptain", "Bridge.Characters.IntMediumAnimations.IntTurnBackAtCFromCaptain")

	pIntSaffi.AddAnimation("IntCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pIntSaffi.AddAnimation("IntCommanderGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")
	pIntSaffi.AddAnimation("IntCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pIntSaffi.AddAnimation("IntCommander1GlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	pIntSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.IntMediumAnimations.EBCTalkE")
	pIntSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.CommonAnimations.SeatedM")
	pIntSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.IntMediumAnimations.EBCTalkH")
	pIntSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.CommonAnimations.SeatedM")
	pIntSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.IntMediumAnimations.EBCTalkT")
	pIntSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.CommonAnimations.SeatedM")
	pIntSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.IntMediumAnimations.EBCTalkS")
	pIntSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.CommonAnimations.SeatedM")

	pIntSaffi.AddAnimation("EBCommanderTurnX", "Bridge.Characters.IntMediumAnimations.EBCTalkE")
	pIntSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pIntSaffi.AddAnimation("IntCommanderBreathe", "Bridge.Characters.CommonAnimations.SeatedM")
	pIntSaffi.AddAnimation("IntCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pIntSaffi.AddAnimation("IntCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pIntSaffi.AddAnimation("IntCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pIntSaffi.AddRandomAnimation("Bridge.Characters.IntMediumAnimations.IntCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# Hit animations
	pIntSaffi.AddAnimation("IntCommanderHit", "Bridge.Characters.IntMediumAnimations.IntCHit")
	pIntSaffi.AddAnimation("IntCommanderHitHard", "Bridge.Characters.IntMediumAnimations.IntCHitHard")
	#pIntSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pIntSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pIntSaffi.AddAnimation("IntCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pIntSaffi.AddAnimation("IntCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pIntSaffi)
	pIntSaffi.SetLocation("IntCommander")
	pIntSaffi.AddPositionZoom("IntCommander", 0.8)
#	debug("Finished configuring Saffi")
	pIntSaffi.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pIntSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntSaffi):
	debug(__name__ + ", AddCommonAnimations")
	pIntSaffi.AddRandomAnimation("Bridge.Characters.IntMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pIntSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.Neck_Rub")
	pIntSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pIntSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pIntSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pIntSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)


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
