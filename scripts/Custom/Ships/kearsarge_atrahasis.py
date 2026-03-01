#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "kearsarge_atrahasis"
iconName = "kearsarge_atrahasis"
longName = "Kearsarge Class"
shipFile = "kearsarge_atrahasis"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.kearsarge_atrahasis = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.kearsarge_atrahasis.desc = "Kearsarge Class\nModel by: Atrahasis\nReleased Sept 19, 2003. \nRE-RELEASED MAY 2007\nConverted for Bridge Commander by MSR1701\nHardpointing by MSR1701"
Foundation.ShipDef.kearsarge_atrahasis.SubMenu = "TOS Ships"
Foundation.ShipDef.kearsarge_atrahasis.SubSubMenu = "Kearsarge Class"

if menuGroup:           Foundation.ShipDef.kearsarge_atrahasis.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.kearsarge_atrahasis.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
