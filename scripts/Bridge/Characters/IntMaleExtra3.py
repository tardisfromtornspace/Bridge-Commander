from bcdebug import debug
###############################################################################
#	Filename:	IntMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador IntMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDIntugObj = App.CPyDIntug()

###############################################################################
#	CreateCharacter()
#
#	Create IntMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDIntugObj.Print("Creating IntMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("IntMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyIntMaleM/BodyIntMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pIntMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyIntMaleM/BodyIntMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pIntMaleExtra3.ReplacIntodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyIntMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/IntMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pIntMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pIntMaleExtra3)

	# Setup the character configuration
	pIntMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pIntMaleExtra3.SetGender(App.CharacterClass.MALE)
	pIntMaleExtra3.SetRandomAnimationChance(.75)
	pIntMaleExtra3.SetBlinkChance(0.1)
	pIntMaleExtra3.SetCharacterName("MaleExtra3")

	pIntMaleExtra3.SetHidden(0)

	# Load IntMaleExtra3's generic sounds
	LoadSounds()

	# Create IntMaleExtra3's menus
	#import IntMaleExtra3MenuHandlers
	#IntMaleExtra3MenuHandlers.CreateMenus(pIntMaleExtra3)

	pIntMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pIntMaleExtra3.GetDatabase(), "IntMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDIntugObj.Print("Finished creating IntMaleExtra3")
	return pIntMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pIntMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pIntMaleExtra3):
#	kDIntugObj.Print("Configuring IntMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pIntMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY IntMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pIntMaleExtra3)

	pIntMaleExtra3.SetAsExtra(1)
	pIntMaleExtra3.SetHidden(0)

	pIntMaleExtra3.SetLocation("DBL1M")
#	kDIntugObj.Print("Finished configuring IntMaleExtra3")

###############################################################################
#	ConfigureForIntrepid()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForIntrepid(pIntMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Sovereign bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForIntrepid")
	pIntMaleExtra3.ClearAnimations()

	# Register animation mappings
	pIntMaleExtra3.AddAnimation("IntL1MToG", "Bridge.Characters.IntMediumAnimations.IntL1ToG3")
	pIntMaleExtra3.AddAnimation("IntG3MToL", "Bridge.Characters.IntMediumAnimations.IntG3ToL1")
	#pIntMaleExtra3.AddAnimation("StandingIntG3M", "Bridge.Characters.CommonAnimations.Seated")
	pIntMaleExtra3.SetStanding(0)

	# Hit animations
	#pIntMaleExtra3.AddAnimation("IntG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pIntMaleExtra3.AddAnimation("IntG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pIntMaleExtra3.AddAnimation("IntG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pIntMaleExtra3.AddAnimation("IntG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pIntMaleExtra3.AddAnimation("IntG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pIntMaleExtra3.SetAsExtra(1)
	pIntMaleExtra3.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pIntMaleExtra3)

	pIntMaleExtra3.SetLocation("IntL1M")
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
#	Args:	pIntMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pIntMaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")

##Standing Anims

	#pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	#pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	#pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	#pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	#pIntMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# IntMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
