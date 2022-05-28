from bcdebug import debug
###############################################################################
#	Filename:	IntFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador IntFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDIntugObj = App.CPyDIntug()

###############################################################################
#	CreateCharacter()
#
#	Create IntFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDIntugObj.Print("Creating IntFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("IntFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pIntFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pIntFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/IntFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pIntFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntFemaleExtra2)

	# Setup the character configuration
	pIntFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pIntFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pIntFemaleExtra2.SetRandomAnimationChance(.75)
	pIntFemaleExtra2.SetBlinkChance(0.1)
	pIntFemaleExtra2.SetCharacterName("FemaleExtra2")

	pIntFemaleExtra2.SetHidden(1)

	# Load IntFemaleExtra2's generic sounds
	LoadSounds()

	# Create IntFemaleExtra2's menus
	#import IntFemaleExtra2MenuHandlers
	#IntFemaleExtra2MenuHandlers.CreateMenus(pIntFemaleExtra2)

	pIntFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pIntFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pIntFemaleExtra2.SetLocation("")

#	kDIntugObj.Print("Finished creating IntFemaleExtra2")
	return pIntFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pIntFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pIntFemaleExtra2):
#	kDIntugObj.Print("Configuring IntFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pIntFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY IntFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pIntFemaleExtra2)

	pIntFemaleExtra2.SetAsExtra(1)
	pIntFemaleExtra2.SetHidden(1)

	pIntFemaleExtra2.SetLocation("DBL2M")
#	kDIntugObj.Print("Finished configuring IntFemaleExtra2")


###############################################################################
#	ConfigureForSovereign()
#
#	Configure ourselves for the Intrepid bridge
#
#	Args:	pIntFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pIntFemaleExtra2):
#	kDIntugObj.Print("Configuring IntFemaleExtra2 for the Intrepid bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForIntrepid")
	pIntFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pIntFemaleExtra2.AddAnimation("IntL2MToG", "Bridge.Characters.IntMediumAnimations.IntL2ToG2")
	pIntFemaleExtra2.AddAnimation("IntG2MToL", "Bridge.Characters.IntMediumAnimations.IntG2ToL2")
	pIntFemaleExtra2.AddAnimation("StandingIntG2M", "Bridge.Characters.CommonAnimations.Standing")
	pIntFemaleExtra2.SetStanding(1)

	# Hit animations
	pIntFemaleExtra2.AddAnimation("IntG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pIntFemaleExtra2.AddAnimation("IntG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pIntFemaleExtra2.AddAnimation("IntG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pIntFemaleExtra2.AddAnimation("IntG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pIntFemaleExtra2.AddAnimation("IntG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pIntFemaleExtra2.SetAsExtra(1)
	pIntFemaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pIntFemaleExtra2)

	pIntFemaleExtra2.SetLocation("IntL2M")
#	kDIntugObj.Print("Finished configuring IntFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pIntFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntFemaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.PushingButtons")
#	pIntFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleSlide")


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
	# IntFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
