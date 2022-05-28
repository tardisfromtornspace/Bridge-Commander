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
	pENASaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pENASaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pENASaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pENASaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENASaffi)

	# Setup the character configuration
	pENASaffi.SetSize(App.CharacterClass.MEDIUM)
	pENASaffi.SetGender(App.CharacterClass.FEMALE)
	pENASaffi.SetRandomAnimationChance(.75)
	pENASaffi.SetBlinkChance(0.1)
	pENASaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pENASaffi.AdENAacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENASaffi.AdENAacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENASaffi.AdENAacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENASaffi.SetBlinkStages(3)

	pENASaffi.AdENAacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENASaffi.AdENAacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENASaffi.AdENAacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pENASaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENASaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pENASaffi


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
	pENASaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pENASaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pENASaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pENASaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pENASaffi):
#	debug("Configuring Saffi for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseA")
	pENASaffi.ClearAnimations()

	# Register animation mappings
	pENASaffi.AddAnimation("SeatedENACommander", "Bridge.Characters.ENAMediumAnimations.ENAPlaceAtC")
	pENASaffi.AddAnimation("StandingENACommander", "Bridge.Characters.CommonAnimations.Standing")
	pENASaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.ENAMediumAnimations.EBMoveFromL1ToC")
	pENASaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.ENAMediumAnimations.EBMoveFromCToL1")
	pENASaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.ENAMediumAnimations.EBMoveFromCToC1")
	pENASaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.ENAMediumAnimations.EBMoveFromC1ToC")
	pENASaffi.AddAnimation("ENACommanderTurnCaptain", "Bridge.Characters.ENAMediumAnimations.ENATurnAtCTowardsCaptain")
	pENASaffi.AddAnimation("ENACommanderBackCaptain", "Bridge.Characters.ENAMediumAnimations.ENATurnBackAtCFromCaptain")

	pENASaffi.AddAnimation("ENACommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pENASaffi.AddAnimation("ENACommanderGlanceAwayCaptain", "Bridge.Characters.ENAMediumAnimations.ENACConsoleInteraction")
	pENASaffi.AddAnimation("ENACommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pENASaffi.AddAnimation("ENACommander1GlanceAwayCaptain", "Bridge.Characters.ENAMediumAnimations.ENACConsoleInteraction")

	pENASaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.ENAMediumAnimations.EBCTalkE")
	pENASaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.ENAMediumAnimations.ENAseatedm")
	pENASaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.ENAMediumAnimations.EBCTalkH")
	pENASaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.ENAMediumAnimations.ENAseatedm")
	pENASaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.ENAMediumAnimations.EBCTalkT")
	pENASaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.ENAMediumAnimations.ENAseatedm")
	pENASaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.ENAMediumAnimations.EBCTalkS")
	pENASaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.ENAMediumAnimations.ENAseatedm")

	pENASaffi.AddAnimation("EBCommanderTurENA", "Bridge.Characters.ENAMediumAnimations.EBCTalkE")
	pENASaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.ENAMediumAnimations.ENAseatedm")

	# Breathing
	pENASaffi.AddAnimation("ENACommanderBreathe", "Bridge.Characters.ENAMediumAnimations.ENAseatedm")
	pENASaffi.AddAnimation("ENACommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pENASaffi.AddAnimation("ENACommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pENASaffi.AddAnimation("ENACommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pENASaffi.AddRandomAnimation("Bridge.Characters.ENAMediumAnimations.ENACConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)
	pENASaffi.AddAnimation("PushingButtons", "Bridge.Characters.ENAMediumAnimations.ENACConsoleInteraction")

	# Hit animations
	pENASaffi.AddAnimation("ENACommanderHit", "Bridge.Characters.ENAMediumAnimations.ENACHit")
	pENASaffi.AddAnimation("ENACommanderHitHard", "Bridge.Characters.ENAMediumAnimations.ENACHitHard")
	#pENASaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pENASaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENASaffi.AddAnimation("ENACommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENASaffi.AddAnimation("ENACommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pENASaffi)
	pENASaffi.SetStanding(0)
	pENASaffi.SetLocation("ENACommander")
	pENASaffi.AddPositionZoom("ENACommander", 0.4)
#	debug("Finished configuring Saffi")
	pENASaffi.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENASaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENASaffi):
	debug(__name__ + ", AddCommonAnimations")
	pENASaffi.AddRandomAnimation("Bridge.Characters.ENAMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pENASaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENASaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENASaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pENASaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pENASaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pENASaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

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
