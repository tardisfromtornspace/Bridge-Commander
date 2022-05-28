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
	pENAFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pENAFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pENAFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pENAFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAFelix)

	# Set up character configuration
	pENAFelix.SetSize(App.CharacterClass.LARGE)
	pENAFelix.SetGender(App.CharacterClass.MALE)
	pENAFelix.SetStanding(1)
	pENAFelix.SetRandomAnimationChance(0.75)
	pENAFelix.SetBlinkChance(0.1)
	pENAFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pENAFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pENAFelix.AdENAacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENAFelix.AdENAacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENAFelix.AdENAacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENAFelix.SetBlinkStages(3)

	pENAFelix.AdENAacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENAFelix.AdENAacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENAFelix.AdENAacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pENAFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pENAFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pENAFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENAFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pENAFelix

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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeaENAelix/felix_head.nif", None)
	pENAFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeaENAelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pENAFelix)
	pENAFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pENAFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pENAFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAFelix)

	# Set up character configuration
	pENAFelix.SetSize(App.CharacterClass.LARGE)
	pENAFelix.SetGender(App.CharacterClass.MALE)
	pENAFelix.SetStanding(1)
	pENAFelix.SetHidden(1)
	pENAFelix.SetRandomAnimationChance(0.75)
	pENAFelix.SetBlinkChance(0.1)
	pENAFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pENAFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENAFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENAFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pENAFelix


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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeaENAelix/felix_head.nif", None)
	pENAFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeaENAelix/felix_head.nif")
	pENAFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeaENAelix/felix_head.tga")

	pENAFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pENAFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAFelix)

	# Set up character configuration
	pENAFelix.SetSize(App.CharacterClass.LARGE)
	pENAFelix.SetGender(App.CharacterClass.MALE)
	pENAFelix.SetStanding(1)
	pENAFelix.SetHidden(1)
	pENAFelix.SetRandomAnimationChance(0.75)
	pENAFelix.SetBlinkChance(0.1)
	pENAFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pENAFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENAFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENAFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pENAFelix


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
	pENAFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pENAFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pENAFelix)


###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pENAFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pENAFelix):
#	kDebugObj.Print("Configuring Felix for the ENA bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseA")
	pENAFelix.ClearAnimations()

	# Register animation mappings
	pENAFelix.AddAnimation("SeatedENATactical", "Bridge.Characters.ENALargeAnimations.ENAseatedTL")
	pENAFelix.AddAnimation("EBL1LToT", "Bridge.Characters.ENALargeAnimations.EBMoveFromL1ToT")
	pENAFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.ENALargeAnimations.EBMoveFromTToL1")
	pENAFelix.AddAnimation("ENATacticalTurnCaptain", "Bridge.Characters.ENALargeAnimations.ENATurnAtTTowardsCaptain")
	pENAFelix.AddAnimation("ENATacticalBackCaptain", "Bridge.Characters.ENALargeAnimations.ENATurnBackAtTFromCaptain")

	pENAFelix.AddAnimation("ENATacticalTurnC", "Bridge.Characters.ENALargeAnimations.ENATurnAtTTowardsCaptain")
	pENAFelix.AddAnimation("ENATacticalBackC", "Bridge.Characters.ENALargeAnimations.ENATurnBackAtTFromCaptain")
	pENAFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.ENALargeAnimations.EBTTalkE")
	pENAFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.ENALargeAnimations.EBTTalkFinE")
	pENAFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.ENALargeAnimations.EBTTalkH")
	pENAFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.ENALargeAnimations.EBTTalkFinH")
	pENAFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.ENALargeAnimations.EBTTalkS")
	pENAFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.ENALargeAnimations.EBTTalkFinS")

	pENAFelix.AddAnimation("EBTacticalTurENA", "Bridge.Characters.ENALargeAnimations.EBTTalkE")
	pENAFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.ENALargeAnimations.EBTTalkFinE")

	pENAFelix.AddAnimation("ENATacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pENAFelix.AddAnimation("ENATacticalGlanceAwayCaptain", "Bridge.Characters.ENALargeAnimations.ENATConsoleInteraction")

	# Breathing
	pENAFelix.AddAnimation("ENATacticalBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pENAFelix.AddAnimation("ENATacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# ENAeraction
	pENAFelix.AddRandomAnimation("Bridge.Characters.ENALargeAnimations.ENATConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pENAFelix.AddAnimation("PushingButtons", "Bridge.Characters.ENALargeAnimations.ENATConsoleInteraction")

	# Hit animations		
	#pENAFelix.AddAnimation("ENATacticalHit", "Bridge.Characters.ENALargeAnimations.ENATHit")
	#pENAFelix.AddAnimation("ENATacticalHitHard", "Bridge.Characters.ENALargeAnimations.ENATHitHard")
	pENAFelix.AddAnimation("ENATacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENAFelix.AddAnimation("ENATacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pENAFelix)
	
	pENAFelix.SetLocation("ENATactical")
	pENAFelix.SetStanding(0)
#	pENAFelix.AddPositionZoom("ENATactical", 1.0, "Tactical")
	pENAFelix.AddPositionZoom("ENATactical", 1.0)
#	pENAFelix.SetLookAtAdj(0, 0, 10)
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
#	Args:	pENAFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENAFelix):
	debug(__name__ + ", AddCommonAnimations")
	pENAFelix.AddRandomAnimation("Bridge.Characters.ENALargeAnimations.TLookAroundConsoleDown", 1, 1)

	pENAFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENAFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENAFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENAFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pENAFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pENAFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pENAFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pENAFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pENAFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pENAFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pENAFelix):
	debug(__name__ + ", OffBridgeStart")
	pENAFelix = App.CharacterClass_Cast(pENAFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pENAFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pENAFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pENAFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pENAFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	pENAFelix.ClearAnimations()

	# Register animation mappings
	pENAFelix.SetStanding(1)
	pENAFelix.SetHidden(0)
	pENAFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pENAFelix)

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
