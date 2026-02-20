import App
import Foundation
import traceback


abbrev = "DarkSongClass"
iconName = "DarkSongClass"
longName = "Dark Timeline Song Class"
shipFile = "DarkSongClass"
species = App.SPECIES_GALAXY
menuGroup = "Dark Timeline Ships"
playerMenuGroup = "Dark Timeline Ships"

try:
	import Custom.Autoload.RaceFutureFed28c
	Foundation.ShipDef.DarkSongClass = Foundation.FutureFed28cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.DarkSongClass = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.DarkSongClass.SubMenu = "Union Power"
Foundation.ShipDef.DarkSongClass.SubSubMenu = "28th Century"
Foundation.ShipDef.DarkSongClass.desc = "The Song Class is the Dark Timeline counterpart of the Federation Song class. Union Power Songs were built earlier than Federation ones, on 2732, and were designed as a superiority factor rather than a timeline explorator vessel.\n\nAs most Union Power vessels, Dark Songs were equipped with several technologies that would have been banned on standard Federation vessels."
Foundation.ShipDef.DarkSongClass.fMaxWarp = 12 + 1.0
Foundation.ShipDef.DarkSongClass.fCruiseWarp = 9.9999993 + 1.0
Foundation.ShipDef.DarkSongClass.OverrideWarpFXColor = Foundation.ShipDef.DarkSongClass.OverrideWarpFXColor
Foundation.ShipDef.DarkSongClass.OverridePlasmaFXColor = Foundation.ShipDef.DarkSongClass.OverridePlasmaFXColor
Foundation.ShipDef.DarkSongClass.dTechs = {
	'Ablative Armour': 87500,
	'Adv Armor Tech': 1,
	"Alternate-Warp-FTL": {
		"Setup": {
			"DrWTimeVortexDrive": {	"Core": ["Partial Isolytic Core", "Temporal Drive"], },
		},
	},
	"Andromedan Tractor-Repulsor Beams Weapon": [{"HullDmgMultiplier": 900.0, "ShieldDmgMultiplier": 50.0}, ["Dark Song Tractor Beam"]],
	#"Andromedan Tractor-Repulsor Beams Weapon Immune": 1,
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	"Borg Attack Resistance": 80,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 25.0, "Power": -10000.0, "Efficiency": 0.99, "Resistance": 0.95,},
	'Digitizer Torpedo Immune': 1,
	'Drainer Immune': 1,
	"GraviticLance": { "Time": 2.0, "TimeEffect": 15.0, "RadDepletionStrength": 365, "Immune": 0},
	"Inversion Beam": [0.5, 0, 0.5, 1500],
	'Multivectral Shields' : 25,
	"Power Drain Beam": [0.5, 0, 0.5, 1500],
	"Phase Cloak": -1, 
	'Phased Torpedo Immune': 1,
	"Reflector Shields": 15,
	'Reflux Weapon': 1000,
	'Regenerative Shields': 60,
	"SGReplicator Attack Resistance": 40,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	'Simulated Point Defence' : { "Distance": 15.0, "InnerDistance": 5.0, "Effectiveness": 0.9, "LimitTurn": 5.0, "LimitSpeed": 120, "LimitDamage": "-10000", "Period": 1.0, "MaxNumberTorps": 2, "Phaser": {"Priority": 1}},
	"Subatomic Disruptor Beams Weapon": [{"HullDmgMultiplier": 1000.0, "ShieldDmgMultiplier": 19000.0, "Beams": ["Proto Isolytic Disruptor"]}, ["ResIsolyticBurstBeam"]],
	"Subparticle Torpedo Immune": 1,
	"TachyonBeam": {"Time": 5.0, "TimeEffect": 1.0, "Immune": 1},
	"Tachyon Sensors": 0,
	'Transphasic Torpedo Immune': 1,
	'Vree Shields': 56,	
}

Foundation.ShipDef.DarkSongClass.CloakingSFX   = "ChronomaticCloak"
Foundation.ShipDef.DarkSongClass.DeCloakingSFX = "ChronomaticUncloak"


if menuGroup:           Foundation.ShipDef.DarkSongClass.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DarkSongClass.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]