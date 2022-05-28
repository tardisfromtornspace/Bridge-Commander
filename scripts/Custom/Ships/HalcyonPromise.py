#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "HalcyonPromise"
iconName = "NSCTHC"
longName = "Halcyon Promise"
shipFile = "HalcyonPromise"
species = App.SPECIES_GALAXY
menuGroup = "Andromeda"
playerMenuGroup = "Andromeda"
SubMenu = "System´s Commonwealth"
Foundation.ShipDef.HalcyonPromise = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.HalcyonPromise.dTechs = {
	'Breen Drainer Immune': 1,
	'Multivectral Shields': 13,
        "Reflector Shields": 55,
	'Fed Ablative Armor': { "Plates": ["Armour"]
}}
Foundation.ShipDef.HalcyonPromise.bPlanetKiller = 1

Foundation.ShipDef.HalcyonPromise.desc = "The Halcyon promise was Tri-Jema's Triumvir Heavy Cruiser. Not much info is known about this class, only that it clearly presents some degree of threat to a Glorious Heritage Class ship, and that it has a similar size, and that is unwieldy enough that it cannot successfully navigate the Gordian Maze, which caused the destruction of this ship."

if menuGroup:           Foundation.ShipDef.HalcyonPromise.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HalcyonPromise.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
