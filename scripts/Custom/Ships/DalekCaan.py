##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
from Custom.Autoload.RaceDalek import *


abbrev = 'DalekCaan'
iconName = 'Dalek2005Gold'
longName = 'Dalek Caan' # Previous versions were not capable of space flight. Type IX is new Paradigm Dalek.
shipFile = 'DalekCaan'
species = App.SPECIES_AKIRA
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"


Foundation.ShipDef.DalekCaan = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": Dalek })
Foundation.ShipDef.DalekCaan.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	"Vree Shields": 100,
}

Foundation.ShipDef.DalekCaan.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekCaan.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekCaan.desc = "Dalek Caan was one of four Daleks in the Cult of Skaro. Like the other members of the Cult, he was tasked to think creatively, like the Daleks's enemies, to find new ways of defeating them. After two defeats by the Tenth Doctor, Caan was thought to be the only Dalek remaining in the universe. To create a new Dalek empire, he accomplished what was thought to be impossible: he breached the time-lock surrounding the Last Great Time War and extracted Davros, the creator of the Daleks, just before he could be destroyed by the Nightmare Child. This action cost Caan his mind but allowed him to see into the infinite complexity of time and manipulate the timelines. Caan was presumably killed, along with virtually the entire New Dalek Empire which he founded, when he betrayed his own kind."


if menuGroup:           Foundation.ShipDef.DalekCaan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekCaan.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
