###############################################################################
#	Filename:	TOSFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador TOSFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create TOSFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating TOSFemaleExtra1")

	if (pSet.GetObject("TOSFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeaTOSem3/fem3_head.nif", None)
	pTOSFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeaTOSem3/fem3_head.nif")

	pTOSFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeTOSemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeaTOSem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSFemaleExtra1)

	# Setup the character configuration
	pTOSFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pTOSFemaleExtra1.SetGender(App.CharacterClass.Female)
	pTOSFemaleExtra1.SetRandomAnimationChance(.75)
	pTOSFemaleExtra1.SetBlinkChance(0.1)
	pTOSFemaleExtra1.SetCharacterName("FemaleExtra1")

	pTOSFemaleExtra1.SetHidden(1)

	# Load TOSFemaleExtra1's generic sounds
	LoadSounds()

	# Create TOSFemaleExtra1's menus
	#import TOSFemaleExtra1MenuHandlers
	#TOSFemaleExtra1MenuHandlers.CreateMenus(pTOSFemaleExtra1)

	pTOSFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pTOSFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pTOSFemaleExtra1.SetLocation("")

#	kDebugObj.Print("Finished creating TOSFemaleExtra1")
	return pTOSFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pTOSFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pTOSFemaleExtra1):
#	kDebugObj.Print("Configuring TOSFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pTOSFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY TOSFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pTOSFemaleExtra1)

	pTOSFemaleExtra1.SetAsExtra(1)
	pTOSFemaleExtra1.SetHidden(1)

	pTOSFemaleExtra1.SetLocation("DBL2M")
#	kDebugObj.Print("Finished configuring TOSFemaleExtra1")

###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pTOSFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pFemaleExtra1):
#	kDebugObj.Print("Configuring TOSFemaleExtra1 for the Constitution bridge")

	# Clear out any old animations from another configuration
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
#	pFemaleExtra1.AddAnimation("TOSL2MToG", "Bridge.Characters.TOSMediumAnimations.TOSL2ToG1")
#	pFemaleExtra1.AddAnimation("TOSG1MToL", "Bridge.Characters.TOSMediumAnimations.TOSG1ToL2")
	pFemaleExtra1.AddAnimation("StandingTOSG1M", "Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
	pFemaleExtra1.SetStanding(1)

	# Hit animations
	#pFemaleExtra1.AddAnimation("TOSG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pFemaleExtra1.AddAnimation("TOSG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pFemaleExtra1.AddAnimation("TOSG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pFemaleExtra1.AddAnimation("TOSG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pFemaleExtra1.AddAnimation("TOSG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(0)
	pFemaleExtra1.SetStanding(0)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("TOSL3M")
#	kDebugObj.Print("Finished configuring TOSFemaleExtra1")

###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSFemaleExtra1):
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.TOSMediumAnimations.TOS_seated_interaction")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pTOSFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# TOSFemaleExtra1 has no generic bridge sounds at this time
	#
	pass
