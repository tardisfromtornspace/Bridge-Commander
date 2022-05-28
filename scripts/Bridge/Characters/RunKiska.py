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
	pRunKiska = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadKiska/kiska_head.nif", 1)
	pRunKiska.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemRed_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadKiska/kiska_head.tga")

	pRunKiska.SetCharacterName("Kiska")

	# Add the character to the set
	pSet.AddObjectToSet(pRunKiska, "Helm")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRunKiska)

	# Setup the character configuration
	pRunKiska.SetSize(App.CharacterClass.MEDIUM)
	pRunKiska.SetGender(App.CharacterClass.FEMALE)
	pRunKiska.SetStanding(0)
	pRunKiska.SetRandomAnimationChance(0.65)
	pRunKiska.SetBlinkChance(0.1)
	pRunKiska.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Helm officer generic sounds
	LoadSounds()
	AddCommonAnimations(pRunKiska)

	pRunKiska.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_blink1.tga")
	pRunKiska.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_blink2.tga")
	pRunKiska.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_eyesclosed.tga")
	pRunKiska.SetBlinkStages(3)

	pRunKiska.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_a.tga")
	pRunKiska.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_e.tga")
	pRunKiska.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadKiska/Kiska_head_u.tga")
	pRunKiska.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pKiska.GetDatabase(), "KiskaNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRunKiska.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Helm")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

#	kDebugObj.Print("Finished creating Kiska")
	return pRunKiska


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
	pRunKiska = App.CharacterClass_Cast(pSet.GetObject("Helm"))
	if (pRunKiska == None):
		return

	import Bridge.HelmCharacterHandlers
	Bridge.HelmCharacterHandlers.AttachMenuToHelm(pRunKiska)


def ConfigureForType11(pRunKiska):

	pRunKiska.ClearAnimations()

	# Register animation mappings
	pRunKiska.AddAnimation("EBL1MToH", "Bridge.Characters.MediumAnimations.EBMoveFromL1ToH")
	pRunKiska.AddAnimation("EBHelmToL1", "Bridge.Characters.MediumAnimations.EBMoveFromHToL1")
	pRunKiska.AddAnimation("EBHelmTurnCaptain", "Bridge.Characters.MediumAnimations.EBTurnAtHTowardsCaptain")
	pRunKiska.AddAnimation("EBHelmBackCaptain", "Bridge.Characters.MediumAnimations.EBTurnBackAtHFromCaptain")

	pRunKiska.AddAnimation("EBHelmTurnC", "Bridge.Characters.MediumAnimations.EBHTalkC")
	pRunKiska.AddAnimation("EBHelmBackC", "Bridge.Characters.MediumAnimations.EBHTalkFinC")
	pRunKiska.AddAnimation("EBHelmTurnE", "Bridge.Characters.MediumAnimations.EBHTalkE")
	pRunKiska.AddAnimation("EBHelmBackE", "Bridge.Characters.MediumAnimations.EBHTalkFinE")
	pRunKiska.AddAnimation("EBHelmTurnS", "Bridge.Characters.MediumAnimations.EBHTalkS")
	pRunKiska.AddAnimation("EBHelmBackS", "Bridge.Characters.MediumAnimations.EBHTalkFinS")
	pRunKiska.AddAnimation("EBHelmTurnT", "Bridge.Characters.MediumAnimations.EBHTalkT")
	pRunKiska.AddAnimation("EBHelmBackT", "Bridge.Characters.MediumAnimations.EBHTalkFinT")

	pRunKiska.AddAnimation("EBHelmTurnX", "Bridge.Characters.MediumAnimations.EBHTalkE")
	pRunKiska.AddAnimation("EBHelmBackX", "Bridge.Characters.MediumAnimations.EBHTalkFinE")

	pRunKiska.AddAnimation("EBHelmGlanceCaptain", "Bridge.Characters.CommonAnimations.GlanceRight")
	pRunKiska.AddAnimation("EBHelmGlanceAwayCaptain", "Bridge.Characters.CommonAnimations.SeatedM")

	# Breathing
	pRunKiska.AddAnimation("EBHelmBreathe", "Bridge.Characters.CommonAnimations.SeatedM")

	# Interaction
	pRunKiska.AddRandomAnimation("Bridge.Characters.MediumAnimations.DBHConsoleInteraction", App.CharacterClass.SITTING_ONLY, 25, 1)

	# So the mission builders can force the call
	pRunKiska.AddAnimation("PushingButtons", "Bridge.Characters.MediumAnimations.DBHConsoleInteraction")

	# Hit animations
	#pRunKiska.AddAnimation("EBHelmHit", "Bridge.Characters.MediumAnimations.HHit")
	#pRunKiska.AddAnimation("EBHelmHitHard", "Bridge.Characters.MediumAnimations.HHitHard")
	pRunKiska.AddAnimation("EBHelmReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pRunKiska.AddAnimation("EBHelmReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	
	AddCommonAnimations(pRunKiska)

	pRunKiska.SetStanding(0)
	pRunKiska.SetLocation("RunHelm")

	
def AddCommonAnimations(pRunKiska):
	
	# Just random stuff
	pRunKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRunKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRunKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pRunKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pRunKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleLookDownForeLeft")
	pRunKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleLookUpForeRight")
	pRunKiska.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")


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
