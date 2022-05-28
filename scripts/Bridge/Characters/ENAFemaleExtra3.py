from bcdebug import debug
###############################################################################
#	Filename:	ENAFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENAFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDENAugObj = App.CPyDENAug()

###############################################################################
#	CreateCharacter()
#
#	Create ENAFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDENAugObj.Print("Creating ENAFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENAFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pENAFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	pENAFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeENAemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/ENAFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENAFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAFemaleExtra3)

	# Setup the character configuration
	pENAFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pENAFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pENAFemaleExtra3.SetRandomAnimationChance(.75)
	pENAFemaleExtra3.SetBlinkChance(0.1)
	pENAFemaleExtra3.SetCharacterName("FemaleExtra3")

	pENAFemaleExtra3.SetHidden(1)

	# Load ENAFemaleExtra3's generic sounds
	LoadSounds()

	# Create ENAFemaleExtra3's menus
	#import ENAFemaleExtra3MenuHandlers
	#ENAFemaleExtra3MenuHandlers.CreateMenus(pENAFemaleExtra3)

	pENAFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENAFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENAFemaleExtra3.SetLocation("")

#	kDENAugObj.Print("Finished creating ENAFemaleExtra3")
	return pENAFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENAFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENAFemaleExtra3):
#	kDENAugObj.Print("Configuring ENAFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENAFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY ENAFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENAFemaleExtra3)

	pENAFemaleExtra3.SetAsExtra(1)
	pENAFemaleExtra3.SetHidden(1)

	pENAFemaleExtra3.SetLocation("DBL1M")
#	kDENAugObj.Print("Finished configuring ENAFemaleExtra3")

###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pENAMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseA")
	pENAMaleExtra3.ClearAnimations()

	# Register animation mappings
	pENAMaleExtra3.AddAnimation("ENAL1MToG", "Bridge.Characters.ENAMediumAnimations.ENAL1ToG3")
	pENAMaleExtra3.AddAnimation("ENAG3MToL", "Bridge.Characters.ENAMediumAnimations.ENAG3ToL1")
	pENAMaleExtra3.AddAnimation("StandingENAG3M", "Bridge.Characters.CommonAnimations.Standing")
	pENAMaleExtra3.SetStanding(1)

	# Hit animations
	pENAMaleExtra3.AddAnimation("ENAG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENAMaleExtra3.AddAnimation("ENAG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENAMaleExtra3.AddAnimation("ENAG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENAMaleExtra3.AddAnimation("ENAG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pENAMaleExtra3.AddAnimation("ENAG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pENAMaleExtra3.SetAsExtra(1)
	pENAMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pENAMaleExtra3)

	pENAMaleExtra3.SetLocation("ENAL1M")
#	kDebugObj.Print("Finished configuring MaleExtra3")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENAFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENAFemaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pENAFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# ENAFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
