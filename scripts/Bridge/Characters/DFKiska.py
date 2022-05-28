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
#	kDebugObj.Print("Creating DFKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pDFKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pDFKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pDFKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pDFKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFKiska)

	# Setup the character configuration
	pDFKiska.SetSize(App.CharacterClass.MEDIUM)
	pDFKiska.SetGender(App.CharacterClass.FEMALE)
	pDFKiska.SetStanding(0)
	pDFKiska.SetRandomAnimationChance(0.75)
	pDFKiska.SetBlinkChance(0.1)
	pDFKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pDFKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pDFKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pDFKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pDFKiska.SetBlinkStages(3)

	pDFKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pDFKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pDFKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pDFKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pDFKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDFKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating DFKiska")
	return pDFKiska


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
	pDFKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pDFKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pDFKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pDFKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pDFKiska):
#	kDebugObj.Print("Configuring DFKiska for the Defiant bridge")

	# Clear out any old animations from another configuration
	pDFKiska.ClearAnimations()

	# Register animation mappings
	pDFKiska.AddAnimation("DFHelmTurnCaptain", "Bridge.Characters.DFMediumAnimations.DFTurnAtHTowardsCaptain")
	pDFKiska.AddAnimation("DFHelmBackCaptain", "Bridge.Characters.DFMediumAnimations.DFTurnBackAtHFromCaptain")


	pDFKiska.AddAnimation("DFHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pDFKiska.AddAnimation("DFHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pDFKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# DFeraction
	pDFKiska.AddRandomAnimation("Bridge.Characters.DFMediumAnimations.EBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pDFKiska.AddAnimation("PushingButtons", "Bridge.Characters.DFMediumAnimations.EBHConsoleInteraction")

	# Hit animations
	#pDFKiska.AddAnimation("DFHelmHit", "Bridge.Characters.DFMediumAnimations.DFHHit")
	#pDFKiska.AddAnimation("DFHelmHitHard", "Bridge.Characters.DFMediumAnimations.DFHHitHard")
	pDFKiska.AddAnimation("DFHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pDFKiska.AddAnimation("DFHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pDFKiska)

	pDFKiska.SetLocation("DFHelm")
	pDFKiska.SetLookAtAdj(-0.001, -10, 10)
	pDFKiska.AddPositionZoom("DFHelm", 0.65, "Helm")
#	kDebugObj.Print("Finished configuring DFKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pDFKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFKiska):
	# DFeraction with their environment
	pDFKiska.AddRandomAnimation("Bridge.Characters.DFMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pDFKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pDFKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pDFKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pDFKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pDFKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
						"gh081",	# DFercept course plotted

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
