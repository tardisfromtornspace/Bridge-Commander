#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "FutureZinTradoShip"
iconName = "FutureZinTradoShip"
longName = "Tradophian/Zinthonian Alliance Ship"
shipFile = "FutureZinTradoShip"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceTraZin
	Foundation.ShipDef.FutureZinTradoShip = Foundation.TraZinShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.FutureZinTradoShip = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.FutureZinTradoShip.desc = ""
Foundation.ShipDef.FutureZinTradoShip.SubMenu = "Tradophian/Zinthonian Alliance Ships"
Foundation.ShipDef.FutureZinTradoShip.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.FutureZinTradoShip.fCruiseWarp = 9.95 + 0.0001
Foundation.ShipDef.FutureZinTradoShip.bPlanetKiller = 1
Foundation.ShipDef.FutureZinTradoShip.OverrideWarpFXColor = Foundation.ShipDef.FutureZinTradoShip.OverrideWarpFXColor
Foundation.ShipDef.FutureZinTradoShip.OverridePlasmaFXColor = Foundation.ShipDef.FutureZinTradoShip.OverridePlasmaFXColor
Foundation.ShipDef.FutureZinTradoShip.CloakingSFX   = "ZinthonianExtraDimensionRefract"
Foundation.ShipDef.FutureZinTradoShip.DeCloakingSFX = "ZinthonianExtraDimensionUnrefract"
Foundation.ShipDef.FutureZinTradoShip.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Adv Armor Tech': 1,
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Phase Cloak': 0,
	'Reflux Weapon Immune': 1,
	'Total Immunity': 1,
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	"Transphasic Torpedo Immune" : 1,
	'Davros Reality Bomb Immune' : 1,
	"Vaccum Decay Protection": 1,
	'Energy Diffusing Immune': 1,
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 15.0, "DoNotInterfere": 0},
	'Defensive AOE Siphoon' : { "Resistance": 5.0},
	"SG Plasma Weapon Immune": 1,
	"SGReplicator Attack Resistance": 1,
	"SG Ori Beams Weapon Immune": 1,
	"SG Ion Weapon Immune": 1,
	"SG Asgard Beams Weapon Immune": 1,
	"GraviticLance": { "Immune": 1},
	"Tachyon Sensors":  1.0,
	"Inversion Beam": [1.0, 0.0, 0.0, 0.0],
	"Power Drain Beam": [1.0, 0.0, 0.0, 0.0],
    "SOTI Size Change": {"Scale": 1.0, "Power": 1, "Types": [App.CT_WEAPON_SYSTEM]}
	
}

if menuGroup:           Foundation.ShipDef.FutureZinTradoShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.FutureZinTradoShip.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
