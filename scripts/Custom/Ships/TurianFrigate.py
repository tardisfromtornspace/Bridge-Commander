#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TurianFrigate"
iconName = "TurianFrigate"
longName = "Turian Frigate"
shipFile = "TurianFrigate"
species = App.SPECIES_GALAXY
menuGroup = "Mass Effect Ships"
playerMenuGroup = "Mass Effect Ships"
SubMenu = "Turian Hierarchy"

worked = 0
try:
	import Custom.Autoload.RaceMETurian
	Foundation.ShipDef.TurianFrigate = Foundation.RaceMETurianShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	worked = 1
except:
	worked = 0
	print "Error while loading a race"
	Foundation.ShipDef.TurianFrigate = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	traceback.print_exc()

if worked == 1:
	Foundation.ShipDef.TurianFrigate.OverrideWarpFXColor = Foundation.ShipDef.TurianFrigate.OverrideWarpFXColor
	Foundation.ShipDef.TurianFrigate.OverridePlasmaFXColor = Foundation.ShipDef.TurianFrigate.OverridePlasmaFXColor

Foundation.ShipDef.TurianFrigate.fMaxWarp = 9.0 + 0.0001
Foundation.ShipDef.TurianFrigate.fCruiseWarp = 7.5 + 0.0001
Foundation.ShipDef.TurianFrigate.fCrew = 80

Foundation.ShipDef.TurianFrigate.dTechs = {
	"Alternate-Warp-FTL": {
		"Setup": {
			"Mass Effect FTL": {	"Nacelles": ["Port Mass Effect Engine", "Star Mass Effect Engine",], "Core": ["Eezo Core"], "Enter FTL Density": 25, "Mid FTL Density": 10, "Exit FTL Density": 25, "Spark Size": 0.10,},
		},
	},
	"AutoTargeting": { "Pulse": [3, 0] },
	'Fed Ablative Armor': { "Plates": ["Aft Armor", "Forward Armor", "Left Armor", "Right Armor",]},
	"ME Shields": { "CollisionBlock": 1, "BypassMultiplier": 1, "FacetFactor": 0, "FacetRegeneration": 1, "MinimumSpeedTrigger": 5, "MaximumSpeedTrigger": 260, "ShieldScaleMultiplier": 0.2, "AtmosphericNerf": -1, },
	'Simulated Point Defence' : { "Distance": 70.0, "InnerDistance": 7.0, "Effectiveness": 0.8, "LimitTurn": 0.3, "LimitSpeed": 55, "LimitDamage": "-400", "Period": 0.2, "MaxNumberTorps": 1, },
	"Systems Changed With GC On": {"Message": {"Content": "This vessel has warp-drives disabled on GC. Please use its Mass Effect Drive instead.", "Time": 4.0}, "Hardpoints": {"Mass Effect Engines": 1.15,},},
}

Foundation.ShipDef.TurianFrigate.desc = "Turian Frigates form the backbone of the Turian Hierarchy Fleet, they are also one of the main force in Citadel Defense Fleet. Although small, Turian Frigates are heavily armed, equipped with multiple Mass Accelerator cannons and Javelin Disruptor Torpedo launchers. Those ships can easily outgun almost any cruiser."

if menuGroup:           Foundation.ShipDef.TurianFrigate.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TurianFrigate.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
