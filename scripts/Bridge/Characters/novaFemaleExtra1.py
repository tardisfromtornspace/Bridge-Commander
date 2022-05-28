###############################################################################
#	Filename:	novaFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador novaFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDnovaugObj = App.CPyDnovaug()

###############################################################################
#	CreateCharacter()
#
#	Create novaFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDnovaugObj.Print("Creating novaFemaleExtra1")

	if (pSet.GetObject("novaFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif", None)
	pnovaFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem3/fem3_head.nif")

	pnovaFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaFemaleExtra1)

	# Setup the character configuration
	pnovaFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pnovaFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pnovaFemaleExtra1.SetRandomAnimationChance(.75)
	pnovaFemaleExtra1.SetBlinkChance(0.1)
	pnovaFemaleExtra1.SetCharacterName("FemaleExtra1")

	pnovaFemaleExtra1.SetHidden(1)

	# Load novaFemaleExtra1's generic sounds
	LoadSounds()

	# Create novaFemaleExtra1's menus
	#import novaFemaleExtra1MenuHandlers
	#novaFemaleExtra1MenuHandlers.CreateMenus(pnovaFemaleExtra1)

	pnovaFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pnovaFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pnovaFemaleExtra1.SetLocation("")

#	kDnovaugObj.Print("Finished creating novaFemaleExtra1")
	return pnovaFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pnovaFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pnovaFemaleExtra1):
#	kDnovaugObj.Print("Configuring novaFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pnovaFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY novaFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pnovaFemaleExtra1)

	pnovaFemaleExtra1.SetAsExtra(1)
	pnovaFemaleExtra1.SetHidden(1)

	pnovaFemaleExtra1.SetLocation("DBL2M")
#	kDnovaugObj.Print("Finished configuring novaFemaleExtra1")

###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pnovaFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pFemaleExtra1):
#	kDnovaugObj.Print("Configuring novaFemaleExtra1 for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("novaL2MToG", "Bridge.Characters.novaMediumAnimations.novaL2ToG1")
	pFemaleExtra1.AddAnimation("novaG1MToL", "Bridge.Characters.novaMediumAnimations.novaG1ToL2")
	pFemaleExtra1.AddAnimation("StandingnovaG1M", "Bridge.Characters.CommonAnimations.Standing")
	pFemaleExtra1.SetStanding(1)

	# Hit animations
	pFemaleExtra1.AddAnimation("novaG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pFemaleExtra1.AddAnimation("novaG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pFemaleExtra1.AddAnimation("novaG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("novaG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pFemaleExtra1.AddAnimation("novaG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("novaL2M")
#	kDnovaugObj.Print("Finished configuring novaFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pnovaFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaFemaleExtra1):
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pnovaFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# novaFemaleExtra1 has no generic bridge sounds at this time
	#
	pass
