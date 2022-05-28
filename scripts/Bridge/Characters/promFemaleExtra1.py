from bcdebug import debug
###############################################################################
#	Filename:	promFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador promFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDpromugObj = App.CPyDpromug()

###############################################################################
#	CreateCharacter()
#
#	Create promFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDpromugObj.Print("Creating promFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("promFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif", None)
	ppromFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	ppromFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(ppromFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromFemaleExtra1)

	# Setup the character configuration
	ppromFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	ppromFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	ppromFemaleExtra1.SetRandomAnimationChance(.75)
	ppromFemaleExtra1.SetBlinkChance(0.1)
	ppromFemaleExtra1.SetCharacterName("FemaleExtra1")

	ppromFemaleExtra1.SetHidden(1)

	# Load promFemaleExtra1's generic sounds
	LoadSounds()

	# Create promFemaleExtra1's menus
	#import promFemaleExtra1MenuHandlers
	#promFemaleExtra1MenuHandlers.CreateMenus(ppromFemaleExtra1)

	ppromFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	ppromFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	ppromFemaleExtra1.SetLocation("")

#	kDpromugObj.Print("Finished creating promFemaleExtra1")
	return ppromFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	ppromFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(ppromFemaleExtra1):
#	kDpromugObj.Print("Configuring promFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	ppromFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY promFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(ppromFemaleExtra1)

	ppromFemaleExtra1.SetAsExtra(1)
	ppromFemaleExtra1.SetHidden(1)

	ppromFemaleExtra1.SetLocation("DBL2M")
#	kDpromugObj.Print("Finished configuring promFemaleExtra1")

###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	ppromFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(pFemaleExtra1):
#	kDpromugObj.Print("Configuring promFemaleExtra1 for the prometheus bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForprometheus")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("promL2MToG", "Bridge.Characters.promMediumAnimations.promL2ToG1")
	pFemaleExtra1.AddAnimation("promG1MToL", "Bridge.Characters.promMediumAnimations.promG1ToL2")
	pFemaleExtra1.AddAnimation("StandingpromG1M", "Bridge.Characters.CommonAnimations.Standing")
	pFemaleExtra1.SetStanding(1)

	# Hit animations
	pFemaleExtra1.AddAnimation("promG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pFemaleExtra1.AddAnimation("promG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pFemaleExtra1.AddAnimation("promG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("promG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pFemaleExtra1.AddAnimation("promG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("promL2M")
#	kDpromugObj.Print("Finished configuring promFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	ppromFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromFemaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	ppromFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# promFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
