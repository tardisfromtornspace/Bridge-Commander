from bcdebug import debug
###############################################################################
#	Filename:	NebFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador NebFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDNebugObj = App.CPyDNebug()

###############################################################################
#	CreateCharacter()
#
#	Create NebFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDNebugObj.Print("Creating NebFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("NebFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pNebFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	pNebFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/NebFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pNebFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebFemaleExtra3)

	# Setup the character configuration
	pNebFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pNebFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pNebFemaleExtra3.SetRandomAnimationChance(.75)
	pNebFemaleExtra3.SetBlinkChance(0.1)
	pNebFemaleExtra3.SetCharacterName("FemaleExtra3")

	pNebFemaleExtra3.SetHidden(1)

	# Load NebFemaleExtra3's generic sounds
	LoadSounds()

	# Create NebFemaleExtra3's menus
	#import NebFemaleExtra3MenuHandlers
	#NebFemaleExtra3MenuHandlers.CreateMenus(pNebFemaleExtra3)

	pNebFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pNebFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pNebFemaleExtra3.SetLocation("")

#	kDNebugObj.Print("Finished creating NebFemaleExtra3")
	return pNebFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pNebFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pNebFemaleExtra3):
#	kDNebugObj.Print("Configuring NebFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pNebFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY NebFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pNebFemaleExtra3)

	pNebFemaleExtra3.SetAsExtra(1)
	pNebFemaleExtra3.SetHidden(1)

	pNebFemaleExtra3.SetLocation("DBL1M")
#	kDNebugObj.Print("Finished configuring NebFemaleExtra3")

###############################################################################
#	ConfigureForNebula()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pNebMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pNebMaleExtra3.ClearAnimations()

	# Register animation mappings
	pNebMaleExtra3.AddAnimation("NebL1MToG", "Bridge.Characters.NebMediumAnimations.NebL1ToG3")
	pNebMaleExtra3.AddAnimation("NebG3MToL", "Bridge.Characters.NebMediumAnimations.NebG3ToL1")
	pNebMaleExtra3.AddAnimation("StandingNebG3M", "Bridge.Characters.CommonAnimations.Standing")
	pNebMaleExtra3.SetStanding(1)

	# Hit animations
	pNebMaleExtra3.AddAnimation("NebG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pNebMaleExtra3.AddAnimation("NebG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pNebMaleExtra3.AddAnimation("NebG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pNebMaleExtra3.AddAnimation("NebG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pNebMaleExtra3.AddAnimation("NebG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pNebMaleExtra3.SetAsExtra(1)
	pNebMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pNebMaleExtra3)

	pNebMaleExtra3.SetLocation("NebL1M")
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
#	Args:	pNebFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebFemaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pNebFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# NebFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
