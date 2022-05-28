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
	pDFFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pDFFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pDFFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pDFFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFFelix)

	# Set up character configuration
	pDFFelix.SetSize(App.CharacterClass.LARGE)
	pDFFelix.SetGender(App.CharacterClass.MALE)
	pDFFelix.SetStanding(1)
	pDFFelix.SetRandomAnimationChance(0.75)
	pDFFelix.SetBlinkChance(0.1)
	pDFFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pDFFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pDFFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pDFFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pDFFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pDFFelix.SetBlinkStages(3)

	pDFFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pDFFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pDFFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pDFFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDFFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pDFFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pDFFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pDFFelix

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
	pDFFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pDFFelix)
	pDFFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pDFFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pDFFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFFelix)

	# Set up character configuration
	pDFFelix.SetSize(App.CharacterClass.LARGE)
	pDFFelix.SetGender(App.CharacterClass.MALE)
	pDFFelix.SetStanding(1)
	pDFFelix.SetHidden(1)
	pDFFelix.SetRandomAnimationChance(0.75)
	pDFFelix.SetBlinkChance(0.1)
	pDFFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pDFFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pDFFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pDFFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pDFFelix


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
	pDFFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pDFFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pDFFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pDFFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFFelix)

	# Set up character configuration
	pDFFelix.SetSize(App.CharacterClass.LARGE)
	pDFFelix.SetGender(App.CharacterClass.MALE)
	pDFFelix.SetStanding(1)
	pDFFelix.SetHidden(1)
	pDFFelix.SetRandomAnimationChance(0.75)
	pDFFelix.SetBlinkChance(0.1)
	pDFFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pDFFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pDFFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pDFFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pDFFelix


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
	pDFFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pDFFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pDFFelix)


###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pDFFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pDFFelix):
#	kDebugObj.Print("Configuring Felix for the DF bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForDefiant")
	pDFFelix.ClearAnimations()

	# Register animation mappings
	pDFFelix.AddAnimation("SeatedDFTactical", "Bridge.Characters.DFLargeAnimations.DFseatedTL")
	pDFFelix.AddAnimation("EBL1LToT", "Bridge.Characters.DFLargeAnimations.EBMoveFromL1ToT")
	pDFFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.DFLargeAnimations.EBMoveFromTToL1")
	pDFFelix.AddAnimation("DFTacticalTurnCaptain", "Bridge.Characters.DFLargeAnimations.DFTurnAtTTowardsCaptain")
	pDFFelix.AddAnimation("DFTacticalBackCaptain", "Bridge.Characters.DFLargeAnimations.DFTurnBackAtTFromCaptain")

	pDFFelix.AddAnimation("DFTacticalTurnC", "Bridge.Characters.DFLargeAnimations.DFTurnAtTTowardsCaptain")
	pDFFelix.AddAnimation("DFTacticalBackC", "Bridge.Characters.DFLargeAnimations.DFTurnBackAtTFromCaptain")
	pDFFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.DFLargeAnimations.EBTTalkE")
	pDFFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.DFLargeAnimations.EBTTalkFinE")
	pDFFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.DFLargeAnimations.EBTTalkH")
	pDFFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.DFLargeAnimations.EBTTalkFinH")
	pDFFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.DFLargeAnimations.EBTTalkS")
	pDFFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.DFLargeAnimations.EBTTalkFinS")

	pDFFelix.AddAnimation("EBTacticalTurDF", "Bridge.Characters.DFLargeAnimations.EBTTalkE")
	pDFFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.DFLargeAnimations.EBTTalkFinE")

	pDFFelix.AddAnimation("DFTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pDFFelix.AddAnimation("DFTacticalGlanceAwayCaptain", "Bridge.Characters.DFLargeAnimations.DFseatedTL")

	# Breathing
	pDFFelix.AddAnimation("DFTacticalBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pDFFelix.AddAnimation("DFTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# DFeraction
	pDFFelix.AddRandomAnimation("Bridge.Characters.DFLargeAnimations.DFTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pDFFelix.AddAnimation("PushingButtons", "Bridge.Characters.DFLargeAnimations.DFTConsoleInteraction")

	# Hit animations		
	#pDFFelix.AddAnimation("DFTacticalHit", "Bridge.Characters.DFLargeAnimations.DFTHit")
	#pDFFelix.AddAnimation("DFTacticalHitHard", "Bridge.Characters.DFLargeAnimations.DFTHitHard")
	pDFFelix.AddAnimation("DFTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pDFFelix.AddAnimation("DFTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pDFFelix)
	
	pDFFelix.SetLocation("DFTactical")
	pDFFelix.SetStanding(0)
	pDFFelix.AddPositionZoom("DFTactical", 0.60, "Tactical")
	pDFFelix.SetLookAtAdj(-0.001, -10, 10)
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
#	Args:	pDFFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFFelix):
	debug(__name__ + ", AddCommonAnimations")
	pDFFelix.AddRandomAnimation("Bridge.Characters.DFLargeAnimations.TLookAroundConsoleDown", 1, 1)

	pDFFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pDFFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pDFFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pDFFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pDFFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pDFFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pDFFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pDFFelix):
	debug(__name__ + ", OffBridgeStart")
	pDFFelix = App.CharacterClass_Cast(pDFFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pDFFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pDFFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pDFFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pDFFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	pDFFelix.ClearAnimations()

	# Register animation mappings
	pDFFelix.SetStanding(1)
	pDFFelix.SetHidden(0)
	pDFFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pDFFelix)

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
