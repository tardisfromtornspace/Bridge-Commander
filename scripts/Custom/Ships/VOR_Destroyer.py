#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "VOR_Destroyer"
iconName = "Vorlon_Destroyer"
longName = "Vorlon Destroyer"
shipFile = "VOR_Destroyer"
species = App.SPECIES_SOVEREIGN
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Vorlon Empire"
SubSubMenu = "Starships"

Foundation.ShipDef.VOR_Destroyer = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.VOR_Destroyer.dTechs = {
	'Breen Drainer Immune': 0,
	'Automated Destroyed System Repair': {"Time": 120.0},
	"Tachyon Sensors": 0.1
}

Foundation.ShipDef.VOR_Destroyer.desc = "The Vorlon Transport, or Destroyer, is a class of ship in use by the Vorlon Empire, sometimes to transport diplomats to various locations, and to guard the frontiers of Vorlon Space. Vorlon Transports have been known to easily destroy Shadow Battlecrabs alone with sustained fire."


if menuGroup:           Foundation.ShipDef.VOR_Destroyer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VOR_Destroyer.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
