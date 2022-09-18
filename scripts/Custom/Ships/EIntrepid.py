#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "EIntrepid"
iconName = "EIntrepid"
longName = "Neptune class"
shipFile = "EIntrepid"
species = App.SPECIES_GALAXY
menuGroup = "Pre-Fed ships"
playerMenuGroup = "Pre-Fed ships"
SubMenu = "United Earth ships"
Foundation.ShipDef.EIntrepid = Foundation.ShipDef(abbrev, species, {'iconName': iconName, 'shipFile': shipFile})
Foundation.ShipDef.EIntrepid.dTechs = {
	'Polarized Hull Plating': { "Plates": ["Hull Polarizer"]
}}

Foundation.ShipDef.EIntrepid.desc = "The Neptune class was a United Earth starship class in service to Earth Starfleet in the 22nd century. The Neptune class saw service in the Earth-Romulan War."


#if menuGroup:           Foundation.ShipDef.EIntrepid.RegisterQBShipMenu(menuGroup)
#if playerMenuGroup:     Foundation.ShipDef.EIntrepid.RegisterQBPlayerShipMenu(playerMenuGroup)


#if Foundation.shipList._keyList.has_key(longName):
#      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
#      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
