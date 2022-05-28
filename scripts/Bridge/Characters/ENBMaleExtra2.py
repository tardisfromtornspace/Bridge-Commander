from bcdebug import debug
###############################################################################
#	Filename:	ENBMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENBMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create ENBMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating ENBMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENBMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyENBMaleM/BodyENBMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pENBMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyENBMaleM/BodyENBMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pENBMaleExtra2.ReplacebodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyENBMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/ENBMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENBMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBMaleExtra2)

	# Setup the character configuration
	pENBMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pENBMaleExtra2.SetGender(App.CharacterClass.MALE)
	pENBMaleExtra2.SetRandomAnimationChance(.75)
	pENBMaleExtra2.SetBlinkChance(0.1)
	pENBMaleExtra2.SetCharacterName("MaleExtra2")

	pENBMaleExtra2.SetHidden(0)

	# Load ENBMaleExtra2's generic sounds
	LoadSounds()

	# Create ENBMaleExtra2's menus
	#import ENBMaleExtra2MenuHandlers
	#ENBMaleExtra2MenuHandlers.CreateMenus(pENBMaleExtra2)

	pENBMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pENBMaleExtra2.GetDatabase(), "ENBMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating ENBMaleExtra2")
	return pENBMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENBMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENBMaleExtra2):
#	kDebugObj.Print("Configuring ENBMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENBMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY ENBMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENBMaleExtra2)

	pENBMaleExtra2.SetAsExtra(1)
	pENBMaleExtra2.SetHidden(0)

	pENBMaleExtra2.SetLocation("DBL2M")
#	kDebugObj.Print("Finished configuring ENBMaleExtra2")


###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pENBMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pENBMaleExtra2):
#	kDebugObj.Print("Configuring ENBMaleExtra2 for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseB")
	pENBMaleExtra2.ClearAnimations()

	# Register animation mappings
	pENBMaleExtra2.AddAnimation("ENBL2MToG", "Bridge.Characters.ENBMediumAnimations.ENBL2ToG2")
	pENBMaleExtra2.AddAnimation("ENBG2MToL", "Bridge.Characters.ENBMediumAnimations.ENBG2ToL2")
	pENBMaleExtra2.AddAnimation("SeatedENBG2M", "Bridge.Characters.CommonAnimations.SeatedM")
	pENBMaleExtra2.SetStanding(0)

	# Hit animations
	pENBMaleExtra2.AddAnimation("ENBG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENBMaleExtra2.AddAnimation("ENBG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pENBMaleExtra2.SetAsExtra(1)
	pENBMaleExtra2.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pENBMaleExtra2)

	pENBMaleExtra2.SetLocation("ENBL2M")
#	kDebugObj.Print("Finished configuring ENBMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENBMaleExtra2	- our Character object
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
	# ENBMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass

