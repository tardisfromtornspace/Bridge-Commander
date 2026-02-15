import App
import Foundation
import traceback

abbrev = "EntI"
iconName = "EntI"
longName = "U.S.S. Enterprise I"
shipFile = "EntI"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.EntI = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.EntI = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.EntI.desc = "In 2494, the tenth generation of the USS Enterprise (NCC-1701-I) Archimedes Class was launched. This ship, while being a ship meant for exploration, was heavily armed and retrofitted with experimental prototype Partical Modulator Arrays (later perfected and installed on the Enterprise-J as Infinity Modulator Phasers). This ship also functioned as a testbed for the new and experimental Inverse Quantums. The ship also had a few second generation Hyperquantums which were first tested and used on the Atlas class (launched mid 25th century). The USS Enterprise I was engaged and destroyed in heavy combat with the 'Sphere Builders' in the early days of the Battle of Procyon V. This ship had undergone several refits before facing its end. If it hadnt have been destroyed there, it most likely would have been decomissioned within a decade."
Foundation.ShipDef.EntI.SubMenu = "2400s"
Foundation.ShipDef.EntI.OverrideWarpFXColor = Foundation.ShipDef.EntI.OverrideWarpFXColor
Foundation.ShipDef.EntI.OverridePlasmaFXColor = Foundation.ShipDef.EntI.OverridePlasmaFXColor
Foundation.ShipDef.EntI.dTechs = {
	"AutoTargeting": { "Phaser": [3, 1] },
	"Borg Attack Resistance": 45,
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'ChronitonTorpe Immune': 1,
	'Phased Torpedo Immune': 1,
	'Multivectral Shields' : 18,
	'Regenerative Shields': 60,
	"Transphasic Torpedo Immune": 1,
	'Fed Ablative Armor': {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}
	
}


if menuGroup:           Foundation.ShipDef.EntI.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EntI.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]