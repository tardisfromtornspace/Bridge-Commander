#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "SFRD_Promellian"
iconName = "SFRD_Promellian"
longName = "Promellian"
shipFile = "SFRD_Promellian"
species = App.SPECIES_GALAXY
menuGroup = "Other Ships"
playerMenuGroup = "Other Ships"
Foundation.ShipDef.SFRD_Promellian = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.SFRD_Promellian.desc = "Promellian BattleCruiser"


if menuGroup:           Foundation.ShipDef.SFRD_Promellian.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SFRD_Promellian.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
