from bcdebug import debug
###############################################################################
#	Filename:	ENBMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENBMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create ENBMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating ENBMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENBMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyENBMaleM/BodyENBMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pENBMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyENBMaleM/BodyENBMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pENBMaleExtra3.ReplacebodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyENBMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/ENBMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENBMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBMaleExtra3)

	# Setup the character configuration
	pENBMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pENBMaleExtra3.SetGender(App.CharacterClass.MALE)
	pENBMaleExtra3.SetRandomAnimationChance(.75)
	pENBMaleExtra3.SetBlinkChance(0.1)
	pENBMaleExtra3.SetCharacterName("MaleExtra3")

	pENBMaleExtra3.SetHidden(1)

	# Load ENBMaleExtra3's generic sounds
	LoadSounds()

	# Create ENBMaleExtra3's menus
	#import ENBMaleExtra3MenuHandlers
	#ENBMaleExtra3MenuHandlers.CreateMenus(pENBMaleExtra3)

	pENBMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pENBMaleExtra3.GetDatabase(), "ENBMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating ENBMaleExtra3")
	return pENBMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENBMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENBMaleExtra3):
#	kDebugObj.Print("Configuring ENBMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENBMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY ENBMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENBMaleExtra3)

	pENBMaleExtra3.SetAsExtra(1)
	pENBMaleExtra3.SetHidden(1)

	pENBMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring ENBMaleExtra3")

###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pENBMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseB")
	pENBMaleExtra3.ClearAnimations()

	# Register animation mappings
	pENBMaleExtra3.AddAnimation("ENBL1MToG", "Bridge.Characters.ENBMediumAnimations.ENBL1ToG3")
	pENBMaleExtra3.AddAnimation("ENBG3MToL", "Bridge.Characters.ENBMediumAnimations.ENBG3ToL1")
	pENBMaleExtra3.AddAnimation("StandingENBG3M", "Bridge.Characters.CommonAnimations.Standing")
	pENBMaleExtra3.SetStanding(1)

	# Hit animations
	pENBMaleExtra3.AddAnimation("ENBG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENBMaleExtra3.AddAnimation("ENBG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENBMaleExtra3.AddAnimation("ENBG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENBMaleExtra3.AddAnimation("ENBG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pENBMaleExtra3.AddAnimation("ENBG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pENBMaleExtra3.SetAsExtra(1)
	pENBMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pENBMaleExtra3)

	pENBMaleExtra3.SetLocation("ENBL1M")
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
#	Args:	pENBMaleExtra3	- our Character object
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
	# ENBMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
