from bcdebug import debug
###############################################################################
#	Filename:	ExcFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ExcFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDExcugObj = App.CPyDExcug()

###############################################################################
#	CreateCharacter()
#
#	Create ExcFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDExcugObj.Print("Creating ExcFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ExcFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif", None)
	pExcFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	pExcFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pExcFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcFemaleExtra1)

	# Setup the character configuration
	pExcFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pExcFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pExcFemaleExtra1.SetRandomAnimationChance(.75)
	pExcFemaleExtra1.SetBlinkChance(0.1)
	pExcFemaleExtra1.SetCharacterName("FemaleExtra1")

	pExcFemaleExtra1.SetHidden(1)

	# Load ExcFemaleExtra1's generic sounds
	LoadSounds()

	# Create ExcFemaleExtra1's menus
	#import ExcFemaleExtra1MenuHandlers
	#ExcFemaleExtra1MenuHandlers.CreateMenus(pExcFemaleExtra1)

	pExcFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pExcFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pExcFemaleExtra1.SetLocation("")

#	kDExcugObj.Print("Finished creating ExcFemaleExtra1")
	return pExcFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pExcFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pExcFemaleExtra1):
#	kDExcugObj.Print("Configuring ExcFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pExcFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY ExcFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pExcFemaleExtra1)

	pExcFemaleExtra1.SetAsExtra(1)
	pExcFemaleExtra1.SetHidden(1)

	pExcFemaleExtra1.SetLocation("DBL2M")
#	kDExcugObj.Print("Finished configuring ExcFemaleExtra1")

###############################################################################
#	ConfigureForExcalibur()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pExcFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pFemaleExtra1):
#	kDExcugObj.Print("Configuring ExcFemaleExtra1 for the Excalibur bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcalibur")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("ExcL2MToG", "Bridge.Characters.ExcMediumAnimations.ExcL2ToG1")
	pFemaleExtra1.AddAnimation("ExcG1MToL", "Bridge.Characters.ExcMediumAnimations.ExcG1ToL2")
	pFemaleExtra1.AddAnimation("StandingExcG1M", "Bridge.Characters.CommonAnimations.Standing")
	pFemaleExtra1.SetStanding(1)

	# Hit animations
	pFemaleExtra1.AddAnimation("ExcG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pFemaleExtra1.AddAnimation("ExcG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pFemaleExtra1.AddAnimation("ExcG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("ExcG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pFemaleExtra1.AddAnimation("ExcG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("ExcL2M")
#	kDExcugObj.Print("Finished configuring ExcFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pExcFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcFemaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pExcFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# ExcFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
