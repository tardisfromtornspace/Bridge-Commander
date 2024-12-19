#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "AllianceNormandySR2"
iconName = "AllianceNormandySR2"
longName = "SSV Normandy SR-2"
shipFile = "AllianceNormandySR2"
species = App.SPECIES_GALAXY
menuGroup = "Mass Effect Ships"
playerMenuGroup = "Mass Effect Ships"
SubMenu = "Systems Alliance"

worked = 0
try:
	import Custom.Autoload.RaceMESystemsAlliance
	Foundation.ShipDef.AllianceNormandySR2 = Foundation.MESystemsAllianceShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	worked = 1
except:
	worked = 0
	print "Error while loading a race"
	Foundation.ShipDef.AllianceNormandySR2 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	traceback.print_exc()

if worked == 1:
	Foundation.ShipDef.AllianceNormandySR2.OverrideWarpFXColor = Foundation.ShipDef.AllianceNormandySR2.OverrideWarpFXColor
	Foundation.ShipDef.AllianceNormandySR2.OverridePlasmaFXColor = Foundation.ShipDef.AllianceNormandySR2.OverridePlasmaFXColor

Foundation.ShipDef.AllianceNormandySR2.fMaxWarp = 9.0 + 0.0001
Foundation.ShipDef.AllianceNormandySR2.fCruiseWarp = 8 + 0.0001
Foundation.ShipDef.AllianceNormandySR2.fCrew = 48

Foundation.ShipDef.AllianceNormandySR2.dTechs = {
	"Alternate-Warp-FTL": {
		"Setup": {
			"Mass Effect FTL": {	"Nacelles": ["Port Mass Effect Engine", "Star Mass Effect Engine"], "Core": ["Element Zero Core"], "Enter FTL Density": 25, "Mid FTL Density": 10, "Exit FTL Density": 25, "Spark Size": 0.10,},
		},
	},
	"AutoTargeting": { "Phaser": [2, 1] },
	'Fed Ablative Armor': { "Plates": ["Aft Silaris Armor", "Forward Silaris Armor", "Left Silaris Armor", "Right Silaris Armor", "Silaris Armor" ]},
	"ME IES Stealth System": 1,
	"ME Shields": { "CollisionBlock": 0, "BypassMultiplier": 1, "FacetFactor": 0, "FacetRegeneration": 1, "MinimumSpeedTrigger": 5, "MaximumSpeedTrigger": -270, "ShieldScaleMultiplier": 0.2, "AtmosphericNerf": -1, },
	"ME Thanix Magnetic-Hydrodynamic Cannon": {"HullDmgMultiplier": 0.05, "ShieldDmgMultiplier": 1.0, "DShieldDmgMultiplier": 1.0, "Beams": ["Thanix Cannons"]},
	'Simulated Point Defence' : { "Distance": 75.0, "InnerDistance": 2.0, "Effectiveness": 0.998, "LimitTurn": 0.17, "LimitSpeed": 55, "LimitDamage": "-400", "Period": 0.8, "MaxNumberTorps": 2, }, #"Phaser": {"Priority": 1} could be used, but no idea how many actual GARDIAN lasers the Normandy has and for this to work efficiently with Phaser option set, we would need quite a few lasers with more accuracy - plus "GARDIAN lasers typically operate in infrared frequencies [...] Salarians use near-UV and Geth use UV", so for an Alliance ship they would not be visible - better for us!"
	"Systems Changed With GC On": {"Message": {"Content": "This vessel has warp-drives disabled on GC. Please use its Mass Effect Drive instead.", "Time": 4.0}, "Hardpoints": {"Mass Effect Engines": 1.15,},},
}

Foundation.ShipDef.AllianceNormandySR2.desc = "After returning from Omega-4 Relay, Normandy SR-2 has been claimed by the Systems Alliance. Feeling that the ship, being based on the Systems Alliance-designed SSV Normandy SR-1, is their property, they have taken it apart, studied it and rebuilt it, adding new parts and opening new areas.\n\nArmaments :\n- 2x Javelin Disruptor Torpedoes tubes \n- 2x Pulse cannons\n- 2x GARDIAN point-defense lasers\n\nDefenses :\n- CBT Multicore Shielding\n- Silaris Heavy Ship Armor\n\nPropulsion & Power :\n- Tantalus Drive Core\n- Fusion Plant\n- Antiproton Thrusters"


if menuGroup:           Foundation.ShipDef.AllianceNormandySR2.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AllianceNormandySR2.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
