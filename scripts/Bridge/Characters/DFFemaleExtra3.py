from bcdebug import debug
###############################################################################
#	Filename:	DFFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador DFFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDFugObj = App.CPyDDFug()

###############################################################################
#	CreateCharacter()
#
#	Create DFFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDDFugObj.Print("Creating DFFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("DFFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pDFFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	pDFFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/DFFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pDFFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFFemaleExtra3)

	# Setup the character configuration
	pDFFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pDFFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pDFFemaleExtra3.SetRandomAnimationChance(.75)
	pDFFemaleExtra3.SetBlinkChance(0.1)
	pDFFemaleExtra3.SetCharacterName("FemaleExtra3")

	pDFFemaleExtra3.SetHidden(1)

	# Load DFFemaleExtra3's generic sounds
	LoadSounds()

	# Create DFFemaleExtra3's menus
	#import DFFemaleExtra3MenuHandlers
	#DFFemaleExtra3MenuHandlers.CreateMenus(pDFFemaleExtra3)

	pDFFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pDFFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pDFFemaleExtra3.SetLocation("")

#	kDDFugObj.Print("Finished creating DFFemaleExtra3")
	return pDFFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pDFFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pDFFemaleExtra3):
#	kDDFugObj.Print("Configuring DFFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pDFFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY DFFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pDFFemaleExtra3)

	pDFFemaleExtra3.SetAsExtra(1)
	pDFFemaleExtra3.SetHidden(1)

	pDFFemaleExtra3.SetLocation("DBL1M")
#	kDDFugObj.Print("Finished configuring DFFemaleExtra3")

###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pDFMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Defiant bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForDefiant")
	pDFMaleExtra3.ClearAnimations()

	# Register animation mappings
	pDFMaleExtra3.AddAnimation("DFL1MToG", "Bridge.Characters.DFMediumAnimations.DFL1ToG3")
	pDFMaleExtra3.AddAnimation("DFG3MToL", "Bridge.Characters.DFMediumAnimations.DFG3ToL1")
	pDFMaleExtra3.AddAnimation("StandingDFG3M", "Bridge.Characters.CommonAnimations.Standing")
	pDFMaleExtra3.SetStanding(1)

	# Hit animations
	pDFMaleExtra3.AddAnimation("DFG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pDFMaleExtra3.AddAnimation("DFG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pDFMaleExtra3.AddAnimation("DFG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pDFMaleExtra3.AddAnimation("DFG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pDFMaleExtra3.AddAnimation("DFG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pDFMaleExtra3.SetAsExtra(1)
	pDFMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pDFMaleExtra3)

	pDFMaleExtra3.SetLocation("DFL1M")
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
#	Args:	pDFFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFFemaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pDFFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# DFFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
