#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "WaythaeonBioship"
iconName = "WaythaeonBioship"
longName = "Waythaeon Bioship"
shipFile = "WaythaeonBioship"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceWaythaeon
	Foundation.ShipDef.WaythaeonBioship = Foundation.WaythaeonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.WaythaeonBioship = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.WaythaeonBioship.desc = ""
Foundation.ShipDef.WaythaeonBioship.SubMenu = "Waythaeon Ships"
Foundation.ShipDef.WaythaeonBioship.fMaxWarp = 9.9999999999999999999999999999999999999999999999999
Foundation.ShipDef.WaythaeonBioship.fCruiseWarp = 9.95 + 0.0001
Foundation.ShipDef.WaythaeonBioship.OverrideWarpFXColor = Foundation.ShipDef.WaythaeonBioship.OverrideWarpFXColor
Foundation.ShipDef.WaythaeonBioship.OverridePlasmaFXColor = Foundation.ShipDef.WaythaeonBioship.OverridePlasmaFXColor
Foundation.ShipDef.WaythaeonBioship.CloakingSFX   = "BiomaskCloak"
Foundation.ShipDef.WaythaeonBioship.DeCloakingSFX = "BiomaskUncloak"

Foundation.ShipDef.WaythaeonBioship.dTechs = {
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


if menuGroup:           Foundation.ShipDef.WaythaeonBioship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WaythaeonBioship.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
