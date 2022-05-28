from bcdebug import debug
###############################################################################
#	Filename:	ENAFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENAFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDFugObj = App.CPyDDFug()

###############################################################################
#	CreateCharacter()
#
#	Create ENAFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDDFugObj.Print("Creating ENAFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENAFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pENAFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pENAFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/ENAFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENAFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENAFemaleExtra2)

	# Setup the character configuration
	pENAFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pENAFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pENAFemaleExtra2.SetRandomAnimationChance(.75)
	pENAFemaleExtra2.SetBlinkChance(0.1)
	pENAFemaleExtra2.SetCharacterName("FemaleExtra2")

	pENAFemaleExtra2.SetHidden(1)

	# Load ENAFemaleExtra2's generic sounds
	LoadSounds()

	# Create ENAFemaleExtra2's menus
	#import ENAFemaleExtra2MenuHandlers
	#ENAFemaleExtra2MenuHandlers.CreateMenus(pENAFemaleExtra2)

	pENAFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENAFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pENAFemaleExtra2.SetLocation("")

#	kDDFugObj.Print("Finished creating ENAFemaleExtra2")
	return pENAFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENAFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENAFemaleExtra2):
#	kDDFugObj.Print("Configuring ENAFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENAFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY ENAFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENAFemaleExtra2)

	pENAFemaleExtra2.SetAsExtra(1)
	pENAFemaleExtra2.SetHidden(1)

	pENAFemaleExtra2.SetLocation("DBL2M")
#	kDDFAugObj.Print("Finished configuring ENAFemaleExtra2")


###############################################################################
#	ConfigureForEnterpriseA()
#
#	Configure ourselves for the EnterpriseA bridge
#
#	Args:	pENAFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseA(pENAFemaleExtra2):
#	kDDFugObj.Print("Configuring ENAFemaleExtra2 for the EnterpriseA bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseA")
	pENAFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pENAFemaleExtra2.AddAnimation("ENAL2MToG", "Bridge.Characters.ENAMediumAnimations.ENAL2ToG2")
	pENAFemaleExtra2.AddAnimation("ENAG2MToL", "Bridge.Characters.ENAMediumAnimations.ENAG2ToL2")
	pENAFemaleExtra2.AddAnimation("StandingENAG2M", "Bridge.Characters.CommonAnimations.Standing")
	pENAFemaleExtra2.SetStanding(1)

	# Hit animations
	pENAFemaleExtra2.AddAnimation("ENAG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pENAFemaleExtra2.AddAnimation("ENAG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pENAFemaleExtra2.AddAnimation("ENAG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENAFemaleExtra2.AddAnimation("ENAG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pENAFemaleExtra2.AddAnimation("ENAG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pENAFemaleExtra2.SetAsExtra(1)
	pENAFemaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pENAFemaleExtra2)

	pENAFemaleExtra2.SetLocation("ENAL2M")
#	kDDFugObj.Print("Finished configuring ENAFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENAFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pENAFemaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pENAFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# ENAFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
