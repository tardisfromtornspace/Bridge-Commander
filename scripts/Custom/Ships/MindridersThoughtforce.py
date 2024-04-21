#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "MindridersThoughtforce"
iconName = "MindridersThoughtforce"
longName = "Thoughtforce"
shipFile = "MindridersThoughtforce"
species = App.SPECIES_SOVEREIGN
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Mindrider Collective"
SubSubMenu = "Capital Ships"

Foundation.ShipDef.MindridersThoughtforce = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.MindridersThoughtforce.dTechs = {
    'Breen Drainer Immune': 1,
    'Automated Destroyed System Repair': {"Time": 10.0},
    "Tachyon Sensors": 0.2
}

Foundation.ShipDef.MindridersThoughtforce.desc = "The Thoughtforce is the ship of the Mindriders, one of the First Ones. It's constructed of carbon molecules that were telekinetically-compressed, and within its shell is a localised bubble of concentrated telepathic energy which contains the life energies of the Mindriders. The ships weapons are projectors of multi-wavelength pulses which the Mindriders aim and operate telepathically. The Mindriders are constantly projecting a telekinetic field to both protect and propel the ship. A field that is so powerful that only high-powered energy weapons have a chance of getting through the field without being deflected. Combined with the ship's self-repairing abilities, it makes the ship impervious to most of the Younger Races' munitions. "

if menuGroup:           Foundation.ShipDef.MindridersThoughtforce.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MindridersThoughtforce.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
