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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pNebSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pNebSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemRed_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadSaffi/saffi_head.tga")

	pNebSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pNebSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebSaffi)

	# Setup the character configuration
	pNebSaffi.SetSize(App.CharacterClass.MEDIUM)
	pNebSaffi.SetGender(App.CharacterClass.FEMALE)
	pNebSaffi.SetRandomAnimationChance(.75)
	pNebSaffi.SetBlinkChance(0.1)
	pNebSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pNebSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadSaffi/Saffi_head_blink1.tga")
	pNebSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadSaffi/Saffi_head_blink2.tga")
	pNebSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadSaffi/Saffi_head_eyesclosed.tga")
	pNebSaffi.SetBlinkStages(3)

	pNebSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadSaffi/saffi_head_a.tga")
	pNebSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadSaffi/saffi_head_e.tga")
	pNebSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadSaffi/saffi_head_u.tga")
	pNebSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pNebSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pNebSaffi


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
	pNebSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pNebSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pNebSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForNebula()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pNebSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pNebSaffi):
#	debug("Configuring Saffi for the Nebula bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pNebSaffi.ClearAnimations()

	# Register animation mappings
	pNebSaffi.AddAnimation("SeatedNebCommander", "Bridge.Characters.CommonAnimations.SeatedM")
	pNebSaffi.AddAnimation("StandingNebCommander", "Bridge.Characters.NebMediumAnimations.NebStanding")
	pNebSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.NebMediumAnimations.EBMoveFromL1ToC")
	pNebSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.NebMediumAnimations.EBMoveFromCToL1")
	pNebSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.NebMediumAnimations.EBMoveFromCToC1")
	pNebSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.NebMediumAnimations.EBMoveFromC1ToC")
	pNebSaffi.AddAnimation("NebCommanderTurnCaptain", "Bridge.Characters.NebMediumAnimations.NebTurnAtCTowardsCaptain")
#	pNebSaffi.AddAnimation("EBCommander1TurnCaptain", "Bridge.Characters.CommonAnimations.LookLeft")
#	pNebSaffi.AddAnimation("NebCommander1TurnCaptain", "Bridge.Characters.NebMediumAnimations.NebTurnAtC1TowardsCaptain")
#	pNebSaffi.AddAnimation("NebCommanderBackCaptain", "Bridge.Characters.CommonAnimations.SeatedM")
	pNebSaffi.AddAnimation("NebCommanderBackCaptain", "Bridge.Characters.NebMediumAnimations.NebStanding")
#	pNebSaffi.AddAnimation("NEbCommander1BackCaptain", "Bridge.Characters.NebMediumAnimations.NebTurnBackAtC1FromCaptain")

	pNebSaffi.AddAnimation("EBCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pNebSaffi.AddAnimation("EBCommanderGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")
	pNebSaffi.AddAnimation("EBCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pNebSaffi.AddAnimation("EBCommander1GlanceAwayCaptain", "Bridge.Characters.CommonAnimations.Standing")

	pNebSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.NebMediumAnimations.EBCTalkE")
	pNebSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.CommonAnimations.SeatedM")
	pNebSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.NebMediumAnimations.EBCTalkH")
	pNebSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.CommonAnimations.SeatedM")
	pNebSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.NebMediumAnimations.EBCTalkT")
	pNebSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.CommonAnimations.SeatedM")
	pNebSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.NebMediumAnimations.EBCTalkS")
	pNebSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.CommonAnimations.SeatedM")

	pNebSaffi.AddAnimation("EBCommanderTurnX", "Bridge.Characters.NebMediumAnimations.EBCTalkE")
	pNebSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pNebSaffi.AddAnimation("EBCommanderBreathe", "Bridge.Characters.CommonAnimations.SeatedM")
	pNebSaffi.AddAnimation("EBCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pNebSaffi.AddAnimation("EBCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pNebSaffi.AddAnimation("EBCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pNebSaffi.AddRandomAnimation("Bridge.Characters.NebMediumAnimations.EBCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pNebSaffi.AddAnimation("PushingButtons", "Bridge.Characters.SmallAnimations.DBECConsoleInteraction")

	# Hit animations
	#pNebSaffi.AddAnimation("EBCommanderHit", "Bridge.Characters.NebMediumAnimations.CHit")
	#pNebSaffi.AddAnimation("EBCommanderHitHard", "Bridge.Characters.NebMediumAnimations.CHitHard")
	#pNebSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pNebSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pNebSaffi.AddAnimation("EBCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pNebSaffi.AddAnimation("EBCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pNebSaffi)
	pNebSaffi.SetStanding(1)
	pNebSaffi.SetLocation("NebCommander")
	pNebSaffi.AddPositionZoom("NebCommander", 0.8)
#	debug("Finished configuring Saffi")
	pNebSaffi.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pNebSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebSaffi):
	debug(__name__ + ", AddCommonAnimations")
	pNebSaffi.AddRandomAnimation("Bridge.Characters.NebNebMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pNebSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pNebSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pNebSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pNebSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

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
