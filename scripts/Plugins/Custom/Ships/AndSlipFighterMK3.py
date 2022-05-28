#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "AndSlipFighterMK3"
iconName = "AndSlipFighterMK3"
longName = "AndSlipFighterMK3"
shipFile = "AndSlipFighterMK3"
species = App.SPECIES_GALAXY
menuGroup = "Other Ships"
playerMenuGroup = "Other Ships"
Foundation.ShipDef.AndSlipFighterMK3 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.AndSlipFighterMK3.desc = "No information available."


if menuGroup:           Foundation.ShipDef.AndSlipFighterMK3.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AndSlipFighterMK3.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
