###############################################################################
#	Filename:	Kiska.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Kiska Lomar, Helm, and configures animations
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create Kiska by building her character and placing her on the passed in set.
#	Create her menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating EXLKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pEXLKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pEXLKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pEXLKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLKiska)

	# Setup the character configuration
	pEXLKiska.SetSize(App.CharacterClass.MEDIUM)
	pEXLKiska.SetGender(App.CharacterClass.FEMALE)
	pEXLKiska.SetStanding(0)
	pEXLKiska.SetRandomAnimationChance(0.75)
	pEXLKiska.SetBlinkChance(0.1)
	pEXLKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pEXLKiska.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pEXLKiska.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pEXLKiska.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pEXLKiska.SetBlinkStages(3)

	pEXLKiska.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pEXLKiska.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pEXLKiska.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pEXLKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pEXLKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pEXLKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating EXLKiska")
	return pEXLKiska


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
	pEXLKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pEXLKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pEXLKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pEXLKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pEXLKiska):
#	kDebugObj.Print("Configuring EXLKiska for the Excelsior bridge")

	# Clear out any old animations from another configuration
	pEXLKiska.ClearAnimations()

	# Register animation mappings
	pEXLKiska.AddAnimation("EXLHelmTurnCaptain", "Bridge.Characters.EXLMediumAnimations.EXLTurnAtHTowardsCaptain")
	pEXLKiska.AddAnimation("EXLHelmBackCaptain", "Bridge.Characters.EXLMediumAnimations.EXLTurnBackAtHFromCaptain")


	pEXLKiska.AddAnimation("EXLHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pEXLKiska.AddAnimation("EXLHelmGlanceAwayCaptain", "Bridge.Characters.EXLMediumAnimations.EBHConsoleInteraction")

	# Breathing
	pEXLKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# EXLeraction
	pEXLKiska.AddRandomAnimation("Bridge.Characters.EXLMediumAnimations.EBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pEXLKiska.AddAnimation("PushingButtons", "Bridge.Characters.EXLMediumAnimations.EBHConsoleInteraction")

	# Hit animations
	#pEXLKiska.AddAnimation("EXLHelmHit", "Bridge.Characters.EXLMediumAnimations.EXLHHit")
	#pEXLKiska.AddAnimation("EXLHelmHitHard", "Bridge.Characters.EXLMediumAnimations.EXLHHitHard")
	pEXLKiska.AddAnimation("EXLHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pEXLKiska.AddAnimation("EXLHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pEXLKiska)

	pEXLKiska.SetLocation("EXLHelm")
#	pEXLKiska.SetLookAtAdj(0, 0, 0)
#	pEXLKiska.AddPositionZoom("EXLHelm", 0.6, "Helm")
	pEXLKiska.AddPositionZoom("EXLHelm", 0.6)
#	kDebugObj.Print("Finished configuring EXLKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pEXLKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLKiska):
	# Interaction with their environment
	pEXLKiska.AddRandomAnimation("Bridge.Characters.EXLMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pEXLKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pEXLKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pEXLKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pEXLKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pEXLKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

###############################################################################
#	LoadSounds()
#
#	Load generic bridge sounds for this character
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")

	#
	# Build a list of sound to load
	#
	lSoundList =	[	"KiskaSir1",	# Click Response
						"KiskaSir2",
						"KiskaSir3",
						"KiskaSir4",
						"KiskaSir5",
						
						"KiskaYes1",	# Order Confirmation
						"KiskaYes2",
						"KiskaYes3",
						"KiskaYes4",

						"gh075",	# Course laid in
						"gh081",	# Intercept course plotted

						"HailOpen1",
						"HailOpen2",
						"NotResponding1",
						"NotResponding2",
						"OnScreen",

						"CollisionAlert1",
						"CollisionAlert2",
						"CollisionAlert3",
						"CollisionAlert4",
						"CollisionAlert5",
						"CollisionAlert6",
						"CollisionAlert7",
						"CollisionAlert10",

						"IncomingMsg1",
						"IncomingMsg2",
						"IncomingMsg3",
						"IncomingMsg4",
						"IncomingMsg5",
						"IncomingMsg6",
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for sLine in lSoundList:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)
