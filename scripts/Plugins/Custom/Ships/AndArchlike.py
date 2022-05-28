#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "AndArchlike"
iconName = "AndArchlike"
longName = "AndArchlike"
shipFile = "AndArchlike"
species = App.SPECIES_GALAXY
menuGroup = "Other Ships"
playerMenuGroup = "Other Ships"
Foundation.ShipDef.AndArchlike = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.AndArchlike.desc = "No information available."


if menuGroup:           Foundation.ShipDef.AndArchlike.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AndArchlike.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
