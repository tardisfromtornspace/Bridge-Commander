from bcdebug import debug
###############################################################################
#	Filename:	EXLFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador EXLFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create EXLFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating EXLFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("EXLFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "Headfem3/fem3_head.nif", None)
	pEXLFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	pEXLFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedfemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLFemaleExtra1)

	# Setup the character configuration
	pEXLFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pEXLFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pEXLFemaleExtra1.SetRandomAnimationChance(.75)
	pEXLFemaleExtra1.SetBlinkChance(0.1)
	pEXLFemaleExtra1.SetCharacterName("FemaleExtra1")

	pEXLFemaleExtra1.SetHidden(1)

	# Load EXLFemaleExtra1's generic sounds
	LoadSounds()

	# Create EXLFemaleExtra1's menus
	#import EXLFemaleExtra1MenuHandlers
	#EXLFemaleExtra1MenuHandlers.CreateMenus(pEXLFemaleExtra1)

	pEXLFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pEXLFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pEXLFemaleExtra1.SetLocation("")

#	kDebugObj.Print("Finished creating EXLFemaleExtra1")
	return pEXLFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pEXLFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pEXLFemaleExtra1):
#	kDebugObj.Print("Configuring EXLFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pEXLFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY EXLFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pEXLFemaleExtra1)

	pEXLFemaleExtra1.SetAsExtra(1)
	pEXLFemaleExtra1.SetHidden(1)

	pEXLFemaleExtra1.SetLocation("DBL2M")
#	kDebugObj.Print("Finished configuring EXLFemaleExtra1")

###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pEXLFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pFemaleExtra1):
#	kDebugObj.Print("Configuring EXLFemaleExtra1 for the Excelsior bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcelsior")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("EXLL2MToG", "Bridge.Characters.EXLMediumAnimations.EXLL2ToG1")
	pFemaleExtra1.AddAnimation("EXLG1MToL", "Bridge.Characters.EXLMediumAnimations.EXLG1ToL2")
	pFemaleExtra1.AddAnimation("StandingEXLG1M", "Bridge.Characters.CommonAnimations.Standing")
	pFemaleExtra1.SetStanding(1)

	# Hit animations
	pFemaleExtra1.AddAnimation("EXLG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pFemaleExtra1.AddAnimation("EXLG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pFemaleExtra1.AddAnimation("EXLG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("EXLG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pFemaleExtra1.AddAnimation("EXLG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("EXLL2M")
#	kDebugObj.Print("Finished configuring EXLFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pEXLFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLFemaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pEXLFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# EXLFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
