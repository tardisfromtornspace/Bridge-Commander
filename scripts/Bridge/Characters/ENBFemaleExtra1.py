from bcdebug import debug
###############################################################################
#	Filename:	ENBFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENBFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create ENBFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating ENBFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENBFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "Headfem3/fem3_head.nif", None)
	pENBFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	pENBFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedfemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENBFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBFemaleExtra1)

	# Setup the character configuration
	pENBFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pENBFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pENBFemaleExtra1.SetRandomAnimationChance(.75)
	pENBFemaleExtra1.SetBlinkChance(0.1)
	pENBFemaleExtra1.SetCharacterName("FemaleExtra1")

	pENBFemaleExtra1.SetHidden(0)

	# Load ENBFemaleExtra1's generic sounds
	LoadSounds()

	# Create ENBFemaleExtra1's menus
	#import ENBFemaleExtra1MenuHandlers
	#ENBFemaleExtra1MenuHandlers.CreateMenus(pENBFemaleExtra1)

	pENBFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENBFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.SeatedM")
	pENBFemaleExtra1.SetLocation("")

#	kDebugObj.Print("Finished creating ENBFemaleExtra1")
	return pENBFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENBFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENBFemaleExtra1):
#	kDebugObj.Print("Configuring ENBFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENBFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY ENBFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENBFemaleExtra1)

	pENBFemaleExtra1.SetAsExtra(1)
	pENBFemaleExtra1.SetHidden(0)

	pENBFemaleExtra1.SetLocation("DBL3M")
#	kDebugObj.Print("Finished configuring ENBFemaleExtra1")

###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pENBFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pFemaleExtra1):
#	kDebugObj.Print("Configuring ENBFemaleExtra1 for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseB")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("ENBL2MToG", "Bridge.Characters.ENBMediumAnimations.ENBL2ToG1")
	pFemaleExtra1.AddAnimation("ENBG1MToL", "Bridge.Characters.ENBMediumAnimations.ENBG1ToL2")
	pFemaleExtra1.AddAnimation("SeatedENBG1M", "Bridge.Characters.CommonAnimations.SeatedM")
	pFemaleExtra1.SetStanding(0)

	# Hit animations
	pFemaleExtra1.AddAnimation("ENBG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("ENBG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")


	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("ENBL3M")
#	kDebugObj.Print("Finished configuring ENBFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENBFemaleExtra1	- our Character object
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
	# ENBFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
