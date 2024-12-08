#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "WaythaeonAC"
iconName = "WaythaeonAC"
longName = "Waythaeon Converted Attack Cruiser"
shipFile = "WaythaeonAC"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceWaythaeon
	Foundation.ShipDef.WaythaeonAC = Foundation.WaythaeonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.WaythaeonAC = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.WaythaeonAC.desc = ""
Foundation.ShipDef.WaythaeonAC.SubMenu = "Waythaeon Ships"
Foundation.ShipDef.WaythaeonAC.fMaxWarp = 9.999999999999999999999999999999999999999999999999999999
Foundation.ShipDef.WaythaeonAC.fCruiseWarp = 9.95 + 0.0001
Foundation.ShipDef.WaythaeonAC.OverrideWarpFXColor = Foundation.ShipDef.WaythaeonAC.OverrideWarpFXColor
Foundation.ShipDef.WaythaeonAC.OverridePlasmaFXColor = Foundation.ShipDef.WaythaeonAC.OverridePlasmaFXColor
Foundation.ShipDef.WaythaeonAC.CloakingSFX   = "BiomaskCloak"
Foundation.ShipDef.WaythaeonAC.DeCloakingSFX = "BiomaskUncloak"

Foundation.ShipDef.WaythaeonAC.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
    'Fed Ablative Armor': { "Plates": ["Organic Armor"]},
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	"Transphasic Torpedo Immune" : 1,
	'Multivectral Shields' : 30,
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 10.0, "DoNotInterfere": 0},
	'Defensive AOE Siphoon' : { "Resistance": 5.0},
	"SG Plasma Weapon Immune": 1,
	"SGReplicator Attack Resistance": 1,
	"SG Ori Beams Weapon Immune": 1,
	"SG Ion Weapon Immune": 1,
	"SG Asgard Beams Weapon Immune": 1,
	"GraviticLance": { "Immune": 1},
	"Tachyon Sensors":  1.0,
	"Inversion Beam": [1.0, 0.0, 0.0, 0.0],
	"Power Drain Beam": [1.0, 0.0, 0.0, 0.0]
}


if menuGroup:           Foundation.ShipDef.WaythaeonAC.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WaythaeonAC.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
