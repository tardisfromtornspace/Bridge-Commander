#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "HarmonyAscendant"
iconName = "HarmonyAscendant"
longName = "Harmony Ascendant"
shipFile = "HarmonyAscendant"
species = App.SPECIES_GALAXY
menuGroup = "Starlight's Dithetaverse"
playerMenuGroup = "Starlight's Dithetaverse"


try:
	import Custom.Autoload.RaceHarmonyAscendant
	Foundation.ShipDef.HarmonyAscendant = Foundation.HarmonyAscendantShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.HarmonyAscendant = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.HarmonyAscendant.desc = "This is Harmony Ascendant. This is what became of Harmony's Spirit after the Void collectively cast it into the infinity cloud. When they did, they allowed it to finish its treansformation that it was heading towards. This then appeared to decimate the Void races and completed the barrier that keeps them in the Void. After that, it remained in the infinity cloud until the times it is required or when the time came that it was forced to leave the forisium to chase the Void races. The Harmony Ascendant is equipped with Infinity Resonance Beams, Prismic Pulses, Foriphasic Torpedoes, Hyperinversal Torpedoes, and the ultimate advancement in cloaking abilities and the most complex and advanced warp capabilities of the entire forisium. This ship is able to best the Exile with a fair amount of ease."
Foundation.ShipDef.HarmonyAscendant.CloakingSFX = "HarmonyAscendantCloakOn"
Foundation.ShipDef.HarmonyAscendant.DeCloakingSFX = "HarmonyAscendantCloakOff"
Foundation.ShipDef.HarmonyAscendant.SubMenu = "Avenger of Harmony"
Foundation.ShipDef.HarmonyAscendant.SubSubMenu = "Harmony Ascendant"
Foundation.ShipDef.HarmonyAscendant.OverrideWarpFXColor = Foundation.ShipDef.HarmonyAscendant.OverrideWarpFXColor
Foundation.ShipDef.HarmonyAscendant.OverridePlasmaFXColor = Foundation.ShipDef.HarmonyAscendant.OverridePlasmaFXColor
Foundation.ShipDef.HarmonyAscendant.bPlanetKiller = 1
Foundation.ShipDef.HarmonyAscendant.fMaxWarp = 15.0
Foundation.ShipDef.HarmonyAscendant.fCruiseWarp = 10

Foundation.ShipDef.HarmonyAscendant.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Adv Armor Tech': 1,
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Phase Cloak': 0,
	'Reflux Weapon Immune': 1,
	'Total Immunity': 1,
	'Regenerative Shields': 20,
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	'Davros Reality Bomb Immune' : 1,
	"Transphasic Torpedo Immune" : 1,
	'Energy Diffusing Immune': 1,
    "TachyonBeam": { "Immune": 1 },
	'Automated Destroyed System Repair': {"Time": 18.0, "DoNotInterfere": 0},
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

if menuGroup:           Foundation.ShipDef.HarmonyAscendant.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HarmonyAscendant.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
