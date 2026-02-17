#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "HestiaClass"
iconName = "HestiaClass"
longName = "U.S.S. Hestia NX-10400"
shipFile = "HestiaClass"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.HestiaClass = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.HestiaClass = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.HestiaClass.desc = "Comissioned into service for both the normal federation tactical task force, and section 31, the Hestia Class is one of the most formidable starships for its time. The first of its kind, USS Hestia NX-10400, was given the role of duty among only executively trained personel for special assignments or higher. Around the year 2429, there were an estimated number of 11 ships of this class throughout starfleet. Each having its own armament of either enhanced multi-spectrum arrays, intraharmonic arrays, or in some cases, expiramental transphasic arrays. Only 1 ship had the liberty of obtaining them due to the high intensity of maintainance required for the M-63 Crystaline matrix used for such weapons. The last of its kind, USS Tridentia NCC-106224-B was officially decomissioned in the year 2434, only 3 years after the new enterprise reached service.\n\nOverall Capabilities:\n- Able to split into smaller ships, overwhealming the enemy with superior firepower\n- Wide selection of phasers, easily being interchangable thanks to the ship's forward-thinking design\n- Adaptable torpedo launchers\n- Onboard Advanced Industrial Replicators\n- Hyper Velocity Octi-Input Quantum Slipstream Drive(only when integrated)\n- Indusive Triciclyc Infold Warp Drive\n- Regenerative Refractive Shielding\n- Deutronitanium Integrated Hull Armour\n- Multi-Injection Impulse Drive"

Foundation.ShipDef.HestiaClass.SubMenu = "2400s"
Foundation.ShipDef.HestiaClass.SubSubMenu = "Hestia Class"
Foundation.ShipDef.HestiaClass.OverrideWarpFXColor = Foundation.ShipDef.HestiaClass.OverrideWarpFXColor
Foundation.ShipDef.HestiaClass.OverridePlasmaFXColor = Foundation.ShipDef.HestiaClass.OverridePlasmaFXColor
Foundation.ShipDef.HestiaClass.dTechs = {
	"Borg Attack Resistance": 25,
	'Transphasic Torpedo Immune': 1,
	'Phased Torpedo Immune': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	'Multivectral Shields': 25,
	'Regenerative Shields': 60,
	"Fed Ablative Armor": {"Plates": ["Aft Saucer Armor","Port Saucer Armor","Starboard Ablative Armor","Engineering Ablative Armor","Top Ablative Armor","Forward Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.HestiaClass.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HestiaClass.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
