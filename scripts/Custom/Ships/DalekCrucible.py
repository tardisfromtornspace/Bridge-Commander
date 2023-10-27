##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
# thank you Mario
from Custom.Autoload.RaceDalek import *

abbrev = 'DalekCrucible'
iconName = 'DalekCrucible'
longName = 'Dalek Crucible'
shipFile = 'DalekCrucible'
species = App.SPECIES_GALAXY
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"

# Once you have implemented the Autoload file, now you need to add the following, replacing "Dalek" by the species name
# , "race": Dalek
#

Foundation.ShipDef.DalekCrucible = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": Dalek})
Foundation.ShipDef.DalekCrucible.dTechs = {
	'Adv Armor Tech': 1,
	"AutoTargeting": { "Pulse": [2, 0] },
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	#'Davros Reality Bomb' : { "Distance": 10000000.0, "Period": 30},
	'Drainer Immune': 1,
	"FiveSecsGodPhaser": 1,
	"Vree Shields": 100,
	"Phased Torpedo Immune": 1,
	'Reflux Weapon': 100,
	'Regenerative Shields': 25,
	"Inversion Beam": [0.5, 0, 0.5, 1500000000],
	"Power Drain Beam": [0.5, 0, 0.5, 1500000000]
}

Foundation.ShipDef.DalekCrucible.bPlanetKiller = 1

Foundation.ShipDef.DalekCrucible.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekCrucible.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekCrucible.desc = "The Crucible was the flagship superweapon of the Dalek Fleet of the New Dalek Empire at the heart of the Medusa Cascade. It was a mostly spherical space station the size of a planet, with numerous docking ports on the outside. It also had a unique core of Z-Neutrino energy which powered the reality bomb."


if menuGroup:           Foundation.ShipDef.DalekCrucible.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekCrucible.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
