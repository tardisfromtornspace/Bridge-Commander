#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "IndependenceNoYacht"
iconName = "Independence"
longName = " Enterprise H (no yacht)"
shipFile = "IndependenceNoYacht"
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
species = App.SPECIES_GALAXY

Foundation.ShipDef.IndependenceNoYacht = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.IndependenceNoYacht.dTechs = {
	"AutoTargeting": { "Phaser": [3, 1] },
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Multivectral Shields': 20,
	'Regenerative Shields': 25,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}

}

Foundation.ShipDef.IndependenceNoYacht.desc = "The Independence class was a type of Federation vessel made by the very late 2490s, it was known for emulating the old Sovereign-class while carrying extremely advanced weaponry like an experimental diffusive lance beam prototype, pulse weaponry projectiles, as well as diffusive phasers. Overall, it is capable of annihiliating its predecessor, the Eclipse class."


if menuGroup:           Foundation.ShipDef.IndependenceNoYacht.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.IndependenceNoYacht.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
