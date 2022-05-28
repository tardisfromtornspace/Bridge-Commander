from bcdebug import debug
###############################################################################
#	Filename:	AmbMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador AmbMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDAmbug()

###############################################################################
#	CreateCharacter()
#
#	Create AmbMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating AmbMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("AmbMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyAmbMaleM/BodyAmbMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pAmbMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyAmbMaleM/BodyAmbMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pAmbMaleExtra3.ReplacAmbodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyAmbMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/AmbMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbMaleExtra3)

	# Setup the character configuration
	pAmbMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pAmbMaleExtra3.SetGender(App.CharacterClass.MALE)
	pAmbMaleExtra3.SetRandomAnimationChance(.75)
	pAmbMaleExtra3.SetBlinkChance(0.1)
	pAmbMaleExtra3.SetCharacterName("MaleExtra3")

	pAmbMaleExtra3.SetHidden(1)

	# Load AmbMaleExtra3's generic sounds
	LoadSounds()

	# Create AmbMaleExtra3's menus
	#import AmbMaleExtra3MenuHandlers
	#AmbMaleExtra3MenuHandlers.CreateMenus(pAmbMaleExtra3)

	pAmbMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pAmbMaleExtra3.GetDatabase(), "AmbMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating AmbMaleExtra3")
	return pAmbMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pAmbMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pAmbMaleExtra3):
#	kDebugObj.Print("Configuring AmbMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pAmbMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY AmbMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pAmbMaleExtra3)

	pAmbMaleExtra3.SetAsExtra(1)
	pAmbMaleExtra3.SetHidden(1)

	pAmbMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring AmbMaleExtra3")

###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pAmbMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Ambassador bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForAmbassador")
	pAmbMaleExtra3.ClearAnimations()

	# Register animation mappings
	pAmbMaleExtra3.AddAnimation("AmbL1MToG", "Bridge.Characters.AmbMediumAnimations.AmbL1ToG3")
	pAmbMaleExtra3.AddAnimation("AmbG3MToL", "Bridge.Characters.AmbMediumAnimations.AmbG3ToL1")
	pAmbMaleExtra3.AddAnimation("StandingAmbG3M", "Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")
	pAmbMaleExtra3.SetStanding(1)

	# Hit animations
	pAmbMaleExtra3.AddAnimation("AmbG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pAmbMaleExtra3.AddAnimation("AmbG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pAmbMaleExtra3.AddAnimation("AmbG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pAmbMaleExtra3.AddAnimation("AmbG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pAmbMaleExtra3.AddAnimation("AmbG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pAmbMaleExtra3.SetAsExtra(1)
	pAmbMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pAmbMaleExtra3)

	pAmbMaleExtra3.SetLocation("AmbL1M")
#	kDebugObj.Print("Finished configuring MaleExtra3")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pAmbMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbMaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
#	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")
	pAmbMaleExtra3.AddRandomAnimation("Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")


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
	#
	# AmbMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
