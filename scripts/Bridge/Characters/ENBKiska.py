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
#	kDebugObj.Print("Creating ENBKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pENBKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pENBKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pENBKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pENBKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBKiska)

	# Setup the character configuration
	pENBKiska.SetSize(App.CharacterClass.MEDIUM)
	pENBKiska.SetGender(App.CharacterClass.FEMALE)
	pENBKiska.SetStanding(0)
	pENBKiska.SetRandomAnimationChance(0.75)
	pENBKiska.SetBlinkChance(0.1)
	pENBKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pENBKiska.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pENBKiska.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pENBKiska.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pENBKiska.SetBlinkStages(3)

	pENBKiska.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pENBKiska.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pENBKiska.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pENBKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pENBKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENBKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating ENBKiska")
	return pENBKiska


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
	pENBKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pENBKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pENBKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pENBKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pENBKiska):
#	kDebugObj.Print("Configuring ENBKiska for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	pENBKiska.ClearAnimations()

	# Register animation mappings
	pENBKiska.AddAnimation("ENBHelmTurnCaptain", "Bridge.Characters.ENBMediumAnimations.ENBTurnAtHTowardsCaptain")
	pENBKiska.AddAnimation("ENBHelmBackCaptain", "Bridge.Characters.ENBMediumAnimations.ENBTurnBackAtHFromCaptain")


	pENBKiska.AddAnimation("ENBHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pENBKiska.AddAnimation("ENBHelmGlanceAwayCaptain", "Bridge.Characters.ENBMediumAnimations.EBHConsoleInteraction")

	# Breathing
	pENBKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# ENBeraction
	pENBKiska.AddRandomAnimation("Bridge.Characters.ENBMediumAnimations.EBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pENBKiska.AddAnimation("PushingButtons", "Bridge.Characters.ENBMediumAnimations.EBHConsoleInteraction")

	# Hit animations
	#pENBKiska.AddAnimation("ENBHelmHit", "Bridge.Characters.ENBMediumAnimations.ENBHHit")
	#pENBKiska.AddAnimation("ENBHelmHitHard", "Bridge.Characters.ENBMediumAnimations.ENBHHitHard")
	pENBKiska.AddAnimation("ENBHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENBKiska.AddAnimation("ENBHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pENBKiska)

	pENBKiska.SetLocation("ENBHelm")
#	pENBKiska.SetLookAtAdj(0, 0, 0)
#	pENBKiska.AddPositionZoom("ENBHelm", 0.6, "Helm")
	pENBKiska.AddPositionZoom("ENBHelm", 0.6)
#	kDebugObj.Print("Finished configuring ENBKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENBKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENBKiska):
	# Interaction with their environment
	pENBKiska.AddRandomAnimation("Bridge.Characters.ENBMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pENBKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENBKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENBKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENBKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pENBKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pENBKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pENBKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pENBKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
