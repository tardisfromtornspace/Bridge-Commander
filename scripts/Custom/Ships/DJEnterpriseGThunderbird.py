#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "DJEnterpriseGThunderbird"
iconName = "DJEnterpriseGThunderbird"
longName = "DJ Thunderbird"
shipFile = "DJEnterpriseGThunderbird"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.DJEnterpriseGThunderbird = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.DJEnterpriseGThunderbird = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.DJEnterpriseGThunderbird.desc = "Thunderbird ASV (Auxillary Support Vehicle)\n\nThe Thunderbird is an ASV that augments the explorative and defensive capacities of the Eclipse Class starship.  The ASV can reach speeds of warp 9.7 for more than 52 hours.  Despite its overall large size, the habitable capacity of the vehicle is limited and there is space for only 16 crew.\n\nThe vehicle has two quantum filament pulse launchers as well as two phaser banks."

Foundation.ShipDef.DJEnterpriseGThunderbird.SubMenu = "2400s"
Foundation.ShipDef.DJEnterpriseGThunderbird.SubSubMenu = "Eclipse Class"
Foundation.ShipDef.DJEnterpriseGThunderbird.SubSubSubMenu = "DJ Enterprise G"

Foundation.ShipDef.DJEnterpriseGThunderbird.fMaxWarp = 9.6 + 0.0001
Foundation.ShipDef.DJEnterpriseGThunderbird.fCruiseWarp = 7.5 + 0.0001
Foundation.ShipDef.DJEnterpriseGThunderbird.OverrideWarpFXColor = Foundation.ShipDef.DJEnterpriseGThunderbird.OverrideWarpFXColor
Foundation.ShipDef.DJEnterpriseGThunderbird.OverridePlasmaFXColor = Foundation.ShipDef.DJEnterpriseGThunderbird.OverridePlasmaFXColor
Foundation.ShipDef.DJEnterpriseGThunderbird.dTechs = {
	"Borg Attack Resistance": 35,
	'Transphasic Torpedo Immune': 1,
	'Drainer Immune': 1,
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 45,
	'Multivectral Shields': 30,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.DJEnterpriseGThunderbird.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJEnterpriseGThunderbird.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
