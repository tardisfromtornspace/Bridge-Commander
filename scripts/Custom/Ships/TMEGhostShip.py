#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "TMEGhostShip"
iconName = "TMEGhostShip"
longName = "Ghost Ship"
shipFile = "TMEGhostShip"
species = App.SPECIES_GALAXY
menuGroup = "The Face of Fear"
playerMenuGroup = "The Face of Fear"

try:
	import Custom.Autoload.RaceTMEGhostShip
	theDefIs = Foundation.TMEGhostShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	theDefIs = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.TMEGhostShip = theDefIs


Foundation.ShipDef.TMEGhostShip.desc = "In the Bizzaro universe, which was also the origin point for The Most Evil Galaxy X from Hell, the Ghost 1701 was created from the spiteful spirits that were reluctant to die when the Enterprise self destructed. This ship has one mission and one mission only... To hunt down and destroy the one who killed them... James T. kirk. It will stop at nothing to achieve its goals, and if you dare stand in its way, I doubt you will survive long"
Foundation.ShipDef.TMEGhostShip.CloakingSFX = "TMEGhostShipCloak"
Foundation.ShipDef.TMEGhostShip.DeCloakingSFX = "TMEGhostShipDecloak"
Foundation.ShipDef.TMEGhostShip.fMaxWarp = 15.0
Foundation.ShipDef.TMEGhostShip.fCruiseWarp = 10
Foundation.ShipDef.TMEGhostShip.OverrideWarpFXColor = Foundation.ShipDef.TMEGhostShip.OverrideWarpFXColor
Foundation.ShipDef.TMEGhostShip.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
    'Fed Ablative Armor': { "Plates": ["Spectral Armor"]},
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Reflux Weapon Immune': 1,
	'TimeVortex Torpedo Immune': 1,
	"Digitizer Torpedo Immune": 1,
	"Transphasic Torpedo Immune" : 1
}

if menuGroup:           Foundation.ShipDef.TMEGhostShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TMEGhostShip.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
