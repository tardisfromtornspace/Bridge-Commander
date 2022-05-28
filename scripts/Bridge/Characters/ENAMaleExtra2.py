from bcdebug import debug
###############################################################################
#	Filename:	ENAMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENAMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDENAugObj = App.CPyDENAug()

###############################################################################
#	CreateCharacter()
#
#	Create ENAMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDENAugObj.Print("Creating ENAMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENAMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyENAMaleM/BodyENAMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pENAMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyENAMaleM/BodyENAMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pENAMaleExtra2.ReplacENAodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyENAMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/ENAMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENAMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAMaleExtra2)

	# Setup the character configuration
	pENAMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pENAMaleExtra2.SetGender(App.CharacterClass.MALE)
	pENAMaleExtra2.SetRandomAnimationChance(.75)
	pENAMaleExtra2.SetBlinkChance(0.1)
	pENAMaleExtra2.SetCharacterName("MaleExtra2")

	pENAMaleExtra2.SetHidden(1)

	# Load ENAMaleExtra2's generic sounds
	LoadSounds()

	# Create ENAMaleExtra2's menus
	#import ENAMaleExtra2MenuHandlers
	#ENAMaleExtra2MenuHandlers.CreateMenus(pENAMaleExtra2)

	pENAMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pENAMaleExtra2.GetDatabase(), "ENAMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDENAugObj.Print("Finished creating ENAMaleExtra2")
	return pENAMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENAMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENAMaleExtra2):
#	kDENAugObj.Print("Configuring ENAMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENAMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY ENAMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENAMaleExtra2)

	pENAMaleExtra2.SetAsExtra(1)
	pENAMaleExtra2.SetHidden(1)

	pENAMaleExtra2.SetLocation("DBL2M")
#	kDENAugObj.Print("Finished configuring ENAMaleExtra2")


###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pENAMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pENAMaleExtra2):
#	kDENAugObj.Print("Configuring ENAMaleExtra2 for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseA")
	pENAMaleExtra2.ClearAnimations()

	# Register animation mappings
	pENAMaleExtra2.AddAnimation("ENAL2MToG", "Bridge.Characters.ENAMediumAnimations.ENAL2ToG2")
	pENAMaleExtra2.AddAnimation("ENAG2MToL", "Bridge.Characters.ENAMediumAnimations.ENAG2ToL2")
	pENAMaleExtra2.AddAnimation("StandingENAG2M", "Bridge.Characters.CommonAnimations.Standing")
	pENAMaleExtra2.SetStanding(1)

	# Hit animations
	pENAMaleExtra2.AddAnimation("ENAG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENAMaleExtra2.AddAnimation("ENAG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENAMaleExtra2.AddAnimation("ENAG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENAMaleExtra2.AddAnimation("ENAG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pENAMaleExtra2.AddAnimation("ENAG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pENAMaleExtra2.SetAsExtra(1)
	pENAMaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pENAMaleExtra2)

	pENAMaleExtra2.SetLocation("ENAL2M")
#	kDENAugObj.Print("Finished configuring ENAMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENAMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENAMaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pENAMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# ENAMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
