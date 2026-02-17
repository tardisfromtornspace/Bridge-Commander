#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "SCIFIKINGOdyssey"
iconName = "Canon Enterprise F"
longName = "USS Enterprise F Canon"
shipFile = "SCIFIKINGOdyssey"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.SCIFIKINGOdyssey = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.SCIFIKINGOdyssey.SubMenu = "2400s"
Foundation.ShipDef.SCIFIKINGOdyssey.SubSubMenu = "Odyssey Class"

Foundation.ShipDef.SCIFIKINGOdyssey.dTechs = {
	"AutoTargeting": { "Phaser": [3, 1] },
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Multivectral Shields': 15,
	'Regenerative Shields': 65,
	'Ablative Armour': 40000.000000
}

Foundation.ShipDef.SCIFIKINGOdyssey.desc = "The USS Enterprise (NCC-1701-F) was an Odyssey-class Federation starship operated by Starfleet in the 25th century. It was the seventh Federation vessel to bear the name Enterprise. On her final mission in 2401, she was under command of Fleet Admiral Elizabeth Shelby."


if menuGroup:           Foundation.ShipDef.SCIFIKINGOdyssey.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SCIFIKINGOdyssey.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
