#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "normandySR1"
iconName = "normandySR1"
longName = "SSV Normandy SR1"
shipFile = "normandySR1"
species = App.SPECIES_GALAXY
menuGroup = "Mass Effect Ships"
playerMenuGroup = "Mass Effect Ships"
SubMenu = "Systems Alliance"

worked = 0
try:
	import Custom.Autoload.RaceMESystemsAlliance
	Foundation.ShipDef.normandySR1 = Foundation.MESystemsAllianceShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	worked = 1
except:
	worked = 0
	print "Error while loading a race"
	Foundation.ShipDef.normandySR1 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	traceback.print_exc()

if worked == 1:
	Foundation.ShipDef.normandySR1.OverrideWarpFXColor = Foundation.ShipDef.normandySR1.OverrideWarpFXColor
	Foundation.ShipDef.normandySR1.OverridePlasmaFXColor = Foundation.ShipDef.normandySR1.OverridePlasmaFXColor

Foundation.ShipDef.normandySR1.fMaxWarp = 9.0 + 0.0001
Foundation.ShipDef.normandySR1.fCruiseWarp = 9 + 0.0001
Foundation.ShipDef.normandySR1.fCrew = 55

Foundation.ShipDef.normandySR1.dTechs = {
	"Alternate-Warp-FTL": {
		"Setup": {
			"Mass Effect FTL": {	"Nacelles": ["Port Mass Effect Engine", "Star Mass Effect Engine"], "Core": ["Element Zero Core"], "Enter FTL Density": 25, "Mid FTL Density": 10, "Exit FTL Density": 25, "Spark Size": 0.10,},
		},
	},
	"ME IES Stealth System": 1,
	"ME Shields": { "CollisionBlock": 0, "BypassMultiplier": 1, "FacetFactor": 0, "FacetRegeneration": 1, "MinimumSpeedTrigger": 5, "MaximumSpeedTrigger": 260, "ShieldScaleMultiplier": 0.2, "AtmosphericNerf": -1},
	'Simulated Point Defence' : { "Distance": 55.0, "InnerDistance": 4.0, "Effectiveness": 0.99, "LimitTurn": 0.3, "LimitSpeed": 55, "LimitDamage": "-400", "Period": 1.0, "MaxNumberTorps": 2, }, #"Phaser": {"Priority": 1} could be used, but no idea how many actual GARDIAN lasers the Normandy has and for this to work efficiently with Phaser option set, we would need quite a few lasers with more accuracy - plus "GARDIAN lasers typically operate in infrared frequencies [...] Salarians use near-UV and Geth use UV", so for an Alliance ship they would not be visible - better for us!"
	"Systems Changed With GC On": {"Message": {"Content": "This vessel has warp-drives disabled on GC. Please use its Mass Effect Drive instead.", "Time": 4.0}, "Hardpoints": {"Mass Effect Engines": 1.15,},},
}

Foundation.ShipDef.normandySR1.desc = "The SSV Normandy SR-1 (Systems Alliance Space Vehicle Stealth Reconnaissance 1) is a Systems Alliance starship. She is a prototype \"deep scout\" frigate, first of the eponymous Normandy class, co-developed by the Alliance and the Turian Hierarchy with the sponsorship of the Citadel Council. She is optimized for solo reconnaissance missions deep within unstable regions, using state-of-the-art stealth technology powered by an experimental drive core.\nCommissioned in 2183, the Normandy was initially captained by David Anderson, however, she was handed over to Commander Shepard when the commander became the first human Spectre, serving as Shepard\'s main source of transportation and base of operations.\n\nArmaments :\n- 8x Javelin Disruptor Torpedo tubes \n- 1x Spinal Mass Accelerator Cannon\n- 2x GARDIAN point-defense lasers\n\nDefenses :\n- Standard Mass-Effect Shielding\n\nPropulsion & Power :\n- Tantalus Drive Core\n- Fusion Plant\n- Antiproton Thrusters"

if menuGroup:           Foundation.ShipDef.normandySR1.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.normandySR1.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
