#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "UENeptune"
iconName = "EIntrepid"
longName = "Neptune Class"
shipFile = "UENeptune"
species = App.SPECIES_GALAXY
menuGroup = "Pre-Fed ships"
playerMenuGroup = "Pre-Fed ships"
SubMenu = "United Earth ships"
Foundation.ShipDef.UENeptune = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.UENeptune.desc = "The Neptune class was a United Earth starship class in service to Earth Starfleet in the 22nd century. The Neptune class saw service in the Earth-Romulan War."
Foundation.ShipDef.UENeptune.dTechs = {
	'Polarized Hull Plating': { "Plates": ["Hull Polarizer"]
}}

if menuGroup:           Foundation.ShipDef.UENeptune.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.UENeptune.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
