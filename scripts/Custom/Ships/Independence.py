#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Independence"
iconName = "Independence"
longName = "USS Enterprise H"
shipFile = "Independence"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.Independence = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.Independence.dTechs = {
	"AutoTargeting": { "Phaser": [3, 1] },
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Multivectral Shields': 20,
	'Regenerative Shields': 25,
	"Transphasic Torpedo Immune": 1,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}

}

Foundation.ShipDef.Independence.desc = "The Independence class was a type of Federation vessel made by the very late 2490s, it was known for emulating the old Sovereign-class while carrying extremely advanced weaponry like an experimental diffusive lance beam prototype, pulse weaponry projectiles, as well as diffusive phasers. Overall, it is capable of annihiliating its predecessor, the Eclipse class."


if menuGroup:           Foundation.ShipDef.Independence.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Independence.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
