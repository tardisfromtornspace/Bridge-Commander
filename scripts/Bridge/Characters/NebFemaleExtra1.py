from bcdebug import debug
###############################################################################
#	Filename:	NebFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador NebFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDExcugObj = App.CPyDExcug()

###############################################################################
#	CreateCharacter()
#
#	Create NebFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDExcugObj.Print("Creating NebFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("NebFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif", None)
	pNebFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	pNebFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pNebFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebFemaleExtra1)

	# Setup the character configuration
	pNebFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pNebFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pNebFemaleExtra1.SetRandomAnimationChance(.75)
	pNebFemaleExtra1.SetBlinkChance(0.1)
	pNebFemaleExtra1.SetCharacterName("FemaleExtra1")

	pNebFemaleExtra1.SetHidden(1)

	# Load NebFemaleExtra1's generic sounds
	LoadSounds()

	# Create NebFemaleExtra1's menus
	#import NebFemaleExtra1MenuHandlers
	#NebFemaleExtra1MenuHandlers.CreateMenus(pNebFemaleExtra1)

	pNebFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pNebFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pNebFemaleExtra1.SetLocation("")

#	kDNebugObj.Print("Finished creating NebFemaleExtra1")
	return pNebFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pNebFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pNebFemaleExtra1):
#	kDNebugObj.Print("Configuring NebFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pNebFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY NebFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pNebFemaleExtra1)

	pNebFemaleExtra1.SetAsExtra(1)
	pNebFemaleExtra1.SetHidden(1)

	pNebFemaleExtra1.SetLocation("DBL2M")
#	kDNebugObj.Print("Finished configuring NebFemaleExtra1")

###############################################################################
#	ConfigureForNebula()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pNebFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pFemaleExtra1):
#	kDExcugObj.Print("Configuring NebFemaleExtra1 for the Nebula bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("NebL2MToG", "Bridge.Characters.NebMediumAnimations.NebL2ToG1")
	pFemaleExtra1.AddAnimation("NebG1MToL", "Bridge.Characters.NebMediumAnimations.NebG1ToL2")
	pFemaleExtra1.AddAnimation("StandingNebG1M", "Bridge.Characters.CommonAnimations.Standing")
	pFemaleExtra1.SetStanding(1)

	# Interaction
	pFemaleExtra1.AddRandomAnimation("Bridge.Characters.NebMediumAnimations.NebCConsoleInteraction", App.CharacterClass.STANDING_ONLY, 25, 1)

	# So the mission builders can force the call
	pFemaleExtra1.AddAnimation("PushingButtons", "Bridge.Characters.SmallAnimations.NebEConsoleInteraction")

	# Hit animations
	pFemaleExtra1.AddAnimation("NebG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pFemaleExtra1.AddAnimation("NebG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pFemaleExtra1.AddAnimation("NebG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("NebG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pFemaleExtra1.AddAnimation("NebG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("NebL2M")
#	kDNebugObj.Print("Finished configuring NebFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pNebFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebFemaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	# pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	# pNebFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# NebFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
