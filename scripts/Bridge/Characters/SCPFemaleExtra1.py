from bcdebug import debug
###############################################################################
#	Filename:	SCPFemaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador SCPFemaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDSCPugObj = App.CPyDSCPug()

###############################################################################
#	CreateCharacter()
#
#	Create SCPFemaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDSCPugObj.Print("Creating SCPFemaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("SCPFemaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeaSCPem3/fem3_head.nif", None)
	pSCPFemaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeaSCPem3/fem3_head.nif")

	pSCPFemaleExtra1.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeSCPemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeaSCPem3/female_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPFemaleExtra1, "FemaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPFemaleExtra1)

	# Setup the character configuration
	pSCPFemaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pSCPFemaleExtra1.SetGender(App.CharacterClass.FEMALE)
	pSCPFemaleExtra1.SetRandomAnimationChance(.75)
	pSCPFemaleExtra1.SetBlinkChance(0.1)
	pSCPFemaleExtra1.SetCharacterName("FemaleExtra1")

	pSCPFemaleExtra1.SetHidden(1)

	# Load SCPFemaleExtra1's generic sounds
	LoadSounds()

	# Create SCPFemaleExtra1's menus
	#import SCPFemaleExtra1MenuHandlers
	#SCPFemaleExtra1MenuHandlers.CreateMenus(pSCPFemaleExtra1)

	pSCPFemaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pSCPFemaleExtra1.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pSCPFemaleExtra1.SetLocation("")

#	kDSCPugObj.Print("Finished creating SCPFemaleExtra1")
	return pSCPFemaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pSCPFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pSCPFemaleExtra1):
#	kDSCPugObj.Print("Configuring SCPFemaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pSCPFemaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY SCPFemaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pSCPFemaleExtra1)

	pSCPFemaleExtra1.SetAsExtra(1)
	pSCPFemaleExtra1.SetHidden(1)

	pSCPFemaleExtra1.SetLocation("DBL2M")
#	kDSCPugObj.Print("Finished configuring SCPFemaleExtra1")

###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pSCPFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pFemaleExtra1):
#	kDSCPugObj.Print("Configuring SCPFemaleExtra1 for the Galor bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalor")
	pFemaleExtra1.ClearAnimations()

	# Register animation mappings
	pFemaleExtra1.AddAnimation("SCPL2MToG", "Bridge.Characters.SCPMediumAnimations.SCPL2ToG1")
	pFemaleExtra1.AddAnimation("SCPG1MToL", "Bridge.Characters.SCPMediumAnimations.SCPG1ToL2")
	pFemaleExtra1.AddAnimation("StandingSCPG1M", "Bridge.Characters.CommonAnimations.Standing")
	pFemaleExtra1.SetStanding(1)

	# Hit animations
	pFemaleExtra1.AddAnimation("SCPG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pFemaleExtra1.AddAnimation("SCPG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pFemaleExtra1.AddAnimation("SCPG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pFemaleExtra1.AddAnimation("SCPG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pFemaleExtra1.AddAnimation("SCPG1MFly", "Bridge.Characters.CommonAnimations.Blast")

	pFemaleExtra1.SetAsExtra(1)
	pFemaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pFemaleExtra1)

	pFemaleExtra1.SetLocation("SCPL2M")
#	kDSCPugObj.Print("Finished configuring SCPFemaleExtra1")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pSCPFemaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPFemaleExtra1):
	#pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	#pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	#pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	debug(__name__ + ", AddCommonAnimations")
	pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.SCP_extra1_M_interaction_1")
	pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.SCP_extra1_M_interaction_2")
	pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")	
	#pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	#pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	#pSCPFemaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# SCPFemaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
