###############################################################################
#	Filename:	TOSFemaleExtra4.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador TOSFemaleExtra4, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create TOSFemaleExtra4 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating TOSFemaleExtra4")

	if (pSet.GetObject("TOSFemaleExtra4") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra4")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pTOSFemaleExtra4 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeaTOSem4/fem4_head.nif")

	pTOSFemaleExtra4.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeTOSemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeaTOSem4/TOSFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSFemaleExtra4, "FemaleExtra4")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSFemaleExtra4)

	# Setup the character configuration
	pTOSFemaleExtra4.SetSize(App.CharacterClass.MEDIUM)
	pTOSFemaleExtra4.SetGender(App.CharacterClass.Female)
	pTOSFemaleExtra4.SetRandomAnimationChance(.75)
	pTOSFemaleExtra4.SetBlinkChance(0.1)
	pTOSFemaleExtra4.SetCharacterName("FemaleExtra4")

	pTOSFemaleExtra4.SetHidden(1)

	# Load TOSFemaleExtra4's generic sounds
	LoadSounds()

	# Create TOSFemaleExtra4's menus
	#import TOSFemaleExtra4MenuHandlers
	#TOSFemaleExtra4MenuHandlers.CreateMenus(pTOSFemaleExtra4)

	pTOSFemaleExtra4.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pTOSFemaleExtra4.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pTOSFemaleExtra4.SetLocation("")

#	kDebugObj.Print("Finished creating TOSFemaleExtra4")
	return pTOSFemaleExtra4

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pTOSFemaleExtra4	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pTOSFemaleExtra4):
#	kDebugObj.Print("Configuring TOSFemaleExtra4 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pTOSFemaleExtra4.ClearAnimations()

	#
	# *** CURRENTLY TOSFemaleExtra4 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pTOSFemaleExtra4)

	pTOSFemaleExtra4.SetAsExtra(1)
	pTOSFemaleExtra4.SetHidden(1)

	pTOSFemaleExtra4.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring TOSFemaleExtra4")

###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pMaleExtra4	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pFemaleExtra4):
#	kDebugObj.Print("Configuring TOSFemaleExtra4 for the Constitution bridge")

	# Clear out any old animations from another configuration
	pFemaleExtra4.ClearAnimations()

	# Register animation mappings
#	pFemaleExtra4.AddAnimation("TOSL2MToG", "Bridge.Characters.TOSMediumAnimations.TOSL2ToG1")
#	pFemaleExtra4.AddAnimation("TOSG1MToL", "Bridge.Characters.TOSMediumAnimations.TOSG1ToL2")
	pFemaleExtra4.AddAnimation("StandingTOSG1M", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pFemaleExtra4.SetStanding(1)

	# Hit animations
	#pFemaleExtra4.AddAnimation("TOSG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pFemaleExtra4.AddAnimation("TOSG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pFemaleExtra4.AddAnimation("TOSG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pFemaleExtra4.AddAnimation("TOSG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pFemaleExtra4.AddAnimation("TOSG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra4.SetAsExtra(1)
	pFemaleExtra4.SetHidden(0)
	pFemaleExtra4.SetStanding(0)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra4)

	pFemaleExtra4.SetLocation("TOSL1M")
#	kDebugObj.Print("Finished configuring TOSFemaleExtra4")

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSFemaleExtra4	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSFemaleExtra4):
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pTOSFemaleExtra4.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# TOSFemaleExtra4 has no generic bridge sounds at this time
	#
	pass
