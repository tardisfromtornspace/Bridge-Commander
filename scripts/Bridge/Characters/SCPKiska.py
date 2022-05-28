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
#	kDebugObj.Print("Creating SCPKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pSCPKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pSCPKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pSCPKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPKiska)

	# Setup the character configuration
	pSCPKiska.SetSize(App.CharacterClass.MEDIUM)
	pSCPKiska.SetGender(App.CharacterClass.FEMALE)
	pSCPKiska.SetStanding(0)
	pSCPKiska.SetRandomAnimationChance(0.75)
	pSCPKiska.SetBlinkChance(0.1)
	pSCPKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pSCPKiska.AdSCPacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pSCPKiska.AdSCPacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pSCPKiska.AdSCPacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pSCPKiska.SetBlinkStages(3)

	pSCPKiska.AdSCPacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pSCPKiska.AdSCPacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pSCPKiska.AdSCPacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pSCPKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pSCPKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pSCPKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating SCPKiska")
	return pSCPKiska


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
	pSCPKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pSCPKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pSCPKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pSCPKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pSCPKiska):
#	kDebugObj.Print("Configuring SCPKiska for the Galor bridge")

	# Clear out any old animations from another configuration
	pSCPKiska.ClearAnimations()

	# Register animation mappings
	pSCPKiska.AddAnimation("SCPHelmTurnCaptain", "Bridge.Characters.SCPMediumAnimations.SCPTurnAtHTowardsCaptain")
	pSCPKiska.AddAnimation("SCPHelmBackCaptain", "Bridge.Characters.SCPMediumAnimations.SCPTurnBackAtHFromCaptain")


	pSCPKiska.AddAnimation("SCPHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pSCPKiska.AddAnimation("SCPHelmGlanceAwayCaptain", "Bridge.Characters.SCPMediumAnimations.EBHConsoleInteraction")

	# Breathing
	pSCPKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# SCPeraction
	pSCPKiska.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.EBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pSCPKiska.AddAnimation("PushingButtons", "Bridge.Characters.SCPMediumAnimations.EBHConsoleInteraction")

	# Hit animations
	pSCPKiska.AddAnimation("SCPHelmHit", "Bridge.Characters.SCPMediumAnimations.SCPHHit")
	pSCPKiska.AddAnimation("SCPHelmHitHard", "Bridge.Characters.SCPMediumAnimations.SCPHHitHard")
	pSCPKiska.AddAnimation("SCPHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pSCPKiska.AddAnimation("SCPHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pSCPKiska)

	pSCPKiska.SetLocation("SCPHelm")
#	pSCPKiska.SetLookAtAdj(0, 0, 0)
#	pSCPKiska.AddPositionZoom("SCPHelm", 0.6, "Helm")
	pSCPKiska.AddPositionZoom("SCPHelm", 0.6)
#	kDebugObj.Print("Finished configuring SCPKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pSCPKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPKiska):
	# SCPeraction with their environment
	pSCPKiska.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pSCPKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pSCPKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pSCPKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pSCPKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pSCPKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pSCPKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pSCPKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
						"gh081",	# SCPercept course plotted

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
