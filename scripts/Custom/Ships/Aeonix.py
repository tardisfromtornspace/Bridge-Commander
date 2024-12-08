import App
import Foundation
import traceback

abbrev = "Aeonix"
iconName = "Aeonix"
longName = "XGN Aeonix"
shipFile = "Aeonix"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"

try:
	import Custom.Autoload.RaceAeonix
	Foundation.ShipDef.Aeonix = Foundation.AeonixShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Aeonix = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.Aeonix.desc = ""
Foundation.ShipDef.Aeonix.fMaxWarp = 9.99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
Foundation.ShipDef.Aeonix.SubMenu = "Val'qtor Ships"
Foundation.ShipDef.Aeonix.OverrideWarpFXColor = Foundation.ShipDef.Aeonix.OverrideWarpFXColor
Foundation.ShipDef.Aeonix.OverridePlasmaFXColor = Foundation.ShipDef.Aeonix.OverridePlasmaFXColor
Foundation.ShipDef.Aeonix.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Adv Armor Tech': 1,
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'TimeVortex Torpedo Immune': 1,
	"Transphasic Torpedo Immune" : 1,
	"Digitizer Torpedo Immune": 1,
	'Davros Reality Bomb Immune' : 1,
	"Reflector Shields": 75,
	'Multivectral Shields' : 55,
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 35.0, "DoNotInterfere": 0},
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

Foundation.ShipDef.Aeonix.CloakingSFX   = "TachyonRefraction"
Foundation.ShipDef.Aeonix.DeCloakingSFX = "TachyonReintegrate"


if menuGroup:           Foundation.ShipDef.Aeonix.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Aeonix.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]