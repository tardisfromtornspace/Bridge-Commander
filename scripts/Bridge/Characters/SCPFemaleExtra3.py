from bcdebug import debug
###############################################################################
#	Filename:	SCPFemaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador SCPFemaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDSCPugObj = App.CPyDSCPug()

###############################################################################
#	CreateCharacter()
#
#	Create SCPFemaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDSCPugObj.Print("Creating SCPFemaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("SCPFemaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pSCPFemaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeaSCPem4/fem4_head.nif")

	pSCPFemaleExtra3.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeSCPemGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeaSCPem4/SCPFemale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPFemaleExtra3, "FemaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPFemaleExtra3)

	# Setup the character configuration
	pSCPFemaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pSCPFemaleExtra3.SetGender(App.CharacterClass.FEMALE)
	pSCPFemaleExtra3.SetRandomAnimationChance(.75)
	pSCPFemaleExtra3.SetBlinkChance(0.1)
	pSCPFemaleExtra3.SetCharacterName("FemaleExtra3")

	pSCPFemaleExtra3.SetHidden(1)

	# Load SCPFemaleExtra3's generic sounds
	LoadSounds()

	# Create SCPFemaleExtra3's menus
	#import SCPFemaleExtra3MenuHandlers
	#SCPFemaleExtra3MenuHandlers.CreateMenus(pSCPFemaleExtra3)

	pSCPFemaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pSCPFemaleExtra3.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pSCPFemaleExtra3.SetLocation("")

#	kDSCPugObj.Print("Finished creating SCPFemaleExtra3")
	return pSCPFemaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pSCPFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pSCPFemaleExtra3):
#	kDSCPugObj.Print("Configuring SCPFemaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pSCPFemaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY SCPFemaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pSCPFemaleExtra3)

	pSCPFemaleExtra3.SetAsExtra(1)
	pSCPFemaleExtra3.SetHidden(1)

	pSCPFemaleExtra3.SetLocation("DBL1M")
#	kDSCPugObj.Print("Finished configuring SCPFemaleExtra3")

###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pSCPFemaleExtra3):
#	kDebugObj.Print("Configuring FemaleExtra3 for the Galor bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalor")
	pSCPFemaleExtra3.ClearAnimations()

	# Register animation mappings
	pSCPFemaleExtra3.AddAnimation("SCPL1MToG", "Bridge.Characters.SCPMediumAnimations.SCPL1ToG3")
	pSCPFemaleExtra3.AddAnimation("SCPG3MToL", "Bridge.Characters.SCPMediumAnimations.SCPG3ToL1")
	pSCPFemaleExtra3.AddAnimation("StandingSCPG3M", "Bridge.Characters.CommonAnimations.Standing")
	pSCPFemaleExtra3.SetStanding(1)

	# Hit animations
	pSCPFemaleExtra3.AddAnimation("SCPG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pSCPFemaleExtra3.AddAnimation("SCPG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pSCPFemaleExtra3.AddAnimation("SCPG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pSCPFemaleExtra3.AddAnimation("SCPG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pSCPFemaleExtra3.AddAnimation("SCPG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pSCPFemaleExtra3.SetAsExtra(1)
	pSCPFemaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pSCPFemaleExtra3)

	pSCPFemaleExtra3.SetLocation("SCPL1M")
#	kDebugObj.Print("Finished configuring FemaleExtra3")
###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pSCPFemaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPFemaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.SCP_extra3_M_interaction")
	#pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	#pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	#pSCPFemaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# SCPFemaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
