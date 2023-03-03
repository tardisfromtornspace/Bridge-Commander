#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DMResurrection"
iconName = "DMResurrection"
longName = "USS Resurrection"
shipFile = "DMResurrection"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.DMResurrection = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DMResurrection.desc = "No information available."
Foundation.ShipDef.DMResurrection.SubMenu = "Constitution class"
Foundation.ShipDef.DMResurrection.SubSubMenu = "Resurrection refit"
Foundation.ShipDef.DMResurrection.fMaxWarp = 9.89 + 0.0001
Foundation.ShipDef.DMResurrection.fCruiseWarp = 7.86 + 0.0001
Foundation.ShipDef.DMResurrection.fCrew = 450


if menuGroup:           Foundation.ShipDef.DMResurrection.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DMResurrection.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
