###############################################################################
#	Filename:	AmbKiska.py
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
#	kDebugObj.Print("Creating AmbKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pAmbKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pAmbKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pAmbKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbKiska)

	# Setup the character configuration
	pAmbKiska.SetSize(App.CharacterClass.MEDIUM)
	pAmbKiska.SetGender(App.CharacterClass.FEMALE)
	pAmbKiska.SetStanding(0)
	pAmbKiska.SetRandomAnimationChance(0.75)
	pAmbKiska.SetBlinkChance(0.1)
	pAmbKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pAmbKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pAmbKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pAmbKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pAmbKiska.SetBlinkStages(3)

	pAmbKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pAmbKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pAmbKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pAmbKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pAmbKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pAmbKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating AmbKiska")
	return pAmbKiska


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
	pAmbKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pAmbKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pAmbKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pAmbKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pAmbKiska):
#	kDebugObj.Print("Configuring AmbKiska for the Ambassador bridge")

	# Clear out any old animations from another configuration
	pAmbKiska.ClearAnimations()

	# Register animation mappings
	pAmbKiska.AddAnimation("AmbHelmTurnCaptain", "Bridge.Characters.AmbMediumAnimations.AmbTurnAtHTowardsCaptain")
	pAmbKiska.AddAnimation("AmbHelmBackCaptain", "Bridge.Characters.AmbMediumAnimations.AmbTurnBackAtHFromCaptain")


	pAmbKiska.AddAnimation("AmbHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pAmbKiska.AddAnimation("AmbHelmGlanceAwayCaptain", "Bridge.Characters.AmbMediumAnimations.AmbHConsoleInteraction")

	# Breathing
	pAmbKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.AmbMediumAnimations.Amb_seated_h")

	# Amberaction
	pAmbKiska.AddRandomAnimation("Bridge.Characters.AmbMediumAnimations.AmbHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pAmbKiska.AddAnimation("PushingButtons", "Bridge.Characters.AmbMediumAnimations.AmbHConsoleInteraction")

	# Hit animations
	#pAmbKiska.AddAnimation("AmbHelmHit", "Bridge.Characters.AmbMediumAnimations.AmbHHit")
	#pAmbKiska.AddAnimation("AmbHelmHitHard", "Bridge.Characters.AmbMediumAnimations.AmbHHitHard")
	pAmbKiska.AddAnimation("AmbHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pAmbKiska.AddAnimation("AmbHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pAmbKiska)

	pAmbKiska.SetLocation("AmbHelm")
	pAmbKiska.SetLookAtAdj(42.6865, -90.582, 0.2922)
	pAmbKiska.SetStanding(0)
	pAmbKiska.AddPositionZoom("AmbHelm", 0.9, "Helm")
#	kDebugObj.Print("Finished configuring AmbKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pAmbKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbKiska):
	# Amberaction with their environment
	pAmbKiska.AddRandomAnimation("Bridge.Characters.AmbMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pAmbKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pAmbKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pAmbKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pAmbKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pAmbKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pAmbKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
