from bcdebug import debug
###############################################################################
#	Filename:	promMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador promMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDpromugObj = App.CPyDpromug()

###############################################################################
#	CreateCharacter()
#
#	Create promMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDpromugObj.Print("Creating promMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("promMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodypromMaleM/BodypromMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	ppromMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodypromMaleM/BodypromMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	ppromMaleExtra1.ReplacpromodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodypromMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/promMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(ppromMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromMaleExtra1)

	# Setup the character configuration
	ppromMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	ppromMaleExtra1.SetGender(App.CharacterClass.MALE)
	ppromMaleExtra1.SetRandomAnimationChance(.75)
	ppromMaleExtra1.SetBlinkChance(0.1)
	ppromMaleExtra1.SetCharacterName("MaleExtra1")

	ppromMaleExtra1.SetHidden(1)

	# Load promMaleExtra1's generic sounds
	LoadSounds()

	# Create promMaleExtra1's menus
	#import promMaleExtra1MenuHandlers
	#promMaleExtra1MenuHandlers.CreateMenus(ppromMaleExtra1)

	ppromMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(ppromMaleExtra1.GetDatabase(), "promMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDpromugObj.Print("Finished creating promMaleExtra1")
	return ppromMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	ppromMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(ppromMaleExtra1):
#	kDpromugObj.Print("Configuring promMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	ppromMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY promMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(ppromMaleExtra1)

	ppromMaleExtra1.SetAsExtra(1)
	ppromMaleExtra1.SetHidden(1)

	ppromMaleExtra1.SetLocation("DBL2M")
#	kDpromugObj.Print("Finished configuring promMaleExtra1")


###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	ppromMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the prometheus bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForprometheus")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("promL2MToG", "Bridge.Characters.promMediumAnimations.promL2ToG1")
	pMaleExtra1.AddAnimation("promG1MToL", "Bridge.Characters.promMediumAnimations.promG1ToL2")
	pMaleExtra1.AddAnimation("StandingpromG1M", "Bridge.Characters.CommonAnimations.Standing")
	pMaleExtra1.SetStanding(1)

	# Hit animations
	pMaleExtra1.AddAnimation("promG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pMaleExtra1.AddAnimation("promG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pMaleExtra1.AddAnimation("promG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("promG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("promL2M")
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
#	Args:	ppromMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromMaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	ppromMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# promMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
