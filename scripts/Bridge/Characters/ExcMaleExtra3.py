from bcdebug import debug
###############################################################################
#	Filename:	ExcMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ExcMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDExcug()

###############################################################################
#	CreateCharacter()
#
#	Create ExcMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating ExcMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ExcMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyExcMaleM/BodyExcMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pExcMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyExcMaleM/BodyExcMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pExcMaleExtra3.ReplacExcodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyExcMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/ExcMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pExcMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcMaleExtra3)

	# Setup the character configuration
	pExcMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pExcMaleExtra3.SetGender(App.CharacterClass.MALE)
	pExcMaleExtra3.SetRandomAnimationChance(.75)
	pExcMaleExtra3.SetBlinkChance(0.1)
	pExcMaleExtra3.SetCharacterName("MaleExtra3")

	pExcMaleExtra3.SetHidden(1)

	# Load ExcMaleExtra3's generic sounds
	LoadSounds()

	# Create ExcMaleExtra3's menus
	#import ExcMaleExtra3MenuHandlers
	#ExcMaleExtra3MenuHandlers.CreateMenus(pExcMaleExtra3)

	pExcMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pExcMaleExtra3.GetDatabase(), "ExcMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating ExcMaleExtra3")
	return pExcMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pExcMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pExcMaleExtra3):
#	kDebugObj.Print("Configuring ExcMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pExcMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY ExcMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pExcMaleExtra3)

	pExcMaleExtra3.SetAsExtra(1)
	pExcMaleExtra3.SetHidden(1)

	pExcMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring ExcMaleExtra3")

###############################################################################
#	ConfigureForExcalibur()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pExcMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcalibur")
	pExcMaleExtra3.ClearAnimations()

	# Register animation mappings
	pExcMaleExtra3.AddAnimation("ExcL1MToG", "Bridge.Characters.ExcMediumAnimations.ExcL1ToG3")
	pExcMaleExtra3.AddAnimation("ExcG3MToL", "Bridge.Characters.ExcMediumAnimations.ExcG3ToL1")
	pExcMaleExtra3.AddAnimation("StandingExcG3M", "Bridge.Characters.CommonAnimations.Standing")
	pExcMaleExtra3.SetStanding(1)

	# Hit animations
	pExcMaleExtra3.AddAnimation("ExcG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pExcMaleExtra3.AddAnimation("ExcG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pExcMaleExtra3.AddAnimation("ExcG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pExcMaleExtra3.AddAnimation("ExcG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pExcMaleExtra3.AddAnimation("ExcG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pExcMaleExtra3.SetAsExtra(1)
	pExcMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pExcMaleExtra3)

	pExcMaleExtra3.SetLocation("ExcL1M")
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
#	Args:	pExcMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcMaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pExcMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# ExcMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
