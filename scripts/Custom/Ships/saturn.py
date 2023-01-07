#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "saturn"
iconName = "saturn"
longName = "U.S.S. Gateway"
shipFile = "saturn"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.saturn = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.saturn.dTechs = {
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Ablative Armour': 485000,
	'ChronitonTorpe Immune': 1,
	"Phased Torpedo Immune": 1,
	'Multivectral Shields': 30,
	'Regenerative Shields': 45
}
Foundation.ShipDef.saturn.CloakingSFX   = "FutureBattleCloak"
Foundation.ShipDef.saturn.DeCloakingSFX = "FutureBattleDecloak"


Foundation.ShipDef.saturn.desc = "The Saturn class was a type of Federation starship operated by Starfleet during the 32nd century. In 3189, the fleet at Federation Headquarters included a ship of this class. The collective energy of this fleet sustained a distortion field that concealed the headquarters' location. In 3190, ships of this class were present at the re-opening of Starfleet Academy and the unveiling of the Archer Spacedock."


if menuGroup:           Foundation.ShipDef.saturn.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.saturn.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
