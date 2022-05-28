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
	pIntFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pIntFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pIntFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pIntFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntFelix)

	# Set up character configuration
	pIntFelix.SetSize(App.CharacterClass.LARGE)
	pIntFelix.SetGender(App.CharacterClass.MALE)
	pIntFelix.SetStanding(1)
	pIntFelix.SetRandomAnimationChance(0.75)
	pIntFelix.SetBlinkChance(0.1)
	pIntFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pIntFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pIntFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pIntFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pIntFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pIntFelix.SetBlinkStages(3)

	pIntFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pIntFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pIntFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pIntFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pIntFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pIntFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pIntFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pIntFelix

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
	pIntFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pIntFelix)
	pIntFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pIntFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pIntFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntFelix)

	# Set up character configuration
	pIntFelix.SetSize(App.CharacterClass.LARGE)
	pIntFelix.SetGender(App.CharacterClass.MALE)
	pIntFelix.SetStanding(1)
	pIntFelix.SetHidden(1)
	pIntFelix.SetRandomAnimationChance(0.75)
	pIntFelix.SetBlinkChance(0.1)
	pIntFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pIntFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pIntFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pIntFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pIntFelix


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
	pIntFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pIntFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pIntFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pIntFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntFelix)

	# Set up character configuration
	pIntFelix.SetSize(App.CharacterClass.LARGE)
	pIntFelix.SetGender(App.CharacterClass.MALE)
	pIntFelix.SetStanding(1)
	pIntFelix.SetHidden(1)
	pIntFelix.SetRandomAnimationChance(0.75)
	pIntFelix.SetBlinkChance(0.1)
	pIntFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pIntFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pIntFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pIntFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pIntFelix


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
	pIntFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pIntFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pIntFelix)


###############################################################################
#	ConfigureForIntrepid()
#
#	Configure ourselves for the Intula bridge
#
#	Args:	pIntFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pIntFelix):
#	kDebugObj.Print("Configuring Felix for the intrepid bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForIntrepid")
	pIntFelix.ClearAnimations()

	# Register animation mappings
	pIntFelix.AddAnimation("SeatedIntTactical", "Bridge.Characters.IntLargeAnimations.StandingConsole")
	pIntFelix.AddAnimation("EBL1LToT", "Bridge.Characters.IntLargeAnimations.EBMoveFromL1ToT")
	pIntFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.IntLargeAnimations.EBMoveFromTToL1")
	pIntFelix.AddAnimation("IntTacticalTurnCaptain", "Bridge.Characters.IntLargeAnimations.IntTurnAtTTowardsCaptain")
	pIntFelix.AddAnimation("IntTacticalBackCaptain", "Bridge.Characters.IntLargeAnimations.IntTurnBackAtTFromCaptain")

	pIntFelix.AddAnimation("IntTacticalTurnC", "Bridge.Characters.IntLargeAnimations.IntTurnAtTTowardsCaptain")
	pIntFelix.AddAnimation("IntTacticalBackC", "Bridge.Characters.IntLargeAnimations.IntTurnBackAtTFromCaptain")
	pIntFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.IntLargeAnimations.EBTTalkE")
	pIntFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.IntLargeAnimations.EBTTalkFinE")
	pIntFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.IntLargeAnimations.EBTTalkH")
	pIntFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.IntLargeAnimations.EBTTalkFinH")
	pIntFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.IntLargeAnimations.EBTTalkS")
	pIntFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.IntLargeAnimations.EBTTalkFinS")

	pIntFelix.AddAnimation("EBTacticalTurnX", "Bridge.Characters.IntLargeAnimations.EBTTalkE")
	pIntFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.IntLargeAnimations.EBTTalkFinE")

	pIntFelix.AddAnimation("IntTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pIntFelix.AddAnimation("IntTacticalGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")

	# Breathing
	pIntFelix.AddAnimation("IntTacticalBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pIntFelix.AddAnimation("IntTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pIntFelix.AddRandomAnimation("Bridge.Characters.IntLargeAnimations.IntTConsoleInteraction",App.CharacterClass.STANDING_ONLY, 25, 1)

	# So the mission builders can force the call
	pIntFelix.AddAnimation("PushingButtons", "Bridge.Characters.IntLargeAnimations.IntTConsoleInteraction")

	# Hit animations		
	#pIntFelix.AddAnimation("IntTacticalHit", "Bridge.Characters.IntLargeAnimations.IntTHit")
	#pIntFelix.AddAnimation("IntTacticalHitHard", "Bridge.Characters.IntLargeAnimations.IntTHitHard")
	pIntFelix.AddAnimation("IntTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pIntFelix.AddAnimation("IntTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pIntFelix)
	
	pIntFelix.SetLocation("IntTactical")
	pIntFelix.SetStanding(1)
	pIntFelix.AddPositionZoom("IntTactical", 0.5, "Tactical")
	pIntFelix.SetLookAtAdj(-30, 0, 50)
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
#	Args:	pIntFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntFelix):
	debug(__name__ + ", AddCommonAnimations")
	pIntFelix.AddRandomAnimation("Bridge.Characters.IntLargeAnimations.TLookAroundConsoleDown", 1, 1)

	pIntFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pIntFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pIntFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pIntFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pIntFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pIntFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pIntFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pIntFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pIntFelix):
	debug(__name__ + ", OffBridgeStart")
	pIntFelix = App.CharacterClass_Cast(pIntFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pIntFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pIntFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pIntFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pIntFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	pIntFelix.ClearAnimations()

	# Register animation mappings
	pIntFelix.SetStanding(1)
	pIntFelix.SetHidden(0)
	pIntFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pIntFelix)

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
