from bcdebug import debug
###############################################################################
#	Filename:	ENBMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENBMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDebugObj = App.CPyDDebug()

###############################################################################
#	CreateCharacter()
#
#	Create ENBMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating ENBMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENBMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyENBMaleM/BodyENBMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pENBMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyENBMaleM/BodyENBMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pENBMaleExtra1.ReplacebodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyENBMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/ENBMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENBMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBMaleExtra1)

	# Setup the character configuration
	pENBMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pENBMaleExtra1.SetGender(App.CharacterClass.MALE)
	pENBMaleExtra1.SetRandomAnimationChance(.75)
	pENBMaleExtra1.SetBlinkChance(0.1)
	pENBMaleExtra1.SetCharacterName("MaleExtra1")

	pENBMaleExtra1.SetHidden(0)

	# Load ENBMaleExtra1's generic sounds
	LoadSounds()

	# Create ENBMaleExtra1's menus
	#import ENBMaleExtra1MenuHandlers
	#ENBMaleExtra1MenuHandlers.CreateMenus(pENBMaleExtra1)

	pENBMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pENBMaleExtra1.GetDatabase(), "ENBMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDDebugObj.Print("Finished creating ENBMaleExtra1")
	return pENBMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENBMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENBMaleExtra1):
#	kDDebugObj.Print("Configuring ENBMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENBMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY ENBMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENBMaleExtra1)

	pENBMaleExtra1.SetAsExtra(1)
	pENBMaleExtra1.SetHidden(0)

	pENBMaleExtra1.SetLocation("DBL3M")
#	kDDebugObj.Print("Finished configuring ENBMaleExtra1")


###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pENBMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseB")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("ENBL2MToG", "Bridge.Characters.ENBMediumAnimations.ENBL2ToG1")
	pMaleExtra1.AddAnimation("ENBG1MToL", "Bridge.Characters.ENBMediumAnimations.ENBG1ToL2")
	pMaleExtra1.AddAnimation("SeatedENBG1M", "Bridge.Characters.CommonAnimations.SeatedM")
	pMaleExtra1.SetStanding(0)

	# Hit animations
	pMaleExtra1.AddAnimation("ENBG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("ENBG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("ENBL3M")
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
#	Args:	pENBMaleExtra1	- our Character object
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
	# ENBMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass

