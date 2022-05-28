from bcdebug import debug
###############################################################################
#	Filename:	NebMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador NebMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDNebug()

###############################################################################
#	CreateCharacter()
#
#	Create NebMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating NebMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("NebMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyNebMaleM/BodyNebMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pNebMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyNebMaleM/BodyNebMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pNebMaleExtra3.ReplacNebodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyNebMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/NebMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pNebMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebMaleExtra3)

	# Setup the character configuration
	pNebMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pNebMaleExtra3.SetGender(App.CharacterClass.MALE)
	pNebMaleExtra3.SetRandomAnimationChance(.75)
	pNebMaleExtra3.SetBlinkChance(0.1)
	pNebMaleExtra3.SetCharacterName("MaleExtra3")

	pNebMaleExtra3.SetHidden(1)

	# Load NebMaleExtra3's generic sounds
	LoadSounds()

	# Create NebMaleExtra3's menus
	#import NebMaleExtra3MenuHandlers
	#NebMaleExtra3MenuHandlers.CreateMenus(pNebMaleExtra3)

	pNebMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pNebMaleExtra3.GetDatabase(), "NebMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating NebMaleExtra3")
	return pNebMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pNebMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pNebMaleExtra3):
#	kDebugObj.Print("Configuring NebMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pNebMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY NebMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pNebMaleExtra3)

	pNebMaleExtra3.SetAsExtra(1)
	pNebMaleExtra3.SetHidden(1)

	pNebMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring NebMaleExtra3")

###############################################################################
#	ConfigureForNebula()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pNebMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pNebMaleExtra3.ClearAnimations()

	# Register animation mappings
	pNebMaleExtra3.AddAnimation("NebL1MToG", "Bridge.Characters.NebMediumAnimations.NebL1ToG3")
	pNebMaleExtra3.AddAnimation("NebG3MToL", "Bridge.Characters.NebMediumAnimations.NebG3ToL1")
	pNebMaleExtra3.AddAnimation("StandingNebG3M", "Bridge.Characters.CommonAnimations.Standing")
	pNebMaleExtra3.SetStanding(1)

	# Hit animations
	pNebMaleExtra3.AddAnimation("NebG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pNebMaleExtra3.AddAnimation("NebG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pNebMaleExtra3.AddAnimation("NebG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pNebMaleExtra3.AddAnimation("NebG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pNebMaleExtra3.AddAnimation("NebG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pNebMaleExtra3.SetAsExtra(1)
	pNebMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pNebMaleExtra3)

	pNebMaleExtra3.SetLocation("NebL1M")
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
#	Args:	pNebMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebMaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pNebMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# NebMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
