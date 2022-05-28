from bcdebug import debug
###############################################################################
#	Filename:	IntMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador IntMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDIntugObj = App.CPyDIntug()

###############################################################################
#	CreateCharacter()
#
#	Create IntMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDIntugObj.Print("Creating IntMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("IntMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyIntMaleM/BodyIntMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pIntMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyIntMaleM/BodyIntMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pIntMaleExtra1.ReplacIntodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyIntMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/IntMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pIntMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntMaleExtra1)

	# Setup the character configuration
	pIntMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pIntMaleExtra1.SetGender(App.CharacterClass.MALE)
	pIntMaleExtra1.SetRandomAnimationChance(.75)
	pIntMaleExtra1.SetBlinkChance(0.1)
	pIntMaleExtra1.SetCharacterName("MaleExtra1")

	pIntMaleExtra1.SetHidden(1)

	# Load IntMaleExtra1's generic sounds
	LoadSounds()

	# Create IntMaleExtra1's menus
	#import IntMaleExtra1MenuHandlers
	#IntMaleExtra1MenuHandlers.CreateMenus(pIntMaleExtra1)

	pIntMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pIntMaleExtra1.GetDatabase(), "IntMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDIntugObj.Print("Finished creating IntMaleExtra1")
	return pIntMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pIntMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pIntMaleExtra1):
#	kDIntugObj.Print("Configuring IntMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pIntMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY IntMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pIntMaleExtra1)

	pIntMaleExtra1.SetAsExtra(1)
	pIntMaleExtra1.SetHidden(1)

	pIntMaleExtra1.SetLocation("DBL2M")
#	kDIntugObj.Print("Finished configuring IntMaleExtra1")


###############################################################################
#	ConfigureForSovereign()
#
#	Configure ourselves for the Intrepid bridge
#
#	Args:	pIntMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForIntrepid")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("IntL2MToG", "Bridge.Characters.IntMediumAnimations.IntL2ToG1")
	pMaleExtra1.AddAnimation("IntG1MToL", "Bridge.Characters.IntMediumAnimations.IntG1ToL2")
	pMaleExtra1.AddAnimation("StandingIntG1M", "Bridge.Characters.CommonAnimations.Standing")
	pMaleExtra1.SetStanding(1)

	# Hit animations
	pMaleExtra1.AddAnimation("IntG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pMaleExtra1.AddAnimation("IntG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pMaleExtra1.AddAnimation("IntG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("IntG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("IntL2M")
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
#	Args:	pIntMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntMaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pIntMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# IntMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
