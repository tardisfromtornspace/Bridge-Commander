import App
import Bridge.BridgeUtils
import FoundationMenu
import MissionLib
import Bridge.XOMenuHandlers

def SneakerCreateMenu(pXOMenu):
	#this import is copied from sleight's FTB framework. Used in TGL bypass
	import Custom.Sneaker.GUIUtils

	#grab the database of strings
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")

	#set up some ET...phone home?
	ET_SAUCER_SEP = App.Game_GetNextEventType()
	ET_STAR_SEP = App.Game_GetNextEventType()
	ET_SAUCER_REIN = App.Game_GetNextEventType()

	#create the list for sep/rein
	pSepName = pDatabase.GetString("Red Alert")
	pSepName.SetString("Galaxy Seperation")
	pSepMenu = App.STCharacterMenu_CreateW(pSepName)
	pXOMenu.AddChild(pSepMenu)
	# Saucer Sep
	pSaucSep = Custom.Sneaker.GUIUtils.CreateIntButton("Saucer Seperate", ET_SAUCER_SEP, pXOMenu, 1)
	pSepMenu.AddChild(pSaucSep)
	# Stardrive Sep
	pStarSep = Custom.Sneaker.GUIUtils.CreateIntButton("Stardrive Seperate", ET_STAR_SEP, pXOMenu, 1)
	pSepMenu.AddChild(pStarSep)
	# Saucer Reintegrate
	pRein = Custom.Sneaker.GUIUtils.CreateIntButton("Reintegrate", ET_SAUCER_REIN, pXOMenu, 1)
	pSepMenu.AddChild(pRein)

	# add python handlers
	pXOMenu.AddPythonFuncHandlerForInstance(ET_SAUCER_SEP,	__name__ + ".SaucSeperate")
	pXOMenu.AddPythonFuncHandlerForInstance(ET_STAR_SEP,	__name__ + ".StarSeperate")
	pXOMenu.AddPythonFuncHandlerForInstance(ET_SAUCER_REIN,	__name__ + ".Reintegrate")

	App.g_kLocalizationManager.Unload(pDatabase)

	return


####################################################### sneaker98 addition
#	SaucSeperate()
#	
#	Seperates the saucer ship
###############################################################################
def SaucSeperate(pObject, pEvent):
	# get the player
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()

	# check if its our galaxy
	if (pPlayer.GetScript() == "ships.MvamGalaxy"):
		import Custom.Sneaker.SaucSeperation
		Custom.Sneaker.SaucSeperation.SaucSeperation()

	pObject.CallNextHandler(pEvent)


####################################################### sneaker98 addition
#	StarSeperate()
#	
#	Seperates the saucer ship
###############################################################################
def StarSeperate(pObject, pEvent):
	# get the player
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()

	# check if its our galaxy
	if (pPlayer.GetScript() == "ships.MvamGalaxy"):
		import Custom.Sneaker.StarSeperation
		Custom.Sneaker.StarSeperation.StarSeperation()

	pObject.CallNextHandler(pEvent)


####################################################### sneaker98 addition
#	Reintegrate()
#	
#	Reintegrates the ships
###############################################################################
def Reintegrate(pObject, pEvent):
	# get the player
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	# check if both ships are around - saucer
	if (pPlayer.GetScript() == "ships.MvamGalaxySaucer"):
		pGalaxy1 = App.ShipClass_GetObject (pSet, "Stardrive")
		if (pGalaxy1 != None):
			import Custom.Sneaker.GalaxyReintegration
			Custom.Sneaker.GalaxyReintegration.GalaxyReintegration()

	# check if both ships are around - stardrive
	elif (pPlayer.GetScript() == "ships.MvamGalaxyStardrive"):
		pGalaxy1 = App.ShipClass_GetObject (pSet, "Saucer")
		if (pGalaxy1 != None):
			import Custom.Sneaker.GalaxyReintegration
			Custom.Sneaker.GalaxyReintegration.GalaxyReintegration()

	pObject.CallNextHandler(pEvent)