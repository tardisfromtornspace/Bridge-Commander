import App
import Foundation
import traceback


abbrev = "DarkWells"
iconName = "DarkWells"
longName = "Dark Timeline Wells"
shipFile = "DarkWells"
species = App.SPECIES_GALAXY
menuGroup = "Dark Timeline Ships"
playerMenuGroup = "Dark Timeline Ships"

try:
	import Custom.Autoload.RaceFutureFed29c
	Foundation.ShipDef.DarkWells = Foundation.FutureFed29cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.DarkWells = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.DarkWells.SubMenu = "Union Power"
Foundation.ShipDef.DarkWells.SubSubMenu = "29th Century"
Foundation.ShipDef.DarkWells.desc = "The Wells Class is the Dark Timeline counterpart of the Federation Wells class. Union Power Wells were designed as a superiority factor rather than a timeline explorator vessel.\n\nAs most Union Power vessels, Dark Wells were equipped with several technologies that would have been banned on standard Federation vessels."
Foundation.ShipDef.DarkWells.OverrideWarpFXColor = Foundation.ShipDef.DarkWells.OverrideWarpFXColor
Foundation.ShipDef.DarkWells.OverridePlasmaFXColor = Foundation.ShipDef.DarkWells.OverridePlasmaFXColor

Foundation.ShipDef.DarkWells.dTechs = {
	'Adv Armor Tech': 1,
	"Alternate-Warp-FTL": {
		"Setup": {
			"DrWTimeVortexDrive": {	"Core": ["Isolytic Reactor", "Temporal Drive"], },
		},
	},
	"Andromedan Tractor-Repulsor Beams Weapon": [{"HullDmgMultiplier": 1200.0, "ShieldDmgMultiplier": 75.0}, ["Dark Wells Tractor Beam"]],
	"Andromedan Tractor-Repulsor Beams Weapon Immune": 1,
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	"Borg Attack Resistance": 80,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 25.0, "Power": -11000.0, "Efficiency": 0.99, "Resistance": 0.95,},
	'Digitizer Torpedo Immune': 1,
	'Drainer Immune': 1,
	"GraviticLance": { "Time": 2.0, "TimeEffect": 15.0, "RadDepletionStrength": 1000, "Immune": 0},
	"Inversion Beam": [0.5, 0, 0.5, 10500],
	'Multivectral Shields' : 27,
	"Power Drain Beam": [0.5, 0, 0.5, 10500],
	"Phase Cloak": -1, 
	'Phased Torpedo Immune': 1,
	"Reflector Shields": 20,
	'Reflux Weapon': 1500,
	'Regenerative Shields': 60,
	"SGReplicator Attack Resistance": 40,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	'Simulated Point Defence' : { "Distance": 15.0, "InnerDistance": 5.0, "Effectiveness": 0.9, "LimitTurn": 5.0, "LimitSpeed": 120, "LimitDamage": "-10000", "Period": 1.0, "MaxNumberTorps": 2, "Phaser": {"Priority": 1}},
	"Subatomic Disruptor Beams Weapon": [{"HullDmgMultiplier": 1000.0, "ShieldDmgMultiplier": 19000.0, "Beams": ["Focused Isolytic Disruptor"]}, ["IsolyticLance"]],
	'Subatomic Disruptor Beams Weapon Immune': 1,
	"Subparticle Torpedo Immune": 1,
	"TachyonBeam": {"Time": 5.0, "TimeEffect": 1.2, "Immune": 1},
	"Tachyon Sensors": 0,
	'Transphasic Torpedo Immune': 1,
	'Transcendental Rodinium Armor': 155000,
	'Vree Shields': 55,	
}



Foundation.ShipDef.DarkWells.CloakingSFX   = "TemporalPhase"
Foundation.ShipDef.DarkWells.DeCloakingSFX = "TemporalUnphase"


if menuGroup:           Foundation.ShipDef.DarkWells.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DarkWells.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]