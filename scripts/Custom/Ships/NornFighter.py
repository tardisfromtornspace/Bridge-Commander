import App
import Foundation
import traceback

abbrev = "NornFighter"
iconName = "NornFighter"
longName = "Norn Fighter"
shipFile = "NornFighter"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed28c
	Foundation.ShipDef.NornFighter = Foundation.FutureFed28cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.NornFighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.NornFighter.desc = "This Fighter is a small craft designed to support the Universe-II class."
Foundation.ShipDef.NornFighter.SubMenu = "28th Century"
Foundation.ShipDef.NornFighter.OverrideWarpFXColor = Foundation.ShipDef.NornFighter.OverrideWarpFXColor
Foundation.ShipDef.NornFighter.OverridePlasmaFXColor = Foundation.ShipDef.NornFighter.OverridePlasmaFXColor
Foundation.ShipDef.NornFighter.CloakingSFX   = "ChronomaticCloak"
Foundation.ShipDef.NornFighter.DeCloakingSFX = "ChronomaticUncloak"
Foundation.ShipDef.NornFighter.dTechs = {
	'Automated Destroyed System Repair': {"Time": 25.0, "DoNotInterfere": 1},
	"Andromedan absorption Armor": [31500, "Elukethite Energy Distribution Plating", {
			"Torpedoes": [],
			"Tractors": [],
			"BeamsFactor": 0.05,
			"PulsesFactor": 0.0,
			"GlobalFactor": 0.05,
			"HealDepletes": 0,
			"DmgStrMod": 0.0,
			"DmgRadMod": 0.0,
		}],
	"Borg Attack Resistance": 60,
	'Breen Drainer Immune': 1,
	'ChronitonTorpe Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 55.0, "Power": -10000.0, "Efficiency": 0.99, "Resistance": 1.0,},
	"Digitizer Torpedo Immune": 1,
	'Drainer Immune': 1,
	'Multivectral Shields': 25,
	'Phased Torpedo Immune': 1,
	'Reflux Weapon Immune': 1,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	"SGReplicator Attack Resistance": 30,
	"SG Ori Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Asgard Beams Weapon Immune": 2,
	'Transphasic Torpedo Immune': 1
}


if menuGroup:           Foundation.ShipDef.NornFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NornFighter.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]