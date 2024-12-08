import App
import Foundation
import traceback

abbrev = "Relcruiser"
iconName = "Relcruiser"
longName = "Rel'dyax Cruiser"
shipFile = "Relcruiser"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceReldyax
	Foundation.ShipDef.Relcruiser = Foundation.ReldyaxShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Relcruiser = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.Relcruiser.desc = ""
Foundation.ShipDef.Relcruiser.fMaxWarp = 9.9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
Foundation.ShipDef.Relcruiser.SubMenu = "Rel'dyax Ships"
Foundation.ShipDef.Relcruiser.OverrideWarpFXColor = Foundation.ShipDef.Relcruiser.OverrideWarpFXColor
Foundation.ShipDef.Relcruiser.OverridePlasmaFXColor = Foundation.ShipDef.Relcruiser.OverridePlasmaFXColor
Foundation.ShipDef.Relcruiser.CloakingSFX   = "RelPhase"
Foundation.ShipDef.Relcruiser.DeCloakingSFX = "RelUnphase"
Foundation.ShipDef.Relcruiser.dTechs = {
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


if menuGroup:           Foundation.ShipDef.Relcruiser.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Relcruiser.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]