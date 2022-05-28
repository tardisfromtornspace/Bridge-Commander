import Foundation
import App
abbrev = 'XCV330o'
iconName = 'XCV330o'
longName = 'XCV-330'
shipFile = 'XCV330o'
menuGroup = 'Pre-Fed ships'
playerMenuGroup = 'Pre-Fed ships'
species = App.SPECIES_GALAXY
SubMenu = "United Earth ships"
SubSubMenu = "XCV Class"
Foundation.ShipDef.XCV330o = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.XCV330o.fMaxWarp = 1.3
Foundation.ShipDef.XCV330o.fCruiseWarp = 1.2

Foundation.ShipDef.XCV330o.desc = "The XCV-330 was one of the most radical experiments in early Earth starship design, partially based on Vulcan annular propulsion system, but using a cyclotron accelerator system to create a proton flux that circulated through the outer rings of verterium gallenide segments. While it proved 17% more efficient than its vulcan predeccesors, it was considered a dead-end since it proved resistant to flight directional changes (typical of a coleopteric drive system), a lack of flexibility humans considered too important."

if menuGroup:           Foundation.ShipDef.XCV330o.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.XCV330o.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]