from bcdebug import debug
###############################################################################
#	Filename:	AmbFelix.py
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
	pAmbFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pAmbFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pAmbFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbFelix)

	# Set up character configuration
	pAmbFelix.SetSize(App.CharacterClass.LARGE)
	pAmbFelix.SetGender(App.CharacterClass.MALE)
	pAmbFelix.SetStanding(0)
	pAmbFelix.SetRandomAnimationChance(1.0)
	pAmbFelix.SetBlinkChance(0.1)
	pAmbFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pAmbFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pAmbFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pAmbFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pAmbFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pAmbFelix.SetBlinkStages(3)

	pAmbFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pAmbFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pAmbFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pAmbFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pAmbFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pAmbFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pAmbFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pAmbFelix

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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif", None)
	pAmbFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pAmbFelix)
	pAmbFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pAmbFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbFelix)

	# Set up character configuration
	pAmbFelix.SetSize(App.CharacterClass.LARGE)
	pAmbFelix.SetGender(App.CharacterClass.MALE)
	pAmbFelix.SetStanding(1)
	pAmbFelix.SetHidden(1)
	pAmbFelix.SetRandomAnimationChance(0.75)
	pAmbFelix.SetBlinkChance(0.1)
	pAmbFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pAmbFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pAmbFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pAmbFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pAmbFelix


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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif", None)
	pAmbFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pAmbFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pAmbFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbFelix)

	# Set up character configuration
	pAmbFelix.SetSize(App.CharacterClass.LARGE)
	pAmbFelix.SetGender(App.CharacterClass.MALE)
	pAmbFelix.SetStanding(1)
	pAmbFelix.SetHidden(1)
	pAmbFelix.SetRandomAnimationChance(0.75)
	pAmbFelix.SetBlinkChance(0.1)
	pAmbFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pAmbFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pAmbFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pAmbFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pAmbFelix


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
	pAmbFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pAmbFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pAmbFelix)


###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pAmbFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pAmbFelix):
#	kDebugObj.Print("Configuring Felix for the Amb bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForAmbassador")
	pAmbFelix.ClearAnimations()

	# Register animation mappings
	pAmbFelix.AddAnimation("SeatedAmbTactical", "Bridge.Characters.AmbLargeAnimations.Amb_seated_t")
	#pAmbFelix.AddAnimation("EBL1LToT", "Bridge.Characters.AmbLargeAnimations.EBMoveFromL1ToT")
	#pAmbFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.AmbLargeAnimations.EBMoveFromTToL1")
	pAmbFelix.AddAnimation("AmbTacticalTurnCaptain", "Bridge.Characters.AmbLargeAnimations.AmbTurnAtTTowardsCaptain")
	pAmbFelix.AddAnimation("AmbTacticalBackCaptain", "Bridge.Characters.AmbLargeAnimations.AmbTurnBackAtTFromCaptain")

	pAmbFelix.AddAnimation("AmbTacticalTurnC", "Bridge.Characters.AmbLargeAnimations.AmbTurnAtTTowardsCaptain")
	pAmbFelix.AddAnimation("AmbTacticalBackC", "Bridge.Characters.AmbLargeAnimations.AmbTurnBackAtTFromCaptain")
	#pAmbFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.AmbLargeAnimations.EBTTalkE")
	#pAmbFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.AmbLargeAnimations.EBTTalkFinE")
	#pAmbFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.AmbLargeAnimations.EBTTalkH")
	#pAmbFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.AmbLargeAnimations.EBTTalkFinH")
	#pAmbFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.AmbLargeAnimations.EBTTalkS")
	#pAmbFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.AmbLargeAnimations.EBTTalkFinS")

	#pAmbFelix.AddAnimation("EBTacticalTurAmb", "Bridge.Characters.AmbLargeAnimations.EBTTalkE")
	#pAmbFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.AmbLargeAnimations.EBTTalkFinE")

	pAmbFelix.AddAnimation("AmbTacticalGlanceCaptain", "Bridge.Characters.AmbLargeAnimations.AmbTConsoleInteraction")
	pAmbFelix.AddAnimation("AmbTacticalGlanceAwayCaptain", "Bridge.Characters.AmbLargeAnimations.Amb_seated_t")

	# Breathing
	pAmbFelix.AddAnimation("AmbTacticalBreathe", "Bridge.Characters.AmbLargeAnimations.Amb_seated_t")
	pAmbFelix.AddAnimation("AmbTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Amberaction
	pAmbFelix.AddRandomAnimation("Bridge.Characters.AmbLargeAnimations.AmbTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pAmbFelix.AddAnimation("PushingButtons", "Bridge.Characters.AmbLargeAnimations.AmbTConsoleInteraction")

	# Hit animations		
	#pAmbFelix.AddAnimation("AmbTacticalHit", "Bridge.Characters.AmbLargeAnimations.AmbTHit")
	#pAmbFelix.AddAnimation("AmbTacticalHitHard", "Bridge.Characters.AmbLargeAnimations.AmbTHitHard")
	pAmbFelix.AddAnimation("AmbTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pAmbFelix.AddAnimation("AmbTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pAmbFelix)
	
	pAmbFelix.SetLocation("AmbTactical")
	pAmbFelix.SetStanding(0)
	pAmbFelix.AddPositionZoom("AmbTactical", 0.9, "Tactical")
	pAmbFelix.SetLookAtAdj(1.69, -228.48, -17.711)
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
#	Args:	pAmbFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbFelix):
	#pAmbFelix.AddRandomAnimation("Bridge.Characters.AmbLargeAnimations.TLookAroundConsoleDown", 1, 1)

	debug(__name__ + ", AddCommonAnimations")
	pAmbFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pAmbFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pAmbFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pAmbFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pAmbFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pAmbFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pAmbFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pAmbFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pAmbFelix):
	debug(__name__ + ", OffBridgeStart")
	pAmbFelix = App.CharacterClass_Cast(pAmbFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pAmbFelix.SetTranslateXYZ(0, 0, -15)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pAmbFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pAmbFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pAmbFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	pAmbFelix.ClearAnimations()

	# Register animation mappings
	pAmbFelix.SetStanding(1)
	pAmbFelix.SetHidden(0)
	pAmbFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pAmbFelix)

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
