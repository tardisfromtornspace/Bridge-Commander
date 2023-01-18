##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
# thank you Mario
from Custom.Autoload.RaceDalek import *

abbrev = 'DalekEmperorSaucer'
iconName = 'DalekEmperorSaucer'
longName = 'Dalek Flagship'
shipFile = 'DalekEmperorSaucer'
species = App.SPECIES_GALAXY
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"

# Once you have implemented the Autoload file, now you need to add the following, replacing "Dalek" by the species name
# , "race": Dalek
#

Foundation.ShipDef.DalekEmperorSaucer = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": Dalek})
Foundation.ShipDef.DalekEmperorSaucer.dTechs = {
	'Adv Armor Tech': 1,
	"AutoTargeting": { "Pulse": [2, 0] },
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Drainer Immune': 1,
	"FiveSecsGodPhaser": 1,
	"Vree Shields": 100,
	"Phased Torpedo Immune": 1,
	'Reflux Weapon': 100,
	'Regenerative Shields': 25,
	"Inversion Beam": [0.5, 0, 0.5, 1500],
	"Power Drain Beam": [0.5, 0, 0.5, 1500]
}

Foundation.ShipDef.DalekEmperorSaucer.bPlanetKiller = 1

Foundation.ShipDef.DalekEmperorSaucer.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekEmperorSaucer.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekEmperorSaucer.desc = "The Dalek flagship was the main warship of the Dalek Fleet. Like many of the other ships, it was a flying saucer, but was many times larger than the size of the standard Dalek flying saucer. On the last day of the Last Great Time War, the flagship fell through time and the Void and arrived around the 2000th century. The ship housed the Dalek Emperor, which was wired directly into the ship and slowly repaired it after it was heavily-damaged, and the Emperor's Personal Guards. The flagship held one hundred thousand Daleks."


if menuGroup:           Foundation.ShipDef.DalekEmperorSaucer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekEmperorSaucer.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
