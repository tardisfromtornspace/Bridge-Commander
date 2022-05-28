from bcdebug import debug
###############################################################################
#	Filename:	AmbMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador AmbMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDAmbugObj = App.CPyDAmbug()

###############################################################################
#	CreateCharacter()
#
#	Create AmbMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDAmbugObj.Print("Creating AmbMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("AmbMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyAmbMaleM/BodyAmbMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pAmbMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyAmbMaleM/BodyAmbMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pAmbMaleExtra1.ReplacAmbodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyAmbMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/AmbMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbMaleExtra1)

	# Setup the character configuration
	pAmbMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pAmbMaleExtra1.SetGender(App.CharacterClass.MALE)
	pAmbMaleExtra1.SetRandomAnimationChance(.75)
	pAmbMaleExtra1.SetBlinkChance(0.1)
	pAmbMaleExtra1.SetCharacterName("MaleExtra1")

	pAmbMaleExtra1.SetHidden(1)

	# Load AmbMaleExtra1's generic sounds
	LoadSounds()

	# Create AmbMaleExtra1's menus
	#import AmbMaleExtra1MenuHandlers
	#AmbMaleExtra1MenuHandlers.CreateMenus(pAmbMaleExtra1)

	pAmbMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pAmbMaleExtra1.GetDatabase(), "AmbMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDAmbugObj.Print("Finished creating AmbMaleExtra1")
	return pAmbMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pAmbMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pAmbMaleExtra1):
#	kDAmbugObj.Print("Configuring AmbMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pAmbMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY AmbMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pAmbMaleExtra1)

	pAmbMaleExtra1.SetAsExtra(1)
	pAmbMaleExtra1.SetHidden(1)

	pAmbMaleExtra1.SetLocation("DBL2M")
#	kDAmbugObj.Print("Finished configuring AmbMaleExtra1")


###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pAmbMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the Ambassador bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForAmbassador")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
#	pMaleExtra1.AddAnimation("AmbL2MToG", "Bridge.Characters.AmbMediumAnimations.AmbL2ToG1")
#	pMaleExtra1.AddAnimation("AmbG1MToL", "Bridge.Characters.AmbMediumAnimations.AmbG1ToL2")
#	pMaleExtra1.AddAnimation("StandingAmbG1M", "Bridge.Characters.CommonAnimations.Standing")
#	pMaleExtra1.SetStanding(1)
#
	# Hit animations
#	pMaleExtra1.AddAnimation("AmbG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
#	pMaleExtra1.AddAnimation("AmbG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
#	pMaleExtra1.AddAnimation("AmbG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
#	pMaleExtra1.AddAnimation("AmbG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("AmbL2M")
#	kDebugObj.Print("Finished configuring MaleExtra1")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pAmbMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbMaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pAmbMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# AmbMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
