#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Shadow_Scout"
iconName = "Shadow_Scout"
longName = "Shadow Scout"
shipFile = "Shadow_Scout"
species = App.SPECIES_AMBASSADOR
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "The Shadows"
SubSubMenu = "Capital Ships"

Foundation.ShipDef.Shadow_Scout = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.Shadow_Scout.dTechs = { "Phase Cloak": 10, 'Breen Drainer Immune': 1, 'Shadow Dispersive Hull': 1, 'Automated Destroyed System Repair': {"Time": 800.0}}

Foundation.ShipDef.Shadow_Scout.desc = "A Shadow Scout Ship was a type of vessel employed by the Shadows. In 2260, shortly before the Battle of Sector 83, one such vessel was sent in ahead of the main fleet to warn if there was a problem. Though it initially tried to run to escape the White Star 2's jamming range, when it was severely damaged it turned and attempted to ram the White Star but was destroyed before it could get off a distress call. Several more were part of the main fleet when it later jumped in."
Foundation.ShipDef.Shadow_Scout.CloakingSFX = "shadowscream"
Foundation.ShipDef.Shadow_Scout.DeCloakingSFX = "shadowscream"

if menuGroup:           Foundation.ShipDef.Shadow_Scout.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Shadow_Scout.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
