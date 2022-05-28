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
#	kDebugObj.Print("Creating novaKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pnovaKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pnovaKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pnovaKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaKiska)

	# Setup the character configuration
	pnovaKiska.SetSize(App.CharacterClass.MEDIUM)
	pnovaKiska.SetGender(App.CharacterClass.FEMALE)
	pnovaKiska.SetStanding(0)
	pnovaKiska.SetRandomAnimationChance(0.75)
	pnovaKiska.SetBlinkChance(0.1)
	pnovaKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pnovaKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pnovaKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pnovaKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pnovaKiska.SetBlinkStages(3)

	pnovaKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pnovaKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pnovaKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pnovaKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pnovaKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pnovaKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating novaKiska")
	return pnovaKiska


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
	pnovaKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pnovaKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pnovaKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pnovaKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pnovaKiska):
#	kDebugObj.Print("Configuring novaKiska for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pnovaKiska.ClearAnimations()

	# Register animation mappings
	pnovaKiska.AddAnimation("novaHelmTurnCaptain", "Bridge.Characters.novaMediumAnimations.novaTurnAtHTowardsCaptain")
	pnovaKiska.AddAnimation("novaHelmBackCaptain", "Bridge.Characters.novaMediumAnimations.novaTurnBackAtHFromCaptain")


	pnovaKiska.AddAnimation("novaHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pnovaKiska.AddAnimation("novaHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pnovaKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# interaction
	pnovaKiska.AddRandomAnimation("Bridge.Characters.novaSmallAnimations.novaSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pnovaKiska.AddAnimation("PushingButtons", "Bridge.Characters.novaMediumAnimations.DBHConsoleInteraction")

	# Hit animations
	#pnovaKiska.AddAnimation("novaHelmHit", "Bridge.Characters.novaMediumAnimations.novaHHit")
	#pnovaKiska.AddAnimation("novaHelmHitHard", "Bridge.Characters.novaMediumAnimations.novaHHitHard")
	pnovaKiska.AddAnimation("novaHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pnovaKiska.AddAnimation("novaHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pnovaKiska)

	pnovaKiska.SetLocation("novaHelm")

#	kDebugObj.Print("Finished configuring novaKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pnovaKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaKiska):
	# novaeraction with their environment
	pnovaKiska.AddRandomAnimation("Bridge.Characters.novaMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pnovaKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pnovaKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pnovaKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pnovaKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pnovaKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pnovaKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pnovaKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
						"gh081",	# intercept course plotted

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
