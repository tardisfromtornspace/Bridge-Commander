from bcdebug import debug
###############################################################################
#	Filename:	SCPMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador SCPMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDSCPugObj = App.CPyDSCPug()

###############################################################################
#	CreateCharacter()
#
#	Create SCPMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDSCPugObj.Print("Creating SCPMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("SCPMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodySCPMaleM/BodySCPMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pSCPMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodySCPMaleM/BodySCPMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pSCPMaleExtra2.ReplacSCPodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodySCPMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/SCPMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pSCPMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pSCPMaleExtra2)

	# Setup the character configuration
	pSCPMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pSCPMaleExtra2.SetGender(App.CharacterClass.MALE)
	pSCPMaleExtra2.SetRandomAnimationChance(.75)
	pSCPMaleExtra2.SetBlinkChance(0.1)
	pSCPMaleExtra2.SetCharacterName("MaleExtra2")

	pSCPMaleExtra2.SetHidden(1)

	# Load SCPMaleExtra2's generic sounds
	LoadSounds()

	# Create SCPMaleExtra2's menus
	#import SCPMaleExtra2MenuHandlers
	#SCPMaleExtra2MenuHandlers.CreateMenus(pSCPMaleExtra2)

	pSCPMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pSCPMaleExtra2.GetDatabase(), "SCPMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDSCPugObj.Print("Finished creating SCPMaleExtra2")
	return pSCPMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pSCPMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pSCPMaleExtra2):
#	kDSCPugObj.Print("Configuring SCPMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pSCPMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY SCPMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pSCPMaleExtra2)

	pSCPMaleExtra2.SetAsExtra(1)
	pSCPMaleExtra2.SetHidden(1)

	pSCPMaleExtra2.SetLocation("DBL2M")
#	kDSCPugObj.Print("Finished configuring SCPMaleExtra2")


###############################################################################
#	ConfigureForGalor()
#
#	Configure ourselves for the Galor bridge
#
#	Args:	pSCPMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalor(pSCPMaleExtra2):
#	kDSCPugObj.Print("Configuring SCPMaleExtra2 for the Galor bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalor")
	pSCPMaleExtra2.ClearAnimations()

	# Register animation mappings
	pSCPMaleExtra2.AddAnimation("SCPL2MToG", "Bridge.Characters.SCPMediumAnimations.SCPL2ToG2")
	pSCPMaleExtra2.AddAnimation("SCPG2MToL", "Bridge.Characters.SCPMediumAnimations.SCPG2ToL2")
	pSCPMaleExtra2.AddAnimation("StandingSCPG2M", "Bridge.Characters.SCPMediumAnimations.SCP_extra2_M_interaction")
	pSCPMaleExtra2.SetStanding(1)

	# Hit animations
	pSCPMaleExtra2.AddAnimation("SCPG2MHitStanding", "Bridge.Characters.SCPMediumAnimations.SCPCHit")
	pSCPMaleExtra2.AddAnimation("SCPG2MHitHardStanding", "Bridge.Characters.SCPMediumAnimations.SCPCHitHard")
	pSCPMaleExtra2.AddAnimation("SCPG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pSCPMaleExtra2.AddAnimation("SCPG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pSCPMaleExtra2.AddAnimation("SCPG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pSCPMaleExtra2.SetAsExtra(1)
	pSCPMaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pSCPMaleExtra2)

	pSCPMaleExtra2.SetLocation("SCPL2M")
#	kDSCPugObj.Print("Finished configuring SCPMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pSCPMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pSCPMaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.SCPMediumAnimations.SCP_extra2_M_interaction")
#	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
#	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pSCPMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# SCPMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
