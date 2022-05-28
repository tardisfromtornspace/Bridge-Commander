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
#	kDebugObj.Print("Creating IntKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pIntKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pIntKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	pIntKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pIntKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntKiska)

	# Setup the character configuration
	pIntKiska.SetSize(App.CharacterClass.MEDIUM)
	pIntKiska.SetGender(App.CharacterClass.FEMALE)
	pIntKiska.SetStanding(0)
	pIntKiska.SetRandomAnimationChance(0.75)
	pIntKiska.SetBlinkChance(0.1)
	pIntKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pIntKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	pIntKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	pIntKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	pIntKiska.SetBlinkStages(3)

	pIntKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	pIntKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	pIntKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	pIntKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pIntKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pIntKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating IntKiska")
	return pIntKiska


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
	pIntKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pIntKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pIntKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForIntrepid()
#
#	Configure ourselves for the Intrepid bridge
#
#	Args:	pIntKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pIntKiska):
#	kDebugObj.Print("Configuring IntKiska for the Intrepid bridge")

	# Clear out any old animations from another configuration
	pIntKiska.ClearAnimations()

	# Register animation mappings
	pIntKiska.AddAnimation("IntHelmTurnCaptain", "Bridge.Characters.IntMediumAnimations.IntTurnAtHTowardsCaptain")
	pIntKiska.AddAnimation("IntHelmBackCaptain", "Bridge.Characters.IntMediumAnimations.IntTurnBackAtHFromCaptain")


	pIntKiska.AddAnimation("IntHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pIntKiska.AddAnimation("IntHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pIntKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# Interaction
	pIntKiska.AddRandomAnimation("Bridge.Characters.IntMediumAnimations.EBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pIntKiska.AddAnimation("PushingButtons", "Bridge.Characters.IntMediumAnimations.EBHConsoleInteraction")

	# Hit animations
	#pIntKiska.AddAnimation("IntHelmHit", "Bridge.Characters.IntMediumAnimations.IntHHit")
	#pIntKiska.AddAnimation("IntHelmHitHard", "Bridge.Characters.IntMediumAnimations.IntHHitHard")
	pIntKiska.AddAnimation("IntHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pIntKiska.AddAnimation("IntHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pIntKiska)

	pIntKiska.SetLocation("IntHelm")
	pIntKiska.SetLookAtAdj(-30, 0, 50)
	pIntKiska.AddPositionZoom("IntHelm", 0.5, "Helm")
#	kDebugObj.Print("Finished configuring IntKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pIntKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntKiska):
	# Interaction with their environment
	pIntKiska.AddRandomAnimation("Bridge.Characters.IntMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pIntKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pIntKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pIntKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pIntKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pIntKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pIntKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
