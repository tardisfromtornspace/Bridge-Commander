#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "PicEntG"
iconName = "PicEntG"
longName = "U.S.S Enterprise G (Connie III)"
shipFile = "PicEntG"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.PicEntG = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.PicEntG = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.PicEntG.desc = "The USS Enterprise (NCC-1701-G), formerly the USS Titan (NCC-80102-A), was a Federation Constitution III-class starship operated by Starfleet in the 24th and 25th centuries. Launched in 2396 under the command of Captain Liam Shaw, the USS Titan-A was originally the fourth Starfleet vessel to bear the name Titan and the second to bear the NCC-80102 registry. In 2401, the Titan-A was instrumental in stopping the Changeling/Borg threat to Starfleet and the Federation. In 2402, she was rechristened as the Enterprise-G under the command of Captain Seven of Nine, the eighth Federation starship to bear the name Enterprise, in honor of the command crew of the USS Enterprise-D and the crucial part the ship had played in assisting their efforts to counter the Borg."
Foundation.ShipDef.PicEntG.SubMenu = "2400s"
Foundation.ShipDef.PicEntG.SubSubMenu = "Neo-Constitution III class"
Foundation.ShipDef.PicEntG.OverrideWarpFXColor = Foundation.ShipDef.PicEntG.OverrideWarpFXColor
Foundation.ShipDef.PicEntG.OverridePlasmaFXColor = Foundation.ShipDef.PicEntG.OverridePlasmaFXColor
Foundation.ShipDef.PicEntG.dTechs = {
	"Borg Attack Resistance": 15,
	"AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]},
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	'Regenerative Shields': 60,
	'Multivectral Shields': 5,
	'ChronitonTorpe Immune': 1
}


if menuGroup:           Foundation.ShipDef.PicEntG.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.PicEntG.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
