#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DanubemkI"
iconName = "DanubemkI"
longName = "Danube Mk-I"
shipFile = "DanubemkI"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
SubMenu = "Shuttles"

Foundation.ShipDef.DanubemkI = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.DanubemkI.desc = "No information available."


if menuGroup:           Foundation.ShipDef.DanubemkI.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DanubemkI.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
