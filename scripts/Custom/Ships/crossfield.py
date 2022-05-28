#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "crossfield"
iconName = "Crossfield"
longName = "Crossfield"
shipFile = "crossfield"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.crossfield = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.crossfield.desc = "The Crossfield class was a type of Federation starship in service during the mid-23rd century. Consisting of a modular saucer section, a wide secondary hull, and two elongated nacelles, these odd design choices were put into place to facilitate an experimental method of travel involving mycelial spores."


if menuGroup:           Foundation.ShipDef.crossfield.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.crossfield.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
