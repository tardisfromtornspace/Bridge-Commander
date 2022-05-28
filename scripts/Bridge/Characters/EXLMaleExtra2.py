from bcdebug import debug
###############################################################################
#	Filename:	EXLMaleExtra2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador EXLMaleExtra2, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create EXLMaleExtra2 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating EXLMaleExtra2")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("EXLMaleExtra2") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra2")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyEXLMaleM/BodyEXLMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif", None)
	pEXLMaleExtra2 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyEXLMaleM/BodyEXLMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/Miguel_head.nif")
	pEXLMaleExtra2.ReplacebodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyEXLMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadMiguel/EXLMale_ensignB_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLMaleExtra2, "MaleExtra2")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLMaleExtra2)

	# Setup the character configuration
	pEXLMaleExtra2.SetSize(App.CharacterClass.MEDIUM)
	pEXLMaleExtra2.SetGender(App.CharacterClass.MALE)
	pEXLMaleExtra2.SetRandomAnimationChance(.75)
	pEXLMaleExtra2.SetBlinkChance(0.1)
	pEXLMaleExtra2.SetCharacterName("MaleExtra2")

	pEXLMaleExtra2.SetHidden(1)

	# Load EXLMaleExtra2's generic sounds
	LoadSounds()

	# Create EXLMaleExtra2's menus
	#import EXLMaleExtra2MenuHandlers
	#EXLMaleExtra2MenuHandlers.CreateMenus(pEXLMaleExtra2)

	pEXLMaleExtra2.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pEXLMaleExtra2.GetDatabase(), "EXLMaleExtra2NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating EXLMaleExtra2")
	return pEXLMaleExtra2

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pEXLMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pEXLMaleExtra2):
#	kDebugObj.Print("Configuring EXLMaleExtra2 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pEXLMaleExtra2.ClearAnimations()

	#
	# *** CURRENTLY EXLMaleExtra2 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pEXLMaleExtra2)

	pEXLMaleExtra2.SetAsExtra(1)
	pEXLMaleExtra2.SetHidden(1)

	pEXLMaleExtra2.SetLocation("DBL2M")
#	kDebugObj.Print("Finished configuring EXLMaleExtra2")


###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pEXLMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pEXLMaleExtra2):
#	kDebugObj.Print("Configuring EXLMaleExtra2 for the Excelsior bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcelsior")
	pEXLMaleExtra2.ClearAnimations()

	# Register animation mappings
	pEXLMaleExtra2.AddAnimation("EXLL2MToG", "Bridge.Characters.EXLMediumAnimations.EXLL2ToG2")
	pEXLMaleExtra2.AddAnimation("EXLG2MToL", "Bridge.Characters.EXLMediumAnimations.EXLG2ToL2")
	pEXLMaleExtra2.AddAnimation("StandingEXLG2M", "Bridge.Characters.CommonAnimations.Standing")
	pEXLMaleExtra2.SetStanding(1)

	# Hit animations
	pEXLMaleExtra2.AddAnimation("EXLG2MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pEXLMaleExtra2.AddAnimation("EXLG2MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pEXLMaleExtra2.AddAnimation("EXLG2MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pEXLMaleExtra2.AddAnimation("EXLG2MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pEXLMaleExtra2.AddAnimation("EXLG2MFly", "Bridge.Characters.CommonAnimations.Blast")

	pEXLMaleExtra2.SetAsExtra(1)
	pEXLMaleExtra2.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pEXLMaleExtra2)

	pEXLMaleExtra2.SetLocation("EXLL2M")
#	kDebugObj.Print("Finished configuring EXLMaleExtra2")


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pEXLMaleExtra2	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLMaleExtra2):
	debug(__name__ + ", AddCommonAnimations")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
#	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
#	pEXLMaleExtra2.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# EXLMaleExtra2 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
