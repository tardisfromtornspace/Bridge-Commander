##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
# thank you Mario
from Custom.Autoload.RaceTimeLord import *


abbrev = 'BattleTardis'
iconName = 'BattleTardis'
longName = 'Type 560 TARDIS'
shipFile = 'BattleTardis'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Gallifreyan"


Foundation.ShipDef.BattleTardis = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": TimeLord })
Foundation.ShipDef.BattleTardis.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Drainer Immune': 1,
	"FiveSecsGodPhaser": 1,
	"Multivectral Shields": 20,
	"Phased Torpedo Immune": 1,
	'Reflux Weapon': 100,
	'Regenerative Shields': 80,
	'TimeVortex Torpedo Immune': 1,
	"Inversion Beam": [0.2, 0, 0.5, 4500],
	"Power Drain Beam": [0.5, 0, 0.5, 1000]
}
Foundation.ShipDef.BattleTardis.bPlanetKiller = 1

Foundation.ShipDef.BattleTardis.fMaxWarp = 9.0 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.BattleTardis.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.BattleTardis.desc = "Type 560 Battle TARDIS was a variant of Time Travel capsule developed by the Time Lords in use during the Last Great Time War. Contrary to the Doctor's obsolete Type 40 and other conventional TARDISes designed for time travel without the threat of attack and for scientific research and exploration missions, these TARDISes were equipped with heavy armaments to engage in battle at a second's notice while being flown into hostile locations. Their main weaponry were time torpedoes, which could be used to freeze time and thus suspend other vessels in the time vortex."


if menuGroup:           Foundation.ShipDef.BattleTardis.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BattleTardis.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
