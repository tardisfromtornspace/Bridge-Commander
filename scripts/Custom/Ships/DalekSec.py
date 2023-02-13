##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
from Custom.Autoload.RaceDalek import *


abbrev = 'DalekSec'
iconName = 'Dalek2005Black'
longName = 'Dalek Sec' # Previous versions were not capable of space flight. Type IX is new Paradigm Dalek.
shipFile = 'DalekSec'
species = App.SPECIES_AKIRA
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"


Foundation.ShipDef.DalekSec = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": Dalek })
Foundation.ShipDef.DalekSec.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	"Vree Shields": 100
}

Foundation.ShipDef.DalekSec.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekSec.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekSec.desc = "Dalek Sec was a Dalek who had the ability to think beyond the capacity of any other Dalek as the leader of the Cult of Skaro. Following the Last Great Time War and Battle of Canary Wharf, Sec believed that the Dalek race needed to evolve by combining their DNA with that of other alien races in order to survive and planned a Final Experiment, which culminated in his assimilation of the human, Mr Diagoras. Dalek Sec's assimilation of a human allowed him to experience human emotions which, along with his vast wisdom, resulted in his transformation from a cold, ruthless strategist to a merciful pacifist. Due to this change in personality, his fellow Daleks unfortunately went from obeying him without question, to actively rebelling against him for going against their race's racial purity doctrines, leading to his extermination. Upon watching the Cult kill the Dalek that had dared to think beyond its conditioning, the Tenth Doctor declared Sec to have been 'the cleverest Dalek ever' and mourned his death."


if menuGroup:           Foundation.ShipDef.DalekSec.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekSec.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
