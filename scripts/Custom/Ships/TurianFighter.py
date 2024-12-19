#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TurianFighter"
iconName = "TurianFighter"
longName = "Turian Fighter"
shipFile = "TurianFighter"
species = App.SPECIES_GALAXY
menuGroup = "Mass Effect Ships"
playerMenuGroup = "Mass Effect Ships"
SubMenu = "Turian Hierarchy"

worked = 0
try:
	import Custom.Autoload.RaceMETurian
	Foundation.ShipDef.TurianFighter = Foundation.RaceMETurianShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	worked = 1
except:
	worked = 0
	print "Error while loading a race"
	Foundation.ShipDef.TurianFighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
	traceback.print_exc()

if worked == 1:
	Foundation.ShipDef.TurianFighter.OverrideWarpFXColor = Foundation.ShipDef.TurianFighter.OverrideWarpFXColor
	Foundation.ShipDef.TurianFighter.OverridePlasmaFXColor = Foundation.ShipDef.TurianFighter.OverridePlasmaFXColor

Foundation.ShipDef.TurianFighter.fMaxWarp = 9.0 + 0.0001
Foundation.ShipDef.TurianFighter.fCruiseWarp = 8 + 0.0001
Foundation.ShipDef.TurianFighter.fCrew = 1

Foundation.ShipDef.TurianFighter.dTechs = {
	# This fighter does not have Mass Effect abilities to propel itself
	#"Alternate-Warp-FTL": {
	#	"Setup": {
	#		"Mass Effect FTL": {	"Nacelles": [], "Core": ["Eezo Core"], "Enter FTL Density": 25, "Mid FTL Density": 10, "Exit FTL Density": 25, "Spark Size": 0.10,},
	#	},
	#},
	"ME Shields": { "CollisionBlock": 0, "BypassMultiplier": 1, "FacetFactor": 0, "FacetRegeneration": 1, "MinimumSpeedTrigger": 5, "MaximumSpeedTrigger": 260, "ShieldScaleMultiplier": 0.2, "AtmosphericNerf": -1, },
	'Simulated Point Defence' : { "Distance": 75.0, "InnerDistance": 2.0, "Effectiveness": 0.198, "LimitTurn": 0.17, "LimitSpeed": 55, "LimitDamage": "-400", "Period": 0.8, "MaxNumberTorps": 1, },
	#"Systems Changed With GC On": {"Message": {"Content": "This vessel has warp-drives disabled on GC. Please use its Mass Effect Drive instead.", "Time": 4.0}, "Hardpoints": {"Mass Effect Engines": 1.15,},},
}

Foundation.ShipDef.TurianFighter.desc = "Turian Fighters are one-man craft exclusively used as support vessels for a warship when close-range attacks on enemy ships are needed. They are lightweight enough that they can be economically fitted with powerful element zero cores, making them capable of greater acceleration and sharper maneuvers than starships.\n\nKinetic barrier shields changed starship battles from short, vicious bloodbaths to extended, indecisive slugging matches. This changed with the development of the fighter-launched mass disruptor torpedo, a short-ranged weapon that can penetrate kinetic barriers, if sluggish and slow enough that an opponent's GARDIAN defenses can take them down. Thus, starship GARDIAN defenses must be overwhelmed through swarm tactics, where fighter groups may take heavy casualties pressing their torpedo attacks home. Once fighter-launched torpedoes have crippled an enemy's barriers, the mass accelerators on frigates and cruisers can make short work of them.\nOn the other side of the spectrum, interceptors are a type of fighter optimized to attack other fighters, with no ability to damage starships but focused on screening friendly units from incoming fighter attacks."



if menuGroup:           Foundation.ShipDef.TurianFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TurianFighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
