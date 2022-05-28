#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "E2M0Warbird"
iconName = "Warbird"
longName = "E2M0Warbird"
shipFile = "E2M0Warbird"
species = App.SPECIES_GALAXY
menuGroup = "Romulan Ships"
playerMenuGroup = "Romulan Ships"
Foundation.ShipDef.E2M0Warbird = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.E2M0Warbird.desc = "No information available."


if menuGroup:           Foundation.ShipDef.E2M0Warbird.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.E2M0Warbird.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
