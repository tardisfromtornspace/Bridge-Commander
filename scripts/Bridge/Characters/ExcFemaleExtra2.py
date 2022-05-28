from bcdebug import debug
###############################################################################
#	Filename:	ExcFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ExcFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDExcugObj = App.CPyDExcug()

###############################################################################
#	CreateCharacter()
#
#	Create ExcFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDExcugObj.Print("Creating ExcFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ExcFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pExcFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pExcFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/ExcFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pExcFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pExcFemaleExtra2)

	# Setup the character configuration
	pExcFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pExcFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pExcFemaleExtra2.SetRandomAnimationChance(.75)
	pExcFemaleExtra2.SetBlinkChance(0.1)
	pExcFemaleExtra2.SetCharacterName("FemaleExtra2")

	pExcFemaleExtra2.SetHidden(1)

	# Load ExcFemaleExtra2's generic sounds
	LoadSounds()

	# Create ExcFemaleExtra2's menus
	#import ExcFemaleExtra2MenuHandlers
	#ExcFemaleExtra2MenuHandlers.CreateMenus(pExcFemaleExtra2)

	pExcFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pExcFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pExcFemaleExtra2.SetLocation("")

#	kDExcugObj.Print("Finished creating ExcFemaleExtra2")
	return pExcFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pExcFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pExcFemaleExtra2):
#	kDExcugObj.Print("Configuring ExcFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pExcFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY ExcFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pExcFemaleExtra2)

	pExcFemaleExtra2.SetAsExtra(1)
	pExcFemaleExtra2.SetHidden(1)

	pExcFemaleExtra2.SetLocation("DBL2M")
#	kDExcugObj.Print("Finished configuring ExcFemaleExtra2")


###############################################################################
#	ConfigureForSovereign()
#
#	Configure ourselves for the Excalibur bridge
#
#	Args:	pExcFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcalibur(pExcFemaleExtra2):
#	kDExcugObj.Print("Configuring ExcFemaleExtra2 for the Excalibur bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcalibur")
	pExcFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pExcFemaleExtra2.AddAnimation("ExcL2MToG", "Bridge.Characters.ExcMediumAnimations.ExcL2ToG2")
	pExcFemaleExtra2.AddAnimation("ExcG2MToL", "Bridge.Characters.ExcMediumAnimations.ExcG2ToL2")
	pExcFemaleExtra2.AddAnimation("StandingExcG2M", "Bridge.Characters.CommonAnimations.Standing")
	pExcFemaleExtra2.SetStanding(1)

	# Hit animations
	pExcFemaleExtra2.AddAnimation("ExcG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pExcFemaleExtra2.AddAnimation("ExcG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pExcFemaleExtra2.AddAnimation("ExcG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pExcFemaleExtra2.AddAnimation("ExcG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pExcFemaleExtra2.AddAnimation("ExcG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pExcFemaleExtra2.SetAsExtra(1)
	pExcFemaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pExcFemaleExtra2)

	pExcFemaleExtra2.SetLocation("ExcL2M")
#	kDExcugObj.Print("Finished configuring ExcFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pExcFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pExcFemaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.PushingButtons")
#	pExcFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleSlide")


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
	# ExcFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
