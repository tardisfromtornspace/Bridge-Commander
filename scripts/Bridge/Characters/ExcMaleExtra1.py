from bcdebug import debug
###############################################################################
#	Filename:	ExcMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ExcMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDExcugObj = App.CPyDExcug()

###############################################################################
#	CreateCharacter()
#
#	Create ExcMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDExcugObj.Print("Creating ExcMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ExcMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyExcMaleM/BodyExcMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pExcMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyExcMaleM/BodyExcMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pExcMaleExtra1.ReplacExcodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyExcMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/ExcMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pExcMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcMaleExtra1)

	# Setup the character configuration
	pExcMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pExcMaleExtra1.SetGender(App.CharacterClass.MALE)
	pExcMaleExtra1.SetRandomAnimationChance(.75)
	pExcMaleExtra1.SetBlinkChance(0.1)
	pExcMaleExtra1.SetCharacterName("MaleExtra1")

	pExcMaleExtra1.SetHidden(1)

	# Load ExcMaleExtra1's generic sounds
	LoadSounds()

	# Create ExcMaleExtra1's menus
	#import ExcMaleExtra1MenuHandlers
	#ExcMaleExtra1MenuHandlers.CreateMenus(pExcMaleExtra1)

	pExcMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pExcMaleExtra1.GetDatabase(), "ExcMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDExcugObj.Print("Finished creating ExcMaleExtra1")
	return pExcMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pExcMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pExcMaleExtra1):
#	kDExcugObj.Print("Configuring ExcMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pExcMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY ExcMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pExcMaleExtra1)

	pExcMaleExtra1.SetAsExtra(1)
	pExcMaleExtra1.SetHidden(1)

	pExcMaleExtra1.SetLocation("DBL2M")
#	kDExcugObj.Print("Finished configuring ExcMaleExtra1")


###############################################################################
#	ConfigureForSovereign()
#
#	Configure ourselves for the Excalibur bridge
#
#	Args:	pExcMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcalibur")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("ExcL2MToG", "Bridge.Characters.ExcMediumAnimations.ExcL2ToG1")
	pMaleExtra1.AddAnimation("ExcG1MToL", "Bridge.Characters.ExcMediumAnimations.ExcG1ToL2")
	pMaleExtra1.AddAnimation("StandingExcG1M", "Bridge.Characters.CommonAnimations.Standing")
	pMaleExtra1.SetStanding(1)

	# Hit animations
	pMaleExtra1.AddAnimation("ExcG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pMaleExtra1.AddAnimation("ExcG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pMaleExtra1.AddAnimation("ExcG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("ExcG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("ExcL2M")
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
#	Args:	pExcMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcMaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pExcMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# ExcMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
