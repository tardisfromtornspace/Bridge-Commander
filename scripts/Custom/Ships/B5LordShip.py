#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "B5LordShip"
iconName = "B5LordShip"
longName = "Lordship"
shipFile = "B5LordShip"
species = App.SPECIES_SOVEREIGN
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Kirishiac Court"
SubSubMenu = "Capital Ships"

Foundation.ShipDef.B5LordShip = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
# Unknown capabilities, just using hull polarizer here because with an appropiate hardpoint it can be repurposed as an unknown type of shield.
Foundation.ShipDef.B5LordShip.dTechs = {
    'Breen Drainer Immune': 1,
    'Automated Destroyed System Repair': {"Time": 130.0},
    'Fed Ablative Armor': { "Plates": ["Armor Layer 1", "Armor Layer 2", "Armor Layer 3"]}
}



Foundation.ShipDef.B5LordShip.desc = "The Lordship is the ship of the Kirishiac, one of the First Ones. The ship is equipped with adaptive armor that is self-repairing. To generate the gravitational fields that are necessary to power the ship and its weapons as well as keep the 10-meter tall Lords comfortable, it uses a series of small revolving satellite systems. When going into battle, smaller segments equipped with anti-gravity beams slowly revolve around the core, making it impossible for smaller craft to approach the Lordship."

if menuGroup:           Foundation.ShipDef.B5LordShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5LordShip.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
