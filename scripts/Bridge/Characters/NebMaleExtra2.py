from bcdebug import debug
###############################################################################
#	Filename:	NebMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador NebMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDNebugObj = App.CPyDNebug()

###############################################################################
#	CreateCharacter()
#
#	Create NebMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDNebugObj.Print("Creating NebMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("NebMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyNebMaleM/BodyNebMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pNebMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyNebMaleM/BodyNebMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pNebMaleExtra2.ReplacNebodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyNebMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/NebMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pNebMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pNebMaleExtra2)

	# Setup the character configuration
	pNebMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pNebMaleExtra2.SetGender(App.CharacterClass.MALE)
	pNebMaleExtra2.SetRandomAnimationChance(.75)
	pNebMaleExtra2.SetBlinkChance(0.1)
	pNebMaleExtra2.SetCharacterName("MaleExtra2")

	pNebMaleExtra2.SetHidden(1)

	# Load NebMaleExtra2's generic sounds
	LoadSounds()

	# Create NebMaleExtra2's menus
	#import NebMaleExtra2MenuHandlers
	#NebMaleExtra2MenuHandlers.CreateMenus(pNebMaleExtra2)

	pNebMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pNebMaleExtra2.GetDatabase(), "NebMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDNebugObj.Print("Finished creating NebMaleExtra2")
	return pNebMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pNebMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pNebMaleExtra2):
#	kDNebugObj.Print("Configuring NebMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pNebMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY NebMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pNebMaleExtra2)

	pNebMaleExtra2.SetAsExtra(1)
	pNebMaleExtra2.SetHidden(1)

	pNebMaleExtra2.SetLocation("DBL2M")
#	kDNebugObj.Print("Finished configuring NebMaleExtra2")


###############################################################################
#	ConfigureForNebula()
#
#	Configure ourselves for the Nebula bridge
#
#	Args:	pNebMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForNebula(pNebMaleExtra2):
#	kDNebugObj.Print("Configuring NebMaleExtra2 for the Nebula bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForNebula")
	pNebMaleExtra2.ClearAnimations()

	# Register animation mappings
	pNebMaleExtra2.AddAnimation("NebL2MToG", "Bridge.Characters.NebMediumAnimations.NebL2ToG2")
	pNebMaleExtra2.AddAnimation("NebG2MToL", "Bridge.Characters.NebMediumAnimations.NebG2ToL2")
	pNebMaleExtra2.AddAnimation("StandingNebG2M", "Bridge.Characters.CommonAnimations.Standing")
	pNebMaleExtra2.SetStanding(1)

	# Hit animations
	pNebMaleExtra2.AddAnimation("NebG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pNebMaleExtra2.AddAnimation("NebG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pNebMaleExtra2.AddAnimation("NebG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pNebMaleExtra2.AddAnimation("NebG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pNebMaleExtra2.AddAnimation("NebG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pNebMaleExtra2.SetAsExtra(1)
	pNebMaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pNebMaleExtra2)

	pNebMaleExtra2.SetLocation("NebL2M")
#	kDNebugObj.Print("Finished configuring NebMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pNebMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pNebMaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.PushingButtons")
#	pNebMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleSlide")


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
	# NebMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
