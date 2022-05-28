from bcdebug import debug
###############################################################################
#	Filename:	promFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador promFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDpromugObj = App.CPyDpromug()

###############################################################################
#	CreateCharacter()
#
#	Create promFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDpromugObj.Print("Creating promFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("promFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	ppromFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	ppromFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/promFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(ppromFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(ppromFemaleExtra2)

	# Setup the character configuration
	ppromFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	ppromFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	ppromFemaleExtra2.SetRandomAnimationChance(.75)
	ppromFemaleExtra2.SetBlinkChance(0.1)
	ppromFemaleExtra2.SetCharacterName("FemaleExtra2")

	ppromFemaleExtra2.SetHidden(0)

	# Load promFemaleExtra2's generic sounds
	LoadSounds()

	# Create promFemaleExtra2's menus
	#import promFemaleExtra2MenuHandlers
	#promFemaleExtra2MenuHandlers.CreateMenus(ppromFemaleExtra2)

	ppromFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	ppromFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	ppromFemaleExtra2.SetLocation("")

#	kDpromugObj.Print("Finished creating promFemaleExtra2")
	return ppromFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	ppromFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(ppromFemaleExtra2):
#	kDpromugObj.Print("Configuring promFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	ppromFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY promFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(ppromFemaleExtra2)

	ppromFemaleExtra2.SetAsExtra(1)
	ppromFemaleExtra2.SetHidden(0)
	ppromFemaleExtra2.SetStanding(0)

	ppromFemaleExtra2.SetLocation("DBL2M")
#	kDpromugObj.Print("Finished configuring promFemaleExtra2")


###############################################################################
#	ConfigureForprometheus()
#
#	Configure ourselves for the prometheus bridge
#
#	Args:	ppromFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForprometheus(ppromFemaleExtra2):
#	kDpromugObj.Print("Configuring promFemaleExtra2 for the prometheus bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForprometheus")
	ppromFemaleExtra2.ClearAnimations()

	# Register animation mappings
	#ppromFemaleExtra2.AddAnimation("promL2MToG", "Bridge.Characters.promMediumAnimations.promL2ToG2")
	#ppromFemaleExtra2.AddAnimation("promG2MToL", "Bridge.Characters.promMediumAnimations.promG2ToL2")
	#ppromFemaleExtra2.AddAnimation("StandingpromG2M", "Bridge.Characters.CommonAnimations.Standing")
	#ppromFemaleExtra2.SetStanding(1)

	# Hit animations
	#ppromFemaleExtra2.AddAnimation("promG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#ppromFemaleExtra2.AddAnimation("promG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#ppromFemaleExtra2.AddAnimation("promG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#ppromFemaleExtra2.AddAnimation("promG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#ppromFemaleExtra2.AddAnimation("promG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	ppromFemaleExtra2.SetAsExtra(1)
	ppromFemaleExtra2.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(ppromFemaleExtra2)

	ppromFemaleExtra2.SetLocation("promL3M")
#	kDpromugObj.Print("Finished configuring promFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	ppromFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(ppromFemaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.promMediumAnimations.prom_seated_interaction")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	ppromFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# promFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
