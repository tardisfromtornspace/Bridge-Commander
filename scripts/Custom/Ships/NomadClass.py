#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "NomadClass"
iconName = "NomadClass"
longName = "U.S.S. Nomad"
shipFile = "NomadClass"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.NomadClass = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.NomadClass = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.NomadClass.desc = "Ship is expected to be from the 2420s, no other information available."
Foundation.ShipDef.NomadClass.SubMenu = "2400s"
Foundation.ShipDef.NomadClass.OverrideWarpFXColor = Foundation.ShipDef.NomadClass.OverrideWarpFXColor
Foundation.ShipDef.NomadClass.OverridePlasmaFXColor = Foundation.ShipDef.NomadClass.OverridePlasmaFXColor
Foundation.ShipDef.NomadClass.dTechs = {
	"Borg Attack Resistance": 20,
	'Transphasic Torpedo Immune': 1,
	'Phased Torpedo Immune': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	'Regenerative Shields': 45,
	'Multivectral Shields': 20,
	"Fed Ablative Armor": {"Plates": ["Dorsal Saucer Armor","Ventral Saucer Armor","Quantum Core Ablative Armor","Ventral Ablative Armor","Port Ablative Armor","Star Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.NomadClass.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NomadClass.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
