from bcdebug import debug
###############################################################################
#	Filename:	DFFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador DFFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDFugObj = App.CPyDDFug()

###############################################################################
#	CreateCharacter()
#
#	Create DFFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDDFugObj.Print("Creating DFFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("DFFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif", None)
	pDFFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	pDFFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pDFFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFFemaleExtra1)

	# Setup the character configuration
	pDFFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pDFFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pDFFemaleExtra1.SetRandomAnimationChance(.75)
	pDFFemaleExtra1.SetBlinkChance(0.1)
	pDFFemaleExtra1.SetCharacterName("FemaleExtra1")

	pDFFemaleExtra1.SetHidden(1)

	# Load DFFemaleExtra1's generic sounds
	LoadSounds()

	# Create DFFemaleExtra1's menus
	#import DFFemaleExtra1MenuHandlers
	#DFFemaleExtra1MenuHandlers.CreateMenus(pDFFemaleExtra1)

	pDFFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pDFFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pDFFemaleExtra1.SetLocation("")

#	kDDFugObj.Print("Finished creating DFFemaleExtra1")
	return pDFFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pDFFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pDFFemaleExtra1):
#	kDDFugObj.Print("Configuring DFFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pDFFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY DFFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pDFFemaleExtra1)

	pDFFemaleExtra1.SetAsExtra(1)
	pDFFemaleExtra1.SetHidden(1)

	pDFFemaleExtra1.SetLocation("DBL2M")
#	kDDFugObj.Print("Finished configuring DFFemaleExtra1")

###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pDFFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pFemaleExtra1):
#	kDDFugObj.Print("Configuring DFFemaleExtra1 for the Defiant bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForDefiant")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("DFL2MToG", "Bridge.Characters.DFMediumAnimations.DFL2ToG1")
	pFemaleExtra1.AddAnimation("DFG1MToL", "Bridge.Characters.DFMediumAnimations.DFG1ToL2")
	pFemaleExtra1.AddAnimation("StandingDFG1M", "Bridge.Characters.CommonAnimations.Standing")
	pFemaleExtra1.SetStanding(1)

	# Hit animations
	pFemaleExtra1.AddAnimation("DFG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pFemaleExtra1.AddAnimation("DFG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pFemaleExtra1.AddAnimation("DFG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("DFG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pFemaleExtra1.AddAnimation("DFG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("DFL2M")
#	kDDFugObj.Print("Finished configuring DFFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pDFFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFFemaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pDFFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# DFFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
