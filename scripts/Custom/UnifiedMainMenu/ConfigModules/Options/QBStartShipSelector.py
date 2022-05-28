##################################################
#This will allow you to select your Quickbattle Startship from Mainmenu
#V0.96 01.10.09 / Defiants Edit to Save/Load and a Bugfix
##################################################
import App
import Foundation
import FoundationMenu
from Registry import Registry
#import MainMenu.mainmenu

#globals
g_pIconPane = None
g_pShipsIcon = None
g_pShipsTextWindow = None
g_pShipsText = None
#Events
ET_SELECT_PLAYER_SHIP_TYPE	= App.Mission_GetNextEventType()
ET_SELECT_BRIDGE_TYPE = App.Mission_GetNextEventType()
#####################################################
# Required Functions for UMM
#############################################
def GetName():
	return "QB StartShip Selector"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
	
	createShipMenu(pOptionsPane, pContentPanel)
	createBridgeMenu(pOptionsPane, pContentPanel)
	return App.TGPane_Create()

##########################################################

def createShipMenu(pOptionsPane, pContentPanel):

	pMenu = App.STCharacterMenu_Create("Ship Selection")
	pContentPanel.AddChild(pMenu)
	
	pMenu.AddPythonFuncHandlerForInstance(ET_SELECT_PLAYER_SHIP_TYPE, __name__ + ".ShipSelected")

	pInfoPane = createInfoPane()
	pMenu.AddChild(pInfoPane)
	
	Mutator = Foundation.MutatorDef()
	Mutator.playerShipMenu = Foundation.qbShipMenu
	Mutator.Update(Foundation.MutatorDef.StockShips)
	FDTNShips = Mutator.playerShipMenu
	
	shipMenuBuilder = FoundationMenu.ShipMenuBuilderDef(App.g_kLocalizationManager.Load("data/TGL/QuickBattle/QuickBattle.tgl"))
	shipMenuBuilder(FDTNShips, pMenu, ET_SELECT_PLAYER_SHIP_TYPE, pMenu)

	return pMenu

def createInfoPane():
	global g_pIconPane, g_pShipsIcon,g_pShipsTextWindow, g_pShipsText
	
	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())
	fWidth = LCARS.MAIN_MENU_CONFIGURE_CONTENT_WIDTH*0.5
	
	g_pShipsWindow = App.STStylizedWindow_CreateW("StylizedWindow", "RightBorder", App.TGString("Ship Selection"))
	g_pShipsWindow.SetFixedSize((fWidth*2)-0.04, fWidth+0.04)
	
	g_pIconPane = App.TGPane_Create(fWidth*0.8, fWidth*0.8)
	g_pShipsIcon = App.TGIcon_Create("ShipIcons", App.SPECIES_UNKNOWN)
	g_pShipsIcon.Resize(fWidth*0.8, fWidth*0.8)
	g_pIconPane.AddChild(g_pShipsIcon)

	# Go to the small font
	# Nah, forget it, this is too small for me
	
	#App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont, MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])
	
	g_pShipsTextWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Ship Description"),0.0, 0.0, None, 1, (fWidth*1.2)-0.035, fWidth)
	g_pShipsText = App.TGParagraph_Create("", g_pShipsTextWindow.GetMaximumInteriorWidth (), None, "", g_pShipsTextWindow.GetMaximumInteriorWidth (), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
	g_pShipsTextWindow.AddChild(g_pShipsText, 0, 0, 0)

	# Go back to the large font	
	#App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont, MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	g_pShipsWindow.AddChild(g_pIconPane, -0.01, 0.02, 0)
	g_pShipsWindow.AddChild(g_pShipsTextWindow, fWidth*0.7, 0.01, 0)

	updateShipInfo( Foundation.MutatorDef.Stock.startShipDef )
	
	return g_pShipsWindow
	
	
def ShipSelected(pOption, pEvent):

	sShipint = pEvent.GetInt()
	#print "You selected "+ Foundation.shipList[sShipint].name  + " as QB Startship" 
	try:
		pNewStartShip = Foundation.shipList[sShipint]
		Foundation.MutatorDef.Stock.startShipDef = pNewStartShip
		updateShipInfo(pNewStartShip)
		App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", "QB start ship", sShipint)
	except:
		print "Something at load of new QB Startship went wrong"
		Foundation.MutatorDef.Stock.startShipDef = Foundation.ShipDef.Galaxy
		
def updateShipInfo(FndtnShip):
	global g_pIconPane, g_pShipsIcon, g_pShipsTextWindow, g_pShipsText
	
	#Set the Icon
	g_pShipsIcon.SetIconNum(FndtnShip.GetIconNum())
	g_pShipsIcon.SizeToArtwork()
	# If we're too big, shrink us down
	if (g_pShipsIcon.GetHeight() > g_pIconPane.GetHeight()):
		fRatio = g_pIconPane.GetHeight() / g_pShipsIcon.GetHeight()
		g_pShipsIcon.Resize(g_pShipsIcon.GetWidth() * fRatio, g_pShipsIcon.GetHeight() * fRatio)
	# Center us in our parent pane
	fXPos = (g_pIconPane.GetWidth() - g_pShipsIcon.GetWidth()) / 2.0
	fYPos = (g_pIconPane.GetHeight() - g_pShipsIcon.GetHeight()) / 2.0
	g_pShipsIcon.SetPosition(fXPos, fYPos)
	
	#And set the Text
	g_pShipsDatabase = App.g_kLocalizationManager.Load("data/TGL/Ships.tgl")
	if g_pShipsDatabase.HasString(FndtnShip.abbrev + " Description"):
		g_pShipsText.SetStringW(g_pShipsDatabase.GetString(FndtnShip.abbrev + " Description"))
	else:
		g_pShipsText.SetString(FndtnShip.desc)
	g_pShipsTextWindow.InteriorChangedSize()
	g_pShipsTextWindow.ScrollToTop()
	g_pShipsText.Layout()
	
#######################################################################
#BridgePart
#######################################################################
def createBridgeMenu(pOptionsPane, pContentPanel):

	pMenu = App.STCharacterMenu_Create("Bridge Selection")
	pContentPanel.AddChild(pMenu)

	pMenu.AddPythonFuncHandlerForInstance(ET_SELECT_BRIDGE_TYPE, __name__ + ".BridgeSelected")
	
	#This needs to be that way, otherwise you will not get what you selected
	brdgList = Registry()
	for i in range(len(Foundation.bridgeList)):
		brdgList.Register(Foundation.bridgeList[i], Foundation.bridgeList[i].name)

	bridgeMenuBuilder = FoundationMenu.BridgeMenuBuilderDef(App.g_kLocalizationManager.Load("data/TGL/QuickBattle/QuickBattle.tgl"))
	bridgeMenuBuilder(brdgList, pMenu, ET_SELECT_BRIDGE_TYPE, pMenu)

	return pMenu

def BridgeSelected(pOption, pEvent):
	global sBridgeInt
	
	sBridgeInt = pEvent.GetInt()
	#print "You selected "+ Foundation.bridgeList[sBridgeInt].name + " as QB Startbridge"
	Foundation.ShipDef.GetBridge = GetBridge
	App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", "QB start bridge", sBridgeInt)
	
def GetBridge(self):
	global sBridgeString
	#return Foundation.bridgeList[sBridgeInt].bridgeString
	return Foundation.bridgeList[sBridgeInt].bridgeString

