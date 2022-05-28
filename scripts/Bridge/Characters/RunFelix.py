###############################################################################
#	Filename:	Felix.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Felix Savali, tactical officer, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
#           Modified: 2/06/05                Blackrook32
###############################################################################

import App
import CharacterPaths


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
        
	if (pSet.GetObject("Tactical") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Tactical")))

	CharacterPaths.UpdatePaths()
	
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif", None)
	pRunFelix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pRunFelix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pRunFelix.SetCharacterName("Felix")

	pSet.AddObjectToSet(pRunFelix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRunFelix)

	pRunFelix.SetSize(App.CharacterClass.LARGE)
	pRunFelix.SetGender(App.CharacterClass.MALE)
	pRunFelix.SetStanding(0)
	pRunFelix.SetRandomAnimationChance(0.35)
	pRunFelix.SetBlinkChance(0.1)
	pRunFelix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pRunFelix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()
        
	pRunFelix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_blink1.tga")
	pRunFelix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_blink2.tga")
	pRunFelix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_eyesclosed.tga")
	pRunFelix.SetBlinkStages(3)

	pRunFelix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_head_a.tga")
	pRunFelix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_head_e.tga")
	pRunFelix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_head_u.tga")
	pRunFelix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRunFelix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pRunFelix.SetLocation("")

	return pRunFelix


def ConfigureForShip(pSet, pShip):
	pRunFelix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pRunFelix == None):
		return

	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pFelix)

def ConfigureForType11(pRunFelix):
        
	pRunFelix.ClearAnimations()

	# Register animation mappings
	pRunFelix.AddAnimation("SeatedEBTactical", "Bridge.Characters.CommonAnimations.SeatedL")
	pRunFelix.AddAnimation("EBL1LToT", "Bridge.Characters.LargeAnimations.EBMoveFromL1ToT")
	pRunFelix.AddAnimation("EBTacticalToL1", "Bridge.Characters.LargeAnimations.EBMoveFromTToL1")
	pRunFelix.AddAnimation("EBTacticalTurnCaptain", "Bridge.Characters.LargeAnimations.EBTurnAtTTowardsCaptain")
	pRunFelix.AddAnimation("EBTacticalBackCaptain", "Bridge.Characters.LargeAnimations.EBTurnBackAtTFromCaptain")

	pRunFelix.AddAnimation("EBTacticalTurnC", "Bridge.Characters.LargeAnimations.EBTTalkC")
	pRunFelix.AddAnimation("EBTacticalBackC", "Bridge.Characters.LargeAnimations.EBTTalkFinC")
	pRunFelix.AddAnimation("EBTacticalTurnE", "Bridge.Characters.LargeAnimations.EBTTalkE")
	pRunFelix.AddAnimation("EBTacticalBackE", "Bridge.Characters.LargeAnimations.EBTTalkFinE")
	pRunFelix.AddAnimation("EBTacticalTurnH", "Bridge.Characters.LargeAnimations.EBTTalkH")
	pRunFelix.AddAnimation("EBTacticalBackH", "Bridge.Characters.LargeAnimations.EBTTalkFinH")
	pRunFelix.AddAnimation("EBTacticalTurnS", "Bridge.Characters.LargeAnimations.EBTTalkS")
	pRunFelix.AddAnimation("EBTacticalBackS", "Bridge.Characters.LargeAnimations.EBTTalkFinS")

	pRunFelix.AddAnimation("EBTacticalTurnX", "Bridge.Characters.LargeAnimations.EBTTalkE")
	pRunFelix.AddAnimation("EBTacticalBackX", "Bridge.Characters.LargeAnimations.EBTTalkFinE")

	pRunFelix.AddAnimation("EBTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pRunFelix.AddAnimation("EBTacticalGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedL")

	# Breathing
	pRunFelix.AddAnimation("EBTacticalBreathe", "Bridge.Characters.CommonAnimations.SeatedL")
	pRunFelix.AddAnimation("EBTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Interaction
	pRunFelix.AddRandomAnimation("Bridge.Characters.LargeAnimations.EBTConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pRunFelix.AddAnimation("PushingButtons", "Bridge.Characters.LargeAnimations.EBTConsoleInteraction")

	# Hit animations		
	#pRunFelix.AddAnimation("EBTacticalHit", "Bridge.Characters.LargeAnimations.THit")
	#pRunFelix.AddAnimation("EBTacticalHitHard", "Bridge.Characters.LargeAnimations.THitHard")
	pRunFelix.AddAnimation("EBTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pRunFelix.AddAnimation("EBTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	
	AddCommonAnimations(pRunFelix)
	
	pRunFelix.SetStanding(0)
	pRunFelix.SetLocation("RunTactical")

	

def AddCommonAnimations(pRunFelix):

	# Just random stuff
	pRunFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRunFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRunFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pRunFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")

	for sLine in g_lsFelixLines:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)

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
