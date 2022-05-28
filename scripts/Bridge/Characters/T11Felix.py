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
	pT11Felix = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyMaleL/BodyMaleL.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFelix/felix_head.nif")
	pT11Felix.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFelix/felix_head.tga")

	pT11Felix.SetCharacterName("Felix")

	pSet.AddObjectToSet(pT11Felix, "Tactical")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pT11Felix)

	pT11Felix.SetSize(App.CharacterClass.LARGE)
	pT11Felix.SetGender(App.CharacterClass.MALE)
	pT11Felix.SetStanding(0)
	pT11Felix.SetRandomAnimationChance(0.35)
	pT11Felix.SetBlinkChance(0.1)
	pT11Felix.SetAudioMode(App.CharacterClass.CAM_EXTREMELY_VOCAL)
	pT11Felix.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()
        
	pT11Felix.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_blink1.tga")
	pT11Felix.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_blink2.tga")
	pT11Felix.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_eyesclosed.tga")
	pT11Felix.SetBlinkStages(3)

	pT11Felix.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_head_a.tga")
	pT11Felix.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_head_e.tga")
	pT11Felix.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadFelix/Felix_head_u.tga")
	pT11Felix.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pT11Felix.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Tactical")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	pT11Felix.SetLocation("")

	return pT11Felix


def ConfigureForShip(pSet, pShip):
	pT11Felix = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
	if (pT11Felix == None):
		return

	import Bridge.TacticalCharacterHandlers
	Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pT11Felix)

def ConfigureForType11(pT11Felix):
        
	pT11Felix.ClearAnimations()

	pT11Felix.AddAnimation("DBL1LToT", "Bridge.Characters.LargeAnimations.MoveFromL1ToT")
	pT11Felix.AddAnimation("DBTacticalToL1", "Bridge.Characters.LargeAnimations.MoveFromTToL1")
	pT11Felix.AddAnimation("DBTacticalTurnCaptain", "Bridge.Characters.LargeAnimations.TurnAtTTowardsCaptain")
	pT11Felix.AddAnimation("DBTacticalBackCaptain", "Bridge.Characters.LargeAnimations.TurnBackAtTFromCaptain")

	pT11Felix.AddAnimation("DBTacticalTurnC", "Bridge.Characters.LargeAnimations.DBTTalkC")
	pT11Felix.AddAnimation("DBTacticalBackC", "Bridge.Characters.LargeAnimations.DBTTalkFinC")
	pT11Felix.AddAnimation("DBTacticalTurnE", "Bridge.Characters.LargeAnimations.DBTTalkE")
	pT11Felix.AddAnimation("DBTacticalBackE", "Bridge.Characters.LargeAnimations.DBTTalkFinE")
	pT11Felix.AddAnimation("DBTacticalTurnH", "Bridge.Characters.LargeAnimations.DBTTalkH")
	pT11Felix.AddAnimation("DBTacticalBackH", "Bridge.Characters.LargeAnimations.DBTTalkFinH")
	pT11Felix.AddAnimation("DBTacticalTurnS", "Bridge.Characters.LargeAnimations.DBTTalkS")
	pT11Felix.AddAnimation("DBTacticalBackS", "Bridge.Characters.LargeAnimations.DBTTalkFinS")

	pT11Felix.AddAnimation("DBTacticalTurnX", "Bridge.Characters.LargeAnimations.DBTTalkX")
	pT11Felix.AddAnimation("DBTacticalBackX", "Bridge.Characters.LargeAnimations.DBTTalkFinX")

	pT11Felix.AddAnimation("DBTacticalGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceLeft")
	pT11Felix.AddAnimation("DBTacticalGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedL")

	# Breathing
	pT11Felix.AddAnimation("DBTacticalBreathe", "Bridge.Characters.CommonAnimations.SeatedL")
	pT11Felix.AddAnimation("DBTacticalBreatheTurned", "Bridge.Characters.CommonAnimations.BreathingTurned")

	# Hit animations		
	pT11Felix.AddAnimation("DBTacticalHit", "Bridge.Characters.LargeAnimations.THit");
	pT11Felix.AddAnimation("DBTacticalHitHard", "Bridge.Characters.LargeAnimations.THitHard");
	pT11Felix.AddAnimation("DBTacticalReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft");
	pT11Felix.AddAnimation("DBTacticalReactRight", "Bridge.Characters.CommonAnimations.ReactRight");
	
	AddCommonAnimations(pT11Felix)
	
	pT11Felix.SetStanding(0)
	pT11Felix.SetLocation("T11Tactical")
	pT11Felix.SetTranslateXYZ(40.000000, 60.000000, -48.000000)
	

def AddCommonAnimations(pFelix):

	# Just random stuff
	pFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.Yawn")
	pFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.Sigh")
	pFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.Neck_Rub")
	pFelix.AddRandomAnimation("Bridge.Characters.CommonAnimations.Hair_Wipe")

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
