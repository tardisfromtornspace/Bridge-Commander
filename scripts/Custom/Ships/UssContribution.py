#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "UssContribution"
iconName = "UssContribution"
longName = "U.S.S Contribution"
shipFile = "UssContribution"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.UssContribution = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.UssContribution = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.UssContribution.desc = "USS Contribution, a borg-enhanced vessel"
Foundation.ShipDef.UssContribution.sBridge = 'SovereignBridge'
Foundation.ShipDef.UssContribution.SubMenu = "2400s"
Foundation.ShipDef.UssContribution.SubSubMenu = "Borg Enhanced Ships"
Foundation.ShipDef.UssContribution.fMaxWarp = 9.99
Foundation.ShipDef.UssContribution.OverrideWarpFXColor = Foundation.ShipDef.UssContribution.OverrideWarpFXColor
Foundation.ShipDef.UssContribution.OverridePlasmaFXColor = Foundation.ShipDef.UssContribution.OverridePlasmaFXColor
Foundation.ShipDef.UssContribution.dTechs = {
	"Borg Attack Resistance": 35,
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	"AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	'Multivectral Shields': 5,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]},
	'Nanite Armor': 10000
}


if menuGroup:           Foundation.ShipDef.UssContribution.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.UssContribution.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
