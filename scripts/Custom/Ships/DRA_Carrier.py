#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DRA_Carrier"
iconName = "DRA_Carrier"
longName = "Drakh Carrier"
shipFile = "DRA_Carrier"
species = App.SPECIES_WARBIRD
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Drakh Horde"
SubSubMenu = "Carriers"
Foundation.ShipDef.DRA_Carrier = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })


Foundation.ShipDef.DRA_Carrier.desc = "The Drakh Carrier was a vessel of unknown class used by the Drakh. The vessel was enormous, much larger than a regular cruiser and capable of carrying large complement of fighter-like craft and shuttlecraft. It can carry Drakh fighters and shuttles, but appears to be unequipped with its own jump engine; a surprise for a carrier type vessel. In 2261, the White Star fleet accompanied Delenn on a mercy mission to Norsai territory which had been under attack by unknown raiders. When the fleet emerged from hyperspace they found a group of unknown type. The unknown vessels escorted the White Stars back to their carrier where a Drakh emissary came aboard Delenn's vessel to create an alliance between them."


if menuGroup:           Foundation.ShipDef.DRA_Carrier.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DRA_Carrier.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
