#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "SCIFIKINGOdyssey"
iconName = "Canon Enterprise F"
longName = "Canon Enterprise F"
shipFile = "SCIFIKINGOdyssey"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.SCIFIKINGOdyssey = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.SCIFIKINGOdyssey.dTechs = {
	"AutoTargeting": { "Phaser": [3, 1] },
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Multivectral Shields': 15,
	'Regenerative Shields': 65,
	'Ablative Armour': 40000.000000
}

Foundation.ShipDef.SCIFIKINGOdyssey.desc = "The USS Enterprise ( NCC-1701-F) was a 25th century Federation starship, initially an Odyssey-class star cruiser and post-refit a Yorktown-class dreadnought in Starfleet service in the 2400s and 2410s decades. Its commanding officer was Captain Va'Kel Shon."


if menuGroup:           Foundation.ShipDef.SCIFIKINGOdyssey.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SCIFIKINGOdyssey.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
