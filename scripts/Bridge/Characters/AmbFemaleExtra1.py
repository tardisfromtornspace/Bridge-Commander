from bcdebug import debug
###############################################################################
#	Filename:	AmbFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador AmbFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDAmbugObj = App.CPyDAmbug()

###############################################################################
#	CreateCharacter()
#
#	Create AmbFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDAmbugObj.Print("Creating AmbFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("AmbFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif", None)
	pAmbFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	pAmbFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pAmbFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pAmbFemaleExtra1)

	# Setup the character configuration
	pAmbFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pAmbFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pAmbFemaleExtra1.SetRandomAnimationChance(.75)
	pAmbFemaleExtra1.SetBlinkChance(0.1)
	pAmbFemaleExtra1.SetCharacterName("FemaleExtra1")

	pAmbFemaleExtra1.SetHidden(1)

	# Load AmbFemaleExtra1's generic sounds
	LoadSounds()

	# Create AmbFemaleExtra1's menus
	#import AmbFemaleExtra1MenuHandlers
	#AmbFemaleExtra1MenuHandlers.CreateMenus(pAmbFemaleExtra1)

	pAmbFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pAmbFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pAmbFemaleExtra1.SetLocation("")

#	kDAmbugObj.Print("Finished creating AmbFemaleExtra1")
	return pAmbFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pAmbFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pAmbFemaleExtra1):
#	kDAmbugObj.Print("Configuring AmbFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pAmbFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY AmbFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pAmbFemaleExtra1)

	pAmbFemaleExtra1.SetAsExtra(1)
	pAmbFemaleExtra1.SetHidden(1)

	pAmbFemaleExtra1.SetLocation("DBL2M")
#	kDAmbugObj.Print("Finished configuring AmbFemaleExtra1")

###############################################################################
#	ConfigureForAmbassador()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pAmbFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForAmbassador(pFemaleExtra1):
#	kDAmbugObj.Print("Configuring AmbFemaleExtra1 for the Ambassador bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForAmbassador")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	#pFemaleExtra1.AddAnimation("AmbL2MToG", "Bridge.Characters.AmbMediumAnimations.AmbL2ToG1")
	#pFemaleExtra1.AddAnimation("AmbG1MToL", "Bridge.Characters.AmbMediumAnimations.AmbG1ToL2")
	#pFemaleExtra1.AddAnimation("StandingAmbG1M", "Bridge.Characters.CommonAnimations.Standing")
	#pFemaleExtra1.SetStanding(1)

	# Hit animations
	#pFemaleExtra1.AddAnimation("AmbG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pFemaleExtra1.AddAnimation("AmbG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pFemaleExtra1.AddAnimation("AmbG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pFemaleExtra1.AddAnimation("AmbG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pFemaleExtra1.AddAnimation("AmbG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("AmbL2M")
#	kDAmbugObj.Print("Finished configuring AmbFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pAmbFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pAmbFemaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pAmbFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# AmbFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
