#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "Bellerophron"
iconName = "Bellerophron"
longName = "USS Bellerophron"
shipFile = "Bellerophron"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.Bellerophron = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Bellerophron = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()
	

Foundation.ShipDef.Bellerophron.desc = "The Bellerophron class is a relative of the now obsolete Intrepid class. It is equppied with a class 5 tunnel array quantum slipstream drive. It is also equipped with advanced phaser arrays and quantum torpedoes, as well as transphasic torpedoes. This  was first comissioned in 2411, as a purposed science vessel as well as an unoficial warship."
Foundation.ShipDef.Bellerophron.SubMenu = "2400s"
Foundation.ShipDef.Bellerophron.OverrideWarpFXColor = Foundation.ShipDef.Bellerophron.OverrideWarpFXColor
Foundation.ShipDef.Bellerophron.OverridePlasmaFXColor = Foundation.ShipDef.Bellerophron.OverridePlasmaFXColor
Foundation.ShipDef.Bellerophron.dTechs = {
	"Borg Attack Resistance": 25,
   'Transphasic Torpedo Immune': 1,
   'Breen Drainer Immune': 1,
   'Drainer Immune': 1,
   'Multivectral Shields': 12,
   "Fed Ablative Armor": {"Plates": ["Dorsal Saucer Armor","Ventral Saucer Armor","Quantum Core Ablative Armor","Ventral Ablative Armor","Port Ablative Armor","Star Ablative Armor"]}}


if menuGroup:           Foundation.ShipDef.Bellerophron.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Bellerophron.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
