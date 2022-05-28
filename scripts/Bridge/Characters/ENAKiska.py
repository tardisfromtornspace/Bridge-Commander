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
#	kDebugObj.Print("Creating ENAKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pENAKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pENAKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pENAKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pENAKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAKiska)

	# Setup the character configuration
	pENAKiska.SetSize(App.CharacterClass.MEDIUM)
	pENAKiska.SetGender(App.CharacterClass.FEMALE)
	pENAKiska.SetStanding(0)
	pENAKiska.SetRandomAnimationChance(0.75)
	pENAKiska.SetBlinkChance(0.1)
	pENAKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pENAKiska.AdENAacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pENAKiska.AdENAacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pENAKiska.AdENAacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pENAKiska.SetBlinkStages(3)

	pENAKiska.AdENAacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pENAKiska.AdENAacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pENAKiska.AdENAacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pENAKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pENAKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENAKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating ENAKiska")
	return pENAKiska


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
	pENAKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pENAKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pENAKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pENAKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pENAKiska):
#	kDebugObj.Print("Configuring ENAKiska for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	pENAKiska.ClearAnimations()

	# Register animation mappings
	pENAKiska.AddAnimation("ENAHelmTurnCaptain", "Bridge.Characters.ENAMediumAnimations.ENATurnAtHTowardsCaptain")
	pENAKiska.AddAnimation("ENAHelmBackCaptain", "Bridge.Characters.ENAMediumAnimations.ENATurnBackAtHFromCaptain")


	pENAKiska.AddAnimation("ENAHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pENAKiska.AddAnimation("ENAHelmGlanceAwayCaptain", "Bridge.Characters.ENAMediumAnimations.EBHConsoleInteraction")

	# Breathing
	pENAKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# ENAeraction
	pENAKiska.AddRandomAnimation("Bridge.Characters.ENAMediumAnimations.EBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pENAKiska.AddAnimation("PushingButtons", "Bridge.Characters.ENAMediumAnimations.EBHConsoleInteraction")

	# Hit animations
	#pENAKiska.AddAnimation("ENAHelmHit", "Bridge.Characters.ENAMediumAnimations.ENAHHit")
	#pENAKiska.AddAnimation("ENAHelmHitHard", "Bridge.Characters.ENAMediumAnimations.ENAHHitHard")
	pENAKiska.AddAnimation("ENAHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENAKiska.AddAnimation("ENAHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pENAKiska)

	pENAKiska.SetLocation("ENAHelm")
#	pENAKiska.SetLookAtAdj(0, 0, 0)
#	pENAKiska.AddPositionZoom("ENAHelm", 0.6, "Helm")
	pENAKiska.AddPositionZoom("ENAHelm", 0.6)
#	kDebugObj.Print("Finished configuring ENAKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENAKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENAKiska):
	# ENAeraction with their environment
	pENAKiska.AddRandomAnimation("Bridge.Characters.ENAMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pENAKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENAKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENAKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENAKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pENAKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pENAKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pENAKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pENAKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
						"gh081",	# ENAercept course plotted

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
