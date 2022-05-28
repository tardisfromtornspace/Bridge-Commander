from bcdebug import debug
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
#	kDebugObj.Print("Creating NebKiska")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadKiska/kiska_head.nif", None)
	pNebKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadKiska/kiska_head.nif", 1)
	pNebKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadKiska/kiska_head.tga")

	pNebKiska.SetCharacterName("NebKiska")

	# Add the character to the set
	pSet.AddObjectToSet(pNebKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebKiska)

	# Setup the character configuration
	pNebKiska.SetSize(App.CharacterClass.MEDIUM)
	pNebKiska.SetGender(App.CharacterClass.FEMALE)
	pNebKiska.SetStanding(0)
	pNebKiska.SetRandomAnimationChance(0.75)
	pNebKiska.SetBlinkChance(0.1)
	pNebKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	pNebKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_blink1.tga")
	pNebKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_blink2.tga")
	pNebKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_eyesclosed.tga")
	pNebKiska.SetBlinkStages(3)

	pNebKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_a.tga")
	pNebKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_e.tga")
	pNebKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_u.tga")
	pNebKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pNebKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pNebKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating NebKiska")
	return pNebKiska


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
	debug(__name__ + ", ConfigureForShip")
	pNebKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pNebKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pNebKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForNebula()
#
#	Configure ourselves for the Nebula bridge
#
#	Args:	pNebKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pNebKiska):
#	kDebugObj.Print("Configuring NebKiska for the Nebula bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pNebKiska.ClearAnimations()

	# Register animation mappings
	pNebKiska.AddAnimation("NebHelmTurnCaptain", "Bridge.Characters.NebMediumAnimations.NebTurnAtHTowardsCaptain")
	pNebKiska.AddAnimation("NebHelmBackCaptain", "Bridge.Characters.NebMediumAnimations.NebTurnBackAtHFromCaptain")


	pNebKiska.AddAnimation("NebHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pNebKiska.AddAnimation("NebHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pNebKiska.AddAnimation("NebHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# Interaction
	pNebKiska.AddRandomAnimation("Bridge.Characters.NebMediumAnimations.NebHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pNebKiska.AddAnimation("PushingButtons", "Bridge.Characters.NebMediumAnimations.NebHConsoleInteraction")

	# Hit animations
	#pNebKiska.AddAnimation("NebHelmHit", "Bridge.Characters.NebMediumAnimations.NebHHit")
	#pNebKiska.AddAnimation("NebHelmHitHard", "Bridge.Characters.NebMediumAnimations.NebHHitHard")
	pNebKiska.AddAnimation("NebHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pNebKiska.AddAnimation("NebHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pNebKiska)

	pNebKiska.SetLocation("NebHelm")
	pNebKiska.AddPositionZoom("NebHelm", 0.8, "Helm")
	pNebKiska.SetLookAtAdj(2, 0, 75)
#	kDebugObj.Print("Finished configuring NebKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pNebKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebKiska):
	# Interaction with their environment
	debug(__name__ + ", AddCommonAnimations")
	pNebKiska.AddRandomAnimation("Bridge.Characters.NebMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	pNebKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#pNebKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pNebKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#pNebKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pNebKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
	debug(__name__ + ", LoadSounds")
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
