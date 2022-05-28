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
#	kDebugObj.Print("Creating TOSKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pTOSKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pTOSKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pTOSKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSKiska)

	# Setup the character configuration
	pTOSKiska.SetSize(App.CharacterClass.MEDIUM)
	pTOSKiska.SetGender(App.CharacterClass.FEMALE)
	pTOSKiska.SetStanding(0)
	pTOSKiska.SetRandomAnimationChance(0.75)
	pTOSKiska.SetBlinkChance(0.1)
	pTOSKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pTOSKiska.AdTOSacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pTOSKiska.AdTOSacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pTOSKiska.AdTOSacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pTOSKiska.SetBlinkStages(3)

	pTOSKiska.AdTOSacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pTOSKiska.AdTOSacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pTOSKiska.AdTOSacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pTOSKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pTOSKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pTOSKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating TOSKiska")
	return pTOSKiska


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
	pTOSKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pTOSKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pTOSKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pTOSKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pTOSKiska):
#	kDebugObj.Print("Configuring TOSKiska for the Constitution bridge")

	# Clear out any old animations from another configuration
	pTOSKiska.ClearAnimations()

	# Register animation mappings
	pTOSKiska.AddAnimation("TOSHelmTurnCaptain", "Bridge.Characters.TOSMediumAnimations.TOSTurnAtHTowardsCaptain")
	pTOSKiska.AddAnimation("TOSHelmBackCaptain", "Bridge.Characters.TOSMediumAnimations.TOSTurnBackAtHFromCaptain")


	pTOSKiska.AddAnimation("TOSHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
#	pTOSKiska.AddAnimation("TOSHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")
	pTOSKiska.AddAnimation("TOSHelmGlanceAwayCaptain", "Bridge.Characters.TOSMediumAnimations.EBHConsoleInteraction")

	# Breathing
	pTOSKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# TOSeraction
	pTOSKiska.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.EBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pTOSKiska.AddAnimation("PushingButtons", "Bridge.Characters.TOSMediumAnimations.EBHConsoleInteraction")

	# Hit animations
	#pTOSKiska.AddAnimation("TOSHelmHit", "Bridge.Characters.TOSMediumAnimations.TOSHHit")
	#pTOSKiska.AddAnimation("TOSHelmHitHard", "Bridge.Characters.TOSMediumAnimations.TOSHHitHard")
	#pTOSKiska.AddAnimation("TOSHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pTOSKiska.AddAnimation("TOSHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pTOSKiska)

	pTOSKiska.SetLocation("TOSHelm")
#	pTOSKiska.SetLookAtAdj(0, 0, 0)
	pTOSKiska.AddPositionZoom("TOSHelm", 1.2)
#	kDebugObj.Print("Finished configuring TOSKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSKiska):
	# TOSeraction with their environment
	pTOSKiska.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pTOSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pTOSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pTOSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pTOSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pTOSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pTOSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pTOSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pTOSKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
						"gh081",	# TOSercept course plotted

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
