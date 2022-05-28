from bcdebug import debug
###############################################################################
#	Filename:	ENAMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENAMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDeugObj = App.CPyDDeug()

###############################################################################
#	CreateCharacter()
#
#	Create ENAMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDENAugObj.Print("Creating ENAMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENAMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyENAMaleM/BodyENAMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pENAMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyENAMaleM/BodyENAMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pENAMaleExtra1.ReplacENAodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyENAMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/ENAMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENAMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAMaleExtra1)

	# Setup the character configuration
	pENAMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pENAMaleExtra1.SetGender(App.CharacterClass.MALE)
	pENAMaleExtra1.SetRandomAnimationChance(.75)
	pENAMaleExtra1.SetBlinkChance(0.1)
	pENAMaleExtra1.SetCharacterName("MaleExtra1")

	pENAMaleExtra1.SetHidden(1)

	# Load ENAMaleExtra1's generic sounds
	LoadSounds()

	# Create ENAMaleExtra1's menus
	#import ENAMaleExtra1MenuHandlers
	#ENAMaleExtra1MenuHandlers.CreateMenus(pENAMaleExtra1)

	pENAMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pENAMaleExtra1.GetDatabase(), "ENAMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDDebugObj.Print("Finished creating ENAMaleExtra1")
	return pENAMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENAMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENAMaleExtra1):
#	kDDebugObj.Print("Configuring ENAMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENAMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY ENAMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENAMaleExtra1)

	pENAMaleExtra1.SetAsExtra(1)
	pENAMaleExtra1.SetHidden(1)

	pENAMaleExtra1.SetLocation("DBL2M")
#	kDDebugObj.Print("Finished configuring ENAMaleExtra1")


###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pENAMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseA")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("ENAL2MToG", "Bridge.Characters.ENAMediumAnimations.ENAL2ToG1")
	pMaleExtra1.AddAnimation("ENAG1MToL", "Bridge.Characters.ENAMediumAnimations.ENAG1ToL2")
	pMaleExtra1.AddAnimation("StandingENAG1M", "Bridge.Characters.CommonAnimations.Standing")
	pMaleExtra1.SetStanding(1)

	# Hit animations
	pMaleExtra1.AddAnimation("ENAG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pMaleExtra1.AddAnimation("ENAG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pMaleExtra1.AddAnimation("ENAG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("ENAG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("ENAL2M")
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
#	Args:	pENAMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENAMaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pENAMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# ENAMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
