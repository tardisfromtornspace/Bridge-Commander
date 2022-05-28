###############################################################################
#	Filename:	novaMaleExtra1.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador novaMaleExtra1, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDnovaugObj = App.CPyDnovaug()

###############################################################################
#	CreateCharacter()
#
#	Create novaMaleExtra1 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDnovaugObj.Print("Creating novaMaleExtra1")

	if (pSet.GetObject("novaMaleExtra1") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra1")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodynovaMaleM/BodynovaMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif", None)
	pnovaMaleExtra1 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodynovaMaleM/BodynovaMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadPicard/Picard_head.nif")
	pnovaMaleExtra1.ReplacnovaodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodynovaMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadPicard/novaMale_ensignA_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaMaleExtra1, "MaleExtra1")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaMaleExtra1)

	# Setup the character configuration
	pnovaMaleExtra1.SetSize(App.CharacterClass.MEDIUM)
	pnovaMaleExtra1.SetGender(App.CharacterClass.MALE)
	pnovaMaleExtra1.SetRandomAnimationChance(.75)
	pnovaMaleExtra1.SetBlinkChance(0.1)
	pnovaMaleExtra1.SetCharacterName("MaleExtra1")

	pnovaMaleExtra1.SetHidden(1)

	# Load novaMaleExtra1's generic sounds
	LoadSounds()

	# Create novaMaleExtra1's menus
	#import novaMaleExtra1MenuHandlers
	#novaMaleExtra1MenuHandlers.CreateMenus(pnovaMaleExtra1)

	pnovaMaleExtra1.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pnovaMaleExtra1.GetDatabase(), "novaMaleExtra1NothingToAdd", "BridgeGeneric")

#	kDnovaugObj.Print("Finished creating novaMaleExtra1")
	return pnovaMaleExtra1

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pnovaMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pnovaMaleExtra1):
#	kDnovaugObj.Print("Configuring novaMaleExtra1 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pnovaMaleExtra1.ClearAnimations()

	#
	# *** CURRENTLY novaMaleExtra1 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pnovaMaleExtra1)

	pnovaMaleExtra1.SetAsExtra(1)
	pnovaMaleExtra1.SetHidden(1)

	pnovaMaleExtra1.SetLocation("DBL2M")
#	kDnovaugObj.Print("Finished configuring novaMaleExtra1")


###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pnovaMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pMaleExtra1):
#	kDebugObj.Print("Configuring MaleExtra1 for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pMaleExtra1.ClearAnimations()

	# Register animation mappings
	pMaleExtra1.AddAnimation("novaL2MToG", "Bridge.Characters.novaMediumAnimations.novaL2ToG1")
	pMaleExtra1.AddAnimation("novaG1MToL", "Bridge.Characters.novaMediumAnimations.novaG1ToL2")
	pMaleExtra1.AddAnimation("StandingnovaG1M", "Bridge.Characters.CommonAnimations.Standing")
	pMaleExtra1.SetStanding(1)

	# Hit animations
	pMaleExtra1.AddAnimation("novaG1MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pMaleExtra1.AddAnimation("novaG1MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pMaleExtra1.AddAnimation("novaG1MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pMaleExtra1.AddAnimation("novaG1MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")

	pMaleExtra1.SetAsExtra(1)
	pMaleExtra1.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pMaleExtra1)

	pMaleExtra1.SetLocation("novaL2M")
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
#	Args:	pnovaMaleExtra1	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaMaleExtra1):
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pnovaMaleExtra1.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")

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
	# novaMaleExtra1 has no generic bridge sounds at this time
	#
	pass
