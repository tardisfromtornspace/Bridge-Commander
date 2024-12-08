import Foundation
import App
import traceback


abbrev = 'MagmarianBC'
iconName = 'MagmarianBC'
longName = 'Magmarian Battlecruiser'
shipFile = 'MagmarianBC' 
menuGroup = 'Sic Mvndvs Circulum'
playerMenuGroup = 'Sic Mvndvs Circulum'
species = App.SPECIES_GALAXY


try:
	import Custom.Autoload.RaceMagmarian
	Foundation.ShipDef.MagmarianBC = Foundation.MagmarianShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.MagmarianBC = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.MagmarianBC.fMaxWarp = 9.999999999999999999999999999999999999999999999999999999
Foundation.ShipDef.MagmarianBC.SubMenu = "Magmarian Ships"
Foundation.ShipDef.MagmarianBC.OverrideWarpFXColor = Foundation.ShipDef.MagmarianBC.OverrideWarpFXColor
Foundation.ShipDef.MagmarianBC.OverridePlasmaFXColor = Foundation.ShipDef.MagmarianBC.OverridePlasmaFXColor
Foundation.ShipDef.MagmarianBC.CloakingSFX   = "ThermalRefraction"
Foundation.ShipDef.MagmarianBC.DeCloakingSFX = "RefractionCooldown"
Foundation.ShipDef.MagmarianBC.desc = ""
Foundation.ShipDef.MagmarianBC.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
    'Fed Ablative Armor': { "Plates": ["Molten Armor"]},
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	"Transphasic Torpedo Immune" : 1,
	'Multivectral Shields' : 30,
    "TachyonBeam": { "Immune": 1 },
	'Defensive AOE Siphoon' : { "Resistance": 0.5},
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

if menuGroup:           Foundation.ShipDef.MagmarianBC.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MagmarianBC.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

