###############################################################################
#	Filename:	Felix.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Felix Savali, tactical officer, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create Felix by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating Felix")
	
	if (pSet.GetObject("Tactical") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Tactical")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif", None)
	pTOSFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pTOSFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pTOSFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSFelix)

	# Set up character configuration
	pTOSFelix.SetSize(App.CharacterClass.LARGE)
	pTOSFelix.SetGender(App.CharacterClass.MALE)
	pTOSFelix.SetStanding(1)
	pTOSFelix.SetRandomAnimationChance(0.75)
	pTOSFelix.SetBlinkChance(0.1)
	pTOSFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pTOSFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pTOSFelix.AdTOSacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pTOSFelix.AdTOSacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pTOSFelix.AdTOSacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pTOSFelix.SetBlinkStages(3)

	pTOSFelix.AdTOSacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pTOSFelix.AdTOSacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pTOSFelix.AdTOSacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pTOSFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pTOSFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pTOSFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pTOSFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pTOSFelix

###############################################################################
#	CreateCharacterNoSounds()
#
#	Create Felix by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacterNoSounds(pSet):
#	kDebugObj.Print("Creating Felix")
	
	import Bridge.TacticalMenuHandlers
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pTOSFelix)

	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeaTOSelix/felix_head.nif", None)
	pTOSFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeaTOSelix/felix_head.nif")
	pTOSFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pTOSFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSFelix)

	# Set up character configuration
	pTOSFelix.SetSize(App.CharacterClass.LARGE)
	pTOSFelix.SetGender(App.CharacterClass.MALE)
	pTOSFelix.SetStanding(1)
	pTOSFelix.SetHidden(1)
	pTOSFelix.SetRandomAnimationChance(0.75)
	pTOSFelix.SetBlinkChance(0.1)
	pTOSFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pTOSFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pBrex.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pTOSFelix


###############################################################################
#	CreateCharacterNoMenu()
#
#	Create Felix by building his character and placing him on the passed in set.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacterNoMenu(pSet):
#	kDebugObj.Print("Creating Felix")
	
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeaTOSelix/felix_head.nif", None)
	pTOSFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeaTOSelix/felix_head.nif")
	pTOSFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeaTOSelix/felix_head.tga")

	pTOSFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSFelix)

	# Set up character configuration
	pTOSFelix.SetSize(App.CharacterClass.LARGE)
	pTOSFelix.SetGender(App.CharacterClass.MALE)
	pTOSFelix.SetStanding(1)
	pTOSFelix.SetHidden(1)
	pTOSFelix.SetRandomAnimationChance(0.75)
	pTOSFelix.SetBlinkChance(0.1)
	pTOSFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pTOSFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pTOSFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pTOSFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pTOSFelix


###############################################################################
#	ConfigureForShip()
#
#	Configure ourselves for the particular ship object.  This involves setting
#	up range watchers that tell us how to report.
#
#	Args:	pSet	- the Set object
#			pShip	- the player's ship
#
#	Return:	none
###############################################################################
def ConfigureForShip(pSet, pShip):
	# Get our character object
	pTOSFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pTOSFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pTOSFelix)


###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pTOSFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pTOSFelix):
#	kDebugObj.Print("Configuring Felix for the TOS bridge")

	# Clear out any old animations from another configuration
	pTOSFelix.ClearAnimations()

	# Register animation mappings
	pTOSFelix.AddAnimation("SeatedTOSTactical", "Bridge.Characters.TOSLargeAnimations.TOSseatedTL")
	pTOSFelix.AddAnimation("EBL1LToT", "Bridge.Characters.TOSLargeAnimations.EBMoveFromL1ToT")
	pTOSFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.TOSLargeAnimations.EBMoveFromTToL1")
	pTOSFelix.AddAnimation("TOSTacticalTurnCaptain", "Bridge.Characters.TOSLargeAnimations.TOSTurnAtTTowardsCaptain")
	pTOSFelix.AddAnimation("TOSTacticalBackCaptain", "Bridge.Characters.TOSLargeAnimations.TOSTurnBackAtTFromCaptain")

	pTOSFelix.AddAnimation("TOSTacticalTurnC", "Bridge.Characters.TOSLargeAnimations.TOSTurnAtTTowardsCaptain")
	pTOSFelix.AddAnimation("TOSTacticalBackC", "Bridge.Characters.TOSLargeAnimations.TOSTurnBackAtTFromCaptain")
	pTOSFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.TOSLargeAnimations.EBTTalkE")
	pTOSFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.TOSLargeAnimations.EBTTalkFinE")
	pTOSFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.TOSLargeAnimations.EBTTalkH")
	pTOSFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.TOSLargeAnimations.EBTTalkFinH")
	pTOSFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.TOSLargeAnimations.EBTTalkS")
	pTOSFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.TOSLargeAnimations.EBTTalkFinS")

	pTOSFelix.AddAnimation("EBTacticalTurTOS", "Bridge.Characters.TOSLargeAnimations.EBTTalkE")
	pTOSFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.TOSLargeAnimations.EBTTalkFinE")

	pTOSFelix.AddAnimation("TOSTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pTOSFelix.AddAnimation("TOSTacticalGlanceAwayCaptain", "Bridge.Characters.TOSLargeAnimations.TOSTConsoleInteraction")

	# Breathing
	pTOSFelix.AddAnimation("TOSTacticalBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pTOSFelix.AddAnimation("TOSTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# TOSeraction
	pTOSFelix.AddRandomAnimation("Bridge.Characters.TOSLargeAnimations.TOSTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pTOSFelix.AddAnimation("PushingButtons", "Bridge.Characters.TOSLargeAnimations.TOSTConsoleInteraction")

	# Hit animations		
	#pTOSFelix.AddAnimation("TOSTacticalHit", "Bridge.Characters.TOSLargeAnimations.TOSTHit")
	#pTOSFelix.AddAnimation("TOSTacticalHitHard", "Bridge.Characters.TOSLargeAnimations.TOSTHitHard")
	#pTOSFelix.AddAnimation("TOSTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pTOSFelix.AddAnimation("TOSTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pTOSFelix)
	
	pTOSFelix.SetLocation("TOSTactical")
	pTOSFelix.SetStanding(0)
	pTOSFelix.AddPositionZoom("TOSTactical", 0.8, "Tactical")
	pTOSFelix.SetLookAtAdj(6.33354, -327.676, 1) 
#	kDebugObj.Print("Finished configuring Felix")



###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSFelix):
	pTOSFelix.AddRandomAnimation("Bridge.Characters.TOSLargeAnimations.TLookAroundConsoleDown", 1, 1)

	pTOSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pTOSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pTOSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pTOSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pTOSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pTOSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pTOSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pTOSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pTOSFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pTOSFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pTOSFelix):
	pTOSFelix = App.CharacterClass_Cast(pTOSFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pTOSFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pTOSFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pTOSFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pTOSFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	pTOSFelix.ClearAnimations()

	# Register animation mappings
	pTOSFelix.SetStanding(1)
	pTOSFelix.SetHidden(0)
	pTOSFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pTOSFelix)

#	kDebugObj.Print("Finished configuring Felix")

###############################################################################
#	LoadSounds
#	
#	Precache Felix's typical voice lines, so they don't hitch the
#	game when they try to play.
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")

	# Loop through all of Felix's voice lines that we want to preload, and load them.
	for sLine in g_lsFelixLines:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)

#
# A list of the voice lines we want preloaded for Felix.
#
g_lsFelixLines = (
	"AttackStatus_EvadingTorps1",
	"AttackStatus_FallingBack1",
	"AttackStatus_LiningUpFront1",
	"AttackStatus_MovingIn1",
	"AttackStatus_RearTorpRun1",
	"AttackStatus_SweepingPhasers1",
	"BadTarget1",
	"BadTarget2",
	"Disengaging",
	"DontShootTac",
	"EvasiveManuvers", # Sumbody furgot to spel this rite.
	"FelixEnDes",
	"FelixNothingToAdd",
	"FelixNothingToAdd2",
	"FelixNothingToAdd3",
	"FelixSir1",
	"FelixSir2",
	"FelixSir3",
	"FelixSir4",
	"FelixSir5",
	"FelixYes1",
	"FelixYes2",
	"FelixYes3",
	"FelixYes4",
	"ForeShieldsOffline",
	"Incoming1",
	"Incoming2",
	"Incoming3",
	"Incoming4",
	"Incoming5",
	"Incoming6",
	"LoadingPhoton",
	"LoadingQuantum",
	"LoadingTorps",
	"NeedPower",
	"OutOfPhotons",
	"OutOfQuantums",
	"OutOfType",
	"TacticalManuver", # This wun to.
	"gt001",
	"gt002",
	"gt007",
	"gt029",
	"gt030",
	"gt037",
	"gt038",
	"gt212",
	"gt213",
	)
