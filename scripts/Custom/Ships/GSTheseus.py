import App
import Foundation
import traceback

abbrev = "GSTheseus"
iconName = "GSTheseus"
longName = "U.S.S Mjolnir"
shipFile = "GSTheseus"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed26c
	Foundation.ShipDef.GSTheseus = Foundation.FutureFed26cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.GSTheseus = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.GSTheseus.desc = "The Theseus class was a 26th century Federation starship class, a temporal escort and variant subclass of the 23rd century Perseus-class escort, in Starfleet service in the 2550s decade. This class was also known as Theseus II class, differentiating it from the 25th century Theseus-class miracle worker destroyer. The Theseus class was based on the 23rd century Perseus-class escort. The Perseus was active in the year 2270, where the Temporal Integrity Commission recruited temporal agents from. Structurally, the ship consisted of an almond-shaped, flat saucer section, with a pair of warp nacelles attached on short nacelle pylons with the hull's aft. The arrangement mirrored the ancestral Perseus escort.\n\nBy the 26th century, the Theseus class operated as escort. For the USS Theseus (NCV-88050), Starfleet carried an advanced science suite with tactical systems. As a result of the Temporal Cold War, the class was also refitted into temporal escort, incorporating timeship technologies such as Chroniphased Infinity Modulator Phasers and a timestream rift warhead. Ships of the class, including the Mjolnir, participated in the Battle of Procyon V alongside the USS Enterprise-J against the Temporal Liberation Front and their Sphere Builder allies in 2554."
Foundation.ShipDef.GSTheseus.fMaxWarp = 9.999999996 + 0.1
Foundation.ShipDef.GSTheseus.fCruiseWarp = 9.95 + 0.1
Foundation.ShipDef.GSTheseus.OverrideWarpFXColor = Foundation.ShipDef.GSTheseus.OverrideWarpFXColor
Foundation.ShipDef.GSTheseus.OverridePlasmaFXColor = Foundation.ShipDef.GSTheseus.OverridePlasmaFXColor

Foundation.ShipDef.GSTheseus.dTechs = {
	'Adv Armor Tech': 1,
	"AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	"Borg Attack Resistance": 50,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 55.0, "Power": -10000.0, "Efficiency": 0.99, "Resistance": 1.0,},
	'Drainer Immune': 1,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor", "Aft Ablative Armor", "Dorsal Ablative Armor", "Ventral Ablative Armor", "Port Nacelle Ablative Armor", "Star Nacelle Ablative Armor"]},
	#"GraviticLance": { "Time": 0.1, "TimeEffect": 5.0, "RadDepletionStrength": 1000, "Beams": ["Gravitic Lance"], "Immune": 0},
	"Inversion Beam": [12000, 0, 0.5, 1500],
	'Multivectral Shields': 10,
	'Phased Torpedo Immune': 1,
	"Power Drain Beam": [1500, 0, 0.5, 1500],
	"Reflector Shields": 2,
	'Reflux Weapon': 3800,
	'Regenerative Shields': 75,
	'Simulated Point Defence' : { "Distance": 75.0, "InnerDistance": 10.0, "Effectiveness": 0.9, "LimitTurn": 5.0, "LimitSpeed": 120, "LimitDamage": "-5000", "Period": 1.0, "MaxNumberTorps": 50, "Phaser": {"Priority": 1}},
	"SGReplicator Attack Resistance": 20,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	"TachyonBeam": {"Immune": -1},
	'Transphasic Torpedo Immune': 1,	
}

Foundation.ShipDef.GSTheseus.SubMenu = "26th Century"

if menuGroup:           Foundation.ShipDef.GSTheseus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GSTheseus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]