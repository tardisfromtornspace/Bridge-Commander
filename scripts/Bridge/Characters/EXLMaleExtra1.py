from bcdebug import debug
###############################################################################
#	Filename:	EXLMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador EXLMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDebugObj = App.CPyDDebug()

###############################################################################
#	CreateCharacter()
#
#	Create EXLMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating EXLMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("EXLMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyEXLMaleM/BodyEXLMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pEXLMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyEXLMaleM/BodyEXLMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pEXLMaleExtra1.ReplacebodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyEXLMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/EXLMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLMaleExtra1)

	# Setup the character configuration
	pEXLMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pEXLMaleExtra1.SetGender(App.CharacterClass.MALE)
	pEXLMaleExtra1.SetRandomAnimationChance(.75)
	pEXLMaleExtra1.SetBlinkChance(0.1)
	pEXLMaleExtra1.SetCharacterName("MaleExtra1")

	pEXLMaleExtra1.SetHidden(1)

	# Load EXLMaleExtra1's generic sounds
	LoadSounds()

	# Create EXLMaleExtra1's menus
	#import EXLMaleExtra1MenuHandlers
	#EXLMaleExtra1MenuHandlers.CreateMenus(pEXLMaleExtra1)

	pEXLMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pEXLMaleExtra1.GetDatabase(), "EXLMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDDebugObj.Print("Finished creating EXLMaleExtra1")
	return pEXLMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pEXLMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pEXLMaleExtra1):
#	kDDebugObj.Print("Configuring EXLMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pEXLMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY EXLMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pEXLMaleExtra1)

	pEXLMaleExtra1.SetAsExtra(1)
	pEXLMaleExtra1.SetHidden(1)

	pEXLMaleExtra1.SetLocation("DBL2M")
#	kDDebugObj.Print("Finished configuring EXLMaleExtra1")


###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pEXLMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the Excelsior bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcelsior")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("EXLL2MToG", "Bridge.Characters.EXLMediumAnimations.EXLL2ToG1")
	pMaleExtra1.AddAnimation("EXLG1MToL", "Bridge.Characters.EXLMediumAnimations.EXLG1ToL2")
	pMaleExtra1.AddAnimation("StandingEXLG1M", "Bridge.Characters.CommonAnimations.Standing")
	pMaleExtra1.SetStanding(1)

	# Hit animations
	pMaleExtra1.AddAnimation("EXLG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pMaleExtra1.AddAnimation("EXLG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pMaleExtra1.AddAnimation("EXLG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("EXLG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("EXLL2M")
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
#	Args:	pEXLMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLMaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pEXLMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# EXLMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
