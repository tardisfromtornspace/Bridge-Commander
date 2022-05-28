###############################################################################
#	Filename:	TOSFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador TOSFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create TOSFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating TOSFemaleExtra2")

	if (pSet.GetObject("TOSFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pTOSFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeaTOSem4/fem4_head.nif")

	pTOSFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeTOSemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeaTOSem4/TOSFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSFemaleExtra2)

	# Setup the character configuration
	pTOSFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pTOSFemaleExtra2.SetGender(App.CharacterClass.Female)
	pTOSFemaleExtra2.SetRandomAnimationChance(.75)
	pTOSFemaleExtra2.SetBlinkChance(0.1)
	pTOSFemaleExtra2.SetCharacterName("FemaleExtra2")

	pTOSFemaleExtra2.SetHidden(1)

	# Load TOSFemaleExtra2's generic sounds
	LoadSounds()

	# Create TOSFemaleExtra2's menus
	#import TOSFemaleExtra2MenuHandlers
	#TOSFemaleExtra2MenuHandlers.CreateMenus(pTOSFemaleExtra2)

	pTOSFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pTOSFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pTOSFemaleExtra2.SetLocation("")

#	kDebugObj.Print("Finished creating TOSFemaleExtra2")
	return pTOSFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pTOSFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pTOSFemaleExtra2):
#	kDebugObj.Print("Configuring TOSFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pTOSFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY TOSFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pTOSFemaleExtra2)

	pTOSFemaleExtra2.SetAsExtra(1)
	pTOSFemaleExtra2.SetHidden(1)

	pTOSFemaleExtra2.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring TOSFemaleExtra2")

###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pFemaleExtra2):
#	kDebugObj.Print("Configuring TOSFemaleExtra2 for the Constitution bridge")

	# Clear out any old animations from another configuration
	pFemaleExtra2.ClearAnimations()

	# Register animation mappings
#	pFemaleExtra2.AddAnimation("TOSL2MToG", "Bridge.Characters.TOSMediumAnimations.TOSL2ToG1")
#	pFemaleExtra2.AddAnimation("TOSG1MToL", "Bridge.Characters.TOSMediumAnimations.TOSG1ToL2")
	pFemaleExtra2.AddAnimation("StandingTOSG1M", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pFemaleExtra2.SetStanding(1)

	# Hit animations
	#pFemaleExtra2.AddAnimation("TOSG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pFemaleExtra2.AddAnimation("TOSG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pFemaleExtra2.AddAnimation("TOSG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pFemaleExtra2.AddAnimation("TOSG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pFemaleExtra2.AddAnimation("TOSG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra2.SetAsExtra(1)
	pFemaleExtra2.SetHidden(0)
	pFemaleExtra2.SetStanding(0)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra2)

	pFemaleExtra2.SetLocation("TOSL4M")
#	kDebugObj.Print("Finished configuring TOSFemaleExtra2")

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSFemaleExtra2):
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pTOSFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# TOSFemaleExtra2 has no generic bridge sounds at this time
	#
	pass
