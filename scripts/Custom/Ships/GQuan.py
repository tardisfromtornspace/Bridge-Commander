#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "GQuan"
iconName = "GQuan"
longName = "G´Quan"
shipFile = "GQuan"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Narn Regime"
Foundation.ShipDef.GQuan = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.GQuan.desc = "G´Quan class heavy cruisers were the backbone of the Narn Regime´s naval forces up until their defeat by the Centauri Republic in 2259. Ma´Kan Industries located at Wings of G´Lan facility over Narn is responsible for manufactoring this class of vessel. "
Foundation.ShipDef.GQuan.SubSubMenu = "Capital ships"

if menuGroup:           Foundation.ShipDef.GQuan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GQuan.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
