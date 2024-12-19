#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "NormandySR2"
iconName = "NormandySR2"
longName = "Normandy SR-2"
shipFile = "NormandySR2"
species = App.SPECIES_GALAXY
menuGroup = "Mass Effect Ships"
playerMenuGroup = "Mass Effect Ships"
SubMenu = "Cerberus"

worked = 0
try:
	import Custom.Autoload.RaceMESystemsAlliance
	Foundation.ShipDef.NormandySR2 = Foundation.MESystemsAllianceShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	worked = 1
except:
	worked = 0
	print "Error while loading a race"
	Foundation.ShipDef.NormandySR2 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	traceback.print_exc()

if worked == 1:
	Foundation.ShipDef.NormandySR2.OverrideWarpFXColor = Foundation.ShipDef.NormandySR2.OverrideWarpFXColor
	Foundation.ShipDef.NormandySR2.OverridePlasmaFXColor = Foundation.ShipDef.NormandySR2.OverridePlasmaFXColor

Foundation.ShipDef.NormandySR2.fMaxWarp = 9.0 + 0.0001
Foundation.ShipDef.NormandySR2.fCruiseWarp = 8.6 + 0.0001
Foundation.ShipDef.NormandySR2.fCrew = 32

Foundation.ShipDef.NormandySR2.dTechs = {
	"Alternate-Warp-FTL": {
		"Setup": {
			"Mass Effect FTL": {	"Nacelles": ["Port Mass Effect Engine", "Star Mass Effect Engine"], "Core": ["Element Zero Core"], "Enter FTL Density": 25, "Mid FTL Density": 10, "Exit FTL Density": 25, "Spark Size": 0.10, },
		},
	},
	"AutoTargeting": { "Phaser": [2, 1] },
	'Fed Ablative Armor': { "Plates": ["Aft Silaris Armor", "Forward Silaris Armor", "Left Silaris Armor", "Right Silaris Armor", "Silaris Armor" ]},
	"ME IES Stealth System": 1,
	"ME Shields": { "CollisionBlock": 0, "BypassMultiplier": 1, "FacetFactor": 0, "FacetRegeneration": 1, "MinimumSpeedTrigger": 5, "MaximumSpeedTrigger": -270, "ShieldScaleMultiplier": 0.2, "AtmosphericNerf": -1, },
	"ME Thanix Magnetic-Hydrodynamic Cannon": {"HullDmgMultiplier": 0.05, "ShieldDmgMultiplier": 1.0, "DShieldDmgMultiplier": 1.0, "Beams": ["Thanix Cannons"]},
	'Simulated Point Defence' : { "Distance": 75.0, "InnerDistance": 2.0, "Effectiveness": 0.998, "LimitTurn": 0.3, "LimitSpeed": 55, "LimitDamage": "-400", "Period": 0.8, "MaxNumberTorps": 2, }, #"Phaser": {"Priority": 1} could be used, but no idea how many actual GARDIAN lasers the Normandy has and for this to work efficiently with Phaser option set, we would need quite a few lasers with more accuracy - plus "GARDIAN lasers typically operate in infrared frequencies [...] Salarians use near-UV and Geth use UV", so for an Alliance ship they would not be visible - better for us!"
	"Systems Changed With GC On": {"Message": {"Content": "This vessel has warp-drives disabled on GC. Please use its Mass Effect Drive instead.", "Time": 4.0}, "Hardpoints": {"Mass Effect Engines": 1.15,},},
}

Foundation.ShipDef.NormandySR2.desc = "The Normandy SR-2 is a starship that appears in Mass Effect 2, serving as the \"successor\" to the SR-1. The Illusive Man had Cerberus build the SR-2 for the newly revived Commander Shepard\'s team to aid them in their mission to stop the Collectors\' galaxy-wide campaign of human abductions. This ship is the headquarters of the Lazarus Cell. \n\nArmaments :\n- 2x Javelin Disruptor Torpedo tubes \n- 2x Pulse cannons\n- 2x GARDIAN point-defense lasers\n- 1x Twin Frigate-sized Thanix Magnetic-Hydrodynamic Cannon\n\nDefenses :\n- CBT Multicore Shielding\n- Silaris Heavy Ship Armor\n\nPropulsion & Power :\n- Tantalus Drive Core\n- Fusion Plant\n- Antiproton Thrusters"


if menuGroup:           Foundation.ShipDef.NormandySR2.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NormandySR2.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
