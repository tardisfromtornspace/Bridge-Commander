from bcdebug import debug
###############################################################################
#	Filename:	AmbFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador AmbFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDAmbugObj = App.CPyDAmbug()

###############################################################################
#	CreateCharacter()
#
#	Create AmbFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDAmbugObj.Print("Creating AmbFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("AmbFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pAmbFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pAmbFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeAmbemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/AmbFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbFemaleExtra2)

	# Setup the character configuration
	pAmbFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pAmbFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pAmbFemaleExtra2.SetRandomAnimationChance(.75)
	pAmbFemaleExtra2.SetBlinkChance(0.1)
	pAmbFemaleExtra2.SetCharacterName("FemaleExtra2")

	pAmbFemaleExtra2.SetHidden(1)

	# Load AmbFemaleExtra2's generic sounds
	LoadSounds()

	# Create AmbFemaleExtra2's menus
	#import AmbFemaleExtra2MenuHandlers
	#AmbFemaleExtra2MenuHandlers.CreateMenus(pAmbFemaleExtra2)

	pAmbFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pAmbFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pAmbFemaleExtra2.SetLocation("")

#	kDAmbugObj.Print("Finished creating AmbFemaleExtra2")
	return pAmbFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pAmbFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pAmbFemaleExtra2):
#	kDAmbugObj.Print("Configuring AmbFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pAmbFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY AmbFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pAmbFemaleExtra2)

	pAmbFemaleExtra2.SetAsExtra(1)
	pAmbFemaleExtra2.SetHidden(1)

	pAmbFemaleExtra2.SetLocation("DBL2M")
#	kDAmbugObj.Print("Finished configuring AmbFemaleExtra2")


###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Ambassador bridge
#
#	Args:	pAmbFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pAmbFemaleExtra2):
#	kDAmbugObj.Print("Configuring AmbFemaleExtra2 for the Ambassador bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForAmbassador")
	pAmbFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pAmbFemaleExtra2.AddAnimation("AmbL2MToG", "Bridge.Characters.AmbMediumAnimations.AmbL2ToG2")
	pAmbFemaleExtra2.AddAnimation("AmbG2MToL", "Bridge.Characters.AmbMediumAnimations.AmbG2ToL2")
	pAmbFemaleExtra2.AddAnimation("StandingAmbG2M", "Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")
	pAmbFemaleExtra2.SetStanding(1)

	# Hit animations
	pAmbFemaleExtra2.AddAnimation("AmbG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pAmbFemaleExtra2.AddAnimation("AmbG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pAmbFemaleExtra2.AddAnimation("AmbG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pAmbFemaleExtra2.AddAnimation("AmbG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pAmbFemaleExtra2.AddAnimation("AmbG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pAmbFemaleExtra2.SetAsExtra(1)
	pAmbFemaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pAmbFemaleExtra2)

	pAmbFemaleExtra2.SetLocation("AmbL2M")
#	kDAmbugObj.Print("Finished configuring AmbFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pAmbFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbFemaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
#	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")
	pAmbFemaleExtra2.AddRandomAnimation("Bridge.Characters.AmbMediumAnimations.AmbCConsoleInteraction")


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
	# AmbFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
