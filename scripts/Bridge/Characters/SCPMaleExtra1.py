from bcdebug import debug
###############################################################################
#	Filename:	SCPMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador SCPMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDeugObj = App.CPyDDeug()

###############################################################################
#	CreateCharacter()
#
#	Create SCPMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDSCPugObj.Print("Creating SCPMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("SCPMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodySCPMaleM/BodySCPMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pSCPMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodySCPMaleM/BodySCPMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pSCPMaleExtra1.ReplacSCPodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodySCPMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/SCPMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPMaleExtra1)

	# Setup the character configuration
	pSCPMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pSCPMaleExtra1.SetGender(App.CharacterClass.MALE)
	pSCPMaleExtra1.SetRandomAnimationChance(.75)
	pSCPMaleExtra1.SetBlinkChance(0.1)
	pSCPMaleExtra1.SetCharacterName("MaleExtra1")

	pSCPMaleExtra1.SetHidden(1)

	# Load SCPMaleExtra1's generic sounds
	LoadSounds()

	# Create SCPMaleExtra1's menus
	#import SCPMaleExtra1MenuHandlers
	#SCPMaleExtra1MenuHandlers.CreateMenus(pSCPMaleExtra1)

	pSCPMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pSCPMaleExtra1.GetDatabase(), "SCPMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDDebugObj.Print("Finished creating SCPMaleExtra1")
	return pSCPMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pSCPMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pSCPMaleExtra1):
#	kDDebugObj.Print("Configuring SCPMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pSCPMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY SCPMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pSCPMaleExtra1)

	pSCPMaleExtra1.SetAsExtra(1)
	pSCPMaleExtra1.SetHidden(1)

	pSCPMaleExtra1.SetLocation("DBL2M")
#	kDDebugObj.Print("Finished configuring SCPMaleExtra1")


###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pSCPMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the Galor bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalor")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("SCPL2MToG", "Bridge.Characters.SCPMediumAnimations.SCPL2ToG1")
	pMaleExtra1.AddAnimation("SCPG1MToL", "Bridge.Characters.SCPMediumAnimations.SCPG1ToL2")
	pMaleExtra1.AddAnimation("StandingSCPG1M", "Bridge.Characters.CommonAnimations.Standing")
	pMaleExtra1.SetStanding(1)

	# Hit animations
	pMaleExtra1.AddAnimation("SCPG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pMaleExtra1.AddAnimation("SCPG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pMaleExtra1.AddAnimation("SCPG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("SCPG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("SCPL2M")
#	kDebugObj.Print("Finished configuring MaleExtra1")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pSCPMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPMaleExtra1):
	#pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	#pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	#pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	#pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	debug(__name__ + ", AddCommonAnimations")
	pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	#pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.SCP_extra1_M_interaction_1")
	pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.SCP_extra1_M_interaction_2")
	#pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	#pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	#pSCPMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# SCPMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
