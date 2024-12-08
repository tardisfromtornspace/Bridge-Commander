#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "TraedonConquestShip"
iconName = "TraedonConquestShip"
longName = "Traedon Scorpion:Conquest Ship"
shipFile = "TraedonConquestShip"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceTraedon
	Foundation.ShipDef.TraedonConquestShip = Foundation.TraedonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.TraedonConquestShip = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.TraedonConquestShip.desc = "An organic and specifically designed ship from a distant parallel universe to the prime universe. They use dimensional travel to conquer universes as they are extremely powerful. The Hull is made out of an unknown biometal with rapid regeneration as well as strong shielding, however, their offenses outweigh their defenses. The whole point of the ship is to destroy and take whats left, or who surrenders. They broke into the prime universe in the early 33rd century, but found themselves outmatched but the technology despite being such an old civilization."
Foundation.ShipDef.TraedonConquestShip.CloakingSFX = "TraedonDecayCloak"
Foundation.ShipDef.TraedonConquestShip.DeCloakingSFX = "TraedonDecayUncloak"
Foundation.ShipDef.TraedonConquestShip.SubMenu = "Traedon Ships"
Foundation.ShipDef.TraedonConquestShip.bPlanetKiller = 1
Foundation.ShipDef.TraedonConquestShip.OverrideWarpFXColor = Foundation.ShipDef.TraedonConquestShip.OverrideWarpFXColor
Foundation.ShipDef.TraedonConquestShip.OverridePlasmaFXColor = Foundation.ShipDef.TraedonConquestShip.OverridePlasmaFXColor
Foundation.ShipDef.TraedonConquestShip.fMaxWarp = 9.9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
Foundation.ShipDef.TraedonConquestShip.fCruiseWarp = 9.9999999999999999999999999999999999999999

Foundation.ShipDef.TraedonConquestShip.dTechs = {
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
	"Reflector Shields": 35,
	'Multivectral Shields' : 50,
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


if menuGroup:           Foundation.ShipDef.TraedonConquestShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TraedonConquestShip.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
