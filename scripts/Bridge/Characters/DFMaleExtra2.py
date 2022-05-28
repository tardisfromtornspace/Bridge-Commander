from bcdebug import debug
###############################################################################
#	Filename:	DFMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador DFMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDDFugObj = App.CPyDDFug()

###############################################################################
#	CreateCharacter()
#
#	Create DFMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDDFugObj.Print("Creating DFMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("DFMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyDFMaleM/BodyDFMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pDFMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyDFMaleM/BodyDFMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pDFMaleExtra2.ReplacDFodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyDFMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/DFMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pDFMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pDFMaleExtra2)

	# Setup the character configuration
	pDFMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pDFMaleExtra2.SetGender(App.CharacterClass.MALE)
	pDFMaleExtra2.SetRandomAnimationChance(.75)
	pDFMaleExtra2.SetBlinkChance(0.1)
	pDFMaleExtra2.SetCharacterName("MaleExtra2")

	pDFMaleExtra2.SetHidden(1)

	# Load DFMaleExtra2's generic sounds
	LoadSounds()

	# Create DFMaleExtra2's menus
	#import DFMaleExtra2MenuHandlers
	#DFMaleExtra2MenuHandlers.CreateMenus(pDFMaleExtra2)

	pDFMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pDFMaleExtra2.GetDatabase(), "DFMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDDFugObj.Print("Finished creating DFMaleExtra2")
	return pDFMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pDFMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pDFMaleExtra2):
#	kDDFugObj.Print("Configuring DFMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pDFMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY DFMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pDFMaleExtra2)

	pDFMaleExtra2.SetAsExtra(1)
	pDFMaleExtra2.SetHidden(1)

	pDFMaleExtra2.SetLocation("DBL2M")
#	kDDFugObj.Print("Finished configuring DFMaleExtra2")


###############################################################################
#	ConfigureForDefiant()
#
#	Configure ourselves for the Defiant bridge
#
#	Args:	pDFMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForDefiant(pDFMaleExtra2):
#	kDDFugObj.Print("Configuring DFMaleExtra2 for the Defiant bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForDefiant")
	pDFMaleExtra2.ClearAnimations()

	# Register animation mappings
	pDFMaleExtra2.AddAnimation("DFL2MToG", "Bridge.Characters.DFMediumAnimations.DFL2ToG2")
	pDFMaleExtra2.AddAnimation("DFG2MToL", "Bridge.Characters.DFMediumAnimations.DFG2ToL2")
	pDFMaleExtra2.AddAnimation("StandingDFG2M", "Bridge.Characters.CommonAnimations.Standing")
	pDFMaleExtra2.SetStanding(1)

	# Hit animations
	pDFMaleExtra2.AddAnimation("DFG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pDFMaleExtra2.AddAnimation("DFG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pDFMaleExtra2.AddAnimation("DFG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pDFMaleExtra2.AddAnimation("DFG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pDFMaleExtra2.AddAnimation("DFG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pDFMaleExtra2.SetAsExtra(1)
	pDFMaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pDFMaleExtra2)

	pDFMaleExtra2.SetLocation("DFL2M")
#	kDDFugObj.Print("Finished configuring DFMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pDFMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pDFMaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pDFMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# DFMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
