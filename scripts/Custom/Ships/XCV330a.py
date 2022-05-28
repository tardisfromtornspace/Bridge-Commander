import Foundation
import App
abbrev = 'XCV330a'
iconName = 'XCV330a'
longName = 'XCV-330a'
shipFile = 'XCV330a'
menuGroup = 'Pre-Fed ships'
playerMenuGroup = 'Pre-Fed ships'
species = App.SPECIES_GALAXY
SubMenu = "United Earth ships"
SubSubMenu = "XCV Class"
Foundation.ShipDef.XCV330a = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.XCV330a.fMaxWarp = 1.3
Foundation.ShipDef.XCV330a.fCruiseWarp = 1.2

Foundation.ShipDef.XCV330a.desc = "The XCV-330a was a refitted model of the old XCV-330 incorporating a pair of warp nacelles to grant more high-warp flexibility."

if menuGroup:           Foundation.ShipDef.XCV330a.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.XCV330a.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]