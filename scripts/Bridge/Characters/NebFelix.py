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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif", None)
	pNebFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pNebFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pNebFelix.SetCharacterName("NebFelix")

	# Add the character to the set
	pSet.AddObjectToSet(pNebFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebFelix)

	# Set up character configuration
	pNebFelix.SetSize(App.CharacterClass.LARGE)
	pNebFelix.SetGender(App.CharacterClass.MALE)
	pNebFelix.SetStanding(0)
	pNebFelix.SetRandomAnimationChance(0.75)
	pNebFelix.SetBlinkChance(0.1)
	pNebFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pNebFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pNebFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_blink1.tga")
	pNebFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_blink2.tga")
	pNebFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_eyesclosed.tga")
	pNebFelix.SetBlinkStages(3)

	pNebFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_head_a.tga")
	pNebFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_head_e.tga")
	pNebFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_head_u.tga")
	pNebFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pNebFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pNebFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pNebFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pNebFelix

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
	pNebFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pNebFelix)
	pNebFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pNebFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pNebFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebFelix)

	# Set up character configuration
	pNebFelix.SetSize(App.CharacterClass.LARGE)
	pNebFelix.SetGender(App.CharacterClass.MALE)
	pNebFelix.SetStanding(0)
	pNebFelix.SetHidden(1)
	pNebFelix.SetRandomAnimationChance(0.75)
	pNebFelix.SetBlinkChance(0.1)
	pNebFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pNebFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pNebFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pNebFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pNebFelix


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
	pNebFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pNebFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pNebFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pNebFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebFelix)

	# Set up character configuration
	pNebFelix.SetSize(App.CharacterClass.LARGE)
	pNebFelix.SetGender(App.CharacterClass.MALE)
	pNebFelix.SetStanding(0)
	pNebFelix.SetHidden(1)
	pNebFelix.SetRandomAnimationChance(0.75)
	pNebFelix.SetBlinkChance(0.1)
	pNebFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pNebFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pNebFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pNebFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pNebFelix


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
	pNebFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pNebFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pNebFelix)

###############################################################################
#	ConfigureForNebula()
#
#	Configure ourselves for the Nebula bridge
#
#	Args:	pNebFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pNebFelix):
#	kDebugObj.Print("Configuring Felix for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pNebFelix.ClearAnimations()

	# Register animation mappings
	pNebFelix.AddAnimation("SeatedNebTactical", "Bridge.Characters.CommonAnimations.SeatedL")
	pNebFelix.AddAnimation("EBL1LToT", "Bridge.Characters.NebLargeAnimations.EBMoveFromL1ToT")
	pNebFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.NebLargeAnimations.EBMoveFromTToL1")
	pNebFelix.AddAnimation("NebTacticalTurnCaptain", "Bridge.Characters.NebLargeAnimations.NebTurnAtTTowardsCaptain")
	pNebFelix.AddAnimation("NebTacticalBackCaptain", "Bridge.Characters.NebLargeAnimations.NebTurnBackAtTFromCaptain")

	pNebFelix.AddAnimation("NebTacticalTurnC", "Bridge.Characters.NebLargeAnimations.NebTTalkC")
	pNebFelix.AddAnimation("NebTacticalBackC", "Bridge.Characters.NebLargeAnimations.NebTTalkFinC")
	pNebFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.NebLargeAnimations.EBTTalkE")
	pNebFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.NebLargeAnimations.EBTTalkFinE")
	pNebFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.NebLargeAnimations.EBTTalkH")
	pNebFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.NebLargeAnimations.EBTTalkFinH")
	pNebFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.NebLargeAnimations.EBTTalkS")
	pNebFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.NebLargeAnimations.EBTTalkFinS")

	pNebFelix.AddAnimation("EBTacticalTurnX", "Bridge.Characters.NebLargeAnimations.EBTTalkE")
	pNebFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.NebLargeAnimations.EBTTalkFinE")

	pNebFelix.AddAnimation("NebTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pNebFelix.AddAnimation("NebTacticalGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedL")

	# Breathing
	pNebFelix.AddAnimation("NebTacticalBreathe", "Bridge.Characters.CommonAnimations.SeatedL")
	pNebFelix.AddAnimation("NebTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pNebFelix.AddRandomAnimation("Bridge.Characters.NebLargeAnimations.NebTConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pNebFelix.AddAnimation("PushingButtons", "Bridge.Characters.NebLargeAnimations.NebTConsoleInteraction")

	# Hit animations		
	#pNebFelix.AddAnimation("NebTacticalHit", "Bridge.Characters.NebLargeAnimations.NebTHit")
	#pNebFelix.AddAnimation("NebTacticalHitHard", "Bridge.Characters.NebLargeAnimations.NebTHitHard")
	pNebFelix.AddAnimation("NebTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pNebFelix.AddAnimation("NebTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pNebFelix)
	
	pNebFelix.SetLocation("NebTactical")
	pNebFelix.AddPositionZoom("NebTactical", 0.8, "Tactical")
	pNebFelix.SetLookAtAdj(-2, 0, 75)
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
#	Args:	pNebFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebFelix):
	debug(__name__ + ", AddCommonAnimations")
	pNebFelix.AddRandomAnimation("Bridge.Characters.NebLargeAnimations.TLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pNebFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pNebFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pNebFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pNebFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pNebFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pNebFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pNebFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pNebFelix):
	debug(__name__ + ", OffBridgeStart")
	pNebFelix = App.CharacterClass_Cast(pNebFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pNebFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pNebFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pNebFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pNebFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	pNebFelix.ClearAnimations()

	# Register animation mappings
	pNebFelix.SetStanding(1)
	pNebFelix.SetHidden(0)
	pNebFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pNebFelix)

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
