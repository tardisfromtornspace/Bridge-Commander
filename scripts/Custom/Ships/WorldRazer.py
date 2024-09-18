#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "WorldRazer"
iconName = "WorldRazer"
longName = "C.S.S WorldRazer"
shipFile = "WorldRazer"
species = App.SPECIES_GALAXY

menuGroup = "Shattered Timeline Ships"
playerMenuGroup = "Shattered Timeline Ships"
SubMenu = "Terran Confederation"
Foundation.ShipDef.WorldRazer = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


Foundation.ShipDef.WorldRazer.desc = "In an alternate timeline created by Q by changing Earth history in 2024, the CSS World Razer was a 24th century Confederation of Earth vessel, a combat starship in Confederation Corps service at some point before the 2400s decade. Its commanding officer was Jean-Luc Picard. According to General Picard, the World Razer helped the Confederation conquer the stars. In the 25th century, a painting of the World Razer, showing the ship guns blazing, was on display at Chateau Picard."
Foundation.ShipDef.WorldRazer.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1
}


if menuGroup:           Foundation.ShipDef.WorldRazer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WorldRazer.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
