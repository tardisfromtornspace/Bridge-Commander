#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "VOR_Cruiser"
iconName = "Vorlon_Cruiser"
longName = "Vorlon Cruiser"
shipFile = "VOR_Cruiser"
species = App.SPECIES_SOVEREIGN
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Vorlon Empire"
Foundation.ShipDef.VOR_Cruiser = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.VOR_Cruiser.dTechs = {'Breen Drainer Immune': 0}

Foundation.ShipDef.VOR_Cruiser.desc = "The Vorlon cruiser was the largest and most powerful ship of the Vorlon fleet, save of course for the Vorlon planetkiller. Fast, powerful and very big, Vorlon Cruisers have seen to be more than a match for the Shadow Vessel and seems to only be vulnerable to overwhelming numbers though they have on occasion been seen to travel alone."
Foundation.ShipDef.VOR_Cruiser.SubSubMenu = "Starships"

if menuGroup:           Foundation.ShipDef.VOR_Cruiser.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VOR_Cruiser.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
