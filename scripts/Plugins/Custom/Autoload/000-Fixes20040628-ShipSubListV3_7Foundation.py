# ShipListSubMenu Addition V2.
# This modification of the Foundation allows you to get a submenu in the race list (ie Federation Ships -> Galaxy Class)
# This modification is by MLeoDaalder

import App
import Foundation
#import types # Not everyone has the types module, fake it...

ListType = type([])
StringType = type("a")
DictType = type({})


class TreeNode:
	def __init__(self, name, oShip=None, prefab = None):
		self.name = name
		self.oShip = oShip
		self.prefab = prefab
		self.children = {}
		self.bMVAM = 0
		self.bShip = 0

if int(Foundation.version[0:8]) < 20040628:
	import FoundationMenu

	class ShipMenuBuilderDef(FoundationMenu.MenuBuilderDef):
		def __init__(self, tglDatabase):
			FoundationMenu.MenuBuilderDef.__init__(self, tglDatabase)

		def __call__(self, raceShipList, menu, buttonType, uiHandler, fWidth = 0.0, fHeight = 0.0):
			foundShips = {}
			for race in raceShipList.keys():
				for ship in raceShipList[race][0]:
					foundShips[race] = 1
					break

			raceList = foundShips.keys()
			raceList.sort()

			oRoot = TreeNode("Root", prefab = menu)
			for race in raceList:

				self.textButton(race)
				pRaceButton = self.textButton.MakeSubMenu()
				oRace = TreeNode(race, prefab = pRaceButton)
				oRoot.children[race] = oRace

				shipList = raceShipList[race][1].keys()
				shipList.sort()

				for key in shipList:
					ship = raceShipList[race][1][key]
					self.textButton(ship.name)

					if ship.__dict__.get("Do not display", 0):
						continue

					if hasattr(ship, "SubMenu") and type(ship.SubMenu) != ListType:
						ship.SubMenu = [ship.SubMenu]
					if hasattr(ship, "SubSubMenu") and type(ship.SubSubMenu) != ListType:
						ship.SubSubMenu = [ship.SubSubMenu]

					oWork = oRace

					for name in (ship.__dict__.get("SubMenu", []) + ship.__dict__.get("SubSubMenu", [])):
						oMenu = oWork.children.get(name + "_m", None)
						if not oMenu:
							oMenu = TreeNode(name, prefab = App.STCharacterMenu_Create(name))
							oWork.children[name + "_m"] = oMenu
						oWork = oMenu
					bCreated = 0
					if HasMVAM():
						oWork, bCreated = DoMVAMMenus(oWork, ship, buttonType, uiHandler, self, raceShipList, fWidth, fHeight)
					if not bCreated:
						appended = ""
						while oWork.children.has_key(ship.name + appended):
							appended = appended + " "
						oWork.children[ship.name + appended] = TreeNode(ship.name, oShip = ship)
						oWork.children[ship.name + appended].bShip = 1

			BuildMenu(oRoot, self, buttonType, uiHandler, fWidth, fHeight)

	FoundationMenu.ShipMenuBuilderDef = ShipMenuBuilderDef
	Foundation.version = "20040628"

	def BuildMenu(oMenu, self, buttonType, uiHandler, fWidth, fHeight, b = 0):
		items = oMenu.children.items()
		items.sort()
		for sort, object in items:
			self.textButton(object.name)

			if object.bShip or (object.bMVAM and not len(object.children)):
				if not object.prefab:
					object.prefab = self.textButton.MakeIntButton(buttonType, object.oShip.num, uiHandler, fWidth, fHeight)
			else:
				if len(object.children):
					if not object.prefab:
						object.prefab = self.textButton.MakeSubMenu()
					if object.name == "Human (Tau'ri) Ships":
						BuildMenu(object, self, buttonType, uiHandler, fWidth, fHeight, 1)
					else:
						BuildMenu(object, self, buttonType, uiHandler, fWidth, fHeight)

					if object.bMVAM:
						object.prefab.SetTwoClicks()
						pEvent = App.TGIntEvent_Create()
						pEvent.SetEventType(buttonType)
						pEvent.SetDestination(uiHandler)
						pEvent.SetSource(object.prefab)
						pEvent.SetInt(object.oShip.num)
						object.prefab.SetActivationEvent(pEvent)

			oMenu.prefab.AddChild(object.prefab)
	bHasMVAM = -1
	def HasMVAM():
		global bHasMVAM
		if bHasMVAM != -1:	return bHasMVAM
		try:	import Custom.Autoload.Mvam
		except:	bHasMVAM = 0
		else:	bHasMVAM = 1
		return bHasMVAM

	def DoMVAMMenus(oWork, ship, buttonType, uiHandler, self, raceShipList, fWidth, fHeight):
		if not ship.__dict__.get("bMvamMenu", 1):
			return oWork, 0

		import nt
		import string

		List = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")
		Mod = None
		for i in List:
			PosModName = string.split(i, ".")
			if len(PosModName) > 1 and PosModName[0] != "__init__":
				try:
					PosMod = __import__("Custom.Autoload.Mvam." + PosModName[0])
					if PosMod and PosMod.__dict__.has_key("MvamShips"):
						if ship.shipFile in PosMod.MvamShips:
							Mod = PosMod
							break
				except:
					continue

		if not Mod:
			return oWork, 0

		shipB = None
		foundShips = {}
		for race in raceShipList.keys():
			for dummyShip in raceShipList[race][0]:
				foundShips[race] = 1
				break

		raceList = foundShips.keys()
		raceList.sort()

		for race in raceList:
			shipB = findShip(Mod.MvamShips[0], raceShipList[race][1])
			if shipB:
				break
		if not shipB:
			return oWork, 0

		if not shipB.__dict__.get("bMvamMenu", 1):
			return oWork, 0

		oTemp = oWork.children.get(shipB.name, None)
		if not oTemp:
			oTemp = TreeNode(shipB.name, oShip = shipB)
			oTemp.bMVAM = 1
			oWork.children[shipB.name] = oTemp
		oWork = oTemp
		return oWork, ship.shipFile == shipB.shipFile

	def findShip(shipFile, raceShipList):
		shipList = raceShipList.keys()
		shipList.sort()
		for key in shipList:
			ship = raceShipList[key]
			if ship.shipFile == shipFile:
				return ship

