#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Yorktown"
iconName = "Yorktown"
longName = "USS-Yorktown"
shipFile = "Yorktown"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.Yorktown = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Yorktown.desc = "USS-Washington NCC-403 \nwas a ship made for a very close friend of the Admiral of StarFleet. This ship was built in 2150 and was in service since february 2150 to 2268. USS Washington has exciting history with his Captain Maciej Napiwocki. The missions of the ship now are studied in 2nd class in school, because most of them are saved the Earth. The ship was destroyed when was trying to save USS Enterprise in dangerous mission and little mystake of Captain Kirk. Captain Maciej Napiwocki was saved by USS Enterprise and now is captain of USS Yorktown \"NCC-1642\". The Yorktown was the second ship of Captain Maciej Napiwocki. The ship was in service from 2269 to 2408. USS Yorktown has a rich history like the previous USS Washington. The ship has several refits. The first was in 2292 (prototype shield generator, hull planting and TNG phasers). The next refit was in 2376 (Shield Generator, Transporters, Phasers, Impulse Engines, Phaser arcs and sensors)."
Foundation.ShipDef.Yorktown.SubMenu = "Yorktown Class"
Foundation.ShipDef.Yorktown.fMaxWarp = 6.29 + 0.0001
Foundation.ShipDef.Yorktown.fCruiseWarp = 4.2 + 0.0001
Foundation.ShipDef.Yorktown.fCrew = 260
Foundation.ShipDef.Yorktown.dTechs = {
	'Polarized Hull Plating': { "Plates": ["Hull"]
}}


if menuGroup:           Foundation.ShipDef.Yorktown.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Yorktown.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
