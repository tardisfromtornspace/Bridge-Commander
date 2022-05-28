#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "EnterpriseF"
iconName = "EnterpriseF"
longName = "EnterpriseF"
shipFile = "EnterpriseF"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.EnterpriseF = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.EnterpriseF.desc = "No information available."


if menuGroup:           Foundation.ShipDef.EnterpriseF.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseF.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
