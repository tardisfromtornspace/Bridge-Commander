from bcdebug import debug
###############################################################################
#	Filename:	EXLMaleExtra3.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Ambassador EXLMaleExtra3, and configures animations.
#	
#	Created:	10/03/00 -	CCarley
###############################################################################

import App
import CharacterPaths

#kDebugObj = App.CPyDebug()

###############################################################################
#	CreateCharacter()
#
#	Create EXLMaleExtra3 by building his character and placing him on the passed in set.
#	Create his menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
#	kDebugObj.Print("Creating EXLMaleExtra3")

	debug(__name__ + ", CreateCharacter")
	if (pSet.GetObject("EXLMaleExtra3") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("MaleExtra3")))

	CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyEXLMaleM/BodyEXLMaleM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif", None)
	pEXLMaleExtra3 = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyEXLMaleM/BodyEXLMaleM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadData/Data_head.nif")
	pEXLMaleExtra3.ReplacebodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyEXLMaleM/FedGold_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadData/EXLMale_ensignC_head.tga")

	# Add the character to the set
	pSet.AddObjectToSet(pEXLMaleExtra3, "MaleExtra3")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pEXLMaleExtra3)

	# Setup the character configuration
	pEXLMaleExtra3.SetSize(App.CharacterClass.MEDIUM)
	pEXLMaleExtra3.SetGender(App.CharacterClass.MALE)
	pEXLMaleExtra3.SetRandomAnimationChance(.75)
	pEXLMaleExtra3.SetBlinkChance(0.1)
	pEXLMaleExtra3.SetCharacterName("MaleExtra3")

	pEXLMaleExtra3.SetHidden(1)

	# Load EXLMaleExtra3's generic sounds
	LoadSounds()

	# Create EXLMaleExtra3's menus
	#import EXLMaleExtra3MenuHandlers
	#EXLMaleExtra3MenuHandlers.CreateMenus(pEXLMaleExtra3)

	pEXLMaleExtra3.SetDatabase("data/TGL/Bridge Crew General.tgl")

	pGame = App.Game_GetCurrentGame()
	#pGame.LoadDatabaseSoundInGroup(pEXLMaleExtra3.GetDatabase(), "EXLMaleExtra3NothingToAdd", "BridgeGeneric")

#	kDebugObj.Print("Finished creating EXLMaleExtra3")
	return pEXLMaleExtra3

###############################################################################
#	ConfigureForGalaxy()
#
#	Configure ourselves for the Galaxy bridge
#
#	Args:	pEXLMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForGalaxy(pEXLMaleExtra3):
#	kDebugObj.Print("Configuring EXLMaleExtra3 for the Galaxy bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForGalaxy")
	pEXLMaleExtra3.ClearAnimations()

	#
	# *** CURRENTLY EXLMaleExtra3 HAS NO GALAXY CLASS ANIMATIONS ***
	#

	# Add common animations.
	AddCommonAnimations(pEXLMaleExtra3)

	pEXLMaleExtra3.SetAsExtra(1)
	pEXLMaleExtra3.SetHidden(1)

	pEXLMaleExtra3.SetLocation("DBL1M")
#	kDebugObj.Print("Finished configuring EXLMaleExtra3")

###############################################################################
#	ConfigureForExcelsior()
#
#	Configure ourselves for the Excelsior bridge
#
#	Args:	pMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForExcelsior(pEXLMaleExtra3):
#	kDebugObj.Print("Configuring MaleExtra3 for the Excelsior bridge")

	# Clear out any old animations from another configuration
	debug(__name__ + ", ConfigureForExcelsior")
	pEXLMaleExtra3.ClearAnimations()

	# Register animation mappings
	pEXLMaleExtra3.AddAnimation("EXLL1MToG", "Bridge.Characters.EXLMediumAnimations.EXLL1ToG3")
	pEXLMaleExtra3.AddAnimation("EXLG3MToL", "Bridge.Characters.EXLMediumAnimations.EXLG3ToL1")
	pEXLMaleExtra3.AddAnimation("StandingEXLG3M", "Bridge.Characters.CommonAnimations.Standing")
	pEXLMaleExtra3.SetStanding(1)

	# Hit animations
	pEXLMaleExtra3.AddAnimation("EXLG3MHitStanding", "Bridge.Characters.CommonAnimations.HitStanding")
	pEXLMaleExtra3.AddAnimation("EXLG3MHitHardStanding", "Bridge.Characters.CommonAnimations.HitHardStanding")
	pEXLMaleExtra3.AddAnimation("EXLG3MReactLeft", "Bridge.Characters.CommonAnimations.ReactLeft")
	pEXLMaleExtra3.AddAnimation("EXLG3MReactRight", "Bridge.Characters.CommonAnimations.ReactRight")
	pEXLMaleExtra3.AddAnimation("EXLG3MFly", "Bridge.Characters.CommonAnimations.Blast2")

	pEXLMaleExtra3.SetAsExtra(1)
	pEXLMaleExtra3.SetHidden(1)

	# Add common animations.
	AddCommonAnimations(pEXLMaleExtra3)

	pEXLMaleExtra3.SetLocation("EXLL1M")
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
#	Args:	pEXLMaleExtra3	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pEXLMaleExtra3):
	debug(__name__ + ", AddCommonAnimations")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.HitCommunicator")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleDown")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsoleUp")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookAroundConsole")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallButtonPresses")
	pEXLMaleExtra3.AddRandomAnimation("Bridge.Characters.CommonAnimations.WallSlides")


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
	# EXLMaleExtra3 has no generic bridge sounds at this time
	#
	debug(__name__ + ", LoadSounds")
	pass
