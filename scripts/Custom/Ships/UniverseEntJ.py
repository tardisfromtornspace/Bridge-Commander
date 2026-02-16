#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "UniverseEntJ"
iconName = "UniverseEntJ"
longName = "U.S.S. Enterprise NCC-1701-J"
shipFile = "UniverseEntJ"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed26c
	Foundation.ShipDef.UniverseEntJ = Foundation.FutureFed26cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.UniverseEntJ = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.UniverseEntJ.desc = "The USS Enterprise NCC-1701-J was a Federation Universe class starship in the mid 26th century.\n\nThe Enterprise-J participated in the pivotal Battle of Procyon V, in which the forces of the Federation (at that point in history included the Klingons and Ithenites) defeated the invasion of the Sphere Builders; transdimensional beings who worked to colonize the galaxy by reconfiguring space. The temporal agent Daniels brought Jonathan Archer from the 22nd century aboard the Enterprise-J to witness the battle; so that he might convince Archer of the need to make peace between the Xindi and the Humans of the 22nd century. The crew of Enterprise-J included several Xindi, one of which owned a medal that Archer used to help convince Degra that he wanted peace.\n\nWeapons : \n- Infinity Modulator Arrays \n- Radiant Quantum Torpedoes \n- Chroniton Torpedoes\n- Chroniton Pulse Cannons"

Foundation.ShipDef.UniverseEntJ.OverrideWarpFXColor = Foundation.ShipDef.UniverseEntJ.OverrideWarpFXColor
Foundation.ShipDef.UniverseEntJ.OverridePlasmaFXColor = Foundation.ShipDef.UniverseEntJ.OverridePlasmaFXColor

#Foundation.ShipDef.UniverseEntJ.CloakingSFX = ""
#Foundation.ShipDef.UniverseEntJ.DeCloakingSFX = ""
Foundation.ShipDef.UniverseEntJ.fMaxWarp = 9.999999996 + 0.1
Foundation.ShipDef.UniverseEntJ.fCruiseWarp = 9.95 + 0.1

Foundation.ShipDef.UniverseEntJ.SubMenu = "26th Century"

Foundation.ShipDef.UniverseEntJ.dTechs = {
	'Adv Armor Tech': 1,
	"AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	"Borg Attack Resistance": 50,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Defensive AOE Siphoon' : { "Distance": 55.0, "Power": -10000.0, "Efficiency": 0.99, "Resistance": 1.0,},
	'Drainer Immune': 1,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]},
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

if menuGroup:           Foundation.ShipDef.UniverseEntJ.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.UniverseEntJ.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
