#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "rednorthstar"
iconName = "rednorthstar"
longName = "ZN-4490 Red North Star"
shipFile = "rednorthstar"
species = App.SPECIES_GALAXY
menuGroup = "Sic Mvndvs Circulum"
playerMenuGroup = "Sic Mvndvs Circulum"


try:
	import Custom.Autoload.RaceZynethlar
	Foundation.ShipDef.rednorthstar = Foundation.ZynethlarShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.rednorthstar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.rednorthstar.desc = "An form of inconcievable power from a different Time Circulum. This ship is the last living artifact of its race, which will never be given the chance to be discovered. It will remain that way for all of eternity. No origin of this ship is hinted throughout all known alephiverses, leading to a hypothesis that indicates it should not exist at all, yet there it lies untouched."
Foundation.ShipDef.rednorthstar.fCruiseWarp = 9.999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 + 100.0
Foundation.ShipDef.rednorthstar.fMaxWarp = 1000 + 100.0
Foundation.ShipDef.rednorthstar.SubMenu = "Unknown Ships"
Foundation.ShipDef.rednorthstar.OverrideWarpFXColor = Foundation.ShipDef.rednorthstar.OverrideWarpFXColor
Foundation.ShipDef.rednorthstar.OverridePlasmaFXColor = Foundation.ShipDef.rednorthstar.OverridePlasmaFXColor
Foundation.ShipDef.rednorthstar.CloakingSFX   = "UNImerge"
Foundation.ShipDef.rednorthstar.DeCloakingSFX = "UNIseparate"
Foundation.ShipDef.rednorthstar.bPlanetKiller = 1
Foundation.ShipDef.rednorthstar.dTechs = {
    'Total Immunity': 1,
    'Phase Cloak': 0, 
    'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'ChronitonTorpe Immune': 1,
	'Reflux Weapon Immune': 1,
	'Transphasic Torpedo Immune': 1,
	'Phased Torpedo Immune': 1,
    'Dicohesive Tech Shields': 1, 
	'TimeVortex Torpedo Immune': 1,
	'Davros Reality Bomb Immune' : 1,
	"Digitizer Torpedo Immune": 1,
	'Energy Diffusing Immune': 1,
    'Adv Armor Tech': 1,
    'Vaccum Decay Protection': 1,
    'Existential Untethering Immunity': 1,
    'Fed Ablative Armor': { "Plates": ['Tribansdusive Field']},
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 5.0, "DoNotInterfere": 0},
	'Defensive AOE Siphoon' : { "Resistance": 50.0},
	"SG Plasma Weapon Immune": 1,
	"SGReplicator Attack Resistance": 1,
	"SG Ori Beams Weapon Immune": 1,
	"SG Ion Weapon Immune": 1,
	"SG Asgard Beams Weapon Immune": 1,
	"GraviticLance": { "Immune": 1},
	"Tachyon Sensors":  1.0,
	"Inversion Beam": [1.0, 0.0, 0.0, 0.0],
	"Power Drain Beam": [1.0, 0.0, 0.0, 0.0]
      #"SOTI Size Change": {"Scale": 1.0, "Power": 1, "Types": [App.CT_SHIELD_SUBSYSTEM]}

}

if menuGroup:           Foundation.ShipDef.rednorthstar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.rednorthstar.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
