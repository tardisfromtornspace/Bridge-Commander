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
#	kDebugObj.Print("Creating ExcKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pExcKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pExcKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pExcKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pExcKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcKiska)

	# Setup the character configuration
	pExcKiska.SetSize(App.CharacterClass.MEDIUM)
	pExcKiska.SetGender(App.CharacterClass.FEMALE)
	pExcKiska.SetStanding(0)
	pExcKiska.SetRandomAnimationChance(0.75)
	pExcKiska.SetBlinkChance(0.1)
	pExcKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pExcKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pExcKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pExcKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pExcKiska.SetBlinkStages(3)

	pExcKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pExcKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pExcKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pExcKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pExcKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pExcKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating ExcKiska")
	return pExcKiska


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
	pExcKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pExcKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pExcKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForExcalibur()
#
#	Configure ourselves for the Excalibur bridge
#
#	Args:	pExcKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pExcKiska):
#	kDebugObj.Print("Configuring ExcKiska for the Excalibur bridge")

	# Clear out any old animations from another configuration
	pExcKiska.ClearAnimations()

	# Register animation mappings
	pExcKiska.AddAnimation("ExcHelmTurnCaptain", "Bridge.Characters.ExcMediumAnimations.ExcTurnAtHTowardsCaptain")
	pExcKiska.AddAnimation("ExcHelmBackCaptain", "Bridge.Characters.ExcMediumAnimations.ExcTurnBackAtHFromCaptain")


	pExcKiska.AddAnimation("ExcHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pExcKiska.AddAnimation("ExcHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pExcKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# Exceraction
	pExcKiska.AddRandomAnimation("Bridge.Characters.ExcMediumAnimations.EBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pExcKiska.AddAnimation("PushingButtons", "Bridge.Characters.ExcMediumAnimations.EBHConsoleInteraction")

	# Hit animations
	#pExcKiska.AddAnimation("ExcHelmHit", "Bridge.Characters.ExcMediumAnimations.ExcHHit")
	#pExcKiska.AddAnimation("ExcHelmHitHard", "Bridge.Characters.ExcMediumAnimations.ExcHHitHard")
	pExcKiska.AddAnimation("ExcHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pExcKiska.AddAnimation("ExcHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pExcKiska)

	pExcKiska.SetLocation("ExcHelm")
	pExcKiska.SetLookAtAdj(0, 0, 40)
	pExcKiska.AddPositionZoom("ExcHelm", 0.8, "Helm")
#	kDebugObj.Print("Finished configuring ExcKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pExcKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcKiska):
	# Exceraction with their environment
	pExcKiska.AddRandomAnimation("Bridge.Characters.ExcMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pExcKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pExcKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pExcKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pExcKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pExcKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pExcKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
						"gh081",	# Excercept course plotted

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
