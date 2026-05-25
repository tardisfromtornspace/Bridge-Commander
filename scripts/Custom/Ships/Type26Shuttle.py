import App
import Foundation
import traceback

abbrev = "Type26Shuttle"
iconName = "Type26Shuttle"
longName = "Type 26 Shuttle"
shipFile = "Type26Shuttle"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed28c
	Foundation.ShipDef.Type26Shuttle = Foundation.FutureFed28cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Type26Shuttle = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.Type26Shuttle.desc = "This shuttle was used by the Universe-II class."
Foundation.ShipDef.Type26Shuttle.SubMenu = "28th Century"
Foundation.ShipDef.Type26Shuttle.OverrideWarpFXColor = Foundation.ShipDef.Type26Shuttle.OverrideWarpFXColor
Foundation.ShipDef.Type26Shuttle.OverridePlasmaFXColor = Foundation.ShipDef.Type26Shuttle.OverridePlasmaFXColor
Foundation.ShipDef.Type26Shuttle.dTechs = {
	'Automated Destroyed System Repair': {"Time": 25.0, "DoNotInterfere": 1},
	"Borg Attack Resistance": 60,
	'Breen Drainer Immune': 1,
	'ChronitonTorpe Immune': 1,
	"Digitizer Torpedo Immune": 1,
	'Drainer Immune': 1,
	'Multivectral Shields': 10,
	'Phased Torpedo Immune': 1,
	'Reflux Weapon Immune': 1,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	"SGReplicator Attack Resistance": 30,
	"SG Ori Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Asgard Beams Weapon Immune": 2,
	'Transphasic Torpedo Immune': 1
}


if menuGroup:           Foundation.ShipDef.Type26Shuttle.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Type26Shuttle.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]