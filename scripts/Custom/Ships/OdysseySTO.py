#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "OdysseySTO"
iconName = "OdysseySTO"
longName = "USS Enterprise F (STO)"
shipFile = "OdysseySTO"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.OdysseySTO = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.OdysseySTO = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.OdysseySTO.desc = "Odyssey Class Starship badged as NCC - 1701 - F, a late 24th century to early 25th century Federation Flagship."
Foundation.ShipDef.OdysseySTO.SubMenu = "2400s"
Foundation.ShipDef.OdysseySTO.SubSubMenu = "Odyssey Class"

Foundation.ShipDef.OdysseySTO.OverrideWarpFXColor = Foundation.ShipDef.OdysseySTO.OverrideWarpFXColor
Foundation.ShipDef.OdysseySTO.OverridePlasmaFXColor = Foundation.ShipDef.OdysseySTO.OverridePlasmaFXColor
Foundation.ShipDef.OdysseySTO.dTechs = {
	"Borg Attack Resistance": 25,
	'Transphasic Torpedo Immune': 1,
	'Phased Torpedo Immune': 1,
	"AutoTargeting": { "Phaser": [3, 1] },
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Multivectral Shields': 15,
	'Regenerative Shields': 65,
   	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.OdysseySTO.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.OdysseySTO.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
