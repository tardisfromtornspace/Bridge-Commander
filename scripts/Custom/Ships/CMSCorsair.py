import App
import Foundation
import traceback

abbrev = "CMSCorsair"
iconName = "CMSCorsair"
longName = "Corsair"
shipFile = "CMSCorsair"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceVortchian
	Foundation.ShipDef.CMSCorsair = Foundation.VortchianShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.CMSCorsair = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.CMSCorsair.desc = ""
Foundation.ShipDef.CMSCorsair.fMaxWarp = 9.999999999999999999999999999999999
Foundation.ShipDef.CMSCorsair.OverrideWarpFXColor = Foundation.ShipDef.CMSCorsair.OverrideWarpFXColor
Foundation.ShipDef.CMSCorsair.OverridePlasmaFXColor = Foundation.ShipDef.CMSCorsair.OverridePlasmaFXColor
Foundation.ShipDef.CMSCorsair.CloakingSFX   = "Spacial_Displacement_On"
Foundation.ShipDef.CMSCorsair.DeCloakingSFX = "Spacial_Displacement_Off"
Foundation.ShipDef.CMSCorsair.SubMenu = "Vortchian Ships"
Foundation.ShipDef.CMSCorsair.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Fed Ablative Armor': { "Plates": ["Rapid Regen Crystalline Armor"]},
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	"Transphasic Torpedo Immune" : 1,
	"Digitizer Torpedo Immune": 1,
	'Multivectral Shields' : 35,
	"SG Plasma Weapon Immune": 1,
	"SGReplicator Attack Resistance": 1,
	"SG Ori Beams Weapon Immune": 1,
	"SG Ion Weapon Immune": 1,
	"SG Asgard Beams Weapon Immune": 1,
	"GraviticLance": { "Immune": 1},
	"Inversion Beam": [1.0, 0.0, 0.0, 0.0],
	"Power Drain Beam": [1.0, 0.0, 0.0, 0.0]	
}


if menuGroup:           Foundation.ShipDef.CMSCorsair.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CMSCorsair.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]