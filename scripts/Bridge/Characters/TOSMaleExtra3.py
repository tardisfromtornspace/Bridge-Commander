###############################################################################
#	Filename:	TOSMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador TOSMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDebugObj = App.CPyDDebug()

###############################################################################
#	CreateCharacter()
#
#	Create TOSMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDDebugObj.Print("Creating TOSMaleExtra3")

	if (pSet.GetObject("TOSMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyTOSMaleM/BodyTOSMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pTOSMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyTOSMaleM/BodyTOSMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pTOSMaleExtra3.ReplacTOSodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyTOSMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/TOSMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSMaleExtra3)

	# Setup the character configuration
	pTOSMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pTOSMaleExtra3.SetGender(App.CharacterClass.Male)
	pTOSMaleExtra3.SetRandomAnimationChance(.75)
	pTOSMaleExtra3.SetBlinkChance(0.1)
	pTOSMaleExtra3.SetCharacterName("MaleExtra3")

	pTOSMaleExtra3.SetHidden(1)

	# Load TOSMaleExtra3's generic sounds
	LoadSounds()

	# Create TOSMaleExtra3's menus
	#import TOSMaleExtra3MenuHandlers
	#TOSMaleExtra3MenuHandlers.CreateMenus(pTOSMaleExtra3)

	pTOSMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pTOSMaleExtra3.GetDatabase(), "TOSMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDDebugObj.Print("Finished creating TOSMaleExtra3")
	return pTOSMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pTOSMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pTOSMaleExtra3):
#	kDDebugObj.Print("Configuring TOSMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pTOSMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY TOSMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pTOSMaleExtra3)

	pTOSMaleExtra3.SetAsExtra(1)
	pTOSMaleExtra3.SetHidden(1)

	pTOSMaleExtra3.SetLocation("DBL2M")
#	kDDebugObj.Print("Finished configuring TOSMaleExtra3")


###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pTOSMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pTOSMaleExtra3):
#	kDDebugObj.Print("Configuring TOSMaleExtra3 for the Constitution bridge")

	# Clear out any old animations from another configuration
	pTOSMaleExtra3.ClearAnimations()

	# Register animation mappings
	pTOSMaleExtra3.AddAnimation("TOSL2MToG", "Bridge.Characters.TOSMediumAnimations.TOSL2ToG2")
	pTOSMaleExtra3.AddAnimation("TOSG2MToL", "Bridge.Characters.TOSMediumAnimations.TOSG2ToL2")
	pTOSMaleExtra3.AddAnimation("StandingTOSG2M", "Bridge.Characters.CommonAnimations.Standing")
	pTOSMaleExtra3.SetStanding(1)

	# Hit animations
	pTOSMaleExtra3.AddAnimation("TOSG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pTOSMaleExtra3.AddAnimation("TOSG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pTOSMaleExtra3.AddAnimation("TOSG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pTOSMaleExtra3.AddAnimation("TOSG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pTOSMaleExtra3.AddAnimation("TOSG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pTOSMaleExtra3.SetAsExtra(1)
	pTOSMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pTOSMaleExtra3)

	pTOSMaleExtra3.SetLocation("TOSL2M")
#	kDDebugObj.Print("Finished configuring TOSMaleExtra3")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSMaleExtra3):
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pTOSMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# TOSMaleExtra3 has no generic bridge sounds at this time
	#
	pass
