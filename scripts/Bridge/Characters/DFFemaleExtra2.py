from bcdebug import debug
###############################################################################
#	Filename:	DFFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador DFFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDFugObj = App.CPyDDFug()

###############################################################################
#	CreateCharacter()
#
#	Create DFFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDDFugObj.Print("Creating DFFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("DFFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pDFFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pDFFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/DFFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pDFFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFFemaleExtra2)

	# Setup the character configuration
	pDFFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pDFFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pDFFemaleExtra2.SetRandomAnimationChance(.75)
	pDFFemaleExtra2.SetBlinkChance(0.1)
	pDFFemaleExtra2.SetCharacterName("FemaleExtra2")

	pDFFemaleExtra2.SetHidden(1)

	# Load DFFemaleExtra2's generic sounds
	LoadSounds()

	# Create DFFemaleExtra2's menus
	#import DFFemaleExtra2MenuHandlers
	#DFFemaleExtra2MenuHandlers.CreateMenus(pDFFemaleExtra2)

	pDFFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pDFFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pDFFemaleExtra2.SetLocation("")

#	kDDFugObj.Print("Finished creating DFFemaleExtra2")
	return pDFFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pDFFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pDFFemaleExtra2):
#	kDDFugObj.Print("Configuring DFFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pDFFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY DFFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pDFFemaleExtra2)

	pDFFemaleExtra2.SetAsExtra(1)
	pDFFemaleExtra2.SetHidden(1)

	pDFFemaleExtra2.SetLocation("DBL2M")
#	kDDFugObj.Print("Finished configuring DFFemaleExtra2")


###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pDFFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pDFFemaleExtra2):
#	kDDFugObj.Print("Configuring DFFemaleExtra2 for the Defiant bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForDefiant")
	pDFFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pDFFemaleExtra2.AddAnimation("DFL2MToG", "Bridge.Characters.DFMediumAnimations.DFL2ToG2")
	pDFFemaleExtra2.AddAnimation("DFG2MToL", "Bridge.Characters.DFMediumAnimations.DFG2ToL2")
	pDFFemaleExtra2.AddAnimation("StandingDFG2M", "Bridge.Characters.CommonAnimations.Standing")
	pDFFemaleExtra2.SetStanding(1)

	# Hit animations
	pDFFemaleExtra2.AddAnimation("DFG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pDFFemaleExtra2.AddAnimation("DFG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pDFFemaleExtra2.AddAnimation("DFG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pDFFemaleExtra2.AddAnimation("DFG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pDFFemaleExtra2.AddAnimation("DFG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pDFFemaleExtra2.SetAsExtra(1)
	pDFFemaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pDFFemaleExtra2)

	pDFFemaleExtra2.SetLocation("DFL2M")
#	kDDFugObj.Print("Finished configuring DFFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pDFFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFFemaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pDFFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# DFFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
