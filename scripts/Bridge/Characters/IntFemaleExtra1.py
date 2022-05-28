from bcdebug import debug
###############################################################################
#	Filename:	IntFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador IntFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDIntugObj = App.CPyDIntug()

###############################################################################
#	CreateCharacter()
#
#	Create IntFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDIntugObj.Print("Creating IntFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("IntFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif", None)
	pIntFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	pIntFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pIntFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntFemaleExtra1)

	# Setup the character configuration
	pIntFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pIntFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pIntFemaleExtra1.SetRandomAnimationChance(.75)
	pIntFemaleExtra1.SetBlinkChance(0.1)
	pIntFemaleExtra1.SetCharacterName("FemaleExtra1")

	pIntFemaleExtra1.SetHidden(1)

	# Load IntFemaleExtra1's generic sounds
	LoadSounds()

	# Create IntFemaleExtra1's menus
	#import IntFemaleExtra1MenuHandlers
	#IntFemaleExtra1MenuHandlers.CreateMenus(pIntFemaleExtra1)

	pIntFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pIntFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pIntFemaleExtra1.SetLocation("")

#	kDIntugObj.Print("Finished creating IntFemaleExtra1")
	return pIntFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pIntFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pIntFemaleExtra1):
#	kDIntugObj.Print("Configuring IntFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pIntFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY IntFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pIntFemaleExtra1)

	pIntFemaleExtra1.SetAsExtra(1)
	pIntFemaleExtra1.SetHidden(1)

	pIntFemaleExtra1.SetLocation("DBL2M")
#	kDIntugObj.Print("Finished configuring IntFemaleExtra1")

###############################################################################
#	ConfigureForIntrepid()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pIntFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pFemaleExtra1):
#	kDIntugObj.Print("Configuring IntFemaleExtra1 for the Intrepid bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForIntrepid")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("IntL2MToG", "Bridge.Characters.IntMediumAnimations.IntL2ToG1")
	pFemaleExtra1.AddAnimation("IntG1MToL", "Bridge.Characters.IntMediumAnimations.IntG1ToL2")
	pFemaleExtra1.AddAnimation("StandingIntG1M", "Bridge.Characters.CommonAnimations.Standing")
	pFemaleExtra1.SetStanding(1)

	# Hit animations
	pFemaleExtra1.AddAnimation("IntG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pFemaleExtra1.AddAnimation("IntG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pFemaleExtra1.AddAnimation("IntG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("IntG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pFemaleExtra1.AddAnimation("IntG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("IntL2M")
#	kDIntugObj.Print("Finished configuring IntFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pIntFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntFemaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pIntFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# IntFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
