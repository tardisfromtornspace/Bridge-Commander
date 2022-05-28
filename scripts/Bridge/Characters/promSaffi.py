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
	ppromSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	ppromSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	ppromSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(ppromSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromSaffi)

	# Setup the character configuration
	ppromSaffi.SetSize(App.CharacterClass.MEDIUM)
	ppromSaffi.SetGender(App.CharacterClass.FEMALE)
	ppromSaffi.SetRandomAnimationChance(.75)
	ppromSaffi.SetBlinkChance(0.1)
	ppromSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	ppromSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	ppromSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	ppromSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	ppromSaffi.SetBlinkStages(3)

	ppromSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	ppromSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	ppromSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	ppromSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	ppromSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return ppromSaffi


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
	ppromSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (ppromSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(ppromSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	ppromSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(ppromSaffi):
#	debug("Configuring Saffi for the prometheus bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForprometheus")
	ppromSaffi.ClearAnimations()

	# Register animation mappings
	ppromSaffi.AddAnimation("SeatedpromCommander", "Bridge.Characters.promMediumAnimations.promPlaceAtC")
	ppromSaffi.AddAnimation("StandingpromCommander", "Bridge.Characters.CommonAnimations.Standing")
	ppromSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.promMediumAnimations.EBMoveFromL1ToC")
	ppromSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.promMediumAnimations.EBMoveFromCToL1")
	ppromSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.promMediumAnimations.EBMoveFromCToC1")
	ppromSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.promMediumAnimations.EBMoveFromC1ToC")
	ppromSaffi.AddAnimation("promCommanderTurnCaptain", "Bridge.Characters.promMediumAnimations.promTurnAtCTowardsCaptain")
	ppromSaffi.AddAnimation("promCommanderBackCaptain", "Bridge.Characters.promMediumAnimations.promTurnBackAtCFromCaptain")

	ppromSaffi.AddAnimation("promCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	ppromSaffi.AddAnimation("promCommanderGlanceAwayCaptain", "Bridge.Characters.promMediumAnimations.promseatedm")
	ppromSaffi.AddAnimation("promCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	ppromSaffi.AddAnimation("promCommander1GlanceAwayCaptain", "Bridge.Characters.promMediumAnimations.promseatedm")

	ppromSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.promMediumAnimations.EBCTalkE")
	ppromSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.promMediumAnimations.promseatedm")
	ppromSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.promMediumAnimations.EBCTalkH")
	ppromSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.promMediumAnimations.promseatedm")
	ppromSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.promMediumAnimations.EBCTalkT")
	ppromSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.promMediumAnimations.promseatedm")
	ppromSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.promMediumAnimations.EBCTalkS")
	ppromSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.promMediumAnimations.promseatedm")

	ppromSaffi.AddAnimation("EBCommanderTurprom", "Bridge.Characters.promMediumAnimations.EBCTalkE")
	ppromSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.promMediumAnimations.promseatedm")

	# Breathing
	ppromSaffi.AddAnimation("promCommanderBreathe", "Bridge.Characters.promMediumAnimations.promseatedm")
	ppromSaffi.AddAnimation("promCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	ppromSaffi.AddAnimation("promCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	ppromSaffi.AddAnimation("promCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	ppromSaffi.AddRandomAnimation("Bridge.Characters.promMediumAnimations.promCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)
	ppromSaffi.AddAnimation("PushingButtons", "Bridge.Characters.promMediumAnimations.promCConsoleInteraction")

	# Hit animations
	ppromSaffi.AddAnimation("promCommanderHit", "Bridge.Characters.promMediumAnimations.promCHit")
	ppromSaffi.AddAnimation("promCommanderHitHard", "Bridge.Characters.promMediumAnimations.promCHitHard")
	#ppromSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#ppromSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	ppromSaffi.AddAnimation("promCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	ppromSaffi.AddAnimation("promCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(ppromSaffi)
	ppromSaffi.SetStanding(0)
	ppromSaffi.SetLocation("promCommander")
	ppromSaffi.AddPositionZoom("promCommander", 0.55)
#	debug("Finished configuring Saffi")
	ppromSaffi.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	ppromSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromSaffi):
	debug(__name__ + ", AddCommonAnimations")
	ppromSaffi.AddRandomAnimation("Bridge.Characters.promMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	ppromSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	ppromSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	ppromSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	ppromSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	ppromSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

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
