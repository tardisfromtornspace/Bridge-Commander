from bcdebug import debug
###############################################################################
#	Filename:	AmbMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador AmbMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDAmbugObj = App.CPyDAmbug()

###############################################################################
#	CreateCharacter()
#
#	Create AmbMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDAmbugObj.Print("Creating AmbMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("AmbMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyAmbMaleM/BodyAmbMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pAmbMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyAmbMaleM/BodyAmbMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pAmbMaleExtra2.ReplacAmbodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyAmbMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/AmbMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbMaleExtra2)

	# Setup the character configuration
	pAmbMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pAmbMaleExtra2.SetGender(App.CharacterClass.MALE)
	pAmbMaleExtra2.SetRandomAnimationChance(.75)
	pAmbMaleExtra2.SetBlinkChance(0.1)
	pAmbMaleExtra2.SetCharacterName("MaleExtra2")

	pAmbMaleExtra2.SetHidden(1)

	# Load AmbMaleExtra2's generic sounds
	LoadSounds()

	# Create AmbMaleExtra2's menus
	#import AmbMaleExtra2MenuHandlers
	#AmbMaleExtra2MenuHandlers.CreateMenus(pAmbMaleExtra2)

	pAmbMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pAmbMaleExtra2.GetDatabase(), "AmbMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDAmbugObj.Print("Finished creating AmbMaleExtra2")
	return pAmbMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pAmbMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pAmbMaleExtra2):
#	kDAmbugObj.Print("Configuring AmbMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pAmbMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY AmbMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pAmbMaleExtra2)

	pAmbMaleExtra2.SetAsExtra(1)
	pAmbMaleExtra2.SetHidden(1)

	pAmbMaleExtra2.SetLocation("DBL2M")
#	kDAmbugObj.Print("Finished configuring AmbMaleExtra2")


###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pAmbMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pAmbMaleExtra2):
#	kDAmbugObj.Print("Configuring AmbMaleExtra2 for the Ambassador bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForAmbassador")
	pAmbMaleExtra2.ClearAnimations()

	# Register animation mappings
	pAmbMaleExtra2.AddAnimation("AmbL2MToG", "Bridge.Characters.AmbMediumAnimations.AmbL2ToG2")
	pAmbMaleExtra2.AddAnimation("AmbG2MToL", "Bridge.Characters.AmbMediumAnimations.AmbG2ToL2")
	pAmbMaleExtra2.AddAnimation("StandingAmbG2M", "Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")
	pAmbMaleExtra2.SetStanding(1)

	# Hit animations
	pAmbMaleExtra2.AddAnimation("AmbG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pAmbMaleExtra2.AddAnimation("AmbG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pAmbMaleExtra2.AddAnimation("AmbG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pAmbMaleExtra2.AddAnimation("AmbG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pAmbMaleExtra2.AddAnimation("AmbG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pAmbMaleExtra2.SetAsExtra(1)
	pAmbMaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pAmbMaleExtra2)

	pAmbMaleExtra2.SetLocation("AmbL2M")
#	kDAmbugObj.Print("Finished configuring AmbMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pAmbMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbMaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
#	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")
	pAmbMaleExtra2.AddRandomAnimation("Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")


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
	# AmbMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
