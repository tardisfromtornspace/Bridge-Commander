import App
import Foundation
import traceback

abbrev = "QuamUniversumSaucer"
iconName = "QuamUniversumSaucer"
longName = "Quam Universum Saucer"
shipFile = "QuamUniversumSaucer"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed27c
	Foundation.ShipDef.QuamUniversumSaucer = Foundation.FutureFed27cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.QuamUniversumSaucer = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.QuamUniversumSaucer.desc = "The saucer section, it possesses a city dome."
Foundation.ShipDef.QuamUniversumSaucer.SubMenu = "27th Century"
Foundation.ShipDef.QuamUniversumSaucer.SubsUBMenu = "Quam Universum"
Foundation.ShipDef.QuamUniversumSaucer.OverrideWarpFXColor = Foundation.ShipDef.QuamUniversumSaucer.OverrideWarpFXColor
Foundation.ShipDef.QuamUniversumSaucer.OverridePlasmaFXColor = Foundation.ShipDef.QuamUniversumSaucer.OverridePlasmaFXColor
Foundation.ShipDef.QuamUniversumSaucer.dTechs = {
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	"AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	"Borg Attack Resistance": 60,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 55.0, "Power": -10000.0, "Efficiency": 0.99, "Resistance": 1.0,},
	'Diffusive Armor': 87500,
	"Digitizer Torpedo Immune": 1,
	'Drainer Immune': 1,
	"Inversion Beam": [12000, 0, 0.5, 1500],
	'Multivectral Shields': 25,
	'Phased Torpedo Immune': 1,
	"Reflector Shields": 2,
	'Reflux Weapon': 3800,
	'Regenerative Shields': 100,
	"Power Drain Beam": [1500, 0, 0.5, 1500],
	'Simulated Point Defence' : { "Distance": 75.0, "InnerDistance": 10.0, "Effectiveness": 0.9, "LimitTurn": 5.0, "LimitSpeed": 120, "LimitDamage": "-5000", "Period": 1.0, "MaxNumberTorps": 50, "Phaser": {"Priority": 1}},
	"SGReplicator Attack Resistance": 30,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	"TachyonBeam": {"Immune": -1},
	'Transphasic Torpedo Immune': 1,
}


if menuGroup:           Foundation.ShipDef.QuamUniversumSaucer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.QuamUniversumSaucer.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]