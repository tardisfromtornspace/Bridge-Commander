##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
from Custom.Autoload.RaceDalek import *


abbrev = 'Dalek2005Gold9'
iconName = 'Dalek2005Gold'
longName = 'Type VIII Bronze Dalek6' # Previous versions were not capable of space flight. Type IX is new Paradigm Dalek.
shipFile = 'Dalek2005Gold9'
species = App.SPECIES_AKIRA
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"


Foundation.ShipDef.Dalek2005Gold9 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": Dalek })
Foundation.ShipDef.Dalek2005Gold9.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	"Vree Shields": 100,
}

Foundation.ShipDef.Dalek2005Gold9.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.Dalek2005Gold9.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.Dalek2005Gold9.desc = "The type VIII were based on the bronze daleks from the Imperial Dalek Time, and designed for the Last Great Time War. Bronze Daleks were the Dalek drones which served during several of the Daleks' biggest conflicts, usually as foot soldiers. The Daleks are a warrior race made up of genetically engineered mutants belonging to fundamental DNA type 467-989. By most accounts they were originally from the planet Skaro. The mutants were encased inside an armoured travel machine built from polycarbide and the metal Dalekanium. Intensely xenophobic and bent on universal domination, the Daleks were hated and feared throughout time and space. Their goal was to eradicate all non-Dalek life, as programmed by their creator, Davros."


#if menuGroup:           Foundation.ShipDef.Dalek2005Gold9.RegisterQBShipMenu(menuGroup)
#if playerMenuGroup:     Foundation.ShipDef.Dalek2005Gold9.RegisterQBPlayerShipMenu(playerMenuGroup)



#if Foundation.shipList._keyList.has_key(longName):
#      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
#      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
