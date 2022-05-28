#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Kumari"
iconName = "Kumari"
longName = "Andorian Kumari"
shipFile = "Kumari"
species = App.SPECIES_GALAXY
menuGroup = "Pre-Fed ships"
playerMenuGroup = "Pre-Fed ships"
SubMenu = "Andorian Empire"
Foundation.ShipDef.Kumari = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.Kumari.desc = "The Kumari was an Andorian battle cruiser that was in service with the Andorian Imperial Guard during the mid-22nd century. It was named after the first ice-cutter to circumnavigate Andoria, and was the first starship of her class. The Kumari was capable of speeds in excess of warp five and was armed with advanced weaponry and a tractor beam. In 2154, the ship had a crew complement of eighty-six."


if menuGroup:           Foundation.ShipDef.Kumari.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Kumari.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
