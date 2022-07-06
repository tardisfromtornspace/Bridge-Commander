#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "SigmaWalkerScienceLab"
iconName = "SigmaWalkerScienceLab"
longName = "The Traveller"
shipFile = "SigmaWalkerScienceLab"
species = App.SPECIES_SOVEREIGN
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Sigma-957 Walkers"
SubSubMenu = "Capital Ships"

Foundation.ShipDef.SigmaWalkerScienceLab = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
# Unknown capabilities, just using hull polarizer here because with an appropiate hardpoint it can be repurposed as an unknown type of shield.
Foundation.ShipDef.SigmaWalkerScienceLab.dTechs = {
    'Breen Drainer Immune': 1,
    'Fed Ablative Armor': { "Plates": ["Shield"]},
}

Foundation.ShipDef.SigmaWalkerScienceLab.desc = "Little is known of these First Ones ships, only that on the strict sense of the word these ships are unarmed. However if necessary their sensor systems can be as destructive."

if menuGroup:           Foundation.ShipDef.SigmaWalkerScienceLab.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SigmaWalkerScienceLab.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
