#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "VreeXill"
iconName = "VreeXill"
longName = "Xill Cruiser"
shipFile = "VreeXill"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "League of Non-Aligned Worlds"
SubSubMenu = "Ventuki Conglomerate"
Foundation.ShipDef.VreeXill = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.VreeXill.dTechs = { "Vree Shields": 100}
Foundation.ShipDef.VreeXill.desc = "The Xill Class Cruiser is the Vree's most common starship. Manufactured by the Merchant/Adventurers Guild at the Madrasi Orbital facility over Photikar, the Xill is very fast and powerful and would become a more and more common sight in the years following the Second Shadow War as the Vree continued to expand their influence. The Xill's primary weapon is a cluster of 15 phased array antimatter cannons, mounted on the vessel's ventral surface and is normally used for a strafing run that unleashes a torrent of energy bolts that can easily rip apart a squadron of Vorlon or Shadow Fighters."


if menuGroup:           Foundation.ShipDef.VreeXill.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VreeXill.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
