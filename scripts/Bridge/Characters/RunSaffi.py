###############################################################################
#	Filename:	Saffi.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Loads Saffi Larsen, XO, and configures animations.
#	
#	Created:	3/28/00 -	Erik Novales
###############################################################################

import App
import CharacterPaths

###############################################################################
#	CreateCharacter()
#
#	Create Saffi by building her character and placing her on the passed in set.
#	Create her menus as well.
#
#	Args:	pSet	- the Set in which to place ourselves
#
#	Return:	none
###############################################################################
def CreateCharacter(pSet):
        
	if (pSet.GetObject("XO") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("XO")))

	CharacterPaths.UpdatePaths()
	
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", "Bip01")
	App.g_kModelManager.LoadModel(CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", None)
	pSaffi = App.CharacterClass_Create(CharacterPaths.g_pcBodyNIFPath + "BodyFemM/BodyFemM.nif", CharacterPaths.g_pcHeadNIFPath + "HeadSaffi/saffi_head.nif", 1)
	pSaffi.ReplaceBodyAndHead(CharacterPaths.g_pcBodyTexPath + "BodyFemS/FedFemRed_body.tga", CharacterPaths.g_pcHeadTexPath + "HeadSaffi/saffi_head.tga")

	pRunSaffi.SetCharacterName("Saffi")

	pSet.AddObjectToSet(pRunSaffi, "XO")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pRunSaffi)

	pRunSaffi.SetSize(App.CharacterClass.MEDIUM)
	pRunSaffi.SetGender(App.CharacterClass.FEMALE)
	pRunSaffi.SetRandomAnimationChance(.75)
	pRunSaffi.SetBlinkChance(0.1)
	pRunSaffi.SetDatabase("data/TGL/Bridge Crew General.tgl")

	LoadSounds()

	pRunSaffi.AddFacialImage("Blink0", CharacterPaths.g_pcHeadTexPath + "HeadRunSaffi/RunSaffi_head_blink1.tga")
	pRunSaffi.AddFacialImage("Blink1", CharacterPaths.g_pcHeadTexPath + "HeadRunSaffi/RunSaffi_head_blink2.tga")
	pRunSaffi.AddFacialImage("Blink2", CharacterPaths.g_pcHeadTexPath + "HeadRunSaffi/RunSaffi_head_eyesclosed.tga")
	pRunSaffi.SetBlinkStages(3)

	pRunSaffi.AddFacialImage("SpeakA", CharacterPaths.g_pcHeadTexPath + "HeadRunSaffi/RunSaffi_head_a.tga")
	pRunSaffi.AddFacialImage("SpeakE", CharacterPaths.g_pcHeadTexPath + "HeadRunSaffi/RunSaffi_head_e.tga")
	pRunSaffi.AddFacialImage("SpeakU", CharacterPaths.g_pcHeadTexPath + "HeadRunSaffi/RunSaffi_head_u.tga")
	pRunSaffi.SetAnimatedSpeaking(1)

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pRunSaffi.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Commander")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

        return pRunSaffi


###############################################################################
#	ConfigureForShip()
#
#	Configure ourselves for the particular ship object.  This involves setting
#	up range watchers that tell us how to report.
#
#	Args:	pSet	- the Set object
#			pShip	- the player's ship (ShipClass object)
#
#	Return:	none
###############################################################################
def ConfigureForShip(pSet, pShip):
	pRunSaffi = App.CharacterClass_Cast(pSet.GetObject("XO"))
	if (pRunSaffi == None):
		return

	import Bridge.XOCharacterHandlers
	Bridge.XOCharacterHandlers.AttachMenuToXO(pRunSaffi)



###############################################################################
#	ConfigureForSovereign()
#
#	Configure ourselves for the Sovereign bridge
#
#	Args:	pRunSaffi	- our Character object
#
#	Return:	none
###############################################################################
def ConfigureForType11(pRunSaffi):
        
	pRunSaffi.ClearAnimations()
	
	pRunSaffi.SetLocation("RunCommander")
       
	


###############################################################################
#	AddCommonAnimations()
#
#	Since we can only clear out all animations when switching bridges (how
#	would we know which not to clear?), we can't really setup animations common
#	to all bridge configurations as we might like.  Because of this we have a
#	routine to add common animations (most of which are randoms) that both
#	configurations will call
#
#	Args:	pRunSaffi	- our Character object
#
#	Return:	none
###############################################################################
def AddCommonAnimations(pRunSaffi):
	pRunSaffi.AddRandomAnimation("Bridge.Characters.MediumAnimations.CLookAroundConsoleDown", App.CharacterClass.SITTING_ONLY, 1, 1)

	pRunSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadLeft")
	pRunSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.TiltHeadRight")
	pRunSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookLeft", App.CharacterClass.SITTING_ONLY)
	pRunSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookRight", App.CharacterClass.SITTING_ONLY)
	pRunSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookUp", App.CharacterClass.SITTING_ONLY)
	pRunSaffi.AddRandomAnimation("Bridge.Characters.CommonAnimations.LookDown", App.CharacterClass.SITTING_ONLY)

###############################################################################
#	LoadSounds
#	
#	Load any of RunSaffi's general or spontaneous sounds, so they don't
#	hitch the game when they're played.
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def LoadSounds():
	pGame = App.Game_GetCurrentGame()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
	
	lSoundList =	[
		"gf001",
		"gf002",

		"gf020",

		"GreenAlert",
		"GreenAlert2",
		"GreenAlert3",
		"YellowAlert",
		"YellowAlert3",
		"YellowAlert2",
		"RedAlert",
		"RedAlert2",

		"gl004",
		"gl005",
					]
	for sLine in lSoundList:
		pGame.LoadDatabaseSoundInGroup(pDatabase, sLine, "BridgeGeneric")

	App.g_kLocalizationManager.Unload(pDatabase)
