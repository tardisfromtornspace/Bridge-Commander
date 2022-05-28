###############################################################################
#	Filename:	RomSaffi.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads RomSaffi Larsen, XO, and configures animations.
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
#	Create RomSaffi by building her character and placing her on the passed in set.
#	Create her menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	debug("Creating RomSaffi")

	if (pSet.GetObject("XO") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("XO")))
	



	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "B5/BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "B5/HeadSaffi/saffi_head.nif", None)
	pRomSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "B5/BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "B5/HeadSaffi/saffi_head.nif", 1)
	pRomSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "B5/BodyFemS/FedFemRed_body.tga", CharacterPaths.g_pcHeadTexPath + "B5/HeadSaffi/saffi_head.tga")

	pRomSaffi.SetCharacterName("Saffi")
	
	# Add the character to the set
	
	pSet.AddObjectToSet(pRomSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRomSaffi)

	# Setup the character configuration
	pRomSaffi.SetSize(App.CharacterClass.MEDIUM)
	pRomSaffi.SetGender(App.CharacterClass.FEMALE)
	pRomSaffi.SetRandomAnimationChance(.75)
	pRomSaffi.SetBlinkChance(0.1)
	pRomSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	
	# Load RomSaffi's general dialogue lines.
	LoadSounds()

	pRomSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "B5/HeadSaffi/Saffi_head_blink1.tga")
	pRomSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "B5/HeadSaffi/Saffi_head_blink2.tga")
	pRomSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "B5/HeadSaffi/Saffi_head_eyesclosed.tga")
	pRomSaffi.SetBlinkStages(3)

	pRomSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "B5/HeadSaffi/saffi_head_a.tga")
	pRomSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "B5/HeadSaffi/saffi_head_e.tga")
	pRomSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "B5/HeadSaffi/saffi_head_u.tga")
	pRomSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRomSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	debug("Finished creating RomSaffi")
	return pRomSaffi


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
	pRomSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pRomSaffi == None):
#		debug("******* Commanding officer not found *********")
		return

#	debug("Attaching menu to XO..")
	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pRomSaffi)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Main power back on line"
	#


###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pRomSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForWarbird(pRomSaffi):
#	debug("Configuring RomSaffi for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pRomSaffi.ClearAnimations()

	kAM = App.g_kAnimationManager

	


	# Register animation mappings
	pRomSaffi.AddAnimation("SeatedRomCommander", "Bridge.Characters.CommonAnimations.SeatedM")
	pRomSaffi.AddAnimation("StandingRomCommander", "Bridge.Characters.CommonAnimations.NebStanding")
	pRomSaffi.AddAnimation("EBL1MToEBCommander", "Bridge.Characters.NebMediumAnimations.EBMoveFromL1ToC")
	pRomSaffi.AddAnimation("EBCommanderToL1", "Bridge.Characters.NebMediumAnimations.EBMoveFromCToL1")
	pRomSaffi.AddAnimation("EBCommanderToC1", "Bridge.Characters.NebMediumAnimations.EBMoveFromCToC1")
	pRomSaffi.AddAnimation("EBCommander1ToC", "Bridge.Characters.NebMediumAnimations.EBMoveFromC1ToC")
	pRomSaffi.AddAnimation("RomCommanderTurnCaptain", "Bridge.Characters.NebMediumAnimations.NebTurnAtCTowardsCaptain")
#	pRomSaffi.AddAnimation("EBCommander1TurnCaptain", "Bridge.Characters.CommonAnimations.LookLeft")
#	pRomSaffi.AddAnimation("RomCommander1TurnCaptain", "Bridge.Characters.NebMediumAnimations.NebTurnAtC1TowardsCaptain")
#	pRomSaffi.AddAnimation("RomCommanderBackCaptain", "Bridge.Characters.CommonAnimations.SeatedM")
	pRomSaffi.AddAnimation("RomCommanderBackCaptain", "Bridge.Characters.CommonAnimations.NebStanding")
#	pRomSaffi.AddAnimation("RomCommander1BackCaptain", "Bridge.Characters.NebMediumAnimations.NebTurnBackAtC1FromCaptain")

	pRomSaffi.AddAnimation("EBCommanderGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pRomSaffi.AddAnimation("EBCommanderGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")
	pRomSaffi.AddAnimation("EBCommander1GlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pRomSaffi.AddAnimation("EBCommander1GlanceAwayCaptain", "Bridge.Characters.CommonAnimations.Standing")

	pRomSaffi.AddAnimation("EBCommanderTurnE", "Bridge.Characters.NebMediumAnimations.EBCTalkE")
	pRomSaffi.AddAnimation("EBCommanderBackE", "Bridge.Characters.CommonAnimations.SeatedM")
	pRomSaffi.AddAnimation("EBCommanderTurnH", "Bridge.Characters.NebMediumAnimations.EBCTalkH")
	pRomSaffi.AddAnimation("EBCommanderBackH", "Bridge.Characters.CommonAnimations.SeatedM")
	pRomSaffi.AddAnimation("EBCommanderTurnT", "Bridge.Characters.NebMediumAnimations.EBCTalkT")
	pRomSaffi.AddAnimation("EBCommanderBackT", "Bridge.Characters.CommonAnimations.SeatedM")
	pRomSaffi.AddAnimation("EBCommanderTurnS", "Bridge.Characters.NebMediumAnimations.EBCTalkS")
	pRomSaffi.AddAnimation("EBCommanderBackS", "Bridge.Characters.CommonAnimations.SeatedM")

	pRomSaffi.AddAnimation("EBCommanderTurnX", "Bridge.Characters.NebMediumAnimations.EBCTalkE")
	pRomSaffi.AddAnimation("EBCommanderBackX", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pRomSaffi.AddAnimation("EBCommanderBreathe", "Bridge.Characters.CommonAnimations.SeatedM")
	pRomSaffi.AddAnimation("EBCommander1Breathe", "Bridge.Characters.CommonAnimations.Standing")
	pRomSaffi.AddAnimation("EBCommanderBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")
	pRomSaffi.AddAnimation("EBCommander1BreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pRomSaffi.AddRandomAnimation("Bridge.Characters.NebMediumAnimations.EBCConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pRomSaffi.AddAnimation("PushingButtons", "Bridge.Characters.SmallAnimations.DBECConsoleInteraction")

	# Hit animations
	#pRomSaffi.AddAnimation("EBCommanderHit", "Bridge.Characters.NebMediumAnimations.CHit")
	#pRomSaffi.AddAnimation("EBCommanderHitHard", "Bridge.Characters.NebMediumAnimations.CHitHard")
	#pRomSaffi.AddAnimation("EBCommanderHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pRomSaffi.AddAnimation("EBCommanderHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pRomSaffi.AddAnimation("EBCommanderReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pRomSaffi.AddAnimation("EBCommanderReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pRomSaffi)
	pRomSaffi.SetStanding(1)
	pRomSaffi.SetLocation("RomCommander")
	pRomSaffi.AddPositionZoom("RomCommander", 0.5)
	#	debug("Finished configuring RomSaffi")




###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pRomSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pRomSaffi):
	pRomSaffi.AddRandomAnimation("Bridge.Characters.MediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pRomSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRomSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRomSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pRomSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pRomSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pRomSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

###############################################################################
#	LoadSounds
#	
#	Load any of RomSaffi's general or spontaneous sounds, so they don't
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
