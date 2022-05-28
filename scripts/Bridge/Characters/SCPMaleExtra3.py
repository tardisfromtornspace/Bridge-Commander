from bcdebug import debug
###############################################################################
#	Filename:	SCPMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador SCPMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDSCPug()

###############################################################################
#	CreateCharacter()
#
#	Create SCPMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating SCPMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("SCPMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodySCPMaleM/BodySCPMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pSCPMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodySCPMaleM/BodySCPMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pSCPMaleExtra3.ReplacSCPodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodySCPMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/SCPMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPMaleExtra3)

	# Setup the character configuration
	pSCPMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pSCPMaleExtra3.SetGender(App.CharacterClass.MALE)
	pSCPMaleExtra3.SetRandomAnimationChance(.75)
	pSCPMaleExtra3.SetBlinkChance(0.1)
	pSCPMaleExtra3.SetCharacterName("MaleExtra3")

	pSCPMaleExtra3.SetHidden(1)

	# Load SCPMaleExtra3's generic sounds
	LoadSounds()

	# Create SCPMaleExtra3's menus
	#import SCPMaleExtra3MenuHandlers
	#SCPMaleExtra3MenuHandlers.CreateMenus(pSCPMaleExtra3)

	pSCPMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pSCPMaleExtra3.GetDatabase(), "SCPMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating SCPMaleExtra3")
	return pSCPMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pSCPMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pSCPMaleExtra3):
#	kDebugObj.Print("Configuring SCPMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pSCPMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY SCPMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pSCPMaleExtra3)

	pSCPMaleExtra3.SetAsExtra(1)
	pSCPMaleExtra3.SetHidden(1)

	pSCPMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring SCPMaleExtra3")

###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pSCPMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Galor bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalor")
	pSCPMaleExtra3.ClearAnimations()

	# Register animation mappings
	pSCPMaleExtra3.AddAnimation("SCPL1MToG", "Bridge.Characters.SCPMediumAnimations.SCPL1ToG3")
	pSCPMaleExtra3.AddAnimation("SCPG3MToL", "Bridge.Characters.SCPMediumAnimations.SCPG3ToL1")
	pSCPMaleExtra3.AddAnimation("StandingSCPG3M", "Bridge.Characters.CommonAnimations.Standing")
	pSCPMaleExtra3.SetStanding(1)

	# Hit animations
	pSCPMaleExtra3.AddAnimation("SCPG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pSCPMaleExtra3.AddAnimation("SCPG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pSCPMaleExtra3.AddAnimation("SCPG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pSCPMaleExtra3.AddAnimation("SCPG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pSCPMaleExtra3.AddAnimation("SCPG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pSCPMaleExtra3.SetAsExtra(1)
	pSCPMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pSCPMaleExtra3)

	pSCPMaleExtra3.SetLocation("SCPL1M")
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
#	Args:	pSCPMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPMaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.SCP_extra3_M_interaction")
	#pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	#pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	#pSCPMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# SCPMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
