from bcdebug import debug
###############################################################################
#	Filename:	ExcMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ExcMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDExcugObj = App.CPyDExcug()

###############################################################################
#	CreateCharacter()
#
#	Create ExcMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDExcugObj.Print("Creating ExcMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ExcMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyExcMaleM/BodyExcMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pExcMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyExcMaleM/BodyExcMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pExcMaleExtra2.ReplacExcodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyExcMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/ExcMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pExcMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcMaleExtra2)

	# Setup the character configuration
	pExcMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pExcMaleExtra2.SetGender(App.CharacterClass.MALE)
	pExcMaleExtra2.SetRandomAnimationChance(.75)
	pExcMaleExtra2.SetBlinkChance(0.1)
	pExcMaleExtra2.SetCharacterName("MaleExtra2")

	pExcMaleExtra2.SetHidden(1)

	# Load ExcMaleExtra2's generic sounds
	LoadSounds()

	# Create ExcMaleExtra2's menus
	#import ExcMaleExtra2MenuHandlers
	#ExcMaleExtra2MenuHandlers.CreateMenus(pExcMaleExtra2)

	pExcMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pExcMaleExtra2.GetDatabase(), "ExcMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDExcugObj.Print("Finished creating ExcMaleExtra2")
	return pExcMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pExcMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pExcMaleExtra2):
#	kDExcugObj.Print("Configuring ExcMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pExcMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY ExcMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pExcMaleExtra2)

	pExcMaleExtra2.SetAsExtra(1)
	pExcMaleExtra2.SetHidden(1)

	pExcMaleExtra2.SetLocation("DBL2M")
#	kDExcugObj.Print("Finished configuring ExcMaleExtra2")


###############################################################################
#	ConfigureForExcalibur()
#
#	Configure ourselves for the Excalibur bridge
#
#	Args:	pExcMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pExcMaleExtra2):
#	kDExcugObj.Print("Configuring ExcMaleExtra2 for the Excalibur bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcalibur")
	pExcMaleExtra2.ClearAnimations()

	# Register animation mappings
	pExcMaleExtra2.AddAnimation("ExcL2MToG", "Bridge.Characters.ExcMediumAnimations.ExcL2ToG2")
	pExcMaleExtra2.AddAnimation("ExcG2MToL", "Bridge.Characters.ExcMediumAnimations.ExcG2ToL2")
	pExcMaleExtra2.AddAnimation("StandingExcG2M", "Bridge.Characters.CommonAnimations.Standing")
	pExcMaleExtra2.SetStanding(1)

	# Hit animations
	pExcMaleExtra2.AddAnimation("ExcG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pExcMaleExtra2.AddAnimation("ExcG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pExcMaleExtra2.AddAnimation("ExcG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pExcMaleExtra2.AddAnimation("ExcG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pExcMaleExtra2.AddAnimation("ExcG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pExcMaleExtra2.SetAsExtra(1)
	pExcMaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pExcMaleExtra2)

	pExcMaleExtra2.SetLocation("ExcL2M")
#	kDExcugObj.Print("Finished configuring ExcMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pExcMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcMaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.PushingButtons")
#	pExcMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleSlide")


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
	# ExcMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
