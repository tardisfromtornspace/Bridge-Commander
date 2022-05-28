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
#	kDebugObj.Print("Creating promKiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character

	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	ppromKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	ppromKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Saffi/saffi_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head.tga")

	ppromKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(ppromKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromKiska)

	# Setup the character configuration
	ppromKiska.SetSize(App.CharacterClass.MEDIUM)
	ppromKiska.SetGender(App.CharacterClass.FEMALE)
	ppromKiska.SetStanding(0)
	ppromKiska.SetRandomAnimationChance(0.75)
	ppromKiska.SetBlinkChance(0.1)
	ppromKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()

	ppromKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink1.tga")
	ppromKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_blink2.tga")
	ppromKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/Saffi_head_eyesclosed.tga")
	ppromKiska.SetBlinkStages(3)

	ppromKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_a.tga")
	ppromKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_e.tga")
	ppromKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Saffi/saffi_head_u.tga")
	ppromKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(ppromKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	ppromKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating promKiska")
	return ppromKiska


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
	ppromKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (ppromKiska == None):
#		kDebugObj.Print("******* Helm officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Helm..")
	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(ppromKiska)

	#
	# This is where code to set up responses based on the ships state
	# e.g. "Orbiting planet"
	#


###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	ppromKiska	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(ppromKiska):
#	kDebugObj.Print("Configuring promKiska for the prometheus bridge")

	# Clear out any old animations from another configuration
	ppromKiska.ClearAnimations()

	# Register animation mappings
	ppromKiska.AddAnimation("promHelmTurnCaptain", "Bridge.Characters.promMediumAnimations.promTurnAtHTowardsCaptain")
	ppromKiska.AddAnimation("promHelmBackCaptain", "Bridge.Characters.promMediumAnimations.promTurnBackAtHFromCaptain")


	ppromKiska.AddAnimation("promHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	ppromKiska.AddAnimation("promHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	ppromKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# interaction
	ppromKiska.AddRandomAnimation("Bridge.Characters.promSmallAnimations.promSConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	ppromKiska.AddAnimation("PushingButtons", "Bridge.Characters.promMediumAnimations.DBHConsoleInteraction")

	# Hit animations
	#ppromKiska.AddAnimation("promHelmHit", "Bridge.Characters.promMediumAnimations.promHHit")
	#ppromKiska.AddAnimation("promHelmHitHard", "Bridge.Characters.promMediumAnimations.promHHitHard")
	ppromKiska.AddAnimation("promHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	ppromKiska.AddAnimation("promHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(ppromKiska)

	ppromKiska.SetLocation("promHelm")
	ppromKiska.SetLookAtAdj(-0.001, -10, 10)
	ppromKiska.AddPositionZoom("promHelm", 0.65, "Helm")
#	kDebugObj.Print("Finished configuring promKiska")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	ppromKiska	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromKiska):
	# promeraction with their environment
	ppromKiska.AddRandomAnimation("Bridge.Characters.promMediumAnimations.HLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	# Just random stuff
	ppromKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	ppromKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	ppromKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	# These look bad
	#ppromKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#ppromKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")

	# These force the arms up
	#ppromKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#ppromKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")

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
