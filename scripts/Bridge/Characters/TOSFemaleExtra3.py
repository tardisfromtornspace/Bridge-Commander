###############################################################################
#	Filename:	TOSFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador TOSFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create TOSFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating TOSFemaleExtra3")

	if (pSet.GetObject("TOSFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pTOSFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pTOSFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeTOSemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/TOSFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pTOSFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pTOSFemaleExtra3)

	# Setup the character configuration
	pTOSFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pTOSFemaleExtra3.SetGender(App.CharacterClass.Female)
	pTOSFemaleExtra3.SetRandomAnimationChance(.75)
	pTOSFemaleExtra3.SetBlinkChance(0.1)
	pTOSFemaleExtra3.SetCharacterName("FemaleExtra3")

	pTOSFemaleExtra3.SetHidden(1)

	# Load TOSFemaleExtra3's generic sounds
	LoadSounds()

	# Create TOSFemaleExtra3's menus
	#import TOSFemaleExtra3MenuHandlers
	#TOSFemaleExtra3MenuHandlers.CreateMenus(pTOSFemaleExtra3)

	pTOSFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pTOSFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pTOSFemaleExtra3.SetLocation("")

#	kDebugObj.Print("Finished creating TOSFemaleExtra3")
	return pTOSFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pTOSFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pTOSFemaleExtra3):
#	kDebugObj.Print("Configuring TOSFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pTOSFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY TOSFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pTOSFemaleExtra3)

	pTOSFemaleExtra3.SetAsExtra(1)
	pTOSFemaleExtra3.SetHidden(1)

	pTOSFemaleExtra3.SetLocation("DBL2M")
#	kDebugObj.Print("Finished configuring TOSFemaleExtra3")


###############################################################################
#	ConfigureForConstitution()
#
#	Configure ourselves for the Constitution bridge
#
#	Args:	pTOSFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForConstitution(pTOSFemaleExtra3):
#	kDebugObj.Print("Configuring TOSFemaleExtra3 for the Constitution bridge")

	# Clear out any old animations from another configuration
	pTOSFemaleExtra3.ClearAnimations()

	# Register animation mappings
	pTOSFemaleExtra3.AddAnimation("TOSL2MToG", "Bridge.Characters.TOSMediumAnimations.TOSL2ToG2")
	pTOSFemaleExtra3.AddAnimation("TOSG2MToL", "Bridge.Characters.TOSMediumAnimations.TOSG2ToL2")
	pTOSFemaleExtra3.AddAnimation("StandingTOSG2M", "Bridge.Characters.CommonAnimations.Standing")
	pTOSFemaleExtra3.SetStanding(1)

	# Hit animations
	pTOSFemaleExtra3.AddAnimation("TOSG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pTOSFemaleExtra3.AddAnimation("TOSG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pTOSFemaleExtra3.AddAnimation("TOSG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pTOSFemaleExtra3.AddAnimation("TOSG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pTOSFemaleExtra3.AddAnimation("TOSG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pTOSFemaleExtra3.SetAsExtra(1)
	pTOSFemaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pTOSFemaleExtra3)

	pTOSFemaleExtra3.SetLocation("TOSL2M")
#	kDebugObj.Print("Finished configuring TOSFemaleExtra3")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pTOSFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pTOSFemaleExtra3):
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pTOSFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# TOSFemaleExtra3 has no generic bridge sounds at this time
	#
	pass
