#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback

abbrev = "Excelsior2"
iconName = "Excelsior2"
longName = "Excelsior II"
shipFile = "Excelsior2"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"


try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.Excelsior2 = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.Excelsior2 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

Foundation.ShipDef.Excelsior2.OverrideWarpFXColor = Foundation.ShipDef.Excelsior2.OverrideWarpFXColor
Foundation.ShipDef.Excelsior2.OverridePlasmaFXColor = Foundation.ShipDef.Excelsior2.OverridePlasmaFXColor

Foundation.ShipDef.Excelsior2.dTechs = {
   'Breen Drainer Immune': 1,
   'Multivectral Shields': 8,
   "Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}}

Foundation.ShipDef.Excelsior2.desc = "The Excelsior II class was a Federation starship class that was in service with Starfleet by the early 25th century. The Excelsior II-class was introduced sometime prior to 2401 as a successor to the successful Excelsior-class, having been in service for well over 100 years. In 2401, sixteen ships of this class were involved in the Frontier Day fleet maneuvers to celebrate the 250th anniversary of the first voyage of the Enterprise NX-01. The ships were subsequently commandeered after officers under the age of 25 were placed under the influence of the Borg with the help of then assimilated Jack Crusher. At least ship of the class, the USS Excelsior (NCC-42037) was lost during this engagement, while many others laid wrecked in orbit following the successful liberation of the fleet."


if menuGroup:           Foundation.ShipDef.Excelsior2.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Excelsior2.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
