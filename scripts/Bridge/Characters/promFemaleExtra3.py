from bcdebug import debug
###############################################################################
#	Filename:	promFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador promFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDpromugObj = App.CPyDpromug()

###############################################################################
#	CreateCharacter()
#
#	Create promFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDpromugObj.Print("Creating promFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("promFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	ppromFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	ppromFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/promFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(ppromFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromFemaleExtra3)

	# Setup the character configuration
	ppromFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	ppromFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	ppromFemaleExtra3.SetRandomAnimationChance(.75)
	ppromFemaleExtra3.SetBlinkChance(0.1)
	ppromFemaleExtra3.SetCharacterName("FemaleExtra3")

	ppromFemaleExtra3.SetHidden(1)

	# Load promFemaleExtra3's generic sounds
	LoadSounds()

	# Create promFemaleExtra3's menus
	#import promFemaleExtra3MenuHandlers
	#promFemaleExtra3MenuHandlers.CreateMenus(ppromFemaleExtra3)

	ppromFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	ppromFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	ppromFemaleExtra3.SetLocation("")

#	kDpromugObj.Print("Finished creating promFemaleExtra3")
	return ppromFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	ppromFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(ppromFemaleExtra3):
#	kDpromugObj.Print("Configuring promFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	ppromFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY promFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(ppromFemaleExtra3)

	ppromFemaleExtra3.SetAsExtra(1)
	ppromFemaleExtra3.SetHidden(1)

	ppromFemaleExtra3.SetLocation("DBL1M")
#	kDpromugObj.Print("Finished configuring promFemaleExtra3")

###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(ppromMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the prometheus bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForprometheus")
	ppromMaleExtra3.ClearAnimations()

	# Register animation mappings
	ppromMaleExtra3.AddAnimation("promL1MToG", "Bridge.Characters.promMediumAnimations.promL1ToG3")
	ppromMaleExtra3.AddAnimation("promG3MToL", "Bridge.Characters.promMediumAnimations.promG3ToL1")
	ppromMaleExtra3.AddAnimation("StandingpromG3M", "Bridge.Characters.CommonAnimations.Standing")
	ppromMaleExtra3.SetStanding(1)

	# Hit animations
	ppromMaleExtra3.AddAnimation("promG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	ppromMaleExtra3.AddAnimation("promG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	ppromMaleExtra3.AddAnimation("promG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	ppromMaleExtra3.AddAnimation("promG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	ppromMaleExtra3.AddAnimation("promG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	ppromMaleExtra3.SetAsExtra(1)
	ppromMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(ppromMaleExtra3)

	ppromMaleExtra3.SetLocation("promL1M")
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
#	Args:	ppromFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromFemaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	#ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	#ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	#ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	#ppromFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# promFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
