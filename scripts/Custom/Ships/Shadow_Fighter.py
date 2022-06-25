#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Shadow_Fighter"
iconName = "Shadow_Fighter"
longName = "Shadow Fighter"
shipFile = "Shadow_Fighter"
species = App.SPECIES_SHUTTLE
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "The Shadows"
SubSubMenu = "Fighters"
Foundation.ShipDef.Shadow_Fighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.Shadow_Fighter.dTechs = { "Phase Cloak": 10, 'Breen Drainer Immune': 1, 'Shadow Dispersive Hull': 1}

Foundation.ShipDef.Shadow_Fighter.desc = "The Shadow Fighter was the standard fighter used by the Shadows. Shadow fighters are extremely tough, fast and powerful. It appears to feature the same resilient, blast refracting material as the larger Shadow Vessels. The squat, spiky body of the Shadow Fighter is built around a central pulse cannon which, when fired causes the entire craft to convulse, appearing to 'spit' as it discharges the weapon. More than capable of holding its own against most fighters used by the Younger Races, the only non-First One fighter seen to outmatch the Shadow Fighter was the early White Star prototype."
Foundation.ShipDef.Shadow_Fighter.CloakingSFX = "shadowscream"
Foundation.ShipDef.Shadow_Fighter.DeCloakingSFX = "shadowscream"


if menuGroup:           Foundation.ShipDef.Shadow_Fighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Shadow_Fighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
