import App
import QuickBattle.QuickBattle

###############################################################################
#	GeneratePlayerBridgeMenu()
#
#	Generates the menus from which the player's ship can be selected
#
#	Args:	iShipsUnlocked1	-	a bitfield specifying which ships are available
#
#	Return:	none
###############################################################################
def GeneratePlayerBridgeMenu(iShipsUnlocked1):
	# Create menus for the player's ship
	#making the bridge menu the slightest bit longer
	pShipMenu = App.STSubPane_Create(QuickBattle.QuickBattle.BRIDGE_MENU_WIDTH, QuickBattle.QuickBattle.BRIDGE_MENU_HEIGHT, 1)

	pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", QuickBattle.QuickBattle.g_pMissionDatabase.GetString("Select Player Bridge"))
	pStylizedWindow.SetUseScrolling(1)

	#making the bridge menu the slightest bit longer
	pStylizedWindow.SetFixedSize(QuickBattle.QuickBattle.BRIDGE_MENU_WIDTH, QuickBattle.QuickBattle.BRIDGE_MENU_HEIGHT)
	pStylizedWindow.SetTitleBarThickness(QuickBattle.QuickBattle.BAR_HEIGHT)
	pStylizedWindow.AddChild(pShipMenu)
	QuickBattle.QuickBattle.g_pPlayerPane.AddChild(pStylizedWindow, QuickBattle.QuickBattle.BRIDGE_MENU_X_POS, QuickBattle.QuickBattle.BRIDGE_MENU_Y_POS)

	###############################################################################
	# Dasher42's additions
	
	QuickBattle.QuickBattle.bridgeMenuBuilder(QuickBattle.QuickBattle.qbGameMode.bridgeList, pShipMenu, QuickBattle.QuickBattle.ET_SELECT_BRIDGE_TYPE, QuickBattle.QuickBattle.g_pXO)
	pShipMenu.Resize(pShipMenu.GetWidth(), pShipMenu.GetTotalHeightOfChildren())
	pStylizedWindow.Layout()
	pStylizedWindow.InteriorChangedSize()

	return pStylizedWindow