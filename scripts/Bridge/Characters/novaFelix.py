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
	pnovaFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pnovaFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pnovaFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaFelix)

	# Set up character configuration
	pnovaFelix.SetSize(App.CharacterClass.LARGE)
	pnovaFelix.SetGender(App.CharacterClass.MALE)
	pnovaFelix.SetStanding(1)
	pnovaFelix.SetRandomAnimationChance(0.75)
	pnovaFelix.SetBlinkChance(0.1)
	pnovaFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pnovaFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pnovaFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pnovaFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pnovaFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pnovaFelix.SetBlinkStages(3)

	pnovaFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pnovaFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pnovaFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pnovaFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pnovaFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pnovaFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pnovaFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pnovaFelix

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

	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif", None)
	pnovaFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pnovaFelix)
	pnovaFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pnovaFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaFelix)

	# Set up character configuration
	pnovaFelix.SetSize(App.CharacterClass.LARGE)
	pnovaFelix.SetGender(App.CharacterClass.MALE)
	pnovaFelix.SetStanding(1)
	pnovaFelix.SetHidden(1)
	pnovaFelix.SetRandomAnimationChance(0.75)
	pnovaFelix.SetBlinkChance(0.1)
	pnovaFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pnovaFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pnovaFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pnovaFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pnovaFelix


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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif", None)
	pnovaFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pnovaFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pnovaFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaFelix)

	# Set up character configuration
	pnovaFelix.SetSize(App.CharacterClass.LARGE)
	pnovaFelix.SetGender(App.CharacterClass.MALE)
	pnovaFelix.SetStanding(1)
	pnovaFelix.SetHidden(1)
	pnovaFelix.SetRandomAnimationChance(0.75)
	pnovaFelix.SetBlinkChance(0.1)
	pnovaFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pnovaFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pnovaFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pnovaFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pnovaFelix


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
	pnovaFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pnovaFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pnovaFelix)


###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pnovaFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pnovaFelix):
#	kDebugObj.Print("Configuring Felix for the nova bridge")

	# Clear out any old animations from another configuration
	pnovaFelix.ClearAnimations()

	# Register animation mappings
	pnovaFelix.AddAnimation("SeatednovaTactical", "Bridge.Characters.novaLargeAnimations.novaseatedTL")
	pnovaFelix.AddAnimation("EBL1LToT", "Bridge.Characters.novaLargeAnimations.EBMoveFromL1ToT")
	pnovaFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.novaLargeAnimations.EBMoveFromTToL1")
	pnovaFelix.AddAnimation("novaTacticalTurnCaptain", "Bridge.Characters.novaLargeAnimations.novaTurnAtTTowardsCaptain")
	pnovaFelix.AddAnimation("novaTacticalBackCaptain", "Bridge.Characters.novaLargeAnimations.novaTurnBackAtTFromCaptain")

	pnovaFelix.AddAnimation("novaTacticalTurnC", "Bridge.Characters.novaLargeAnimations.novaTurnAtTTowardsCaptain")
	pnovaFelix.AddAnimation("novaTacticalBackC", "Bridge.Characters.novaLargeAnimations.novaTurnBackAtTFromCaptain")
	pnovaFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.novaLargeAnimations.EBTTalkE")
	pnovaFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.novaLargeAnimations.EBTTalkFinE")
	pnovaFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.novaLargeAnimations.EBTTalkH")
	pnovaFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.novaLargeAnimations.EBTTalkFinH")
	pnovaFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.novaLargeAnimations.EBTTalkS")
	pnovaFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.novaLargeAnimations.EBTTalkFinS")

	pnovaFelix.AddAnimation("EBTacticalTurnova", "Bridge.Characters.novaLargeAnimations.EBTTalkE")
	pnovaFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.novaLargeAnimations.EBTTalkFinE")

	pnovaFelix.AddAnimation("novaTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pnovaFelix.AddAnimation("novaTacticalGlanceAwayCaptain", "Bridge.Characters.novaLargeAnimations.novaseatedTL")

	# Breathing
	pnovaFelix.AddAnimation("novaTacticalBreathe", "Bridge.Characters.CommonAnimations.StandingConsole")
	pnovaFelix.AddAnimation("novaTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# novaeraction
	pnovaFelix.AddRandomAnimation("Bridge.Characters.novaLargeAnimations.novaTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pnovaFelix.AddAnimation("PushingButtons", "Bridge.Characters.novaLargeAnimations.novaTConsoleInteraction")

	# Hit animations		
	#pnovaFelix.AddAnimation("novaTacticalHit", "Bridge.Characters.novaLargeAnimations.novaTHit")
	#pnovaFelix.AddAnimation("novaTacticalHitHard", "Bridge.Characters.novaLargeAnimations.novaTHitHard")
	pnovaFelix.AddAnimation("novaTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pnovaFelix.AddAnimation("novaTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pnovaFelix)
	
	pnovaFelix.SetLocation("novaTactical")
	pnovaFelix.SetStanding(0)

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
#	Args:	pnovaFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaFelix):
	pnovaFelix.AddRandomAnimation("Bridge.Characters.novaLargeAnimations.TLookAroundConsoleDown", 1, 1)

	pnovaFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pnovaFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pnovaFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pnovaFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pnovaFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pnovaFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pnovaFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pnovaFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pnovaFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pnovaFelix):
	pnovaFelix = App.CharacterClass_Cast(pnovaFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pnovaFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pnovaFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pnovaFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pnovaFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	pnovaFelix.ClearAnimations()

	# Register animation mappings
	pnovaFelix.SetStanding(1)
	pnovaFelix.SetHidden(0)
	pnovaFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pnovaFelix)

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
