#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "VreeXorr"
iconName = "VreeXorr"
longName = "Xorr Saucer"
shipFile = "VreeXorr"
species = App.SPECIES_AMBASSADOR
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "League of Non-Aligned Worlds"
SubSubMenu = "Ventuki Conglomerate"
Foundation.ShipDef.VreeXorr = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.VreeXorr.dTechs = { "Vree Shields": 100, "Tachyon Sensors": 1.0}
Foundation.ShipDef.VreeXorr.desc = "The Vree saucer was a class of Vree warship. A pair of these were among the first to visit Babylon 5 during the Deathwalker incident. This was a smaller and less powerful design than the Xill Class Saucer. The ship was configured only for non-atmospheric flight."


if menuGroup:           Foundation.ShipDef.VreeXorr.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VreeXorr.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
