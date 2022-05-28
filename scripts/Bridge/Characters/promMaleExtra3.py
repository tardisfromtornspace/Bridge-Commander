from bcdebug import debug
###############################################################################
#	Filename:	promMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador promMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDpromug()

###############################################################################
#	CreateCharacter()
#
#	Create promMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating promMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("promMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodypromMaleM/BodypromMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	ppromMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodypromMaleM/BodypromMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	ppromMaleExtra3.ReplacpromodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodypromMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/promMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(ppromMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromMaleExtra3)

	# Setup the character configuration
	ppromMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	ppromMaleExtra3.SetGender(App.CharacterClass.MALE)
	ppromMaleExtra3.SetRandomAnimationChance(.75)
	ppromMaleExtra3.SetBlinkChance(0.1)
	ppromMaleExtra3.SetCharacterName("MaleExtra3")

	ppromMaleExtra3.SetHidden(1)

	# Load promMaleExtra3's generic sounds
	LoadSounds()

	# Create promMaleExtra3's menus
	#import promMaleExtra3MenuHandlers
	#promMaleExtra3MenuHandlers.CreateMenus(ppromMaleExtra3)

	ppromMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(ppromMaleExtra3.GetDatabase(), "promMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating promMaleExtra3")
	return ppromMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	ppromMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(ppromMaleExtra3):
#	kDebugObj.Print("Configuring promMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	ppromMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY promMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(ppromMaleExtra3)

	ppromMaleExtra3.SetAsExtra(1)
	ppromMaleExtra3.SetHidden(1)

	ppromMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring promMaleExtra3")

###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(ppromMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the prometheus bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForprometheus")
	ppromMaleExtra3.ClearAnimations()

	# Register animation mappings
	ppromMaleExtra3.AddAnimation("promL1MToG", "Bridge.Characters.promMediumAnimations.promL1ToG3")
	ppromMaleExtra3.AddAnimation("promG3MToL", "Bridge.Characters.promMediumAnimations.promG3ToL1")
	ppromMaleExtra3.AddAnimation("StandingpromG3M", "Bridge.Characters.CommonAnimations.Standing")
	ppromMaleExtra3.SetStanding(1)

	# Hit animations
	ppromMaleExtra3.AddAnimation("promG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	ppromMaleExtra3.AddAnimation("promG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	ppromMaleExtra3.AddAnimation("promG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	ppromMaleExtra3.AddAnimation("promG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	ppromMaleExtra3.AddAnimation("promG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	ppromMaleExtra3.SetAsExtra(1)
	ppromMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(ppromMaleExtra3)

	ppromMaleExtra3.SetLocation("promL1M")
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
#	Args:	ppromMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromMaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	#ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	#ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	#ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	#ppromMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# promMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
