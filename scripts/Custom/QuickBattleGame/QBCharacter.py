import App
import MissionLib
import Bridge.Characters.CharacterPaths

def LoadCrew(sPath, sBridge):
	pBridge = App.g_kSetManager.GetSet('bridge')
	pPlayer = MissionLib.GetPlayer()
	if ((pPlayer is None) or (pBridge is None)):
		return
	SetupMiguel(pBridge, pPlayer, sPath, sBridge)


def SetupMiguel(pSet, pPlayer, sPath, sBridge):
	pSet.RemoveObjectFromSet('Science')
	import Bridge.Characters.Miguel
	pMiguel = CreateMiguel(pSet, sPath)
	Bridge.Characters.Miguel.AddCommonAnimations(pMiguel)
	if (sBridge == "Sovereign"):
		Bridge.Characters.Miguel.ConfigureForSovereign(pMiguel)
	else:
		Bridge.Characters.Miguel.ConfigureForGalaxy(pMiguel)	
	Bridge.Characters.Miguel.ConfigureForShip(pSet, pPlayer)
	import Bridge.ScienceCharacterHandlers
	Bridge.ScienceCharacterHandlers.AttachMenuToScience(pMiguel)
	Bridge.Characters.Miguel.LoadSounds()
	return pMiguel


def CreateMiguel(pSet, path):

	if (pSet.GetObject("Science") != None):
		return(App.CharacterClass_Cast(pSet.GetObject("Science")))

	Bridge.Characters.CharacterPaths.UpdatePaths()
	# Create the character
	App.g_kModelManager.LoadModel(Bridge.Characters.CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", "Bip01")
	App.g_kModelManager.LoadModel(Bridge.Characters.CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif", None)
	pMiguel = App.CharacterClass_Create(Bridge.Characters.CharacterPaths.g_pcBodyNIFPath + "BodyMaleS/BodyMaleS.nif", Bridge.Characters.CharacterPaths.g_pcHeadNIFPath + "HeadMiguel/miguel_head.nif")
	pMiguel.ReplaceBodyAndHead(path + "Miguel/miguel_body.tga", path + "Miguel/miguel_head.tga")

	pMiguel.SetCharacterName("Miguel")

	# Add the character to the set
	pSet.AddObjectToSet(pMiguel, "Science")
	pLight = pSet.GetLight("ambientlight1")
	pLight.AddIlluminatedObject(pMiguel)

	# Setup the character configuration
	pMiguel.SetSize(App.CharacterClass.SMALL)
	pMiguel.SetGender(App.CharacterClass.MALE)
	pMiguel.SetRandomAnimationChance(.75)
	pMiguel.SetBlinkChance(0.1)
	pMiguel.SetDatabase("data/TGL/Bridge Crew General.tgl")

	# Load Science officer generic sounds
	#import Bridge.Characters.Miguel
	#Bridge.Characters.Miguel.LoadSounds()

	pMiguel.AddFacialImage("Blink0", path + "Miguel/Miguel_head_blink1.tga")
	pMiguel.AddFacialImage("Blink1", path + "Miguel/Miguel_head_blink2.tga")
	pMiguel.AddFacialImage("Blink2", path + "Miguel/Miguel_head_eyesclosed.tga")
	pMiguel.SetBlinkStages(3)

	pMiguel.AddFacialImage("SpeakA", path + "Miguel/Miguel_head_a.tga")
	pMiguel.AddFacialImage("SpeakE", path + "Miguel/Miguel_head_e.tga")
	pMiguel.AddFacialImage("SpeakU", path + "Miguel/Miguel_head_u.tga")
	pMiguel.SetAnimatedSpeaking(1)

	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pMiguel.GetDatabase(), "MiguelNothingToAdd", "BridgeGeneric")

	pMenusDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTop = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pMiguel.SetMenu(pTacticalControlWindow.FindMenu(pMenusDatabase.GetString("Science")))
	App.g_kLocalizationManager.Unload(pMenusDatabase)

	return pMiguel


