#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DJEnterpriseGThunderbird"
iconName = "DJEnterpriseGThunderbird"
longName = "DJ Thunderbird"
shipFile = "DJEnterpriseGThunderbird"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.DJEnterpriseGThunderbird = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DJEnterpriseGThunderbird.desc = "Thunderbird ASV (Auxillary Support Vehicle)\n\nThe Thunderbird is an ASV that augments the explorative and defensive capacities of the Eclipse Class starship.  The ASV can reach speeds of warp 9.7 for more than 52 hours.  Despite its overall large size, the habitable capacity of the vehicle is limited and there is space for only 16 crew.\n\nThe vehicle has two quantum filament pulse launchers as well as two phaser banks."
Foundation.ShipDef.DJEnterpriseGThunderbird.SubMenu = "Eclipse Class"
Foundation.ShipDef.DJEnterpriseGThunderbird.SubSubMenu = "DJ Enterprise G"
Foundation.ShipDef.DJEnterpriseGThunderbird.fMaxWarp = 9.6 + 0.0001
Foundation.ShipDef.DJEnterpriseGThunderbird.fCruiseWarp = 7.5 + 0.0001
Foundation.ShipDef.DJEnterpriseGThunderbird.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 20,
	'Multivectral Shields': 20,
	"Transphasic Torpedo Immune": 1
}


if menuGroup:           Foundation.ShipDef.DJEnterpriseGThunderbird.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJEnterpriseGThunderbird.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
