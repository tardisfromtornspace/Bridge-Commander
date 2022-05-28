#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Hideki"
iconName = "Hideki"
longName = "Hideki"
shipFile = "Hideki"
species = App.SPECIES_GALAXY
menuGroup = "Card Ships"
playerMenuGroup = "Card Ships"
Foundation.ShipDef.Hideki = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Hideki.desc = "No information available."


if menuGroup:           Foundation.ShipDef.Hideki.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Hideki.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
