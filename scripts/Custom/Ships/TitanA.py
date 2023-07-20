#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "TitanA"
iconName = "TitanA"
longName = "USS Titan-A"
shipFile = "TitanA"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.TitanA = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.TitanA.dTechs = {
	"AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
	#'Ablative Armour': 30000.000000,
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Regenerative Shields': 60,
	'Multivectral Shields': 5,
	'ChronitonTorpe Immune': 1,
	'Fed Ablative Armor': { "Plates": ["Ablative Armour", "Hull"]
}}

Foundation.ShipDef.TitanA.desc = "USS Titan (NCC-80102-A), was a Federation Constitution III-class starship operated by Starfleet in the 24th and 25th centuries. The Titan-A incorporated components from the previous Luna-class USS Titan, such as the warp coils, nacelle shield mechanism, and computer systems."


if menuGroup:           Foundation.ShipDef.TitanA.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TitanA.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
