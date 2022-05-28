from bcdebug import debug
###############################################################################
#	Filename:	EXLFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador EXLFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create EXLFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating EXLFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("EXLFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pEXLFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	pEXLFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedfemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/EXLFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLFemaleExtra3)

	# Setup the character configuration
	pEXLFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pEXLFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pEXLFemaleExtra3.SetRandomAnimationChance(.75)
	pEXLFemaleExtra3.SetBlinkChance(0.1)
	pEXLFemaleExtra3.SetCharacterName("FemaleExtra3")

	pEXLFemaleExtra3.SetHidden(1)

	# Load EXLFemaleExtra3's generic sounds
	LoadSounds()

	# Create EXLFemaleExtra3's menus
	#import EXLFemaleExtra3MenuHandlers
	#EXLFemaleExtra3MenuHandlers.CreateMenus(pEXLFemaleExtra3)

	pEXLFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pEXLFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pEXLFemaleExtra3.SetLocation("")

#	kDebugObj.Print("Finished creating EXLFemaleExtra3")
	return pEXLFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pEXLFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pEXLFemaleExtra3):
#	kDebugObj.Print("Configuring EXLFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pEXLFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY EXLFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pEXLFemaleExtra3)

	pEXLFemaleExtra3.SetAsExtra(1)
	pEXLFemaleExtra3.SetHidden(1)

	pEXLFemaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring EXLFemaleExtra3")

###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pEXLMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Excelsior bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcelsior")
	pEXLMaleExtra3.ClearAnimations()

	# Register animation mappings
	pEXLMaleExtra3.AddAnimation("EXLL1MToG", "Bridge.Characters.EXLMediumAnimations.EXLL1ToG3")
	pEXLMaleExtra3.AddAnimation("EXLG3MToL", "Bridge.Characters.EXLMediumAnimations.EXLG3ToL1")
	pEXLMaleExtra3.AddAnimation("StandingEXLG3M", "Bridge.Characters.CommonAnimations.Standing")
	pEXLMaleExtra3.SetStanding(1)

	# Hit animations
	pEXLMaleExtra3.AddAnimation("EXLG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pEXLMaleExtra3.AddAnimation("EXLG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pEXLMaleExtra3.AddAnimation("EXLG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pEXLMaleExtra3.AddAnimation("EXLG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pEXLMaleExtra3.AddAnimation("EXLG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pEXLMaleExtra3.SetAsExtra(1)
	pEXLMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pEXLMaleExtra3)

	pEXLMaleExtra3.SetLocation("EXLL1M")
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
#	Args:	pEXLFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLFemaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pEXLFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# EXLFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
