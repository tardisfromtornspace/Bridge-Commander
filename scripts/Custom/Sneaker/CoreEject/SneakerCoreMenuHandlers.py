import App
import Bridge.BridgeUtils
import FoundationMenu
import MissionLib
import Bridge.XOMenuHandlers

def SneakerCoreCreateMenu(pXOMenu):
	#this import is copied from sleight's FTB framework. Used in TGL bypass
	import Custom.Sneaker.CoreEject.GUIUtils

	#grab the database of strings
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")

	#set up the list in the XO menu
	pCoreEjectMenu = pDatabase.GetString("Red Alert")
	pCoreEjectMenu.SetString("Core Ejection")
	pCoreEjectMenu = App.STCharacterMenu_CreateW(pCoreEjectMenu)
	pXOMenu.AddChild(pCoreEjectMenu)

	#add 2 menus, set up ET's first
	ET_CORE_EJECT = App.Game_GetNextEventType()
	pCoreEject = Custom.Sneaker.CoreEject.GUIUtils.CreateIntButton("Eject Core", ET_CORE_EJECT, pXOMenu, 1)
	pCoreEjectMenu.AddChild(pCoreEject)

	# add python handlers
	pXOMenu.AddPythonFuncHandlerForInstance(ET_CORE_EJECT, __name__ + ".CoreEject")

	App.g_kLocalizationManager.Unload(pDatabase)

	return


####################################################### sneaker98 addition
#	CoreEject()
#	
#	This launches the core out of the ship
###############################################################################
def CoreEject(pObject, pEvent):
	# get the player
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()

	# these are checks on the player ship....
	import Custom.Sneaker.CoreEject.CheckShip
	# first, check to see that its a federation ship
	snkRaceCheck = Custom.Sneaker.CoreEject.CheckShip.CheckRace(pPlayer)
	# next, check to make sure it has a Warp Core and not a fusion thing, so i'll be looking at its name
	snkPowerCheck = Custom.Sneaker.CoreEject.CheckShip.CheckPower(pPlayer)

	# these all turned out true. DUMP THE CORE!
	if (snkRaceCheck == 1 and snkPowerCheck == 1):
		import Custom.Sneaker.CoreEject.CoreActions
		Custom.Sneaker.CoreEject.CoreActions.DumpIt()

	pObject.CallNextHandler(pEvent)
