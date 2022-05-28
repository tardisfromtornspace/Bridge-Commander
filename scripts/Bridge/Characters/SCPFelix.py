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
	pSCPFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "Headklingon/klingon_head.nif")
	pSCPFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")

	pSCPFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPFelix)

	# Set up character configuration
	pSCPFelix.SetSize(App.CharacterClass.LARGE)
	pSCPFelix.SetGender(App.CharacterClass.MALE)
	pSCPFelix.SetStanding(1)
	pSCPFelix.SetRandomAnimationChance(0.75)
	pSCPFelix.SetBlinkChance(0.1)
	pSCPFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pSCPFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pSCPFelix.AdSCPacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pSCPFelix.AdSCPacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pSCPFelix.AdSCPacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pSCPFelix.SetBlinkStages(3)

	pSCPFelix.AdSCPacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pSCPFelix.AdSCPacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pSCPFelix.AdSCPacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "../Ramblers/heads/HeadKlingon/kartok_head.tga")
	pSCPFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pSCPFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pSCPFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pSCPFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pSCPFelix

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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeaSCPelix/felix_head.nif", None)
	pSCPFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeaSCPelix/felix_head.nif")
	Bridge.TacticalMenuHandlers.CreateMenusNoSounds(pSCPFelix)
	pSCPFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "../BridgeCrew/Felix/felix_body.tga", CharacterPaths.g_pcHeadTexPath + "../BridgeCrew/Felix/felix_head.tga")

	pSCPFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPFelix)

	# Set up character configuration
	pSCPFelix.SetSize(App.CharacterClass.LARGE)
	pSCPFelix.SetGender(App.CharacterClass.MALE)
	pSCPFelix.SetStanding(1)
	pSCPFelix.SetHidden(1)
	pSCPFelix.SetRandomAnimationChance(0.75)
	pSCPFelix.SetBlinkChance(0.1)
	pSCPFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pSCPFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pSCPFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pSCPFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pSCPFelix


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
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeaSCPelix/felix_head.nif", None)
	pSCPFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeaSCPelix/felix_head.nif")
	pSCPFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeaSCPelix/felix_head.tga")

	pSCPFelix.SetCharacterName("Felix")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPFelix)

	# Set up character configuration
	pSCPFelix.SetSize(App.CharacterClass.LARGE)
	pSCPFelix.SetGender(App.CharacterClass.MALE)
	pSCPFelix.SetStanding(1)
	pSCPFelix.SetHidden(1)
	pSCPFelix.SetRandomAnimationChance(0.75)
	pSCPFelix.SetBlinkChance(0.1)
	pSCPFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pSCPFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pSCPFelix.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pSCPFelix.SetLocation("")

#	kDebugObj.Print("Finished creating Felix")
	return pSCPFelix


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
	pSCPFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pSCPFelix == None):
#		kDebugObj.Print("******* Tactical officer not found *********")
		return

#	kDebugObj.Print("Attaching menu to Tactical..")
	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pSCPFelix)


###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pSCPFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pSCPFelix):
#	kDebugObj.Print("Configuring Felix for the SCP bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalor")
	pSCPFelix.ClearAnimations()

	# Register animation mappings
	pSCPFelix.AddAnimation("SeatedSCPTactical", "Bridge.Characters.SCPLargeAnimations.SCPseatedTL")
	pSCPFelix.AddAnimation("EBL1LToT", "Bridge.Characters.SCPLargeAnimations.EBMoveFromL1ToT")
	pSCPFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.SCPLargeAnimations.EBMoveFromTToL1")
	pSCPFelix.AddAnimation("SCPTacticalTurnCaptain", "Bridge.Characters.SCPLargeAnimations.SCPTurnAtTTowardsCaptain")
	pSCPFelix.AddAnimation("SCPTacticalBackCaptain", "Bridge.Characters.SCPLargeAnimations.SCPTurnBackAtTFromCaptain")

	pSCPFelix.AddAnimation("SCPTacticalTurnC", "Bridge.Characters.SCPLargeAnimations.SCPTurnAtTTowardsCaptain")
	pSCPFelix.AddAnimation("SCPTacticalBackC", "Bridge.Characters.SCPLargeAnimations.SCPTurnBackAtTFromCaptain")
	pSCPFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.SCPLargeAnimations.EBTTalkE")
	pSCPFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.SCPLargeAnimations.EBTTalkFinE")
	pSCPFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.SCPLargeAnimations.EBTTalkH")
	pSCPFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.SCPLargeAnimations.EBTTalkFinH")
	pSCPFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.SCPLargeAnimations.EBTTalkS")
	pSCPFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.SCPLargeAnimations.EBTTalkFinS")

	pSCPFelix.AddAnimation("EBTacticalTurSCP", "Bridge.Characters.SCPLargeAnimations.EBTTalkE")
	pSCPFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.SCPLargeAnimations.EBTTalkFinE")

	pSCPFelix.AddAnimation("SCPTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pSCPFelix.AddAnimation("SCPTacticalGlanceAwayCaptain", "Bridge.Characters.SCPLargeAnimations.SCPTConsoleInteraction")

	# Breathing
	pSCPFelix.AddAnimation("SCPTacticalBreathe", "Bridge.Characters.SCPLargeAnimations.SCPTConsoleInteraction")
	pSCPFelix.AddAnimation("SCPTacticalBreatheTurned", "Bridge.Characters.SCPLargeAnimations.SCPTConsoleInteraction")

	# SCPeraction
	pSCPFelix.AddRandomAnimation("Bridge.Characters.SCPLargeAnimations.SCPTConsoleInteraction",App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pSCPFelix.AddAnimation("PushingButtons", "Bridge.Characters.SCPLargeAnimations.SCPTConsoleInteraction")

	# Hit animations		
	#pSCPFelix.AddAnimation("SCPTacticalHit", "Bridge.Characters.SCPLargeAnimations.SCPTHit")
	#pSCPFelix.AddAnimation("SCPTacticalHitHard", "Bridge.Characters.SCPLargeAnimations.SCPTHitHard")
	pSCPFelix.AddAnimation("SCPTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pSCPFelix.AddAnimation("SCPTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	# Add common animations.
	AddCommonAnimations(pSCPFelix)
	
	pSCPFelix.SetLocation("SCPTactical")
	pSCPFelix.SetStanding(0)
#	pSCPFelix.AddPositionZoom("SCPTactical", 0.60, "Tactical")
	pSCPFelix.AddPositionZoom("SCPTactical", 0.60)
#	pSCPFelix.SetLookAtAdj(0, 0, 10)
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
#	Args:	pSCPFelix	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPFelix):
	debug(__name__ + ", AddCommonAnimations")
	pSCPFelix.AddRandomAnimation("Bridge.Characters.SCPLargeAnimations.TLookAroundConsoleDown", 1, 1)

	pSCPFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pSCPFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pSCPFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")

	#pSCPFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowLeft")
	#pSCPFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.WipingBrowRight")
	#pSCPFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pSCPFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	#pSCPFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.AtEase", App.CharacterClass.STANDING_ONLY)

###############################################################################
#	OffBridgeStart
#	
#	Sets Felix's location to start in the off bridge partial set
#	
#	Args:	pSCPFelix	- our character object
#	
#	Return:	none
###############################################################################
def OffBridgeStart(pSCPFelix):
	debug(__name__ + ", OffBridgeStart")
	pSCPFelix = App.CharacterClass_Cast(pSCPFelix)
	# Nothing else to do, unless you want to change his position

	#Adjust positions of bridge characters here
	pSCPFelix.SetTranslateXYZ(0, 0, -5)

	import Bridge.Characters.CommonAnimations
	return Bridge.Characters.CommonAnimations.Standing(pSCPFelix)


###############################################################################
#	ConfigureForOffBridge()
#
#	Configure ourselves for another partial set
#
#	Args:	pSCPFelix	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForOffBridge(pSCPFelix):
#	kDebugObj.Print("Configuring Felix for off bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForOffBridge")
	pSCPFelix.ClearAnimations()

	# Register animation mappings
	pSCPFelix.SetStanding(1)
	pSCPFelix.SetHidden(0)
	pSCPFelix.SetLocation("KlingonSeated")
	AddCommonAnimations(pSCPFelix)

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
