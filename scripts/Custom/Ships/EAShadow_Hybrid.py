#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "EAShadow_Hybrid"
iconName = "EAShadow_Hybrid"
longName = "Shadow Hybrid"
shipFile = "EAShadow_Hybrid"
species = App.SPECIES_AMBASSADOR
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Earth Alliance"
SubSubMenu = "Prototypes"

Foundation.ShipDef.EAShadow_Hybrid = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.EAShadow_Hybrid.dTechs = {'Breen Drainer Immune': 1}

Foundation.ShipDef.EAShadow_Hybrid.desc = "A Shadow Hybrid was a prototype starship based on Shadow technology, built by a secret division of Earthforce. It was the first ship to have original Shadow technology in cooperation with Earth Alliance capabilities, equipped with a hybrid version of the Shadow Pulse Ray. In 2259, one such ship was witnessed to have destroyed the EAS Cerberus, leaving then Ensign Matthew Gideon as the only survivor."


if menuGroup:           Foundation.ShipDef.EAShadow_Hybrid.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EAShadow_Hybrid.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
