#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "HestiaVentral"
iconName = "HestiaVentral"
longName = "Hestia Ventral"
shipFile = "HestiaVentral"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.HestiaVentral = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.HestiaVentral = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()
	
Foundation.ShipDef.HestiaVentral.desc = "Ventral Flight Section of the Hestia Class."
Foundation.ShipDef.HestiaVentral.SubMenu = "2400s"
Foundation.ShipDef.HestiaVentral.SubSubMenu = "Hestia Class"
Foundation.ShipDef.HestiaVentral.OverrideWarpFXColor = Foundation.ShipDef.HestiaVentral.OverrideWarpFXColor
Foundation.ShipDef.HestiaVentral.OverridePlasmaFXColor = Foundation.ShipDef.HestiaVentral.OverridePlasmaFXColor
Foundation.ShipDef.HestiaVentral.dTechs = {
	"Borg Attack Resistance": 25,
	'Transphasic Torpedo Immune': 1,
	'Phased Torpedo Immune': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	'Multivectral Shields': 25,
	'Regenerative Shields': 60,
	"Fed Ablative Armor": {"Plates": ["Aft Saucer Armor","Port Saucer Armor","Starboard Ablative Armor","Engineering Ablative Armor","Top Ablative Armor","Forward Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.HestiaVentral.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HestiaVentral.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
