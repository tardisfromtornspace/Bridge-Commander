#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "TraedonDragon"
iconName = "TraedonDragon"
longName = "Traedon Dragon:Heavy Raider"
shipFile = "TraedonDragon"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceTraedon
	Foundation.ShipDef.TraedonDragon = Foundation.TraedonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.TraedonDragon = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.TraedonDragon.desc = "A Traedon Heavy Raider newly equipt with a trans-dimensional Drive and a Decay core. Also organic, but more heavily shielded and more resiliant to damage. These ships functioned as warships and traveled with conquest ships, usually being the head of the pack, the main 5th ship. They were only grown for the best of the best traedon commanders."
Foundation.ShipDef.TraedonDragon.CloakingSFX = "TraedonDecayCloak"
Foundation.ShipDef.TraedonDragon.DeCloakingSFX = "TraedonDecayUncloak"
Foundation.ShipDef.TraedonDragon.SubMenu = "Traedon Ships"
Foundation.ShipDef.TraedonDragon.bPlanetKiller = 1
Foundation.ShipDef.TraedonDragon.OverrideWarpFXColor = Foundation.ShipDef.TraedonDragon.OverrideWarpFXColor
Foundation.ShipDef.TraedonDragon.OverridePlasmaFXColor = Foundation.ShipDef.TraedonDragon.OverridePlasmaFXColor
Foundation.ShipDef.TraedonDragon.fMaxWarp = 9.9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
Foundation.ShipDef.TraedonDragon.fCruiseWarp = 9.999999999999999999999999999999999999999999999999999999999999

Foundation.ShipDef.TraedonDragon.dTechs = {
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
	'Multivectral Shields' : 50,
	"Reflector Shields": 25,
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 5.0, "DoNotInterfere": 0},
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
    "SOTI Size Change": {"Scale": 1.0, "Power": 2, "Types": [App.CT_WEAPON_SYSTEM]}
}


if menuGroup:           Foundation.ShipDef.TraedonDragon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TraedonDragon.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
