import App
import Foundation
import traceback

abbrev = "Windrunner"
iconName = "Windrunner"
longName = "U.S.S. Windrunner"
shipFile = "Windrunner"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed27c
	Foundation.ShipDef.Windrunner = Foundation.FutureFed27cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Windrunner = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.Windrunner.desc = "The Windrunner Class is an escort vessel from the far future of starfleet in the prime timeline. It is a period in the 27th century where the dominion conjoined with the federation to combine their skills in several areas to in turn, give the beta quadrant and alpha quadrant any chance of surviving a devastating war agaisnt the Voth, these vessels were widespread mass produced and earned a legendary historic Miranda badge to the class' name, for its versatility and easy construction.\n\nThe federation used quantum zero point energy weapons at this time period, diffusive technology within torpedoes, and multispectrum chronitonic technology for alternate torpedoes and shielding. This would prevent the utility of transphasic, enyptic, and infinity modulation technology. This was however a stalemate compared to the Voth's thoroniphasic transwarp beam weapons."
Foundation.ShipDef.Windrunner.SubMenu = "27th Century"
Foundation.ShipDef.Windrunner.OverrideWarpFXColor = Foundation.ShipDef.Windrunner.OverrideWarpFXColor
Foundation.ShipDef.Windrunner.OverridePlasmaFXColor = Foundation.ShipDef.Windrunner.OverridePlasmaFXColor
Foundation.ShipDef.Windrunner.dTechs = {
	'Automated Destroyed System Repair': {"Time": 45.0, "DoNotInterfere": 1},
	'Breen Drainer Immune': 0,
	"Borg Attack Resistance": 60,
	'ChronitonTorpe Immune': 1,
	'Diffusive Armor': 45000,
	"Digitizer Torpedo Immune": 1,
	'Drainer Immune': 1,
	"Inversion Beam": [12000, 0, 0.5, 1500],
	'Multivectral Shields': 25,
	"Power Drain Beam": [1500, 0, 0.5, 1500],
	'Phased Torpedo Immune': 1,
	"Reflector Shields": 2,
	'Reflux Weapon': 3800,
	'Regenerative Shields': 75,
	"SGReplicator Attack Resistance": 30,
	"SG Asgard Beams Weapon Immune": 2,
	"SG Ion Weapon Immune": 2,
	"SG Ori Beams Weapon Immune": 2,
	"SG Plasma Weapon Immune": 2,
	"SG Railgun Weapon Immune": 2,
	"TachyonBeam": {"Immune": -1},
	'Transphasic Torpedo Immune': 1,
	'Vree Shields': 55,
}


if menuGroup:           Foundation.ShipDef.Windrunner.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Windrunner.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]