#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "TorvalusDarkKnife"
iconName = "TorvalusDarkKnife"
longName = "Dark Knife"
shipFile = "TorvalusDarkKnife"
species = App.SPECIES_SOVEREIGN
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Torvalus Speculation"
SubSubMenu = "Capital Ships"

import F_CloakAttackDef
Foundation.ShipDef.TorvalusDarkKnife = F_CloakAttackDef.CloakAttackDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu})
Foundation.ShipDef.TorvalusDarkKnife.dTechs = {
    'Breen Drainer Immune': 1,
    'Automated Destroyed System Repair': {"Time": 50.0}
}

Foundation.ShipDef.TorvalusDarkKnife.desc = "The Dark Knife is the ship of the Torvalus, one of the First Ones. The Dark Knife is a massive ship that is highly maneuverable with the shape of a long slender wing. It was built to avoid combat if possible, in the process creating the greatest scouting vessel that the wormlike Torvalus could have dreamed of. A curious race that's unwilling to meddle in the affairs of the Younger Races, they used their incredibly advanced stealth technology to construct their signature vessel. It's more than capable of defending itself, perfect for hit and run tactics."

if menuGroup:           Foundation.ShipDef.TorvalusDarkKnife.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TorvalusDarkKnife.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
