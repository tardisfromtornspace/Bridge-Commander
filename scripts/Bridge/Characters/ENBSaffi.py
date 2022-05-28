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
	pENBSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pENBSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pENBSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pENBSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBSaffi)

	# Setup the character configuration
	pENBSaffi.SetSize(App.CharacterClass.MEDIUM)
	pENBSaffi.SetGender(App.CharacterClass.FEMALE)
	pENBSaffi.SetRandomAnimationChance(.75)
	pENBSaffi.SetBlinkChance(0.1)
	pENBSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pENBSaffi.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENBSaffi.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENBSaffi.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENBSaffi.SetBlinkStages(3)

	pENBSaffi.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENBSaffi.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENBSaffi.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENBSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENBSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pENBSaffi


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
	pENBSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pENBSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pENBSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pENBSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pENBSaffi):
#	debug("Configuring Saffi for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseB")
	pENBSaffi.ClearAnimations()

	# Register animation mappings
	pENBSaffi.AddAnimation("SeatedENBCommander", "Bridge.Characters.ENBMediumAnimations.ENBPlaceAtC")
	pENBSaffi.AddAnimation("StandingENBCommander", "Bridge.Characters.CommonAnimations.Standing")
	pENBSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.ENBMediumAnimations.EBMoveFromL1ToC")
	pENBSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.ENBMediumAnimations.EBMoveFromCToL1")
	pENBSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.ENBMediumAnimations.EBMoveFromCToC1")
	pENBSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.ENBMediumAnimations.EBMoveFromC1ToC")
	pENBSaffi.AddAnimation("ENBCommanderTurnCaptain", "Bridge.Characters.ENBMediumAnimations.ENBTurnAtCTowardsCaptain")
	pENBSaffi.AddAnimation("ENBCommanderBackCaptain", "Bridge.Characters.ENBMediumAnimations.ENBTurnBackAtCFromCaptain")

	pENBSaffi.AddAnimation("ENBCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pENBSaffi.AddAnimation("ENBCommanderGlanceAwayCaptain", "Bridge.Characters.ENBMediumAnimations.ENBCConsoleInteraction")
	pENBSaffi.AddAnimation("ENBCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pENBSaffi.AddAnimation("ENBCommander1GlanceAwayCaptain", "Bridge.Characters.ENBMediumAnimations.ENBCConsoleInteraction")

	pENBSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.ENBMediumAnimations.EBCTalkE")
	pENBSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.ENBMediumAnimations.ENBseatedm")
	pENBSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.ENBMediumAnimations.EBCTalkH")
	pENBSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.ENBMediumAnimations.ENBseatedm")
	pENBSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.ENBMediumAnimations.EBCTalkT")
	pENBSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.ENBMediumAnimations.ENBseatedm")
	pENBSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.ENBMediumAnimations.EBCTalkS")
	pENBSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.ENBMediumAnimations.ENBseatedm")

	pENBSaffi.AddAnimation("EBCommanderTurnX", "Bridge.Characters.ENBMediumAnimations.EBCTalkE")
	pENBSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.ENBMediumAnimations.ENBseatedm")

	# Breathing
	pENBSaffi.AddAnimation("ENBCommanderBreathe", "Bridge.Characters.ENBMediumAnimations.ENBseatedm")
	pENBSaffi.AddAnimation("ENBCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pENBSaffi.AddAnimation("ENBCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pENBSaffi.AddAnimation("ENBCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pENBSaffi.AddRandomAnimation("Bridge.Characters.ENBMediumAnimations.ENBCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)
	pENBSaffi.AddAnimation("PushingButtons", "Bridge.Characters.ENBMediumAnimations.ENBCConsoleInteraction")

	# Hit animations
	pENBSaffi.AddAnimation("ENBCommanderHit", "Bridge.Characters.ENBMediumAnimations.ENBCHit")
	pENBSaffi.AddAnimation("ENBCommanderHitHard", "Bridge.Characters.ENBMediumAnimations.ENBCHitHard")
	#pENBSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pENBSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENBSaffi.AddAnimation("ENBCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENBSaffi.AddAnimation("ENBCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pENBSaffi)
	pENBSaffi.SetStanding(0)
	pENBSaffi.SetLocation("ENBCommander")
	pENBSaffi.AddPositionZoom("ENBCommander", 0.4)
#	debug("Finished configuring Saffi")
	pENBSaffi.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENBSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENBSaffi):
	debug(__name__ + ", AddCommonAnimations")
	pENBSaffi.AddRandomAnimation("Bridge.Characters.ENBMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pENBSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENBSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENBSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pENBSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pENBSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pENBSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

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
