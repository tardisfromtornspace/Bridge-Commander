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
	pExcFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pExcFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pExcFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pExcFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcFelix)

	# Set up character configuration
	pExcFelix.SetSize(App.CharacterClass.LARGE)
	pExcFelix.SetGender(App.CharacterClass.MALE)
	pExcFelix.SetStanding(1)
	pExcFelix.SetRandomAnimationChance(0.75)
	pExcFelix.SetBlinkChance(0.1)
	pExcFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pExcFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pExcFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pExcFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pExcFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pExcFelix.SetBlinkStages(3)

	pExcFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pExcFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pExcFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pExcFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pExcFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pExcFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pExcFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pExcFelix

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
	pExcFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pExcFelix)
	pExcFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pExcFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pExcFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcFelix)

	# Set up character configuration
	pExcFelix.SetSize(App.CharacterClass.LARGE)
	pExcFelix.SetGender(App.CharacterClass.MALE)
	pExcFelix.SetStanding(1)
	pExcFelix.SetHidden(1)
	pExcFelix.SetRandomAnimationChance(0.75)
	pExcFelix.SetBlinkChance(0.1)
	pExcFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pExcFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pExcFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pExcFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pExcFelix


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
	pExcFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pExcFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pExcFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pExcFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcFelix)

	# Set up character configuration
	pExcFelix.SetSize(App.CharacterClass.LARGE)
	pExcFelix.SetGender(App.CharacterClass.MALE)
	pExcFelix.SetStanding(1)
	pExcFelix.SetHidden(1)
	pExcFelix.SetRandomAnimationChance(0.75)
	pExcFelix.SetBlinkChance(0.1)
	pExcFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pExcFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pExcFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pExcFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pExcFelix


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
	pExcFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pExcFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pExcFelix)


###############################################################################
#	ConfigureForExcalibur()
#
#	Configure ourselves for the Excula bridge
#
#	Args:	pExcFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pExcFelix):
#	kDebugObj.Print("Configuring Felix for the Excalibur bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcalibur")
	pExcFelix.ClearAnimations()

	# Register animation mappings
	pExcFelix.AddAnimation("SeatedExcTactical", "Bridge.Characters.ExcLargeAnimations.StandingConsole")
	pExcFelix.AddAnimation("EBL1LToT", "Bridge.Characters.ExcLargeAnimations.EBMoveFromL1ToT")
	pExcFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.ExcLargeAnimations.EBMoveFromTToL1")
	pExcFelix.AddAnimation("ExcTacticalTurnCaptain", "Bridge.Characters.ExcLargeAnimations.ExcTurnAtTTowardsCaptain")
	pExcFelix.AddAnimation("ExcTacticalBackCaptain", "Bridge.Characters.ExcLargeAnimations.ExcTurnBackAtTFromCaptain")

	pExcFelix.AddAnimation("ExcTacticalTurnC", "Bridge.Characters.ExcLargeAnimations.ExcTurnAtTTowardsCaptain")
	pExcFelix.AddAnimation("ExcTacticalBackC", "Bridge.Characters.ExcLargeAnimations.ExcTurnBackAtTFromCaptain")
	pExcFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.ExcLargeAnimations.EBTTalkE")
	pExcFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.ExcLargeAnimations.EBTTalkFinE")
	pExcFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.ExcLargeAnimations.EBTTalkH")
	pExcFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.ExcLargeAnimations.EBTTalkFinH")
	pExcFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.ExcLargeAnimations.EBTTalkS")
	pExcFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.ExcLargeAnimations.EBTTalkFinS")

	pExcFelix.AddAnimation("EBTacticalTurnX", "Bridge.Characters.ExcLargeAnimations.EBTTalkE")
	pExcFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.ExcLargeAnimations.EBTTalkFinE")

	pExcFelix.AddAnimation("ExcTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pExcFelix.AddAnimation("ExcTacticalGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.StandingConsole")

	# Breathing
	pExcFelix.AddAnimation("ExcTacticalBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pExcFelix.AddAnimation("ExcTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Exceraction
	pExcFelix.AddRandomAnimation("Bridge.Characters.ExcLargeAnimations.ExcTConsoleInteraction",App.CharacterClass.STANDING_ONLY, 25, 1)

	# So the mission builders can force the call
	pExcFelix.AddAnimation("PushingButtons", "Bridge.Characters.ExcLargeAnimations.ExcTConsoleInteraction")

	# Hit animations		
	#pExcFelix.AddAnimation("ExcTacticalHit", "Bridge.Characters.ExcLargeAnimations.ExcTHit")
	#pExcFelix.AddAnimation("ExcTacticalHitHard", "Bridge.Characters.ExcLargeAnimations.ExcTHitHard")
	pExcFelix.AddAnimation("ExcTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pExcFelix.AddAnimation("ExcTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pExcFelix)
	
	pExcFelix.SetLocation("ExcTactical")
	pExcFelix.SetStanding(0)
	pExcFelix.AddPositionZoom("ExcTactical", 0.8, "Tactical")
	pExcFelix.SetLookAtAdj(0, -90, 40)
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
#	Args:	pExcFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcFelix):
	debug(__name__ + ", AddCommonAnimations")
	pExcFelix.AddRandomAnimation("Bridge.Characters.ExcLargeAnimations.TLookAroundConsoleDown", 1, 1)

	pExcFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pExcFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pExcFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pExcFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pExcFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pExcFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pExcFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pExcFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pExcFelix):
	debug(__name__ + ", OffBridgeStart")
	pExcFelix = App.CharacterClass_Cast(pExcFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pExcFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pExcFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pExcFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pExcFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	pExcFelix.ClearAnimations()

	# Register animation mappings
	pExcFelix.SetStanding(1)
	pExcFelix.SetHidden(0)
	pExcFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pExcFelix)

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
