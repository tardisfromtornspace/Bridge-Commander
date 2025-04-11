#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "UpgradedVorchanbyKlingonNarn"
iconName = "Vorchan"
longName = "Captured-Upgraded Vorchan"
shipFile = "UpgradedVorchanbyKlingonNarn"
species = App.SPECIES_GALAXY
menuGroup = "Non canon X-Overs"
playerMenuGroup = "Non canon X-Overs"
SubMenu = "Narn-Klingon Alliance"
Foundation.ShipDef.UpgradedVorchanbyKlingonNarn = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubMenu": SubMenu })

Foundation.ShipDef.UpgradedVorchanbyKlingonNarn.dTechs = {
	'Gravimetric Defense': 195,
	"Tachyon Sensors": 1.1
}

Foundation.ShipDef.UpgradedVorchanbyKlingonNarn.desc = "This Vorchans were stolen by the Klingons after the Centauri attack on Narn in order to create a fleet that refilled the massive losses of ships. In order to have a real possibility against a greater number of enemies, most of their systems were modified, being capable of matching a Primus-Shadow hybrid built by house Refa in a 1 vs 1 battle."


if menuGroup:           Foundation.ShipDef.UpgradedVorchanbyKlingonNarn.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.UpgradedVorchanbyKlingonNarn.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
