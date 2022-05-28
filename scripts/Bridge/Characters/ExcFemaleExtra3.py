from bcdebug import debug
###############################################################################
#	Filename:	ExcFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ExcFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDExcugObj = App.CPyDExcug()

###############################################################################
#	CreateCharacter()
#
#	Create ExcFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDExcugObj.Print("Creating ExcFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ExcFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pExcFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	pExcFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/ExcFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pExcFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcFemaleExtra3)

	# Setup the character configuration
	pExcFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pExcFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pExcFemaleExtra3.SetRandomAnimationChance(.75)
	pExcFemaleExtra3.SetBlinkChance(0.1)
	pExcFemaleExtra3.SetCharacterName("FemaleExtra3")

	pExcFemaleExtra3.SetHidden(1)

	# Load ExcFemaleExtra3's generic sounds
	LoadSounds()

	# Create ExcFemaleExtra3's menus
	#import ExcFemaleExtra3MenuHandlers
	#ExcFemaleExtra3MenuHandlers.CreateMenus(pExcFemaleExtra3)

	pExcFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pExcFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pExcFemaleExtra3.SetLocation("")

#	kDExcugObj.Print("Finished creating ExcFemaleExtra3")
	return pExcFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pExcFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pExcFemaleExtra3):
#	kDExcugObj.Print("Configuring ExcFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pExcFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY ExcFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pExcFemaleExtra3)

	pExcFemaleExtra3.SetAsExtra(1)
	pExcFemaleExtra3.SetHidden(1)

	pExcFemaleExtra3.SetLocation("DBL1M")
#	kDExcugObj.Print("Finished configuring ExcFemaleExtra3")

###############################################################################
#	ConfigureForExcalibur()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pExcMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcalibur")
	pExcMaleExtra3.ClearAnimations()

	# Register animation mappings
	pExcMaleExtra3.AddAnimation("ExcL1MToG", "Bridge.Characters.ExcMediumAnimations.ExcL1ToG3")
	pExcMaleExtra3.AddAnimation("ExcG3MToL", "Bridge.Characters.ExcMediumAnimations.ExcG3ToL1")
	pExcMaleExtra3.AddAnimation("StandingExcG3M", "Bridge.Characters.CommonAnimations.Standing")
	pExcMaleExtra3.SetStanding(1)

	# Hit animations
	pExcMaleExtra3.AddAnimation("ExcG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pExcMaleExtra3.AddAnimation("ExcG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pExcMaleExtra3.AddAnimation("ExcG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pExcMaleExtra3.AddAnimation("ExcG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pExcMaleExtra3.AddAnimation("ExcG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pExcMaleExtra3.SetAsExtra(1)
	pExcMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pExcMaleExtra3)

	pExcMaleExtra3.SetLocation("ExcL1M")
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
#	Args:	pExcFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcFemaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pExcFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# ExcFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
