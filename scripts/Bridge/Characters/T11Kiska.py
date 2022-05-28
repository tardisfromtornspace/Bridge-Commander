###############################################################################
#	Filename:	Kiska.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Kiska Lomar, Helm, and configures animations
#	
#	Created:	3/28/00 -	Erik Novales
#           Modified: 2/06/05                Blackrook32
###############################################################################

import App
import CharacterPaths
import Bridge.Characters.MediumAnimations

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create Kiska by building her character and placing her on the passed in set.
#	Create her menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating Kiska")

	if (pSet.GetObject("Helm") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Helm")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadKiska/kiska_head.nif", None)
	pT11Kiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadKiska/kiska_head.nif", 1)
	pT11Kiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemRed_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadKiska/kiska_head.tga")

	pT11Kiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pT11Kiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pT11Kiska)

	# Setup the character configuration
	pT11Kiska.SetSize(App.CharacterClass.MEDIUM)
	pT11Kiska.SetGender(App.CharacterClass.FEMALE)
	pT11Kiska.SetStanding(0)
	pT11Kiska.SetRandomAnimationChance(0.65)
	pT11Kiska.SetBlinkChance(0.1)
	pT11Kiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()
	AddCommonAnimations(pT11Kiska)

	pT11Kiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_blink1.tga")
	pT11Kiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_blink2.tga")
	pT11Kiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_eyesclosed.tga")
	pT11Kiska.SetBlinkStages(3)

	pT11Kiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_a.tga")
	pT11Kiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_e.tga")
	pT11Kiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_u.tga")
	pT11Kiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pT11Kiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pT11Kiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Kiska")
	return pT11Kiska


###############################################################################
#	ConfigureForShip()
#
#	Configure ourselves for the particular ship object.  This involves setting
#	up range watchers that tell us how to report.
#
#	Args:	pSet	- the Set object
#			pShip	- the player's ship (ShipClass object)
#
#	Return:	none
###############################################################################
def ConfigureForShip(pSet, pShip):
	pT11Kiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pT11Kiska == None):
		return

	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pT11Kiska)


def ConfigureForType11(pT11Kiska):

	pT11Kiska.ClearAnimations()

	pT11Kiska.AddAnimation("T11L1MToH", "Bridge.Characters.MediumAnimations.MoveFromL1ToH")
	pT11Kiska.AddAnimation("T11HelmToL1", "Bridge.Characters.MediumAnimations.MoveFromHToL1")

	pT11Kiska.AddAnimation("T11BHelmTurnCaptain", "Bridge.Characters.MediumAnimations.TurnAtHTowardsCaptain")
	pT11Kiska.AddAnimation("T11BHelmBackCaptain", "Bridge.Characters.MediumAnimations.TurnBackAtHFromCaptain")

	pT11Kiska.AddAnimation("T11BHelmTurnC", "Bridge.Characters.MediumAnimations.DBHTalkC")
	pT11Kiska.AddAnimation("T11BHelmBackC", "Bridge.Characters.MediumAnimations.DBHTalkFinC")
	pT11Kiska.AddAnimation("T11BHelmTurnE", "Bridge.Characters.MediumAnimations.DBHTalkE")
	pT11Kiska.AddAnimation("T11BHelmBackE", "Bridge.Characters.MediumAnimations.DBHTalkFinE")
	pT11Kiska.AddAnimation("T11BHelmTurnS", "Bridge.Characters.MediumAnimations.DBHTalkS")
	pT11Kiska.AddAnimation("T11BHelmBackS", "Bridge.Characters.MediumAnimations.DBHTalkFinS")
	pT11Kiska.AddAnimation("T11BHelmTurnT", "Bridge.Characters.MediumAnimations.DBHTalkT")
	pT11Kiska.AddAnimation("T11BHelmBackT", "Bridge.Characters.MediumAnimations.DBHTalkFinT")

	pT11Kiska.AddAnimation("T11BHelmTurnX", "Bridge.Characters.MediumAnimations.DBHTalkX")
	pT11Kiska.AddAnimation("T11BHelmBackX", "Bridge.Characters.MediumAnimations.DBHTalkFinX")

	pT11Kiska.AddAnimation("T11BHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pT11Kiska.AddAnimation("T11BHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pT11Kiska.AddAnimation("T11BHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# Hit animations
	pT11Kiska.AddAnimation("T11BHelmHit", "Bridge.Characters.MediumAnimations.HHit")
	pT11Kiska.AddAnimation("T11BHelmHitHard", "Bridge.Characters.MediumAnimations.HHitHard")
	pT11Kiska.AddAnimation("T11BHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pT11Kiska.AddAnimation("T11BHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	
	AddCommonAnimations(pT11Kiska)

	pT11Kiska.SetStanding(0)
	pT11Kiska.SetLocation("T11Helm")
	pT11Kiska.SetTranslateXYZ(22.000000, 60.000000, -48.000000)
	
def AddCommonAnimations(pT11Kiska):
	
	# Just random stuff
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.Yawn")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.Sigh")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.Neck_Rub")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.Hair_Wipe")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleLookDownForeLeft")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleLookUpForeRight")
	pT11Kiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")


###############################################################################
#	LoadSounds()
#
#	Load generic bridge sounds for this character
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")

	#
	# Build a list of sound to load
	#
	lSoundList =	[	"KiskaSir1",	# Click Response
						"KiskaSir2",
						"KiskaSir3",
						"KiskaSir4",
						"KiskaSir5",
						
						"KiskaYes1",	# Order Confirmation
						"KiskaYes2",
						"KiskaYes3",
						"KiskaYes4",

						"gh075",	# Course laid in
						"gh081",	# Intercept course plotted

						"HailOpen1",
						"HailOpen2",
						"NotResponding1",
						"NotResponding2",
						"OnScreen",

						"CollisionAlert1",
						"CollisionAlert2",
						"CollisionAlert3",
						"CollisionAlert4",
						"CollisionAlert5",
						"CollisionAlert6",
						"CollisionAlert7",
						"CollisionAlert10",

						"IncomingMsg1",
						"IncomingMsg2",
						"IncomingMsg3",
						"IncomingMsg4",
						"IncomingMsg5",
						"IncomingMsg6",
					]
	#
	# Loop through that list, loading each sound in the "BridgeGeneric" group
	#
	for sLine in lSoundList:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)
