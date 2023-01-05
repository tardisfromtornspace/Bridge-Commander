#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "IndependenceYacht"
iconName = "IndependenceYacht"
longName = "Enterprise H yacht"
shipFile = "IndependenceYacht"
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
species = App.SPECIES_GALAXY

Foundation.ShipDef.IndependenceYacht = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.IndependenceYacht.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Multivectral Shields': 20,
	'Regenerative Shields': 25,
	"Transphasic Torpedo Immune": 1
}

Foundation.ShipDef.IndependenceYacht.desc = "Emulating the old Sovereign class, the Enterprise H included an upgraded Captain's Yacht as well."


if menuGroup:           Foundation.ShipDef.IndependenceYacht.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.IndependenceYacht.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
