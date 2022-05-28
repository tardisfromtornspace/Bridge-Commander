from bcdebug import debug
import App
import Multiplayer.MissionShared
import Multiplayer.SpeciesToShip
import nt
import string

def BuildShipSelectWindow (pMissionPane, pDatabase):

	# Create the window
	debug(__name__ + ", BuildShipSelectWindow")
	pWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", pDatabase.GetString("Select Your Ship"), 
						0.0, 0.0, None, 1, Multiplayer.MissionMenusShared.SHIPS_WINDOW_WIDTH, Multiplayer.MissionMenusShared.SHIPS_WINDOW_HEIGHT)
	pWindow.SetTitleBarThickness(Multiplayer.MissionMenusShared.SHIPS_WINDOW_BAR_THICKNESS)
	App.g_kFocusManager.AddObjectToTabOrder(pWindow)

	pSubPane = App.STSubPane_Create (Multiplayer.MissionMenusShared.SHIPS_SUBPANE_WIDTH, 500.0, 0)
	pWindow.AddChild (pSubPane, 0, 0, 0)

	
	#########################################
	# Create the buttons
	for iIndex in range(1, Multiplayer.SpeciesToShip.MAX_FLYABLE_SHIPS):
		# Setup the event for when this button is clicked
		pEvent = App.TGIntEvent_Create ()
		pEvent.SetEventType(Multiplayer.MissionMenusShared.ET_SELECT_SHIP_SPECIES)
		pEvent.SetInt(iIndex)		# store the index so we know which button was clicked.
		pEvent.SetDestination(pMissionPane)
	
		# Create the button.	
		pButton = App.STButton_CreateW (Multiplayer.MissionShared.g_pShipDatabase.GetString (Multiplayer.SpeciesToShip.GetScriptFromSpecies (iIndex)), pEvent)
		if (iIndex == Multiplayer.MissionMenusShared.g_iSpecies):
			pButton.SetChosen (1)
			Multiplayer.MissionMenusShared.g_pChosenSpecies = pButton
		pEvent.SetSource (pButton)

		tuple = Multiplayer.SpeciesToShip.kSpeciesTuple[iIndex]
		pMenu = pSubPane
		if len(tuple) > 4:
			if(str(tuple[4]) == "" or tuple[4] == None):
				pSubMenu = pMenu.GetSubmenuW(App.TGString(tuple[2] + " Ships"))
				if(pSubMenu == None):
					pSubMenu = App.STCharacterMenu_CreateW(App.TGString(tuple[2] + " Ships"))
					pMenu.AddChild(pSubMenu, 0, 0, 0)
				pMenu = pSubMenu
			else:
				if str(tuple[4])[0] == "[" and str(tuple[4])[-1] == "]":
					pMenu = DoSubMenus(pMenu, tuple[4])
				else:
					pSubMenu = pMenu.GetSubmenuW(App.TGString(tuple[4]))
					if(pSubMenu == None):
						pSubMenu = App.STCharacterMenu_CreateW(App.TGString(tuple[4]))
						pMenu.AddChild(pSubMenu, 0, 0, 0)
					pMenu = pSubMenu
					pMenu.Open()
					pMenu.Close()

			if len(tuple) > 5:
				if(tuple[5] != None and str(tuple[5]) != ""):
					if str(tuple[5])[0] == "[" and str(tuple[5])[-1] == "]":
						pMenu = DoSubMenus(pMenu, tuple[5])
					else:
						pSubMenu = pMenu.GetSubMenuW(App.TGString(tuple[5]))
						if pSubMenu == None:
							pSubMenu = App.STCharacterMenu_CreateW(App.TGString(tuple[5]))
							pMenu.AddChild(pSubMenu, 0, 0, 0)
						pMenu = pSubMenu
						pMenu.Open()
						pMenu.Close()

			if not DoMvamMenus(pMenu, tuple, iIndex, pDatabase, pButton, pMissionPane):
				pMenu.AddChild(pButton, 0, 0, 0)
				pMenu.Open()
				pMenu.Close()

		else:
			#raise tuple, "Not good!"
			pSubMenu = pSubPane.GetSubmenuW(App.TGString(tuple[2] + " Ships"))
			if(pSubMenu == None):
				pSubMenu = App.STCharacterMenu_CreateW(App.TGString(tuple[2] + " Ships"))
				pSubPane.AddChild(pSubMenu, 0, 0, 0)

			if not DoMvamMenus(pSubMenu, tuple, iIndex, pDatabase, pButton, pMissionPane):
				pSubMenu.AddChild(pButton, 0, 0 ,0)
				pSubMenu.ForceUpdate(0)

	pSubPane.ResizeToContents ()

	return pWindow
import Multiplayer.MissionMenusShared
Multiplayer.MissionMenusShared.BuildShipSelectWindow = BuildShipSelectWindow

def DoSubMenus(pMenu, entrys):
	debug(__name__ + ", DoSubMenus")
	CurMenu = pMenu
	for entry in entrys:
		pSubMenu = CurMenu.GetSubmenuW(App.TGString(entry))
		if not pSubMenu:
			pSubMenu = App.STCharacterMenu_CreateW(App.TGString(entry))
			CurMenu.AddChild(pSubMenu, 0, 0, 0)
			pSubMenu.Open()
			pSubMenu.Close()
		CurMenu = pSubMenu
	try:
		pMenu.Open()
		pMenu.Close()
	except:
		return CurMenu
	return CurMenu

def DoMvamMenus(pMenu, tuple, num, pDatabase, pButton, pMissionPane):
	debug(__name__ + ", DoMvamMenus")
	try:
		import Custom.Autoload.Mvam
	except:
		return 0

	if len(tuple) >= 7 and tuple[7] != None:

		List = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

		Mod = None
		for i in range(len(List)):
			PosModName = string.split(List[i], ".")
			if len(PosModName) > 1 and PosModName[0] != "__init__":
				try:
					PosMod = __import__("Custom.Autoload.Mvam." + PosModName[0])
					if PosMod and hasattr(PosMod, "MvamShips"):
						if IsInList(tuple[0], PosMod.MvamShips):
							Mod = PosMod
							break
				except:
					continue

		if not Mod:
			return 0
		if Mod.MvamShips[0] == tuple[0]:
			# Full Ship
			TGName = Multiplayer.MissionShared.g_pShipDatabase.GetString(Multiplayer.SpeciesToShip.GetScriptFromSpecies(num))
			pParentShipMenu = pMenu.GetSubmenuW(TGName)
			if not pParentShipMenu:
				pParentShipMenu = App.STCharacterMenu_CreateW(TGName)
				pEvent = App.TGIntEvent_Create()
				pEvent.SetEventType(Multiplayer.MissionMenusShared.ET_SELECT_SHIP_SPECIES)
				pEvent.SetDestination(pMissionPane)
				pEvent.SetSource(pParentShipMenu)
				pEvent.SetInt(num)
				pParentShipMenu.SetActivationEvent(pEvent)
				pParentShipMenu.SetTwoClicks()
				pMenu.AddChild(pParentShipMenu, 0, 0, 0)
				pMenu.ForceUpdate(0)
		else:
			# Sep Ship
			TGName = Multiplayer.MissionShared.g_pShipDatabase.GetString(Mod.MvamShips[0])
			pParentShipMenu = pMenu.GetSubmenuW(TGName)
			if not pParentShipMenu:
				pParentShipMenu = App.STCharacterMenu_CreateW(TGName)
				pEvent = App.TGIntEvent_Create()
				pEvent.SetEventType(Multiplayer.MissionMenusShared.ET_SELECT_SHIP_SPECIES)
				pEvent.SetDestination(pMissionPane)
				pEvent.SetSource(pParentShipMenu)
				pEvent.SetInt(num)
				pParentShipMenu.SetActivationEvent(pEvent)
				pParentShipMenu.SetTwoClicks()
				pMenu.AddChild(pParentShipMenu, 0, 0, 0)
				pMenu.ForceUpdate(0)
			pParentShipMenu.AddChild(pButton, 0, 0, 0)
			pMenu.ForceUpdate(0)
	return 0

def IsInList(item, list):
	debug(__name__ + ", IsInList")
	for i in list:
		if i == item:
			return 1
		return 0

