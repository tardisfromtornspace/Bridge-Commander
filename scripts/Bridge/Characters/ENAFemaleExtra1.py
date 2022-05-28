from bcdebug import debug
###############################################################################
#	Filename:	ENAFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENAFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDENAugObj = App.CPyDENAug()

###############################################################################
#	CreateCharacter()
#
#	Create ENAFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDENAugObj.Print("Creating ENAFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENAFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeaENAem3/fem3_head.nif", None)
	pENAFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	pENAFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeENAemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENAFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAFemaleExtra1)

	# Setup the character configuration
	pENAFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pENAFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pENAFemaleExtra1.SetRandomAnimationChance(.75)
	pENAFemaleExtra1.SetBlinkChance(0.1)
	pENAFemaleExtra1.SetCharacterName("FemaleExtra1")

	pENAFemaleExtra1.SetHidden(1)

	# Load ENAFemaleExtra1's generic sounds
	LoadSounds()

	# Create ENAFemaleExtra1's menus
	#import ENAFemaleExtra1MenuHandlers
	#ENAFemaleExtra1MenuHandlers.CreateMenus(pENAFemaleExtra1)

	pENAFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENAFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENAFemaleExtra1.SetLocation("")

#	kDENAugObj.Print("Finished creating ENAFemaleExtra1")
	return pENAFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENAFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENAFemaleExtra1):
#	kDENAugObj.Print("Configuring ENAFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENAFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY ENAFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENAFemaleExtra1)

	pENAFemaleExtra1.SetAsExtra(1)
	pENAFemaleExtra1.SetHidden(1)

	pENAFemaleExtra1.SetLocation("DBL2M")
#	kDENAugObj.Print("Finished configuring ENAFemaleExtra1")

###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pENAFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pFemaleExtra1):
#	kDENAugObj.Print("Configuring ENAFemaleExtra1 for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseA")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("ENAL2MToG", "Bridge.Characters.ENAMediumAnimations.ENAL2ToG1")
	pFemaleExtra1.AddAnimation("ENAG1MToL", "Bridge.Characters.ENAMediumAnimations.ENAG1ToL2")
	pFemaleExtra1.AddAnimation("StandingENAG1M", "Bridge.Characters.CommonAnimations.Standing")
	pFemaleExtra1.SetStanding(1)

	# Hit animations
	pFemaleExtra1.AddAnimation("ENAG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pFemaleExtra1.AddAnimation("ENAG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pFemaleExtra1.AddAnimation("ENAG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("ENAG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pFemaleExtra1.AddAnimation("ENAG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("ENAL2M")
#	kDENAugObj.Print("Finished configuring ENAFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENAFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENAFemaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pENAFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# ENAFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
