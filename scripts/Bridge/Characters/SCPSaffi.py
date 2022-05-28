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
	pSCPSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "../BridgeCrew/borgqueen/borgqueen_head.nif", 1)
	pSCPSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/borgqueen/borgqueen_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")

	pSCPSaffi.SetCharacterName("Saffi")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPSaffi)

	# Setup the character configuration
	pSCPSaffi.SetSize(App.CharacterClass.MEDIUM)
	pSCPSaffi.SetGender(App.CharacterClass.FEMALE)
	pSCPSaffi.SetRandomAnimationChance(.75)
	pSCPSaffi.SetBlinkChance(0.1)
	pSCPSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Saffi's general dialogue lines.
	LoadSounds()

	pSCPSaffi.AdSCPacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pSCPSaffi.AdSCPacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pSCPSaffi.AdSCPacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pSCPSaffi.SetBlinkStages(3)

	pSCPSaffi.AdSCPacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pSCPSaffi.AdSCPacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pSCPSaffi.AdSCPacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/borgqueen/borgqueen_head.tga")
	pSCPSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pSCPSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating Saffi")
	return pSCPSaffi


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
	pSCPSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pSCPSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pSCPSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#

###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pSCPSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pSCPSaffi):
#	debug("Configuring Saffi for the Galor bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalor")
	pSCPSaffi.ClearAnimations()

	# Register animation mappings
	pSCPSaffi.AddAnimation("SeatedSCPCommander", "Bridge.Characters.SCPMediumAnimations.SCPPlaceAtC")
	pSCPSaffi.AddAnimation("StandingSCPCommander", "Bridge.Characters.CommonAnimations.Standing")
	pSCPSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.SCPMediumAnimations.EBMoveFromL1ToC")
	pSCPSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.SCPMediumAnimations.EBMoveFromCToL1")
	pSCPSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.SCPMediumAnimations.EBMoveFromCToC1")
	pSCPSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.SCPMediumAnimations.EBMoveFromC1ToC")
	pSCPSaffi.AddAnimation("SCPCommanderTurnCaptain", "Bridge.Characters.SCPMediumAnimations.SCPTurnAtCTowardsCaptain")
	pSCPSaffi.AddAnimation("SCPCommanderBackCaptain", "Bridge.Characters.SCPMediumAnimations.SCPTurnBackAtCFromCaptain")

	pSCPSaffi.AddAnimation("SCPCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pSCPSaffi.AddAnimation("SCPCommanderGlanceAwayCaptain", "Bridge.Characters.SCPMediumAnimations.SCPCConsoleInteraction")
	pSCPSaffi.AddAnimation("SCPCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pSCPSaffi.AddAnimation("SCPCommander1GlanceAwayCaptain", "Bridge.Characters.SCPMediumAnimations.SCPCConsoleInteraction")

	pSCPSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.SCPMediumAnimations.EBCTalkE")
	pSCPSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.SCPMediumAnimations.SCPseatedm")
	pSCPSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.SCPMediumAnimations.EBCTalkH")
	pSCPSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.SCPMediumAnimations.SCPseatedm")
	pSCPSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.SCPMediumAnimations.EBCTalkT")
	pSCPSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.SCPMediumAnimations.SCPseatedm")
	pSCPSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.SCPMediumAnimations.EBCTalkS")
	pSCPSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.SCPMediumAnimations.SCPseatedm")

	pSCPSaffi.AddAnimation("EBCommanderTurSCP", "Bridge.Characters.SCPMediumAnimations.EBCTalkE")
	pSCPSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.SCPMediumAnimations.SCPseatedm")

	# Breathing
	pSCPSaffi.AddAnimation("SCPCommanderBreathe", "Bridge.Characters.SCPMediumAnimations.SCPseatedm")
	pSCPSaffi.AddAnimation("SCPCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pSCPSaffi.AddAnimation("SCPCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pSCPSaffi.AddAnimation("SCPCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pSCPSaffi.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.SCPCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)
	pSCPSaffi.AddAnimation("PushingButtons", "Bridge.Characters.SCPMediumAnimations.SCPCConsoleInteraction")

	# Hit animations
	#pSCPSaffi.AddAnimation("SCPCommanderHit", "Bridge.Characters.SCPMediumAnimations.SCPCHit")
	#pSCPSaffi.AddAnimation("SCPCommanderHitHard", "Bridge.Characters.SCPMediumAnimations.SCPCHitHard")
	#pSCPSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pSCPSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pSCPSaffi.AddAnimation("SCPCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pSCPSaffi.AddAnimation("SCPCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pSCPSaffi)
	pSCPSaffi.SetStanding(0)
	pSCPSaffi.SetLocation("SCPCommander")
	pSCPSaffi.AddPositionZoom("SCPCommander", 0.4)
#	debug("Finished configuring Saffi")
	pSCPSaffi.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pSCPSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPSaffi):
	debug(__name__ + ", AddCommonAnimations")
	pSCPSaffi.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pSCPSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pSCPSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pSCPSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pSCPSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pSCPSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pSCPSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

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
