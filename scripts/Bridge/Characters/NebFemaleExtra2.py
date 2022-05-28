from bcdebug import debug
###############################################################################
#	Filename:	NebFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador NebFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDNebugObj = App.CPyDNebug()

###############################################################################
#	CreateCharacter()
#
#	Create NebFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDNebugObj.Print("Creating NebFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("NebFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pNebFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pNebFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/NebFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pNebFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebFemaleExtra2)

	# Setup the character configuration
	pNebFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pNebFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pNebFemaleExtra2.SetRandomAnimationChance(.75)
	pNebFemaleExtra2.SetBlinkChance(0.1)
	pNebFemaleExtra2.SetCharacterName("FemaleExtra2")

	pNebFemaleExtra2.SetHidden(1)

	# Load NebFemaleExtra2's generic sounds
	LoadSounds()

	# Create NebFemaleExtra2's menus
	#import NebFemaleExtra2MenuHandlers
	#NebFemaleExtra2MenuHandlers.CreateMenus(pNebFemaleExtra2)

	pNebFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pNebFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pNebFemaleExtra2.SetLocation("")

#	kDNebugObj.Print("Finished creating NebFemaleExtra2")
	return pNebFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pNebFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pNebFemaleExtra2):
#	kDNebugObj.Print("Configuring NebFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pNebFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY NebFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pNebFemaleExtra2)

	pNebFemaleExtra2.SetAsExtra(1)
	pNebFemaleExtra2.SetHidden(1)

	pNebFemaleExtra2.SetLocation("DBL2M")
#	kDNebugObj.Print("Finished configuring NebFemaleExtra2")


###############################################################################
#	ConfigureForSovereign()
#
#	Configure ourselves for the Nebula bridge
#
#	Args:	pNebFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pNebFemaleExtra2):
#	kDNebugObj.Print("Configuring NebFemaleExtra2 for the Nebula bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pNebFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pNebFemaleExtra2.AddAnimation("NebL2MToG", "Bridge.Characters.NebMediumAnimations.NebL2ToG2")
	pNebFemaleExtra2.AddAnimation("NebG2MToL", "Bridge.Characters.NebMediumAnimations.NebG2ToL2")
	pNebFemaleExtra2.AddAnimation("StandingNebG2M", "Bridge.Characters.CommonAnimations.Standing")
	pNebFemaleExtra2.SetStanding(1)

	# Hit animations
	pNebFemaleExtra2.AddAnimation("NebG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pNebFemaleExtra2.AddAnimation("NebG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pNebFemaleExtra2.AddAnimation("NebG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pNebFemaleExtra2.AddAnimation("NebG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pNebFemaleExtra2.AddAnimation("NebG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pNebFemaleExtra2.SetAsExtra(1)
	pNebFemaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pNebFemaleExtra2)

	pNebFemaleExtra2.SetLocation("NebL2M")
#	kDNebugObj.Print("Finished configuring NebFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pNebFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebFemaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.PushingButtons")
#	pNebFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleSlide")


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
	# NebFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
