##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
# thank you Mario
from Custom.Autoload.RaceDalek import *

abbrev = 'DalekSmallSaucer'
iconName = 'DalekSmallSaucer'
longName = 'Dalek Saucer Fighter'
shipFile = 'DalekSmallSaucer'
species = App.SPECIES_GALAXY
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"

# Once you have implemented the Autoload file, now you need to add the following, replacing "Dalek" by the species name
# , "race": Dalek
#

Foundation.ShipDef.DalekSmallSaucer = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": Dalek})
Foundation.ShipDef.DalekSmallSaucer.dTechs = {
	'Adv Armor Tech': 1,
	"AutoTargeting": { "Pulse": [2, 0] },
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Drainer Immune': 1,
	#"FiveSecsGodPhaser": 1,
	"Vree Shields": 100,
	"Phased Torpedo Immune": 1,
	'Reflux Weapon': 100,
	'Regenerative Shields': 60,
	"Inversion Beam": [0.5, 0, 0.5, 1500],
	"Power Drain Beam": [0.5, 0, 0.5, 1500]
}

Foundation.ShipDef.DalekSmallSaucer.bPlanetKiller = 1

Foundation.ShipDef.DalekSmallSaucer.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekSmallSaucer.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekSmallSaucer.desc = "By the time of the Etra Prime incident, Dalek ships were dimensionally transcendental and could use chameleon circuit technology; a new generation of Dalek saucer with increased firepower was built for the Last Great Time War. The New Dalek Empire used saucers with a modified appearance in their 2009 invasion of Earth. Though the Daleks themselves could fly and had personal weaponry, smaller versions of the saucers served as fighter craft."


if menuGroup:           Foundation.ShipDef.DalekSmallSaucer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekSmallSaucer.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
