import App
import Foundation
import traceback

abbrev = "RelVger"
iconName = "RelVger"
longName = "Rel'dyax V'ger Voyage Ship"
shipFile = "RelVger"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceReldyax
	Foundation.ShipDef.RelVger = Foundation.ReldyaxShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.RelVger = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.RelVger.desc = ""
Foundation.ShipDef.RelVger.fMaxWarp = 9.9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
Foundation.ShipDef.RelVger.SubMenu = "Rel'dyax Ships"
Foundation.ShipDef.RelVger.OverrideWarpFXColor = Foundation.ShipDef.RelVger.OverrideWarpFXColor
Foundation.ShipDef.RelVger.OverridePlasmaFXColor = Foundation.ShipDef.RelVger.OverridePlasmaFXColor
Foundation.ShipDef.RelVger.CloakingSFX   = "RelPhase"
Foundation.ShipDef.RelVger.DeCloakingSFX = "RelUnphase"
Foundation.ShipDef.RelVger.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
    'Fed Ablative Armor': { "Plates": ["Plasmatic Armor"]},
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Phase Cloak': 1,
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	"Transphasic Torpedo Immune" : 1,
	'Multivectral Shields' : 30,
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 12.0, "DoNotInterfere": 0},
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


if menuGroup:           Foundation.ShipDef.RelVger.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.RelVger.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]