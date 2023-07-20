#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "kirk"
iconName = "kirk"
longName = "USS Armstrong"
shipFile = "kirk"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.kirk = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.kirk.desc = "The Kirk Constitution-class was a type of Federation starship operated by Starfleet during the 31st and the 32nd centuries. A Constitution layout vessel in the 32nd Century, ship class named after the legendary captain James T. Kirk. In 3190, various Constitution-class starships participated in the evacuation of United Earth when Earth was under siege from the Dark Matter Anomaly that was sent by Species 10-C."
Foundation.ShipDef.kirk.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Ablative Armour': 550000,
	'ChronitonTorpe Immune': 1,
	"Phased Torpedo Immune": 1,
	'Multivectral Shields': 30,
	'Regenerative Shields': 40
}
Foundation.ShipDef.kirk.CloakingSFX   = "FutureBattleCloak"
Foundation.ShipDef.kirk.DeCloakingSFX = "FutureBattleDecloak"


if menuGroup:           Foundation.ShipDef.kirk.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.kirk.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
