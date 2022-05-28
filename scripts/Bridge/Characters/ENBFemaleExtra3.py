from bcdebug import debug
###############################################################################
#	Filename:	ENBFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENBFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create ENBFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating ENBFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENBFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pENBFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	pENBFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedfemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/ENBFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENBFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBFemaleExtra3)

	# Setup the character configuration
	pENBFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pENBFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pENBFemaleExtra3.SetRandomAnimationChance(.75)
	pENBFemaleExtra3.SetBlinkChance(0.1)
	pENBFemaleExtra3.SetCharacterName("FemaleExtra3")

	pENBFemaleExtra3.SetHidden(1)

	# Load ENBFemaleExtra3's generic sounds
	LoadSounds()

	# Create ENBFemaleExtra3's menus
	#import ENBFemaleExtra3MenuHandlers
	#ENBFemaleExtra3MenuHandlers.CreateMenus(pENBFemaleExtra3)

	pENBFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENBFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENBFemaleExtra3.SetLocation("")

#	kDebugObj.Print("Finished creating ENBFemaleExtra3")
	return pENBFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENBFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENBFemaleExtra3):
#	kDebugObj.Print("Configuring ENBFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENBFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY ENBFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENBFemaleExtra3)

	pENBFemaleExtra3.SetAsExtra(1)
	pENBFemaleExtra3.SetHidden(1)

	pENBFemaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring ENBFemaleExtra3")

###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pENBMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseB")
	pENBMaleExtra3.ClearAnimations()

	# Register animation mappings
	pENBMaleExtra3.AddAnimation("ENBL1MToG", "Bridge.Characters.ENBMediumAnimations.ENBL1ToG3")
	pENBMaleExtra3.AddAnimation("ENBG3MToL", "Bridge.Characters.ENBMediumAnimations.ENBG3ToL1")
	pENBMaleExtra3.AddAnimation("StandingENBG3M", "Bridge.Characters.CommonAnimations.Standing")
	pENBMaleExtra3.SetStanding(1)

	# Hit animations
	pENBMaleExtra3.AddAnimation("ENBG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENBMaleExtra3.AddAnimation("ENBG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENBMaleExtra3.AddAnimation("ENBG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENBMaleExtra3.AddAnimation("ENBG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pENBMaleExtra3.AddAnimation("ENBG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pENBMaleExtra3.SetAsExtra(1)
	pENBMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pENBMaleExtra3)

	pENBMaleExtra3.SetLocation("ENBL1M")
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
#	Args:	pENBFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
#########
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
	# ENBFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
