import App
import Foundation
import traceback


abbrev = "DarkWellsRef"
iconName = "DarkWellsRef"
longName = "Dark Timeline Wells Refit"
shipFile = "DarkWellsRef"
species = App.SPECIES_GALAXY
menuGroup = "Dark Timeline Ships"
playerMenuGroup = "Dark Timeline Ships"

try:
	import Custom.Autoload.RaceFutureFed29c
	Foundation.ShipDef.DarkWellsRef = Foundation.FutureFed29cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.DarkWellsRef = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.DarkWellsRef.SubMenu = "Union Power"
Foundation.ShipDef.DarkWellsRef.SubSubMenu = "29th Century"
Foundation.ShipDef.DarkWellsRef.desc = "The Wells Class is the Dark Timeline counterpart of the Federation Wells class. Unlike Federation Wells classes, Dark Wells were designed as a superiority factor rather than a timeline explorator vessel.\n\nThe Wells received a refit that would have been more than a match for prime timeline Sorites-class Timeships.\n\nAs most Union Power vessels, Dark Wells were equipped with several technologies that would have been banned on standard Federation vessels."
Foundation.ShipDef.DarkWellsRef.OverrideWarpFXColor = Foundation.ShipDef.DarkWellsRef.OverrideWarpFXColor
Foundation.ShipDef.DarkWellsRef.OverridePlasmaFXColor = Foundation.ShipDef.DarkWellsRef.OverridePlasmaFXColor


Foundation.ShipDef.DarkWellsRef.dTechs = {
	'Adv Armor Tech': 1,
	"Alternate-Warp-FTL": {
		"Setup": {
			"DrWTimeVortexDrive": {	"Core": ["Isofractic Reactor", "Chronofractic Drive"], },
		},
	},
	"Andromedan Tractor-Repulsor Beams Weapon": [{"HullDmgMultiplier": 2400.0, "ShieldDmgMultiplier": 150.0}, ["Dark Wells Ref Tractor Beam"]],
	"Andromedan Tractor Beams Weapon Immune": 1,
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	"Borg Attack Resistance": 80,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 25.0, "Power": -11000.0, "Efficiency": 0.99, "Resistance": 0.95,},
	'Digitizer Torpedo Immune': 1,
	'Drainer Immune': 1,
	"GraviticLance": { "Time": 2.0, "TimeEffect": 15.0, "RadDepletionStrength": 2000, "Immune": 1},
	"Inversion Beam": [0.5, 0, 0.5, 10500],
	'Multivectral Shields' : 27,
	"Power Drain Beam": [0.5, 0, 0.5, 10500],
	"Phase Cloak": -1, 
	'Phased Torpedo Immune': 1,
	"Reflector Shields": 25,
	'Reflux Weapon': 1500,
	'Regenerative Shields': 60,
	"SGReplicator Attack Resistance": 40,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	'Simulated Point Defence' : { "Distance": 15.0, "InnerDistance": 5.0, "Effectiveness": 0.9, "LimitTurn": 5.0, "LimitSpeed": 120, "LimitDamage": "-10000", "Period": 1.0, "MaxNumberTorps": 2, "Phaser": {"Priority": 1}},
	"Subatomic Disruptor Beams Weapon": [{"HullDmgMultiplier": 1000.0, "ShieldDmgMultiplier": 19000.0, "Beams": ["Isofractic Transwarp Lance"]}, ["DTTranswarpLance"]],
	'Subatomic Disruptor Beams Weapon Immune': 1,
	"Subparticle Torpedo Immune": 1,
	"TachyonBeam": {"Time": 5.0, "TimeEffect": 1.2, "Immune": 1},
	"Tachyon Sensors": 0,
	"TimeVortex Torpedo Immune": 1,
	'Transphasic Torpedo Immune': 1,
	'Transcendental Rodinium Armor': 230000,
	'Vree Shields': 58,	
}


Foundation.ShipDef.DarkWellsRef.CloakingSFX   = "Future_cloak"
Foundation.ShipDef.DarkWellsRef.DeCloakingSFX = "Future_uncloak"


if menuGroup:           Foundation.ShipDef.DarkWellsRef.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DarkWellsRef.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]