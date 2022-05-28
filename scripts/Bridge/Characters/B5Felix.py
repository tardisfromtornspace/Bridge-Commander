###############################################################################
#	Filename:	RomFelix.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads RomFelix Savali, tactical officer, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create RomFelix by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating RomFelix")
	
	if (pSet.GetObject("Tactical") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Tactical")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.NIF", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "B5/HeadFelix/Felix_head.NIF", None)
	pRomFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.NIF", CharacterPaths.g_pcHeadNIFPath + "B5/HeadFelix/Felix_head.NIF")
	pRomFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "B5/BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "B5/HeadFelix/Felix_head.tga")

	pRomFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pRomFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRomFelix)

	# Set up character configuration
	pRomFelix.SetSize(App.CharacterClass.LARGE)
	pRomFelix.SetGender(App.CharacterClass.MALE)
	pRomFelix.SetStanding(0)
	pRomFelix.SetRandomAnimationChance(0.75)
	pRomFelix.SetBlinkChance(0.1)
	pRomFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pRomFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pRomFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "B5/HeadFelix/felix_blink1.tga")
	pRomFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "B5/HeadFelix/felix_blink2.tga")
	pRomFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "B5/HeadFelix/felix_eyesclosed.tga")
	pRomFelix.SetBlinkStages(3)

	pRomFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "B5/HeadFelix/felix_head_a.tga")
	pRomFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "B5/HeadFelix/felix_head_e.tga")
	pRomFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "B5/HeadFelix/felix_head_u.tga")
	pRomFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRomFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pRomFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pRomFelix.SetLocation("")

#	kDebugObj.Print("Finished creating RomFelix")
	return pRomFelix

###############################################################################
#	CreateCharacterNoSounds()
#
#	Create RomFelix by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacterNoSounds(pSet):
#	kDebugObj.Print("Creating RomFelix")
	
	import Bridge.TacticalMenuHandlers
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pRomFelix)

	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "B5/HeadFelix/felix_head.nif", None)
	pRomFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "B5/BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "B5/HeadFelix/felix_head.nif")
	pRomFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "B5/BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "B5/HeadFelix/felix_head.tga")

	pRomFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pRomFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRomFelix)

	# Set up character configuration
	pRomFelix.SetSize(App.CharacterClass.LARGE)
	pRomFelix.SetGender(App.CharacterClass.MALE)
	pRomFelix.SetStanding(0)
	pRomFelix.SetHidden(1)
	pRomFelix.SetRandomAnimationChance(0.75)
	pRomFelix.SetBlinkChance(0.1)
	pRomFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pRomFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pBrex.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pBrex.SetLocation("")

#	kDebugObj.Print("Finished creating RomFelix")
	return pRomFelix


###############################################################################
#	CreateCharacterNoMenu()
#
#	Create RomFelix by building his character and placing him on the passed in set.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacterNoMenu(pSet):
#	kDebugObj.Print("Creating RomFelix")
	
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "B5/HeadFelix/felix_head.nif", None)
	pRomFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "B5/BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "B5/HeadFelix/felix_head.nif")
	pRomFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "B5/BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "B5/HeadFelix/felix_head.tga")

	pRomFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pRomFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRomFelix)

	# Set up character configuration
	pRomFelix.SetSize(App.CharacterClass.LARGE)
	pRomFelix.SetGender(App.CharacterClass.MALE)
	pRomFelix.SetStanding(0)
	pRomFelix.SetHidden(1)
	pRomFelix.SetRandomAnimationChance(0.75)
	pRomFelix.SetBlinkChance(0.1)
	pRomFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pRomFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pRomFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pRomFelix.SetLocation("")

#	kDebugObj.Print("Finished creating RomFelix")
	return pRomFelix


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
	pRomFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pRomFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pRomFelix)


###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pRomFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForWarbird(pRomFelix):
#	kDebugObj.Print("Configuring RomFelix for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pRomFelix.ClearAnimations()

	# Register animation mappings
	pRomFelix.AddAnimation("DBL1LToT", "Bridge.Characters.LargeAnimations.MoveFromL1ToT")
	pRomFelix.AddAnimation("DBTacticalToL1", "Bridge.Characters.LargeAnimations.MoveFromTToL1")
	pRomFelix.AddAnimation("RomTacticalTurnCaptain", "Bridge.Characters.LargeAnimations.TurnAtTTowardsCaptain")
	pRomFelix.AddAnimation("RomTacticalBackCaptain", "Bridge.Characters.LargeAnimations.TurnBackAtTFromCaptain")

	pRomFelix.AddAnimation("DBTacticalTurnC", "Bridge.Characters.LargeAnimations.DBTTalkC")
	pRomFelix.AddAnimation("DBTacticalBackC", "Bridge.Characters.LargeAnimations.DBTTalkFinC")
	pRomFelix.AddAnimation("DBTacticalTurnE", "Bridge.Characters.LargeAnimations.DBTTalkE")
	pRomFelix.AddAnimation("DBTacticalBackE", "Bridge.Characters.LargeAnimations.DBTTalkFinE")
	pRomFelix.AddAnimation("DBTacticalTurnH", "Bridge.Characters.LargeAnimations.DBTTalkH")
	pRomFelix.AddAnimation("DBTacticalBackH", "Bridge.Characters.LargeAnimations.DBTTalkFinH")
	pRomFelix.AddAnimation("DBTacticalTurnS", "Bridge.Characters.LargeAnimations.DBTTalkS")
	pRomFelix.AddAnimation("DBTacticalBackS", "Bridge.Characters.LargeAnimations.DBTTalkFinS")

	pRomFelix.AddAnimation("DBTacticalTurnX", "Bridge.Characters.LargeAnimations.DBTTalkX")
	pRomFelix.AddAnimation("DBTacticalBackX", "Bridge.Characters.LargeAnimations.DBTTalkFinX")

	pRomFelix.AddAnimation("RomTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pRomFelix.AddAnimation("RomTacticalGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedL")

	# Breathing
	pRomFelix.AddAnimation("DBTacticalBreathe", "Bridge.Characters.CommonAnimations.SeatedL")
	pRomFelix.AddAnimation("DBTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pRomFelix.AddRandomAnimation("Bridge.Characters.LargeAnimations.DBTConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pRomFelix.AddAnimation("PushingButtons", "Bridge.Characters.LargeAnimations.DBTConsoleInteraction")

	# Hit animations		
	pRomFelix.AddAnimation("DBTacticalHit", "Bridge.Characters.LargeAnimations.THit");
	pRomFelix.AddAnimation("DBTacticalHitHard", "Bridge.Characters.LargeAnimations.THitHard");
	pRomFelix.AddAnimation("DBTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft");
	pRomFelix.AddAnimation("DBTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight");

	# Add common animations.
	AddCommonAnimations(pRomFelix)
	
	pRomFelix.SetLocation("RomTactical")
	pRomFelix.AddPositionZoom("RomTactical", 0.5, "Tactical")
	pRomFelix.SetLookAtAdj(0, -224, 66)
#	kDebugObj.Print("Finished configuring RomFelix")



###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pRomFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pRomFelix):
	pRomFelix.AddRandomAnimation("Bridge.Characters.LargeAnimations.TLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pRomFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRomFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRomFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pRomFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pRomFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pRomFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pRomFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pRomFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pRomFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets RomFelix's location to start in the off bridge partial set
#	
#	Args:	pRomFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pRomFelix):
	pRomFelix = App.CharacterClass_Cast(pRomFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pRomFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pRomFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pRomFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pRomFelix):
#	kDebugObj.Print("Configuring RomFelix for off bridge")

	# Clear out any old animations from another configuration
	pRomFelix.ClearAnimations()

	# Register animation mappings
	pRomFelix.SetStanding(1)
	pRomFelix.SetHidden(0)
	pRomFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pRomFelix)

#	kDebugObj.Print("Finished configuring RomFelix")

###############################################################################
#	LoadSounds
#	
#	Precache RomFelix's typical voice lines, so they don't hitch the
#	game when they try to play.
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")

	# Loop through all of RomFelix's voice lines that we want to preload, and load them.
	for sLine in g_lsFelixLines:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)

#
# A list of the voice lines we want preloaded for RomFelix.
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
