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
	ppromFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	ppromFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	ppromFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(ppromFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromFelix)

	# Set up character configuration
	ppromFelix.SetSize(App.CharacterClass.LARGE)
	ppromFelix.SetGender(App.CharacterClass.MALE)
	ppromFelix.SetStanding(1)
	ppromFelix.SetRandomAnimationChance(0.75)
	ppromFelix.SetBlinkChance(0.1)
	ppromFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	ppromFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	ppromFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	ppromFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	ppromFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	ppromFelix.SetBlinkStages(3)

	ppromFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	ppromFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	ppromFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	ppromFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	ppromFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	ppromFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	ppromFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return ppromFelix

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
	ppromFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(ppromFelix)
	ppromFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	ppromFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(ppromFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromFelix)

	# Set up character configuration
	ppromFelix.SetSize(App.CharacterClass.LARGE)
	ppromFelix.SetGender(App.CharacterClass.MALE)
	ppromFelix.SetStanding(1)
	ppromFelix.SetHidden(1)
	ppromFelix.SetRandomAnimationChance(0.75)
	ppromFelix.SetBlinkChance(0.1)
	ppromFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	ppromFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	ppromFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	ppromFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return ppromFelix


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
	ppromFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	ppromFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	ppromFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(ppromFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromFelix)

	# Set up character configuration
	ppromFelix.SetSize(App.CharacterClass.LARGE)
	ppromFelix.SetGender(App.CharacterClass.MALE)
	ppromFelix.SetStanding(1)
	ppromFelix.SetHidden(1)
	ppromFelix.SetRandomAnimationChance(0.75)
	ppromFelix.SetBlinkChance(0.1)
	ppromFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	ppromFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	ppromFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	ppromFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return ppromFelix


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
	ppromFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (ppromFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(ppromFelix)


###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	ppromFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(ppromFelix):
#	kDebugObj.Print("Configuring Felix for the prom bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForprometheus")
	ppromFelix.ClearAnimations()

	# Register animation mappings
	ppromFelix.AddAnimation("SeatedpromTactical", "Bridge.Characters.promLargeAnimations.promseatedTL")
	ppromFelix.AddAnimation("EBL1LToT", "Bridge.Characters.promLargeAnimations.EBMoveFromL1ToT")
	ppromFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.promLargeAnimations.EBMoveFromTToL1")
	ppromFelix.AddAnimation("promTacticalTurnCaptain", "Bridge.Characters.promLargeAnimations.promTurnAtTTowardsCaptain")
	ppromFelix.AddAnimation("promTacticalBackCaptain", "Bridge.Characters.promLargeAnimations.promTurnBackAtTFromCaptain")

	ppromFelix.AddAnimation("promTacticalTurnC", "Bridge.Characters.promLargeAnimations.promTurnAtTTowardsCaptain")
	ppromFelix.AddAnimation("promTacticalBackC", "Bridge.Characters.promLargeAnimations.promTurnBackAtTFromCaptain")
	ppromFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.promLargeAnimations.EBTTalkE")
	ppromFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.promLargeAnimations.EBTTalkFinE")
	ppromFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.promLargeAnimations.EBTTalkH")
	ppromFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.promLargeAnimations.EBTTalkFinH")
	ppromFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.promLargeAnimations.EBTTalkS")
	ppromFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.promLargeAnimations.EBTTalkFinS")

	ppromFelix.AddAnimation("EBTacticalTurprom", "Bridge.Characters.promLargeAnimations.EBTTalkE")
	ppromFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.promLargeAnimations.EBTTalkFinE")

	ppromFelix.AddAnimation("promTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	ppromFelix.AddAnimation("promTacticalGlanceAwayCaptain", "Bridge.Characters.promLargeAnimations.promseatedTL")

	# Breathing
	ppromFelix.AddAnimation("promTacticalBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	ppromFelix.AddAnimation("promTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# promeraction
	ppromFelix.AddRandomAnimation("Bridge.Characters.promLargeAnimations.promTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	ppromFelix.AddAnimation("PushingButtons", "Bridge.Characters.promLargeAnimations.promTConsoleInteraction")

	# Hit animations		
	#ppromFelix.AddAnimation("promTacticalHit", "Bridge.Characters.promLargeAnimations.promTHit")
	#ppromFelix.AddAnimation("promTacticalHitHard", "Bridge.Characters.promLargeAnimations.promTHitHard")
	ppromFelix.AddAnimation("promTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	ppromFelix.AddAnimation("promTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(ppromFelix)
	
	ppromFelix.SetLocation("promTactical")
	ppromFelix.SetStanding(0)
	ppromFelix.AddPositionZoom("promTactical", 0.60, "Tactical")
	ppromFelix.SetLookAtAdj(0.0, 0, 0)
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
#	Args:	ppromFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromFelix):
	debug(__name__ + ", AddCommonAnimations")
	ppromFelix.AddRandomAnimation("Bridge.Characters.promLargeAnimations.TLookAroundConsoleDown", 1, 1)

	ppromFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	ppromFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	ppromFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#ppromFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#ppromFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#ppromFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#ppromFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#ppromFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	ppromFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(ppromFelix):
	debug(__name__ + ", OffBridgeStart")
	ppromFelix = App.CharacterClass_Cast(ppromFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	ppromFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(ppromFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	ppromFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(ppromFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	ppromFelix.ClearAnimations()

	# Register animation mappings
	ppromFelix.SetStanding(1)
	ppromFelix.SetHidden(0)
	ppromFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(ppromFelix)

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
