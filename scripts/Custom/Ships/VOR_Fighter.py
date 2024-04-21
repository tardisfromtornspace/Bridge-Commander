#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "VOR_Fighter"
iconName = "Vorlon_Fighter"
longName = "Vorlon Fighter"
shipFile = "VOR_Fighter"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Vorlon Empire"
SubSubMenu = "Fighters"

Foundation.ShipDef.VOR_Fighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.VOR_Fighter.dTechs = {
	'Breen Drainer Immune': 0,
	'Automated Destroyed System Repair': {"Time": 120.0},
	"Tachyon Sensors": 0.1
}

Foundation.ShipDef.VOR_Fighter.desc = "The Vorlon fighter was the Vorlons´ smallest known vessel and only known type of fighter. The Vorlon fighters appear to be able to create their own independent jump points into hyperspace. Fast, powerful and in numbers, these ships have been seen capable of overwhelming and destroying a Shadow Vessel."


if menuGroup:           Foundation.ShipDef.VOR_Fighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VOR_Fighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
