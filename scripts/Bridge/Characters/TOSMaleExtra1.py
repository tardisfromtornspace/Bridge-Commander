###############################################################################
#	Filename:	TOSMaleExtra4.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador TOSMaleExtra4, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDTOSug()

###############################################################################
#	CreateCharacter()
#
#	Create TOSMaleExtra4 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating TOSMaleExtra4")

	if (pSet.GetObject("TOSMaleExtra4") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra4")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyTOSMaleM/BodyTOSMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pTOSMaleExtra4 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyTOSMaleM/BodyTOSMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pTOSMaleExtra4.ReplacTOSodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyTOSMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/TOSMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSMaleExtra4, "MaleExtra4")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSMaleExtra4)

	# Setup the character configuration
	pTOSMaleExtra4.SetSize(App.CharacterClass.MEDIUM)
	pTOSMaleExtra4.SetGender(App.CharacterClass.Male)
	pTOSMaleExtra4.SetRandomAnimationChance(.75)
	pTOSMaleExtra4.SetBlinkChance(0.1)
	pTOSMaleExtra4.SetCharacterName("MaleExtra4")

	pTOSMaleExtra4.SetHidden(1)

	# Load TOSMaleExtra4's generic sounds
	LoadSounds()

	# Create TOSMaleExtra4's menus
	#import TOSMaleExtra4MenuHandlers
	#TOSMaleExtra4MenuHandlers.CreateMenus(pTOSMaleExtra4)

	pTOSMaleExtra4.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pTOSMaleExtra4.GetDatabase(), "TOSMaleExtra4NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating TOSMaleExtra4")
	return pTOSMaleExtra4

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pTOSMaleExtra4	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pTOSMaleExtra4):
#	kDebugObj.Print("Configuring TOSMaleExtra4 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pTOSMaleExtra4.ClearAnimations()

	#
	# *** CURRENTLY TOSMaleExtra4 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pTOSMaleExtra4)

	pTOSMaleExtra4.SetAsExtra(1)
	pTOSMaleExtra4.SetHidden(1)

	pTOSMaleExtra4.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring TOSMaleExtra4")

###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pMaleExtra4	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pMaleExtra4):
#	kDebugObj.Print("Configuring TOSMaleExtra4 for the Constitution bridge")

	# Clear out any old animations from another configuration
	pMaleExtra4.ClearAnimations()

	# Register animation mappings
#	pMaleExtra4.AddAnimation("TOSL2MToG", "Bridge.Characters.TOSMediumAnimations.TOSL2ToG1")
#	pMaleExtra4.AddAnimation("TOSG1MToL", "Bridge.Characters.TOSMediumAnimations.TOSG1ToL2")
	pMaleExtra4.AddAnimation("StandingTOSG1M", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pMaleExtra4.SetStanding(1)

	# Hit animations
	#pMaleExtra4.AddAnimation("TOSG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pMaleExtra4.AddAnimation("TOSG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pMaleExtra4.AddAnimation("TOSG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pMaleExtra4.AddAnimation("TOSG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pMaleExtra4.AddAnimation("TOSG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pMaleExtra4.SetAsExtra(1)
	pMaleExtra4.SetHidden(0)
	pMaleExtra4.SetStanding(0)

	# Add common animations.
	AddCommonAnimations(pMaleExtra4)

	pMaleExtra4.SetLocation("TOSL1M")
#	kDebugObj.Print("Finished configuring TOSMaleExtra4")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSMaleExtra4	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSMaleExtra4):
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pTOSMaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# TOSMaleExtra4 has no generic bridge sounds at this time
	#
	pass
