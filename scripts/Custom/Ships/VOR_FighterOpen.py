#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "VOR_FighterOpen"
iconName = "Vorlon_FighterOpen"
longName = "Vorlon Fighter (Open)"
shipFile = "VOR_FighterOpen"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Vorlon Empire"
SubSubMenu = "Fighters"

Foundation.ShipDef.VOR_FighterOpen = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.VOR_FighterOpen.dTechs = {
	'Breen Drainer Immune': 0,
	'Automated Destroyed System Repair': {"Time": 120.0}
}

Foundation.ShipDef.VOR_FighterOpen.desc = "The Vorlon Fighter was the Vorlons´ smallest known vessel and only known type of fighter. The Vorlon fighters appear to be able to create their own independent jump points into hyperspace. Fast, powerful and in numbers, these ships have been seen capable of overwhelming and destroying a Shadow Vessel."


if menuGroup:           Foundation.ShipDef.VOR_FighterOpen.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VOR_FighterOpen.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
