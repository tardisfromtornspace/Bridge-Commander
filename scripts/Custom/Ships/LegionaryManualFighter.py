#####  Created by:StarFleet R&D 2010.02.13
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "LegionaryManualFighter"
iconName = "LegionaryManualFighter"
longName = "Legionary Manual Fighter"
shipFile = "LegionaryManualFighter"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed34c
	Foundation.ShipDef.LegionaryManualFighter = Foundation.FutureFed34cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.LegionaryManualFighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.LegionaryManualFighter.desc = "The Manual fighter of the Legionary for when the crew is certain that the enemy they are facing will not pose harm to the saftey of the crew inside of it. While it is more powerful than the Autofighter, the manual fighter is hardly used for combat purposes unless absolutely necessary and is rather used for exploration and scanning of new anomalies in the universe\n\n\nSTATS:\n\nMANUAL FIGHTER:\n\nTriquantallic Biocrystalline Hull: 26500\n\nTemporal Confucation Mesh Armor: 42500\n\nTemporal Confucation Mesh Armor: 42500\n\nAlterspace Negation Shielding Stats:\nForward: 53500, 200 Regen\nAft: 53500, 200 regen\nPort: 53500, 200 regen\nStar: 53500, 200 regen\nDorsal: 53500, 200 regen\nVentral: 53500, 200 regen\n(+MV Shields 25)\n\nLight Phaser damage: 52500\n\nTorpedo loadout:\nRechargeable Dimensional Trifusion Slingers"
Foundation.ShipDef.LegionaryManualFighter.fMaxWarp = 13.0
Foundation.ShipDef.LegionaryManualFighter.fCruiseWarp = 12.0
Foundation.ShipDef.LegionaryManualFighter.SubMenu = "34th Century"
Foundation.ShipDef.LegionaryManualFighter.SubSubMenu = "Legionary Class"
Foundation.ShipDef.LegionaryManualFighter.OverrideWarpFXColor = Foundation.ShipDef.LegionaryManualFighter.OverrideWarpFXColor
Foundation.ShipDef.LegionaryManualFighter.OverridePlasmaFXColor = Foundation.ShipDef.LegionaryManualFighter.OverridePlasmaFXColor
Foundation.ShipDef.LegionaryManualFighter.CloakingSFX   = "SubmaterialismCloak"
Foundation.ShipDef.LegionaryManualFighter.DeCloakingSFX = "SubmaterialismDecloak"
Foundation.ShipDef.LegionaryManualFighter.dTechs = {
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


if menuGroup:           Foundation.ShipDef.LegionaryManualFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.LegionaryManualFighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
