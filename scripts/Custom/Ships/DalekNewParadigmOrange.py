##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
from Custom.Autoload.RaceDalek import *


abbrev = 'DalekNewParadigmOrange'
iconName = 'DalekNewParadigmOrange'
longName = 'Type IX Dalek Scientist' # Previous versions were not capable of space flight. Type IX is new Paradigm Dalek.
shipFile = 'DalekNewParadigmOrange'
species = App.SPECIES_AKIRA
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"
SubSubMenu = "New Paradigm"

Foundation.ShipDef.DalekNewParadigmOrange = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu, "race": Dalek })
Foundation.ShipDef.DalekNewParadigmOrange.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	"Vree Shields": 100
}

Foundation.ShipDef.DalekNewParadigmOrange.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekNewParadigmOrange.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekNewParadigmOrange.desc = "'Dalek Scientist' was a specialised caste in the hierarchy of the Dalek Empire. Within the New Dalek Paradigm, the Scientists had a specialised casing, distinguished by its orange colour. The Daleks are a warrior race made up of genetically engineered mutants belonging to fundamental DNA type 467-989. By most accounts they were originally from the planet Skaro. The mutants were encased inside an armoured travel machine built from polycarbide and the metal Dalekanium. Intensely xenophobic and bent on universal domination, the Daleks were hated and feared throughout time and space. Their goal was to eradicate all non-Dalek life, as programmed by their creator, Davros. The type IX was a newer model built from Dalek remnants that managed to escape the Time Lock around the Last Great Time War and were later used by the New Paradigm, but later fell in disuse, with its predecessor becoming more common."


if menuGroup:           Foundation.ShipDef.DalekNewParadigmOrange.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekNewParadigmOrange.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
