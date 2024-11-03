#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TMEExcelsior"
iconName = "TMEExcelsior"
longName = "Most Evil Excelsior"
shipFile = "TMEExcelsior"
species = App.SPECIES_GALAXY
menuGroup = "The Face of Fear"
playerMenuGroup = "The Face of Fear"


try:
	import Custom.Autoload.RaceTMEExcelsior
	Foundation.ShipDef.TMEExcelsior = Foundation.TMEExcelsiorShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.TMEExcelsior = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.TMEExcelsior.desc = "Due to some unforeseen circumstances, a race that used Universal Improbability technology (magic) created a ship from a dead wreck they found in some Unholy reality. They Used this ship to terrorize their universe for the crimes it had committed"
Foundation.ShipDef.TMEExcelsior.CloakingSFX = "InvisibilitySpellActivate"
Foundation.ShipDef.TMEExcelsior.DeCloakingSFX = "InvisibilitySpellDeactivate"
Foundation.ShipDef.TMEExcelsior.fMaxWarp = 15.0
Foundation.ShipDef.TMEExcelsior.fCruiseWarp = 10
Foundation.ShipDef.TMEExcelsior.OverrideWarpFXColor = Foundation.ShipDef.TMEExcelsior.OverrideWarpFXColor
Foundation.ShipDef.TMEExcelsior.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Adv Armor Tech': 1,
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Reflux Weapon Immune': 1,
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	"Transphasic Torpedo Immune" : 1,
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
	"Power Drain Beam": [1.0, 0.0, 0.0, 0.0]
}

if menuGroup:           Foundation.ShipDef.TMEExcelsior.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TMEExcelsior.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
