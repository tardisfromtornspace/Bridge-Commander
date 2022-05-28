from bcdebug import debug
###############################################################################
#	Filename:	AmbFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador AmbFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDAmbugObj = App.CPyDAmbug()

###############################################################################
#	CreateCharacter()
#
#	Create AmbFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDAmbugObj.Print("Creating AmbFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("AmbFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pAmbFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	pAmbFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/AmbFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbFemaleExtra3)

	# Setup the character configuration
	pAmbFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pAmbFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pAmbFemaleExtra3.SetRandomAnimationChance(.75)
	pAmbFemaleExtra3.SetBlinkChance(0.1)
	pAmbFemaleExtra3.SetCharacterName("FemaleExtra3")

	pAmbFemaleExtra3.SetHidden(1)

	# Load AmbFemaleExtra3's generic sounds
	LoadSounds()

	# Create AmbFemaleExtra3's menus
	#import AmbFemaleExtra3MenuHandlers
	#AmbFemaleExtra3MenuHandlers.CreateMenus(pAmbFemaleExtra3)

	pAmbFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pAmbFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pAmbFemaleExtra3.SetLocation("")

#	kDAmbugObj.Print("Finished creating AmbFemaleExtra3")
	return pAmbFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pAmbFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pAmbFemaleExtra3):
#	kDAmbugObj.Print("Configuring AmbFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pAmbFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY AmbFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pAmbFemaleExtra3)

	pAmbFemaleExtra3.SetAsExtra(1)
	pAmbFemaleExtra3.SetHidden(1)

	pAmbFemaleExtra3.SetLocation("DBL1M")
#	kDAmbugObj.Print("Finished configuring AmbFemaleExtra3")

###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pAmbMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Ambassador bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForAmbassador")
	pAmbMaleExtra3.ClearAnimations()

	# Register animation mappings
	pAmbMaleExtra3.AddAnimation("AmbL1MToG", "Bridge.Characters.AmbMediumAnimations.AmbL1ToG3")
	pAmbMaleExtra3.AddAnimation("AmbG3MToL", "Bridge.Characters.AmbMediumAnimations.AmbG3ToL1")
	pAmbMaleExtra3.AddAnimation("StandingAmbG3M", "Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")
	pAmbMaleExtra3.SetStanding(1)

	# Hit animations
	pAmbMaleExtra3.AddAnimation("AmbG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pAmbMaleExtra3.AddAnimation("AmbG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pAmbMaleExtra3.AddAnimation("AmbG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pAmbMaleExtra3.AddAnimation("AmbG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pAmbMaleExtra3.AddAnimation("AmbG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pAmbMaleExtra3.SetAsExtra(1)
	pAmbMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pAmbMaleExtra3)

	pAmbMaleExtra3.SetLocation("AmbL1M")
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
#	Args:	pAmbFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbFemaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
#	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")
	pAmbFemaleExtra3.AddRandomAnimation("Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")


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
	# AmbFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
