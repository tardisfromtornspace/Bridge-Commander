from bcdebug import debug
###############################################################################
#	Filename:	SCPFemaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador SCPFemaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDSCPugObj = App.CPyDSCPug()

###############################################################################
#	CreateCharacter()
#
#	Create SCPFemaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDSCPugObj.Print("Creating SCPFemaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("SCPFemaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("FemaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif", None)
	pSCPFemaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadLiu/liu_head.nif")

	pSCPFemaleExtra2.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FeSCPemTeal_body1.tga", CharacterPaths.g_pcHeadTexPath + "HeadLiu/SCPFemale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPFemaleExtra2, "FemaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPFemaleExtra2)

	# Setup the character configuration
	pSCPFemaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pSCPFemaleExtra2.SetGender(App.CharacterClass.FEMALE)
	pSCPFemaleExtra2.SetRandomAnimationChance(.75)
	pSCPFemaleExtra2.SetBlinkChance(0.1)
	pSCPFemaleExtra2.SetCharacterName("FemaleExtra2")

	pSCPFemaleExtra2.SetHidden(1)

	# Load SCPFemaleExtra2's generic sounds
	LoadSounds()

	# Create SCPFemaleExtra2's menus
	#import SCPFemaleExtra2MenuHandlers
	#SCPFemaleExtra2MenuHandlers.CreateMenus(pSCPFemaleExtra2)

	pSCPFemaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pSCPFemaleExtra2.AddAnimation("Place", "Bridge.Characters.CommonAnimations.Standing")
	pSCPFemaleExtra2.SetLocation("")

#	kDSCPugObj.Print("Finished creating SCPFemaleExtra2")
	return pSCPFemaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pSCPFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pSCPFemaleExtra2):
#	kDSCPugObj.Print("Configuring SCPFemaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pSCPFemaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY SCPFemaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pSCPFemaleExtra2)

	pSCPFemaleExtra2.SetAsExtra(1)
	pSCPFemaleExtra2.SetHidden(1)

	pSCPFemaleExtra2.SetLocation("DBL2M")
#	kDSCPugObj.Print("Finished configuring SCPFemaleExtra2")


###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pSCPFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pSCPFemaleExtra2):
#	kDSCPugObj.Print("Configuring SCPFemaleExtra2 for the Galor bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalor")
	pSCPFemaleExtra2.ClearAnimations()

	# Register animation mappings
	pSCPFemaleExtra2.AddAnimation("SCPL2MToG", "Bridge.Characters.SCPMediumAnimations.SCPL2ToG2")
	pSCPFemaleExtra2.AddAnimation("SCPG2MToL", "Bridge.Characters.SCPMediumAnimations.SCPG2ToL2")
	pSCPFemaleExtra2.AddAnimation("StandingSCPG2M", "Bridge.Characters.SCPMediumAnimations.SCP_extra2_M_interaction")
	pSCPFemaleExtra2.SetStanding(1)

	# Hit animations
	pSCPFemaleExtra2.AddAnimation("SCPG2MHitStanding", "Bridge.Characters.SCPMediumAnimations.SCPCHit")
	pSCPFemaleExtra2.AddAnimation("SCPG2MHitHardStanding", "Bridge.Characters.SCPMediumAnimations.SCPCHitHard")
	pSCPFemaleExtra2.AddAnimation("SCPG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pSCPFemaleExtra2.AddAnimation("SCPG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pSCPFemaleExtra2.AddAnimation("SCPG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pSCPFemaleExtra2.SetAsExtra(1)
	pSCPFemaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pSCPFemaleExtra2)

	pSCPFemaleExtra2.SetLocation("SCPL2M")
#	kDSCPugObj.Print("Finished configuring SCPFemaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pSCPFemaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPFemaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.SCP_extra2_M_interaction")
#	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pSCPFemaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# SCPFemaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
