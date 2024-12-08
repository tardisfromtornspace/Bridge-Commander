#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TradoOrderBC"
iconName = "TradoOrderBC"
longName = "Tradophian Battlecruiser MK.II"
shipFile = "TradoOrderBC"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceTradophian
	Foundation.ShipDef.TradoOrderBC = Foundation.TradophianShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.TradoOrderBC = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.TradoOrderBC.desc = ""
Foundation.ShipDef.TradoOrderBC.SubMenu = "Tradophian Ships"
Foundation.ShipDef.TradoOrderBC.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.TradoOrderBC.fCruiseWarp = 9.95 + 0.0001
Foundation.ShipDef.TradoOrderBC.bPlanetKiller = 1
Foundation.ShipDef.TradoOrderBC.OverrideWarpFXColor = Foundation.ShipDef.TradoOrderBC.OverrideWarpFXColor
Foundation.ShipDef.TradoOrderBC.OverridePlasmaFXColor = Foundation.ShipDef.TradoOrderBC.OverridePlasmaFXColor
Foundation.ShipDef.TradoOrderBC.CloakingSFX   = "TemporalDeintegration"
Foundation.ShipDef.TradoOrderBC.DeCloakingSFX = "TemporalReintegration"
Foundation.ShipDef.TradoOrderBC.dTechs = {
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
	'Automated Destroyed System Repair': {"Time": 17.0, "DoNotInterfere": 0},
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

if menuGroup:           Foundation.ShipDef.TradoOrderBC.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TradoOrderBC.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
