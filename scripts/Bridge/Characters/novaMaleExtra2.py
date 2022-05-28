###############################################################################
#	Filename:	novaMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador novaMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDnovaugObj = App.CPyDnovaug()

###############################################################################
#	CreateCharacter()
#
#	Create novaMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDnovaugObj.Print("Creating novaMaleExtra2")

	if (pSet.GetObject("novaMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodynovaMaleM/BodynovaMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pnovaMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodynovaMaleM/BodynovaMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pnovaMaleExtra2.ReplacnovaodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodynovaMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/novaMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pnovaMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pnovaMaleExtra2)

	# Setup the character configuration
	pnovaMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pnovaMaleExtra2.SetGender(App.CharacterClass.MALE)
	pnovaMaleExtra2.SetRandomAnimationChance(.75)
	pnovaMaleExtra2.SetBlinkChance(0.1)
	pnovaMaleExtra2.SetCharacterName("MaleExtra2")

	pnovaMaleExtra2.SetHidden(0)

	# Load novaMaleExtra2's generic sounds
	LoadSounds()

	# Create novaMaleExtra2's menus
	#import novaMaleExtra2MenuHandlers
	#novaMaleExtra2MenuHandlers.CreateMenus(pnovaMaleExtra2)

	pnovaMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pnovaMaleExtra2.GetDatabase(), "novaMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDnovaugObj.Print("Finished creating novaMaleExtra2")
	return pnovaMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pnovaMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pnovaMaleExtra2):
#	kDnovaugObj.Print("Configuring novaMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	pnovaMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY novaMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pnovaMaleExtra2)

	pnovaMaleExtra2.SetAsExtra(1)
	pnovaMaleExtra2.SetHidden(0)
	pnovaMaleExtra2.SetStanding(0)

	pnovaMaleExtra2.SetLocation("DBL2M")
#	kDnovaugObj.Print("Finished configuring novaMaleExtra2")


###############################################################################
#	ConfigureForPrometheus()
#
#	Configure ourselves for the novaetheus bridge
#
#	Args:	pnovaMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForPrometheus(pnovaMaleExtra2):
#	kDnovaugObj.Print("Configuring novaMaleExtra2 for the novaetheus bridge")

	# Clear out any old animations from another configuration
	pnovaMaleExtra2.ClearAnimations()

	# Register animation mappings
	#pnovaMaleExtra2.AddAnimation("novaL2MToG", "Bridge.Characters.novaMediumAnimations.novaL2ToG2")
	#pnovaMaleExtra2.AddAnimation("novaG2MToL", "Bridge.Characters.novaMediumAnimations.novaG2ToL2")
	#pnovaMaleExtra2.AddAnimation("StandingnovaG2M", "Bridge.Characters.CommonAnimations.Standing")
	#pnovaMaleExtra2.SetStanding(1)

	# Hit animations
	#pnovaMaleExtra2.AddAnimation("novaG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	#pnovaMaleExtra2.AddAnimation("novaG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	#pnovaMaleExtra2.AddAnimation("novaG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	#pnovaMaleExtra2.AddAnimation("novaG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	#pnovaMaleExtra2.AddAnimation("novaG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pnovaMaleExtra2.SetAsExtra(1)
	pnovaMaleExtra2.SetHidden(0)

	# Add common animations.
	AddCommonAnimations(pnovaMaleExtra2)

	pnovaMaleExtra2.SetLocation("novaL3M")
#	kDnovaugObj.Print("Finished configuring novaMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pnovaMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pnovaMaleExtra2):
	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.novaMediumAnimations.nova_seated_interaction")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pnovaMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# novaMaleExtra2 has no generic bridge sounds at this time
	#
	pass
