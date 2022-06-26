#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DRA_Raider"
iconName = "DRA_Raider"
longName = "Drakh Fighter"
shipFile = "DRA_Raider"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Drakh Horde"
SubSubMenu = "Fighters"
Foundation.ShipDef.DRA_Raider = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })


Foundation.ShipDef.DRA_Raider.desc = "The Drakh fighter was a large fighter vessel used by the Drakh. Ships of this type are carried into the battle usually by large carriers or cruisers. Two of these vessels are capable of shooting down a White Star with just a few direct hits."


if menuGroup:           Foundation.ShipDef.DRA_Raider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DRA_Raider.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
