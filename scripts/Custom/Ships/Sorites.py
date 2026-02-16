import Foundation
import App
import traceback


abbrev = 'Sorites'
iconName = 'Sorites'
longName = 'U.S.S. Sorites'
shipFile = 'Sorites' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY


try:
	import Custom.Autoload.RaceFutureFed29c
	Foundation.ShipDef.Sorites = Foundation.FutureFed29cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Sorites = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.Sorites.fMaxWarp = 12 + 4.0
Foundation.ShipDef.Sorites.fCruiseWarp = 9.9999999999998 + 4.0
Foundation.ShipDef.Sorites.OverrideWarpFXColor = Foundation.ShipDef.Sorites.OverrideWarpFXColor
Foundation.ShipDef.Sorites.OverridePlasmaFXColor = Foundation.ShipDef.Sorites.OverridePlasmaFXColor

Foundation.ShipDef.Sorites.dTechs = {
	'Adv Armor Tech': 1,
	"Alternate-Warp-FTL": {
		"Setup": {
			"DrWTimeVortexDrive": {	"Core": ["Quantum Singularity Reactor", "Adv Temporal Drive", "Omni inversic Shields"], },
		},
	},
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	"Borg Attack Resistance": 95,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Digitizer Torpedo Immune': 1,
	'Drainer Immune': 1,
	"Inversion Beam": [0.5, 0, 0.5, 1500],
	'Multivectral Shields' : 28,
	"Power Drain Beam": [0.5, 0, 0.5, 1500],
	"Phase Cloak": -1, 
	'Phased Torpedo Immune': 1,
	'Reflux Weapon': 1000,
	'Regenerative Shields': 60,
	'Transphasic Torpedo Immune': 1,
	"SGReplicator Attack Resistance": 40,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	'Subatomic Disruptor Beams Weapon Immune': 1,
	"Subparticle Torpedo Immune": 1,
	'Tetraburnium Armour': 200000,
	"TimeVortex Torpedo Immune": 1,
	'Vree Shields': 55,	
}

Foundation.ShipDef.Sorites.SubMenu = "31st Century"
Foundation.ShipDef.Sorites.CloakingSFX   = "Future_cloak2"
Foundation.ShipDef.Sorites.DeCloakingSFX = "Future_uncloak2"                                                                                 
Foundation.ShipDef.Sorites.desc = 'The last generation of Timeships put into service before the Burn and the ban of temporal tech following the Temporal Cold War and Temporal Wars.'


if menuGroup:           Foundation.ShipDef.Sorites.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Sorites.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
