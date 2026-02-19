##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
# thank you Mario
from Custom.Autoload.RaceDalek import *

abbrev = 'DalekCrucibleBomb'
iconName = 'DalekCrucible'
longName = 'Crucible Reality Bomb'
shipFile = 'DalekCrucibleBomb'
species = App.SPECIES_GALAXY
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"

# Once you have implemented the Autoload file, now you need to add the following, replacing "Dalek" by the species name
# , "race": Dalek
#

Foundation.ShipDef.DalekCrucibleBomb = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": Dalek})
Foundation.ShipDef.DalekCrucibleBomb.dTechs = {
	'Adv Armor Tech': 1,
	"AutoTargeting": { "Pulse": [2, 0] },
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Davros Reality Bomb' : { "Distance": 10000000.0, "Period": 30},
	'Drainer Immune': 1,
	"FiveSecsGodPhaser": 1,
	"GraviticLance": { "Time": 5.0, "TimeEffect": 60.0, "RadDepletionStrength": 50000, "Immune": 1},
	"Vree Shields": 100,
	"Phased Torpedo Immune": 1,
	'Reflux Weapon': 100,
	'Regenerative Shields': 25,
	"Inversion Beam": [0.5, 0, 0.5, 1500000000],
	"Power Drain Beam": [0.5, 0, 0.5, 1500000000]
}

Foundation.ShipDef.DalekCrucibleBomb.bPlanetKiller = 1

Foundation.ShipDef.DalekCrucibleBomb.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekCrucibleBomb.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekCrucibleBomb.desc = "The Crucible was the flagship superweapon of the Dalek Fleet of the New Dalek Empire at the heart of the Medusa Cascade. It was a mostly spherical space station the size of a planet, with numerous docking ports on the outside. It also had a unique core of Z-Neutrino energy which powered the reality bomb.\n\nThe reality bomb was a superweapon created by Davros for use by the Daleks. It had the potential to annihilate all non-Dalek matter in the omniverse. This bomb worked by cancelling out the electric field holding atoms together, and was capable of wiping out the entire universe and all of creation, except for those within or near the Crucible, fulfilling the Daleks' stated goal of wiping out all other life in the universe many times over. Once the weapon penetrated the time rift at the heart of the Medusa Cascade, it would spread into every parallel universe and alternate dimension (even the Void) as well.\n\nThe Tenth Doctor and his companions were successful in preventing the use of the weapon on a large scale. It was shut down using an internalised synchronous back-feed reversal loop, and then destroyed when the Crucible exploded."


if menuGroup:           Foundation.ShipDef.DalekCrucibleBomb.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekCrucibleBomb.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
