from bcdebug import debug
###############################################################################
#	Filename:	promMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador promMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDpromugObj = App.CPyDpromug()

###############################################################################
#	CreateCharacter()
#
#	Create promMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDpromugObj.Print("Creating promMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("promMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodypromMaleM/BodypromMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	ppromMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodypromMaleM/BodypromMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	ppromMaleExtra2.ReplacpromodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodypromMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/promMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(ppromMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromMaleExtra2)

	# Setup the character configuration
	ppromMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	ppromMaleExtra2.SetGender(App.CharacterClass.MALE)
	ppromMaleExtra2.SetRandomAnimationChance(.75)
	ppromMaleExtra2.SetBlinkChance(0.1)
	ppromMaleExtra2.SetCharacterName("MaleExtra2")

	ppromMaleExtra2.SetHidden(0)

	# Load promMaleExtra2's generic sounds
	LoadSounds()

	# Create promMaleExtra2's menus
	#import promMaleExtra2MenuHandlers
	#promMaleExtra2MenuHandlers.CreateMenus(ppromMaleExtra2)

	ppromMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(ppromMaleExtra2.GetDatabase(), "promMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDpromugObj.Print("Finished creating promMaleExtra2")
	return ppromMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	ppromMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(ppromMaleExtra2):
#	kDpromugObj.Print("Configuring promMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	ppromMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY promMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(ppromMaleExtra2)

	ppromMaleExtra2.SetAsExtra(1)
	ppromMaleExtra2.SetHidden(0)
	ppromMaleExtra2.SetStanding(0)

	ppromMaleExtra2.SetLocation("DBL2M")
#	kDpromugObj.Print("Finished configuring promMaleExtra2")


###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	ppromMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(ppromMaleExtra2):
#	kDpromugObj.Print("Configuring promMaleExtra2 for the prometheus bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForprometheus")
	ppromMaleExtra2.ClearAnimations()

	# Register animation mappings
	#ppromMaleExtra2.AddAnimation("promL2MToG", "Bridge.Characters.promMediumAnimations.promL2ToG2")
	#ppromMaleExtra2.AddAnimation("promG2MToL", "Bridge.Characters.promMediumAnimations.promG2ToL2")
	#ppromMaleExtra2.AddAnimation("StandingpromG2M", "Bridge.Characters.CommonAnimations.Standing")
	#ppromMaleExtra2.SetStanding(1)

	# Hit animations
	#ppromMaleExtra2.AddAnimation("promG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#ppromMaleExtra2.AddAnimation("promG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#ppromMaleExtra2.AddAnimation("promG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#ppromMaleExtra2.AddAnimation("promG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#ppromMaleExtra2.AddAnimation("promG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	ppromMaleExtra2.SetAsExtra(1)
	ppromMaleExtra2.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(ppromMaleExtra2)

	ppromMaleExtra2.SetLocation("promL3M")
#	kDpromugObj.Print("Finished configuring promMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	ppromMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromMaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.promMediumAnimations.prom_seated_interaction")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	ppromMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# promMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
