from bcdebug import debug
###############################################################################
#	Filename:	IntFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador IntFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDIntugObj = App.CPyDIntug()

###############################################################################
#	CreateCharacter()
#
#	Create IntFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDIntugObj.Print("Creating IntFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("IntFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pIntFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	pIntFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/IntFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pIntFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntFemaleExtra3)

	# Setup the character configuration
	pIntFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pIntFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pIntFemaleExtra3.SetRandomAnimationChance(.75)
	pIntFemaleExtra3.SetBlinkChance(0.1)
	pIntFemaleExtra3.SetCharacterName("FemaleExtra3")

	pIntFemaleExtra3.SetHidden(0)

	# Load IntFemaleExtra3's generic sounds
	LoadSounds()

	# Create IntFemaleExtra3's menus
	#import IntFemaleExtra3MenuHandlers
	#IntFemaleExtra3MenuHandlers.CreateMenus(pIntFemaleExtra3)

	pIntFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pIntFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Seated")
	pIntFemaleExtra3.SetLocation("")

#	kDIntugObj.Print("Finished creating IntFemaleExtra3")
	return pIntFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pIntFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pIntFemaleExtra3):
#	kDIntugObj.Print("Configuring IntFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pIntFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY IntFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pIntFemaleExtra3)

	pIntFemaleExtra3.SetAsExtra(1)
	pIntFemaleExtra3.SetHidden(0)

	pIntFemaleExtra3.SetLocation("DBL1M")
#	kDIntugObj.Print("Finished configuring IntFemaleExtra3")

###############################################################################
#	ConfigureForIntrepid()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pInFemaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForIntrepid")
	pInFemaleExtra3.ClearAnimations()

	# Register animation mappings
	pInFemaleExtra3.AddAnimation("IntL1MToG", "Bridge.Characters.IntMediumAnimations.IntL1ToG3")
	pInFemaleExtra3.AddAnimation("IntG3MToL", "Bridge.Characters.IntMediumAnimations.IntG3ToL1")
	#pInFemaleExtra3.AddAnimation("StandingIntG3M", "Bridge.Characters.CommonAnimations.Standing")
	pInFemaleExtra3.SetStanding(0)

	# Hit animations
	#pInFemaleExtra3.AddAnimation("IntG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pInFemaleExtra3.AddAnimation("IntG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pInFemaleExtra3.AddAnimation("IntG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pInFemaleExtra3.AddAnimation("IntG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pInFemaleExtra3.AddAnimation("IntG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pInFemaleExtra3.SetAsExtra(1)
	pInFemaleExtra3.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pInFemaleExtra3)

	pInFemaleExtra3.SetLocation("IntL1M")
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
#	Args:	pIntFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntFemaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	
##Standing Only

#	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pIntFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# IntFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
