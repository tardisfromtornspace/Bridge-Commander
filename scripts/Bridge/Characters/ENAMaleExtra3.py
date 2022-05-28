from bcdebug import debug
###############################################################################
#	Filename:	ENAMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENAMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDENAug()

###############################################################################
#	CreateCharacter()
#
#	Create ENAMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating ENAMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENAMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyENAMaleM/BodyENAMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pENAMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyENAMaleM/BodyENAMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pENAMaleExtra3.ReplacENAodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyENAMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/ENAMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENAMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAMaleExtra3)

	# Setup the character configuration
	pENAMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pENAMaleExtra3.SetGender(App.CharacterClass.MALE)
	pENAMaleExtra3.SetRandomAnimationChance(.75)
	pENAMaleExtra3.SetBlinkChance(0.1)
	pENAMaleExtra3.SetCharacterName("MaleExtra3")

	pENAMaleExtra3.SetHidden(1)

	# Load ENAMaleExtra3's generic sounds
	LoadSounds()

	# Create ENAMaleExtra3's menus
	#import ENAMaleExtra3MenuHandlers
	#ENAMaleExtra3MenuHandlers.CreateMenus(pENAMaleExtra3)

	pENAMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pENAMaleExtra3.GetDatabase(), "ENAMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating ENAMaleExtra3")
	return pENAMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENAMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENAMaleExtra3):
#	kDebugObj.Print("Configuring ENAMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENAMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY ENAMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENAMaleExtra3)

	pENAMaleExtra3.SetAsExtra(1)
	pENAMaleExtra3.SetHidden(1)

	pENAMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring ENAMaleExtra3")

###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pENAMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseA")
	pENAMaleExtra3.ClearAnimations()

	# Register animation mappings
	pENAMaleExtra3.AddAnimation("ENAL1MToG", "Bridge.Characters.ENAMediumAnimations.ENAL1ToG3")
	pENAMaleExtra3.AddAnimation("ENAG3MToL", "Bridge.Characters.ENAMediumAnimations.ENAG3ToL1")
	pENAMaleExtra3.AddAnimation("StandingENAG3M", "Bridge.Characters.CommonAnimations.Standing")
	pENAMaleExtra3.SetStanding(1)

	# Hit animations
	pENAMaleExtra3.AddAnimation("ENAG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENAMaleExtra3.AddAnimation("ENAG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENAMaleExtra3.AddAnimation("ENAG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENAMaleExtra3.AddAnimation("ENAG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pENAMaleExtra3.AddAnimation("ENAG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pENAMaleExtra3.SetAsExtra(1)
	pENAMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pENAMaleExtra3)

	pENAMaleExtra3.SetLocation("ENAL1M")
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
#	Args:	pENAMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENAMaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pENAMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# ENAMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
