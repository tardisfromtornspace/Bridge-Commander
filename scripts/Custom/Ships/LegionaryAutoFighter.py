#####  Created by:StarFleet R&D 2010.02.13
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "LegionaryAutoFighter"
iconName = "LegionaryAutoFighter"
longName = "Legionary Auto Fighter"
shipFile = "LegionaryAutoFighter"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed34c
	Foundation.ShipDef.LegionaryAutoFighter = Foundation.FutureFed34cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.LegionaryAutoFighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.LegionaryAutoFighter.desc = "The Autofighter of the Legionary. They are automated drone fighters that come equipped on ships to help with combat against opposing ships or factions. They do not rely on human control, and are ran through the central processing brain of the ship they are tethered to.\n\n\nSTATS:\n\nAUTO FIGHTER:\n\nTriquantallic Biocrystalline Hull: 21500\n\nTemporal Confucation Mesh Armor: 34500\n\nAlterspace Negation Shielding Stats:\nForward: 41500, 150 Regen\nAft: 41500, 150 regen\nPort: 41500, 150 regen\nStar: 41500, 150 regen\nDorsal: 41500, 150 regen\nVentral: 41500, 150 regen\n(+MV Shields 25)\n\nLight Phaser damage: 50000\n\nTorpedo loadout:\nRechargeable Dimensional Trifusion Slingers"
Foundation.ShipDef.LegionaryAutoFighter.fMaxWarp = 13.0
Foundation.ShipDef.LegionaryAutoFighter.fCruiseWarp = 12.0
Foundation.ShipDef.LegionaryAutoFighter.SubMenu = "34th Century"
Foundation.ShipDef.LegionaryAutoFighter.SubSubMenu = "Legionary Class"
Foundation.ShipDef.LegionaryAutoFighter.OverrideWarpFXColor = Foundation.ShipDef.LegionaryAutoFighter.OverrideWarpFXColor
Foundation.ShipDef.LegionaryAutoFighter.OverridePlasmaFXColor = Foundation.ShipDef.LegionaryAutoFighter.OverridePlasmaFXColor
Foundation.ShipDef.LegionaryAutoFighter.CloakingSFX   = "SubmaterialismCloak"
Foundation.ShipDef.LegionaryAutoFighter.DeCloakingSFX = "SubmaterialismDecloak"
Foundation.ShipDef.LegionaryAutoFighter.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
    'Fed Ablative Armor': { "Plates": ["Temporal Confucation Mesh Armor"]},
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Phase Cloak': 0,
	'Automated Destroyed System Repair': {"Time": 20.0, "DoNotInterfere": 1},
	'Reflux Weapon Immune': 1,
	'Multivectral Shields' : 25,
	"Digitizer Torpedo Immune": 1,
	'TimeVortex Torpedo Immune': 1,
	'Defensive AOE Siphoon' : { "Resistance": 5.0},
	"SG Plasma Weapon Immune": 1,
	"SGReplicator Attack Resistance": 50,
	"SG Ori Beams Weapon Immune": 1,
	"SG Ion Weapon Immune": 1,
	"SG Asgard Beams Weapon Immune": 1,
	"GraviticLance": { "Immune": 1},
	"Tachyon Sensors":  1.0,
	"Inversion Beam": [1.0, 0.0, 0.0, 0.0],
	"Power Drain Beam": [1.0, 0.0, 0.0, 0.0],
	"Transphasic Torpedo Immune" : 1
	
}


if menuGroup:           Foundation.ShipDef.LegionaryAutoFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.LegionaryAutoFighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
