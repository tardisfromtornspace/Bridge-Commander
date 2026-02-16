#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "Sagittarius"
iconName = "Sagittarius"
longName = "U.S.S. Seleucia"
shipFile = "Sagittarius"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed26c
	Foundation.ShipDef.Sagittarius = Foundation.FutureFed26cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Sagittarius = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.Sagittarius.desc = "A 26th century vessel, similar to 4-nacelled vessels of older eras like the Prometheus class."
#Foundation.ShipDef.Sagittarius.CloakingSFX = ""
#Foundation.ShipDef.Sagittarius.DeCloakingSFX = ""
Foundation.ShipDef.Sagittarius.OverrideWarpFXColor = Foundation.ShipDef.Sagittarius.OverrideWarpFXColor
Foundation.ShipDef.Sagittarius.OverridePlasmaFXColor = Foundation.ShipDef.Sagittarius.OverridePlasmaFXColor
Foundation.ShipDef.Sagittarius.fMaxWarp = 9.999999996 + 0.1
Foundation.ShipDef.Sagittarius.fCruiseWarp = 9.95 + 0.1

Foundation.ShipDef.Sagittarius.dTechs = {
	'Adv Armor Tech': 1,
	"AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	"Borg Attack Resistance": 50,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 55.0, "Power": -10000.0, "Efficiency": 0.99, "Resistance": 1.0,},
	'Drainer Immune': 1,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]},
	"GraviticLance": { "Time": 0.1, "TimeEffect": 5.0, "RadDepletionStrength": 1000, "Beams": ["Graviton Lance"], "Immune": 0},
	"Inversion Beam": [12000, 0, 0.5, 1500],
	'Multivectral Shields': 10,
	'Phased Torpedo Immune': 1,
	"Power Drain Beam": [1500, 0, 0.5, 1500],
	"Reflector Shields": 2,
	'Reflux Weapon': 3800,
	'Regenerative Shields': 75,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]},
	"SGReplicator Attack Resistance": 20,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	"TachyonBeam": {"Immune": -1},
	'Transphasic Torpedo Immune': 1,
}
   

Foundation.ShipDef.Sagittarius.SubMenu = "26th Century"


if menuGroup:           Foundation.ShipDef.Sagittarius.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Sagittarius.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
