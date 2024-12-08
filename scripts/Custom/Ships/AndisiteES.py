import Foundation
import App
import traceback

abbrev = 'AndisiteES'
iconName = 'AndisiteES'
longName = 'Andisite Exploration Ship'
shipFile = 'AndisiteES' 
menuGroup = 'Sic Mvndvs Circulum'
playerMenuGroup = 'Sic Mvndvs Circulum'
species = App.SPECIES_GALAXY


try:
	import Custom.Autoload.RaceAndisite
	Foundation.ShipDef.AndisiteES = Foundation.AndisiteShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.AndisiteES = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.AndisiteES.fMaxWarp = 9.999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
Foundation.ShipDef.AndisiteES.SubMenu = "Andisite Ships"
Foundation.ShipDef.AndisiteES.desc = ""
Foundation.ShipDef.AndisiteES.bPlanetKiller = 1
Foundation.ShipDef.AndisiteES.OverrideWarpFXColor = Foundation.ShipDef.AndisiteES.OverrideWarpFXColor
Foundation.ShipDef.AndisiteES.OverridePlasmaFXColor = Foundation.ShipDef.AndisiteES.OverridePlasmaFXColor
Foundation.ShipDef.AndisiteES.CloakingSFX   = "NeutralmatterCloak"
Foundation.ShipDef.AndisiteES.DeCloakingSFX = "NeutralmatterUncloak"
Foundation.ShipDef.AndisiteES.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Adv Armor Tech': 1,
	'ChronitonTorpe Immune': 1,
	'TimeVortex Torpedo Immune': 1,
	'Phased Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	"Transphasic Torpedo Immune" : 1,
	'Davros Reality Bomb Immune' : 1,
	'Multivectral Shields' : 30,
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 30.0, "DoNotInterfere": 0},
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

if menuGroup:           Foundation.ShipDef.AndisiteES.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AndisiteES.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

