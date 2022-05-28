from bcdebug import debug
###############################################################################
#	Filename:	NebMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador NebMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDNebugObj = App.CPyDNebug()

###############################################################################
#	CreateCharacter()
#
#	Create NebMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDNebugObj.Print("Creating NebMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("NebMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyNebMaleM/BodyNebMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pNebMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyNebMaleM/BodyNebMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pNebMaleExtra1.ReplacNebodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyNebMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/NebMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pNebMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebMaleExtra1)

	# Setup the character configuration
	pNebMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pNebMaleExtra1.SetGender(App.CharacterClass.MALE)
	pNebMaleExtra1.SetRandomAnimationChance(.75)
	pNebMaleExtra1.SetBlinkChance(0.1)
	pNebMaleExtra1.SetCharacterName("MaleExtra1")

	pNebMaleExtra1.SetHidden(1)

	# Load NebMaleExtra1's generic sounds
	LoadSounds()

	# Create NebMaleExtra1's menus
	#import NebMaleExtra1MenuHandlers
	#NebMaleExtra1MenuHandlers.CreateMenus(pNebMaleExtra1)

	pNebMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pNebMaleExtra1.GetDatabase(), "NebMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDNebugObj.Print("Finished creating NebMaleExtra1")
	return pNebMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pNebMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pNebMaleExtra1):
#	kDNebugObj.Print("Configuring NebMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pNebMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY NebMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pNebMaleExtra1)

	pNebMaleExtra1.SetAsExtra(1)
	pNebMaleExtra1.SetHidden(1)

	pNebMaleExtra1.SetLocation("DBL2M")
#	kDNebugObj.Print("Finished configuring NebMaleExtra1")


###############################################################################
#	ConfigureForSovereign()
#
#	Configure ourselves for the Nebula bridge
#
#	Args:	pNebMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("NebL2MToG", "Bridge.Characters.NebMediumAnimations.NebL2ToG1")
	pMaleExtra1.AddAnimation("NebG1MToL", "Bridge.Characters.NebMediumAnimations.NebG1ToL2")
	pMaleExtra1.AddAnimation("StandingNebG1M", "Bridge.Characters.CommonAnimations.Standing")
	pMaleExtra1.SetStanding(1)

	# Interaction
	pMaleExtra1.AddRandomAnimation("Bridge.Characters.NebMediumAnimations.NebCConsoleInteraction", App.CharacterClass.STANDING_ONLY, 25, 1)

	# So the mission builders can force the call
	pMaleExtra1.AddAnimation("PushingButtons", "Bridge.Characters.SmallAnimations.NebECConsoleInteraction")

	# Hit animations
	pMaleExtra1.AddAnimation("NebG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pMaleExtra1.AddAnimation("NebG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pMaleExtra1.AddAnimation("NebG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("NebG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("NebL2M")
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
#	Args:	pNebMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebMaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	# pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	# pNebMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# NebMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
