from bcdebug import debug
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
	
	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("Tactical") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Tactical")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif", None)
	pEXLFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pEXLFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pEXLFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLFelix)

	# Set up character configuration
	pEXLFelix.SetSize(App.CharacterClass.LARGE)
	pEXLFelix.SetGender(App.CharacterClass.MALE)
	pEXLFelix.SetStanding(1)
	pEXLFelix.SetRandomAnimationChance(0.75)
	pEXLFelix.SetBlinkChance(0.1)
	pEXLFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pEXLFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pEXLFelix.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pEXLFelix.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pEXLFelix.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pEXLFelix.SetBlinkStages(3)

	pEXLFelix.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pEXLFelix.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pEXLFelix.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pEXLFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pEXLFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pEXLFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pEXLFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pEXLFelix

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
	
	debug(__name__ + ", CreateCharacterNoSounds")
	import Bridge.TacticalMenuHandlers

	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "Headfelix/felix_head.nif", None)
	pEXLFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headfelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pEXLFelix)
	pEXLFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pEXLFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLFelix)

	# Set up character configuration
	pEXLFelix.SetSize(App.CharacterClass.LARGE)
	pEXLFelix.SetGender(App.CharacterClass.MALE)
	pEXLFelix.SetStanding(1)
	pEXLFelix.SetHidden(1)
	pEXLFelix.SetRandomAnimationChance(0.75)
	pEXLFelix.SetBlinkChance(0.1)
	pEXLFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pEXLFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pEXLFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pEXLFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pEXLFelix


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
	debug(__name__ + ", CreateCharacterNoMenu")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "Headfelix/felix_head.nif", None)
	pEXLFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headfelix/felix_head.nif")
	pEXLFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "Headfelix/felix_head.tga")

	pEXLFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLFelix)

	# Set up character configuration
	pEXLFelix.SetSize(App.CharacterClass.LARGE)
	pEXLFelix.SetGender(App.CharacterClass.MALE)
	pEXLFelix.SetStanding(1)
	pEXLFelix.SetHidden(1)
	pEXLFelix.SetRandomAnimationChance(0.75)
	pEXLFelix.SetBlinkChance(0.1)
	pEXLFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pEXLFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pEXLFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pEXLFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pEXLFelix


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
	debug(__name__ + ", ConfigureForShip")
	pEXLFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pEXLFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pEXLFelix)


###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pEXLFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pEXLFelix):
#	kDebugObj.Print("Configuring Felix for the EXL bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcelsior")
	pEXLFelix.ClearAnimations()

	# Register animation mappings
	pEXLFelix.AddAnimation("SeatedEXLTactical", "Bridge.Characters.EXLLargeAnimations.EXLseatedTL")
	pEXLFelix.AddAnimation("EBL1LToT", "Bridge.Characters.EXLLargeAnimations.EBMoveFromL1ToT")
	pEXLFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.EXLLargeAnimations.EBMoveFromTToL1")
	pEXLFelix.AddAnimation("EXLTacticalTurnCaptain", "Bridge.Characters.EXLLargeAnimations.EXLTurnAtTTowardsCaptain")
	pEXLFelix.AddAnimation("EXLTacticalBackCaptain", "Bridge.Characters.EXLLargeAnimations.EXLTurnBackAtTFromCaptain")

	pEXLFelix.AddAnimation("EXLTacticalTurnC", "Bridge.Characters.EXLLargeAnimations.EXLTurnAtTTowardsCaptain")
	pEXLFelix.AddAnimation("EXLTacticalBackC", "Bridge.Characters.EXLLargeAnimations.EXLTurnBackAtTFromCaptain")
	pEXLFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.EXLLargeAnimations.EBTTalkE")
	pEXLFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.EXLLargeAnimations.EBTTalkFinE")
	pEXLFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.EXLLargeAnimations.EBTTalkH")
	pEXLFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.EXLLargeAnimations.EBTTalkFinH")
	pEXLFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.EXLLargeAnimations.EBTTalkS")
	pEXLFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.EXLLargeAnimations.EBTTalkFinS")

	pEXLFelix.AddAnimation("EBTacticalTurEXL", "Bridge.Characters.EXLLargeAnimations.EBTTalkE")
	pEXLFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.EXLLargeAnimations.EBTTalkFinE")

	pEXLFelix.AddAnimation("EXLTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pEXLFelix.AddAnimation("EXLTacticalGlanceAwayCaptain", "Bridge.Characters.EXLLargeAnimations.EXLTConsoleInteraction")

	# Breathing
	pEXLFelix.AddAnimation("EXLTacticalBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pEXLFelix.AddAnimation("EXLTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pEXLFelix.AddRandomAnimation("Bridge.Characters.EXLLargeAnimations.EXLTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pEXLFelix.AddAnimation("PushingButtons", "Bridge.Characters.EXLLargeAnimations.EXLTConsoleInteraction")

	# Hit animations		
	#pEXLFelix.AddAnimation("EXLTacticalHit", "Bridge.Characters.EXLLargeAnimations.EXLTHit")
	#pEXLFelix.AddAnimation("EXLTacticalHitHard", "Bridge.Characters.EXLLargeAnimations.EXLTHitHard")
	pEXLFelix.AddAnimation("EXLTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pEXLFelix.AddAnimation("EXLTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pEXLFelix)
	
	pEXLFelix.SetLocation("EXLTactical")
	pEXLFelix.SetStanding(0)
#	pEXLFelix.AddPositionZoom("EXLTactical", 1.0, "Tactical")
	pEXLFelix.AddPositionZoom("EXLTactical", 1.0)
#	pEXLFelix.SetLookAtAdj(0, 0, 10)
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
#	Args:	pEXLFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLFelix):
	debug(__name__ + ", AddCommonAnimations")
	pEXLFelix.AddRandomAnimation("Bridge.Characters.EXLLargeAnimations.TLookAroundConsoleDown", 1, 1)

	pEXLFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pEXLFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pEXLFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pEXLFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pEXLFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pEXLFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pEXLFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pEXLFelix):
	debug(__name__ + ", OffBridgeStart")
	pEXLFelix = App.CharacterClass_Cast(pEXLFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pEXLFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pEXLFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pEXLFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pEXLFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	pEXLFelix.ClearAnimations()

	# Register animation mappings
	pEXLFelix.SetStanding(1)
	pEXLFelix.SetHidden(0)
	pEXLFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pEXLFelix)

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
	debug(__name__ + ", LoadSounds")
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
