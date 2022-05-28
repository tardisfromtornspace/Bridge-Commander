#####  Created by:
#####  Bridge 
#Foundation.ShipDef.SFRD_T18.hasTGLName = 1
#Foundation.ShipDef.SFRD_T18.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.SFRD_T18.desc = 'reated by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "SFRD_T18"
iconName = "SFRD_T18"
longName = "Type 18"
shipFile = "SFRD_T18"
species = App.SPECIES_GALAXY
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Shuttles"
Foundation.ShipDef.SFRD_T18 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.SFRD_T18.desc = "Type 18 shuttle"
Foundation.ShipDef.SFRD_T18.fMaxWarp = 3
Foundation.ShipDef.SFRD_T18.sBridge = 'Type11Bridge'

if menuGroup:           Foundation.ShipDef.SFRD_T18.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SFRD_T18.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
