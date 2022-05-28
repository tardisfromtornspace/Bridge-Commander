###############################################################################
#	Filename:	novaFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador novaFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDnovaugObj = App.CPyDnovaug()

###############################################################################
#	CreateCharacter()
#
#	Create novaFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDnovaugObj.Print("Creating novaFemaleExtra3")

	if (pSet.GetObject("novaFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pnovaFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadFem4/fem4_head.nif")

	pnovaFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadFem4/novaFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaFemaleExtra3)

	# Setup the character configuration
	pnovaFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pnovaFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pnovaFemaleExtra3.SetRandomAnimationChance(.75)
	pnovaFemaleExtra3.SetBlinkChance(0.1)
	pnovaFemaleExtra3.SetCharacterName("FemaleExtra3")

	pnovaFemaleExtra3.SetHidden(1)

	# Load novaFemaleExtra3's generic sounds
	LoadSounds()

	# Create novaFemaleExtra3's menus
	#import novaFemaleExtra3MenuHandlers
	#novaFemaleExtra3MenuHandlers.CreateMenus(pnovaFemaleExtra3)

	pnovaFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pnovaFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pnovaFemaleExtra3.SetLocation("")

#	kDnovaugObj.Print("Finished creating novaFemaleExtra3")
	return pnovaFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pnovaFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pnovaFemaleExtra3):
#	kDnovaugObj.Print("Configuring novaFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pnovaFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY novaFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pnovaFemaleExtra3)

	pnovaFemaleExtra3.SetAsExtra(1)
	pnovaFemaleExtra3.SetHidden(1)

	pnovaFemaleExtra3.SetLocation("DBL1M")
#	kDnovaugObj.Print("Finished configuring novaFemaleExtra3")

###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pnovaMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pnovaMaleExtra3.ClearAnimations()

	# Register animation mappings
	pnovaMaleExtra3.AddAnimation("novaL1MToG", "Bridge.Characters.novaMediumAnimations.novaL1ToG3")
	pnovaMaleExtra3.AddAnimation("novaG3MToL", "Bridge.Characters.novaMediumAnimations.novaG3ToL1")
	pnovaMaleExtra3.AddAnimation("StandingnovaG3M", "Bridge.Characters.CommonAnimations.Standing")
	pnovaMaleExtra3.SetStanding(1)

	# Hit animations
	pnovaMaleExtra3.AddAnimation("novaG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pnovaMaleExtra3.AddAnimation("novaG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pnovaMaleExtra3.AddAnimation("novaG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pnovaMaleExtra3.AddAnimation("novaG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pnovaMaleExtra3.AddAnimation("novaG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pnovaMaleExtra3.SetAsExtra(1)
	pnovaMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pnovaMaleExtra3)

	pnovaMaleExtra3.SetLocation("novaL1M")
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
#	Args:	pnovaFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaFemaleExtra3):
	pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	#pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	#pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	#pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	#pnovaFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# novaFemaleExtra3 has no generic bridge sounds at this time
	#
	pass
