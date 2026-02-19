#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Thompson"
iconName = "Thompson"
longName = "U.S.S. Thompson"
shipFile = "Thompson"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.Thompson = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Thompson.desc = "Thompson Class by Jeff Wallace\nBased on original sKetches for the Enterprise Before the first pilot was made circa 1964\nmodel and textures by Jeff Wallace\nConverted to Bridge Commander by MSR1701\nHardpointing by MSR1701"
Foundation.ShipDef.Thompson.SubMenu = "TOS Ships"
Foundation.ShipDef.Thompson.SubSubMenu = "Thompson class"


if menuGroup:           Foundation.ShipDef.Thompson.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Thompson.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
