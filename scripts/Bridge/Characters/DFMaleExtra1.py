from bcdebug import debug
###############################################################################
#	Filename:	DFMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador DFMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDFugObj = App.CPyDDFug()

###############################################################################
#	CreateCharacter()
#
#	Create DFMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDDFugObj.Print("Creating DFMaleExtra1")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("DFMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyDFMaleM/BodyDFMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pDFMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyDFMaleM/BodyDFMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pDFMaleExtra1.ReplacDFodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyDFMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/DFMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pDFMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFMaleExtra1)

	# Setup the character configuration
	pDFMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pDFMaleExtra1.SetGender(App.CharacterClass.MALE)
	pDFMaleExtra1.SetRandomAnimationChance(.75)
	pDFMaleExtra1.SetBlinkChance(0.1)
	pDFMaleExtra1.SetCharacterName("MaleExtra1")

	pDFMaleExtra1.SetHidden(1)

	# Load DFMaleExtra1's generic sounds
	LoadSounds()

	# Create DFMaleExtra1's menus
	#import DFMaleExtra1MenuHandlers
	#DFMaleExtra1MenuHandlers.CreateMenus(pDFMaleExtra1)

	pDFMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pDFMaleExtra1.GetDatabase(), "DFMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDDFugObj.Print("Finished creating DFMaleExtra1")
	return pDFMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pDFMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pDFMaleExtra1):
#	kDDFugObj.Print("Configuring DFMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pDFMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY DFMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pDFMaleExtra1)

	pDFMaleExtra1.SetAsExtra(1)
	pDFMaleExtra1.SetHidden(1)

	pDFMaleExtra1.SetLocation("DBL2M")
#	kDDFugObj.Print("Finished configuring DFMaleExtra1")


###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pDFMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the Defiant bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForDefiant")
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("DFL2MToG", "Bridge.Characters.DFMediumAnimations.DFL2ToG1")
	pMaleExtra1.AddAnimation("DFG1MToL", "Bridge.Characters.DFMediumAnimations.DFG1ToL2")
	pMaleExtra1.AddAnimation("StandingDFG1M", "Bridge.Characters.CommonAnimations.Standing")
	pMaleExtra1.SetStanding(1)

	# Hit animations
	pMaleExtra1.AddAnimation("DFG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pMaleExtra1.AddAnimation("DFG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pMaleExtra1.AddAnimation("DFG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("DFG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("DFL2M")
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
#	Args:	pDFMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFMaleExtra1):
	debug(__name__ + ", AddCommonAnimations")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pDFMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# DFMaleExtra1 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
