#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "California"
iconName = "California"
longName = "California"
shipFile = "California"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.California = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.California.dTechs = {
#	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
#	'Regenerative Shields': 10,
	"Disable Immunity": { "Power": 150, "Sensor": 100, "Phaser": 100, "Torpedo": 100, "Pulse": 100}
}

Foundation.ShipDef.California.fMaxWarp = 8.0 + 0.0001
Foundation.ShipDef.California.fCruiseWarp = 7.9 + 0.0001


Foundation.ShipDef.California.desc = "The California was a type of Federation starship in service during the late 24th century. They were support ships designed for second contact missions, and the perfect fit for any delinquent officers not quite fit for Starbase 80."


if menuGroup:           Foundation.ShipDef.California.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.California.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
