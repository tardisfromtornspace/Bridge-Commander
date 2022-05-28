from bcdebug import debug
###############################################################################
#	Filename:	ENBFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador ENBFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create ENBFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating ENBFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("ENBFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pENBFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pENBFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/ENBFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pENBFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pENBFemaleExtra2)

	# Setup the character configuration
	pENBFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pENBFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pENBFemaleExtra2.SetRandomAnimationChance(.75)
	pENBFemaleExtra2.SetBlinkChance(0.1)
	pENBFemaleExtra2.SetCharacterName("FemaleExtra2")

	pENBFemaleExtra2.SetHidden(0)

	# Load ENBFemaleExtra2's generic sounds
	LoadSounds()

	# Create ENBFemaleExtra2's menus
	#import ENBFemaleExtra2MenuHandlers
	#ENBFemaleExtra2MenuHandlers.CreateMenus(pENBFemaleExtra2)

	pENBFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pENBFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Seated")
	pENBFemaleExtra2.SetLocation("")

#	kDebugObj.Print("Finished creating ENBFemaleExtra2")
	return pENBFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pENBFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pENBFemaleExtra2):
#	kDebugObj.Print("Configuring ENBFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pENBFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY ENBFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pENBFemaleExtra2)

	pENBFemaleExtra2.SetAsExtra(1)
	pENBFemaleExtra2.SetHidden(0)

	pENBFemaleExtra2.SetLocation("DBL2M")
#	kDebAugObj.Print("Finished configuring ENBFemaleExtra2")


###############################################################################
#	ConfigureForEnterpriseB()
#
#	Configure ourselves for the EnterpriseB bridge
#
#	Args:	pENBFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForEnterpriseB(pENBFemaleExtra2):
#	kDebugObj.Print("Configuring ENBFemaleExtra2 for the EnterpriseB bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForEnterpriseB")
	pENBFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pENBFemaleExtra2.AddAnimation("ENBL2MToG", "Bridge.Characters.ENBMediumAnimations.ENBL2ToG2")
	pENBFemaleExtra2.AddAnimation("ENBG2MToL", "Bridge.Characters.ENBMediumAnimations.ENBG2ToL2")
	pENBFemaleExtra2.AddAnimation("SeatedENBG2M", "Bridge.Characters.CommonAnimations.SeatedM")
	pENBFemaleExtra2.SetStanding(0)

	# Hit animations
	pENBFemaleExtra2.AddAnimation("ENBG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pENBFemaleExtra2.AddAnimation("ENBG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")


	pENBFemaleExtra2.SetAsExtra(1)
	pENBFemaleExtra2.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pENBFemaleExtra2)

	pENBFemaleExtra2.SetLocation("ENBL2M")
#	kDebugObj.Print("Finished configuring ENBFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pENBFemaleExtra2	- our Character object
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
	# ENBFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
