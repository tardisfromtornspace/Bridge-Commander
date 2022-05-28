from bcdebug import debug
###############################################################################
#	Filename:	DFMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador DFMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDDFug()

###############################################################################
#	CreateCharacter()
#
#	Create DFMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating DFMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("DFMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyDFMaleM/BodyDFMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pDFMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyDFMaleM/BodyDFMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pDFMaleExtra3.ReplacDFodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyDFMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/DFMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pDFMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFMaleExtra3)

	# Setup the character configuration
	pDFMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pDFMaleExtra3.SetGender(App.CharacterClass.MALE)
	pDFMaleExtra3.SetRandomAnimationChance(.75)
	pDFMaleExtra3.SetBlinkChance(0.1)
	pDFMaleExtra3.SetCharacterName("MaleExtra3")

	pDFMaleExtra3.SetHidden(1)

	# Load DFMaleExtra3's generic sounds
	LoadSounds()

	# Create DFMaleExtra3's menus
	#import DFMaleExtra3MenuHandlers
	#DFMaleExtra3MenuHandlers.CreateMenus(pDFMaleExtra3)

	pDFMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pDFMaleExtra3.GetDatabase(), "DFMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating DFMaleExtra3")
	return pDFMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pDFMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pDFMaleExtra3):
#	kDebugObj.Print("Configuring DFMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pDFMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY DFMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pDFMaleExtra3)

	pDFMaleExtra3.SetAsExtra(1)
	pDFMaleExtra3.SetHidden(1)

	pDFMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring DFMaleExtra3")

###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pDFMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Defiant bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForDefiant")
	pDFMaleExtra3.ClearAnimations()

	# Register animation mappings
	pDFMaleExtra3.AddAnimation("DFL1MToG", "Bridge.Characters.DFMediumAnimations.DFL1ToG3")
	pDFMaleExtra3.AddAnimation("DFG3MToL", "Bridge.Characters.DFMediumAnimations.DFG3ToL1")
	pDFMaleExtra3.AddAnimation("StandingDFG3M", "Bridge.Characters.CommonAnimations.Standing")
	pDFMaleExtra3.SetStanding(1)

	# Hit animations
	pDFMaleExtra3.AddAnimation("DFG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pDFMaleExtra3.AddAnimation("DFG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pDFMaleExtra3.AddAnimation("DFG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pDFMaleExtra3.AddAnimation("DFG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pDFMaleExtra3.AddAnimation("DFG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pDFMaleExtra3.SetAsExtra(1)
	pDFMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pDFMaleExtra3)

	pDFMaleExtra3.SetLocation("DFL1M")
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
#	Args:	pDFMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFMaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pDFMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# DFMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
