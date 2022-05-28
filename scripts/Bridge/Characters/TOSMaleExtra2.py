###############################################################################
#	Filename:	TOSMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador TOSMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDTOSug()

###############################################################################
#	CreateCharacter()
#
#	Create TOSMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating TOSMaleExtra2")

	if (pSet.GetObject("TOSMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyTOSMaleM/BodyTOSMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pTOSMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyTOSMaleM/BodyTOSMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pTOSMaleExtra2.ReplacTOSodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyTOSMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/TOSMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSMaleExtra2)

	# Setup the character configuration
	pTOSMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pTOSMaleExtra2.SetGender(App.CharacterClass.Male)
	pTOSMaleExtra2.SetRandomAnimationChance(.75)
	pTOSMaleExtra2.SetBlinkChance(0.1)
	pTOSMaleExtra2.SetCharacterName("MaleExtra2")

	pTOSMaleExtra2.SetHidden(1)

	# Load TOSMaleExtra2's generic sounds
	LoadSounds()

	# Create TOSMaleExtra2's menus
	#import TOSMaleExtra2MenuHandlers
	#TOSMaleExtra2MenuHandlers.CreateMenus(pTOSMaleExtra2)

	pTOSMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pTOSMaleExtra2.GetDatabase(), "TOSMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating TOSMaleExtra2")
	return pTOSMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pTOSMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pTOSMaleExtra2):
#	kDebugObj.Print("Configuring TOSMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pTOSMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY TOSMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pTOSMaleExtra2)

	pTOSMaleExtra2.SetAsExtra(1)
	pTOSMaleExtra2.SetHidden(1)

	pTOSMaleExtra2.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring TOSMaleExtra2")

###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pMaleExtra2):
#	kDebugObj.Print("Configuring TOSMaleExtra2 for the Constitution bridge")

	# Clear out any old animations from another configuration
	pMaleExtra2.ClearAnimations()

	# Register animation mappings
#	pMaleExtra2.AddAnimation("TOSL2MToG", "Bridge.Characters.TOSMediumAnimations.TOSL2ToG1")
#	pMaleExtra2.AddAnimation("TOSG1MToL", "Bridge.Characters.TOSMediumAnimations.TOSG1ToL2")
	pMaleExtra2.AddAnimation("StandingTOSG1M", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pMaleExtra2.SetStanding(1)

	# Hit animations
	#pMaleExtra2.AddAnimation("TOSG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pMaleExtra2.AddAnimation("TOSG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pMaleExtra2.AddAnimation("TOSG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pMaleExtra2.AddAnimation("TOSG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pMaleExtra2.AddAnimation("TOSG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pMaleExtra2.SetAsExtra(1)
	pMaleExtra2.SetHidden(0)
	pMaleExtra2.SetStanding(0)

	# Add common animations.
	AddCommonAnimations(pMaleExtra2)

	pMaleExtra2.SetLocation("TOSL4M")
#	kDebugObj.Print("Finished configuring TOSMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSMaleExtra2):
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pTOSMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# TOSMaleExtra2 has no generic bridge sounds at this time
	#
	pass
