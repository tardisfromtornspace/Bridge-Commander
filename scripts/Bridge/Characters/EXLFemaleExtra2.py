from bcdebug import debug
###############################################################################
#	Filename:	EXLFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador EXLFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create EXLFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating EXLFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("EXLFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pEXLFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pEXLFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/EXLFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLFemaleExtra2)

	# Setup the character configuration
	pEXLFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pEXLFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pEXLFemaleExtra2.SetRandomAnimationChance(.75)
	pEXLFemaleExtra2.SetBlinkChance(0.1)
	pEXLFemaleExtra2.SetCharacterName("FemaleExtra2")

	pEXLFemaleExtra2.SetHidden(1)

	# Load EXLFemaleExtra2's generic sounds
	LoadSounds()

	# Create EXLFemaleExtra2's menus
	#import EXLFemaleExtra2MenuHandlers
	#EXLFemaleExtra2MenuHandlers.CreateMenus(pEXLFemaleExtra2)

	pEXLFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pEXLFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pEXLFemaleExtra2.SetLocation("")

#	kDebugObj.Print("Finished creating EXLFemaleExtra2")
	return pEXLFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pEXLFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pEXLFemaleExtra2):
#	kDebugObj.Print("Configuring EXLFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pEXLFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY EXLFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pEXLFemaleExtra2)

	pEXLFemaleExtra2.SetAsExtra(1)
	pEXLFemaleExtra2.SetHidden(1)

	pEXLFemaleExtra2.SetLocation("DBL2M")
#	kDebAugObj.Print("Finished configuring EXLFemaleExtra2")


###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pEXLFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pEXLFemaleExtra2):
#	kDebugObj.Print("Configuring EXLFemaleExtra2 for the Excelsior bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcelsior")
	pEXLFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pEXLFemaleExtra2.AddAnimation("EXLL2MToG", "Bridge.Characters.EXLMediumAnimations.EXLL2ToG2")
	pEXLFemaleExtra2.AddAnimation("EXLG2MToL", "Bridge.Characters.EXLMediumAnimations.EXLG2ToL2")
	pEXLFemaleExtra2.AddAnimation("StandingEXLG2M", "Bridge.Characters.CommonAnimations.Standing")
	pEXLFemaleExtra2.SetStanding(1)

	# Hit animations
	pEXLFemaleExtra2.AddAnimation("EXLG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pEXLFemaleExtra2.AddAnimation("EXLG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pEXLFemaleExtra2.AddAnimation("EXLG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pEXLFemaleExtra2.AddAnimation("EXLG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pEXLFemaleExtra2.AddAnimation("EXLG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pEXLFemaleExtra2.SetAsExtra(1)
	pEXLFemaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pEXLFemaleExtra2)

	pEXLFemaleExtra2.SetLocation("EXLL2M")
#	kDebugObj.Print("Finished configuring EXLFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pEXLFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLFemaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pEXLFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# EXLFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
