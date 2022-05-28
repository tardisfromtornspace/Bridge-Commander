from bcdebug import debug
###############################################################################
#	Filename:	IntMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador IntMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDIntugObj = App.CPyDIntug()

###############################################################################
#	CreateCharacter()
#
#	Create IntMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDIntugObj.Print("Creating IntMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("IntMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyIntMaleM/BodyIntMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pIntMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyIntMaleM/BodyIntMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pIntMaleExtra2.ReplacIntodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyIntMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/IntMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pIntMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntMaleExtra2)

	# Setup the character configuration
	pIntMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pIntMaleExtra2.SetGender(App.CharacterClass.MALE)
	pIntMaleExtra2.SetRandomAnimationChance(.75)
	pIntMaleExtra2.SetBlinkChance(0.1)
	pIntMaleExtra2.SetCharacterName("MaleExtra2")

	pIntMaleExtra2.SetHidden(1)

	# Load IntMaleExtra2's generic sounds
	LoadSounds()

	# Create IntMaleExtra2's menus
	#import IntMaleExtra2MenuHandlers
	#IntMaleExtra2MenuHandlers.CreateMenus(pIntMaleExtra2)

	pIntMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pIntMaleExtra2.GetDatabase(), "IntMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDIntugObj.Print("Finished creating IntMaleExtra2")
	return pIntMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pIntMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pIntMaleExtra2):
#	kDIntugObj.Print("Configuring IntMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pIntMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY IntMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pIntMaleExtra2)

	pIntMaleExtra2.SetAsExtra(1)
	pIntMaleExtra2.SetHidden(1)

	pIntMaleExtra2.SetLocation("DBL2M")
#	kDIntugObj.Print("Finished configuring IntMaleExtra2")


###############################################################################
#	ConfigureForIntrepid()
#
#	Configure ourselves for the Intrepid bridge
#
#	Args:	pIntMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pIntMaleExtra2):
#	kDIntugObj.Print("Configuring IntMaleExtra2 for the Intrepid bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForIntrepid")
	pIntMaleExtra2.ClearAnimations()

	# Register animation mappings
	pIntMaleExtra2.AddAnimation("IntL2MToG", "Bridge.Characters.IntMediumAnimations.IntL2ToG2")
	pIntMaleExtra2.AddAnimation("IntG2MToL", "Bridge.Characters.IntMediumAnimations.IntG2ToL2")
	pIntMaleExtra2.AddAnimation("StandingIntG2M", "Bridge.Characters.CommonAnimations.Standing")
	pIntMaleExtra2.SetStanding(1)

	# Hit animations
	pIntMaleExtra2.AddAnimation("IntG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pIntMaleExtra2.AddAnimation("IntG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pIntMaleExtra2.AddAnimation("IntG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pIntMaleExtra2.AddAnimation("IntG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pIntMaleExtra2.AddAnimation("IntG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pIntMaleExtra2.SetAsExtra(1)
	pIntMaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pIntMaleExtra2)

	pIntMaleExtra2.SetLocation("IntL2M")
#	kDIntugObj.Print("Finished configuring IntMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pIntMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntMaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.PushingButtons")
#	pIntMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.ConsoleSlide")


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
	# IntMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
