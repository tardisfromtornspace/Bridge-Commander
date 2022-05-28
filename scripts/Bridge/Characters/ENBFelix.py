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
	pENBFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pENBFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pENBFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pENBFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBFelix)

	# Set up character configuration
	pENBFelix.SetSize(App.CharacterClass.LARGE)
	pENBFelix.SetGender(App.CharacterClass.MALE)
	pENBFelix.SetStanding(1)
	pENBFelix.SetRandomAnimationChance(0.75)
	pENBFelix.SetBlinkChance(0.1)
	pENBFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pENBFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pENBFelix.AddfacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENBFelix.AddfacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENBFelix.AddfacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENBFelix.SetBlinkStages(3)

	pENBFelix.AddfacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENBFelix.AddfacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENBFelix.AddfacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENBFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENBFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pENBFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENBFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pENBFelix

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
	pENBFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headfelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pENBFelix)
	pENBFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pENBFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pENBFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBFelix)

	# Set up character configuration
	pENBFelix.SetSize(App.CharacterClass.LARGE)
	pENBFelix.SetGender(App.CharacterClass.MALE)
	pENBFelix.SetStanding(1)
	pENBFelix.SetHidden(1)
	pENBFelix.SetRandomAnimationChance(0.75)
	pENBFelix.SetBlinkChance(0.1)
	pENBFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pENBFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENBFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENBFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pENBFelix


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
	pENBFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headfelix/felix_head.nif")
	pENBFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "Headfelix/felix_head.tga")

	pENBFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pENBFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBFelix)

	# Set up character configuration
	pENBFelix.SetSize(App.CharacterClass.LARGE)
	pENBFelix.SetGender(App.CharacterClass.MALE)
	pENBFelix.SetStanding(1)
	pENBFelix.SetHidden(1)
	pENBFelix.SetRandomAnimationChance(0.75)
	pENBFelix.SetBlinkChance(0.1)
	pENBFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pENBFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENBFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENBFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pENBFelix


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
	pENBFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pENBFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pENBFelix)


###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pENBFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pENBFelix):
#	kDebugObj.Print("Configuring Felix for the ENB bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseB")
	pENBFelix.ClearAnimations()

	# Register animation mappings
	pENBFelix.AddAnimation("SeatedENBTactical", "Bridge.Characters.ENBLargeAnimations.ENBseatedTL")
	pENBFelix.AddAnimation("EBL1LToT", "Bridge.Characters.ENBLargeAnimations.EBMoveFromL1ToT")
	pENBFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.ENBLargeAnimations.EBMoveFromTToL1")
	pENBFelix.AddAnimation("ENBTacticalTurnCaptain", "Bridge.Characters.ENBLargeAnimations.ENBTurnAtTTowardsCaptain")
	pENBFelix.AddAnimation("ENBTacticalBackCaptain", "Bridge.Characters.ENBLargeAnimations.ENBTurnBackAtTFromCaptain")

	pENBFelix.AddAnimation("ENBTacticalTurnC", "Bridge.Characters.ENBLargeAnimations.ENBTurnAtTTowardsCaptain")
	pENBFelix.AddAnimation("ENBTacticalBackC", "Bridge.Characters.ENBLargeAnimations.ENBTurnBackAtTFromCaptain")
	pENBFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.ENBLargeAnimations.EBTTalkE")
	pENBFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.ENBLargeAnimations.EBTTalkFinE")
	pENBFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.ENBLargeAnimations.EBTTalkH")
	pENBFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.ENBLargeAnimations.EBTTalkFinH")
	pENBFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.ENBLargeAnimations.EBTTalkS")
	pENBFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.ENBLargeAnimations.EBTTalkFinS")

	pENBFelix.AddAnimation("EBTacticalTurENB", "Bridge.Characters.ENBLargeAnimations.EBTTalkE")
	pENBFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.ENBLargeAnimations.EBTTalkFinE")

	pENBFelix.AddAnimation("ENBTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pENBFelix.AddAnimation("ENBTacticalGlanceAwayCaptain", "Bridge.Characters.ENBLargeAnimations.ENBTConsoleInteraction")

	# Breathing
	pENBFelix.AddAnimation("ENBTacticalBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENBFelix.AddAnimation("ENBTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pENBFelix.AddRandomAnimation("Bridge.Characters.ENBLargeAnimations.ENBTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pENBFelix.AddAnimation("PushingButtons", "Bridge.Characters.ENBLargeAnimations.ENBTConsoleInteraction")

	# Hit animations		
	#pENBFelix.AddAnimation("ENBTacticalHit", "Bridge.Characters.ENBLargeAnimations.ENBTHit")
	#pENBFelix.AddAnimation("ENBTacticalHitHard", "Bridge.Characters.ENBLargeAnimations.ENBTHitHard")
	pENBFelix.AddAnimation("ENBTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENBFelix.AddAnimation("ENBTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pENBFelix)
	
	pENBFelix.SetLocation("ENBTactical")
	pENBFelix.SetStanding(0)
#	pENBFelix.AddPositionZoom("ENBTactical", 1.0, "Tactical")
	pENBFelix.AddPositionZoom("ENBTactical", 1.0)
#	pENBFelix.SetLookAtAdj(0, 0, 10)
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
#	Args:	pENBFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENBFelix):
	debug(__name__ + ", AddCommonAnimations")
	pENBFelix.AddRandomAnimation("Bridge.Characters.ENBLargeAnimations.TLookAroundConsoleDown", 1, 1)

	pENBFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENBFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENBFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENBFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pENBFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pENBFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pENBFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pENBFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pENBFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pENBFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pENBFelix):
	debug(__name__ + ", OffBridgeStart")
	pENBFelix = App.CharacterClass_Cast(pENBFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pENBFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pENBFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pENBFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pENBFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	pENBFelix.ClearAnimations()

	# Register animation mappings
	pENBFelix.SetStanding(1)
	pENBFelix.SetHidden(0)
	pENBFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pENBFelix)

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
