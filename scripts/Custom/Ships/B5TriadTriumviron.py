#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "B5TriadTriumviron"
iconName = "B5TriadTriumviron"
longName = "Triumviron"
shipFile = "B5TriadTriumviron"
species = App.SPECIES_SOVEREIGN
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Triad Will"
SubSubMenu = "Capital Ships"

Foundation.ShipDef.B5TriadTriumviron = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
# Unknown capabilities, just using hull polarizer here because with an appropiate hardpoint it can be repurposed as an unknown type of shield.
Foundation.ShipDef.B5TriadTriumviron.dTechs = {
    'Breen Drainer Immune': 1,
    'Automated Destroyed System Repair': {"Time": 180.0},
    'Fed Ablative Armor': { "Plates": ["Armor Layer 1", "Armor Layer 2", "Armor Layer 3"]},
    "Tachyon Sensors": 0.2
}

Foundation.ShipDef.B5TriadTriumviron.desc = "The Triumviron is the ship of the Triad, one of the First Ones. Heavily armored, not much is known about them. However, the Triumviron is thought to not actually be a ship but a mental construct based on the Triad's phantasmal designs, a dream given form by the Triad's mental ability to shape matter."

if menuGroup:           Foundation.ShipDef.B5TriadTriumviron.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5TriadTriumviron.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
