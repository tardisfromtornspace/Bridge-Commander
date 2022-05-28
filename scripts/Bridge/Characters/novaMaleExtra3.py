###############################################################################
#	Filename:	novaMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador novaMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDnovaug()

###############################################################################
#	CreateCharacter()
#
#	Create novaMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating novaMaleExtra3")

	if (pSet.GetObject("novaMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodynovaMaleM/BodynovaMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pnovaMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodynovaMaleM/BodynovaMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pnovaMaleExtra3.ReplacnovaodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodynovaMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/novaMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaMaleExtra3)

	# Setup the character configuration
	pnovaMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pnovaMaleExtra3.SetGender(App.CharacterClass.MALE)
	pnovaMaleExtra3.SetRandomAnimationChance(.75)
	pnovaMaleExtra3.SetBlinkChance(0.1)
	pnovaMaleExtra3.SetCharacterName("MaleExtra3")

	pnovaMaleExtra3.SetHidden(1)

	# Load novaMaleExtra3's generic sounds
	LoadSounds()

	# Create novaMaleExtra3's menus
	#import novaMaleExtra3MenuHandlers
	#novaMaleExtra3MenuHandlers.CreateMenus(pnovaMaleExtra3)

	pnovaMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pnovaMaleExtra3.GetDatabase(), "novaMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating novaMaleExtra3")
	return pnovaMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pnovaMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pnovaMaleExtra3):
#	kDebugObj.Print("Configuring novaMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pnovaMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY novaMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pnovaMaleExtra3)

	pnovaMaleExtra3.SetAsExtra(1)
	pnovaMaleExtra3.SetHidden(1)

	pnovaMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring novaMaleExtra3")

###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pnovaMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pnovaMaleExtra3.ClearAnimations()

	# Register animation mappings
	pnovaMaleExtra3.AddAnimation("novaL1MToG", "Bridge.Characters.novaMediumAnimations.novaL1ToG3")
	pnovaMaleExtra3.AddAnimation("novaG3MToL", "Bridge.Characters.novaMediumAnimations.novaG3ToL1")
	pnovaMaleExtra3.AddAnimation("StandingnovaG3M", "Bridge.Characters.CommonAnimations.Standing")
	pnovaMaleExtra3.SetStanding(1)

	# Hit animations
	pnovaMaleExtra3.AddAnimation("novaG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pnovaMaleExtra3.AddAnimation("novaG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pnovaMaleExtra3.AddAnimation("novaG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pnovaMaleExtra3.AddAnimation("novaG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pnovaMaleExtra3.AddAnimation("novaG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pnovaMaleExtra3.SetAsExtra(1)
	pnovaMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pnovaMaleExtra3)

	pnovaMaleExtra3.SetLocation("novaL1M")
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
#	Args:	pnovaMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaMaleExtra3):
	pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	#pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	#pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	#pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	#pnovaMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# novaMaleExtra3 has no generic bridge sounds at this time
	#
	pass
