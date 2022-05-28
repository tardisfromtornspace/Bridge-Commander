###############################################################################
#	Filename:	TOSMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador TOSMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create TOSMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating TOSMaleExtra1")

	if (pSet.GetObject("TOSMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyTOSMaleM/BodyTOSMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pTOSMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyTOSMaleM/BodyTOSMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pTOSMaleExtra1.ReplacTOSodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyTOSMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/TOSMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSMaleExtra1)

	# Setup the character configuration
	pTOSMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pTOSMaleExtra1.SetGender(App.CharacterClass.Male)
	pTOSMaleExtra1.SetRandomAnimationChance(.75)
	pTOSMaleExtra1.SetBlinkChance(0.1)
	pTOSMaleExtra1.SetCharacterName("MaleExtra1")

	pTOSMaleExtra1.SetHidden(1)

	# Load TOSMaleExtra1's generic sounds
	LoadSounds()

	# Create TOSMaleExtra1's menus
	#import TOSMaleExtra1MenuHandlers
	#TOSMaleExtra1MenuHandlers.CreateMenus(pTOSMaleExtra1)

	pTOSMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pTOSMaleExtra1.GetDatabase(), "TOSMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating TOSMaleExtra1")
	return pTOSMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pTOSMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pTOSMaleExtra1):
#	kDebugObj.Print("Configuring TOSMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pTOSMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY TOSMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pTOSMaleExtra1)

	pTOSMaleExtra1.SetAsExtra(1)
	pTOSMaleExtra1.SetHidden(1)

	pTOSMaleExtra1.SetLocation("DBL2M")
#	kDebugObj.Print("Finished configuring TOSMaleExtra1")


###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pTOSMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pMaleExtra1):
#	kDebugObj.Print("Configuring TOSMaleExtra1 for the Constitution bridge")

	# Clear out any old animations from another configuration
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
#	pMaleExtra1.AddAnimation("TOSL2MToG", "Bridge.Characters.TOSMediumAnimations.TOSL2ToG1")
#	pMaleExtra1.AddAnimation("TOSG1MToL", "Bridge.Characters.TOSMediumAnimations.TOSG1ToL2")
	pMaleExtra1.AddAnimation("StandingTOSG1M", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pMaleExtra1.SetStanding(1)

	# Hit animations
	#pMaleExtra1.AddAnimation("TOSG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pMaleExtra1.AddAnimation("TOSG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pMaleExtra1.AddAnimation("TOSG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pMaleExtra1.AddAnimation("TOSG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pMaleExtra1.AddAnimation("TOSG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(0)
	pMaleExtra1.SetStanding(0)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("TOSL3M")
#	kDebugObj.Print("Finished configuring TOSMaleExtra1")

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSMaleExtra1):
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pTOSMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# TOSMaleExtra1 has no generic bridge sounds at this time
	#
	pass
