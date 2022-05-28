#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "SolarSail"
iconName = "SolarSail"
longName = "SolarSail"
shipFile = "SolarSail"
species = App.SPECIES_GALAXY
menuGroup = "Bajoran Ships"
playerMenuGroup = "Bajoran Ships"
Foundation.ShipDef.SolarSail = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.SolarSail.desc = "Bajoran lightships were equipped with solar sails which could be individually ejected in the event of an emergency. It was discovered that these sails also made them capable of faster-than-light speeds and interstellar travel due to the presence of tachyon eddies in the Bajoran system. The Bajorans used solar sails as early as the 16th century, and continued to do so until as late as the 21st century."


if menuGroup:           Foundation.ShipDef.SolarSail.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SolarSail.RegisterQBPlayerShipMenu(playerMenuGroup)


Foundation.ShipDef.SolarSail.fMaxWarp = 1.0
Foundation.ShipDef.SolarSail.fWarpEntryDelayTime = 1.0

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
