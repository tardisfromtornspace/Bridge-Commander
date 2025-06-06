##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
from Custom.Autoload.RaceDalek import *


abbrev = 'DalekNewParadigmBlue'
iconName = 'DalekNewParadigmBlue'
longName = 'Type IX Dalek Strategist' # Previous versions were not capable of space flight. Type IX is new Paradigm Dalek.
shipFile = 'DalekNewParadigmBlue'
species = App.SPECIES_AKIRA

menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"
SubSubMenu = "New Paradigm"


Foundation.ShipDef.DalekNewParadigmBlue = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu, "race": Dalek })
Foundation.ShipDef.DalekNewParadigmBlue.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	"Vree Shields": 100
}

Foundation.ShipDef.DalekNewParadigmBlue.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekNewParadigmBlue.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekNewParadigmBlue.desc = "The Strategist Dalek was a blue, specialised Dalek of the New Dalek Paradigm. The Daleks are a warrior race made up of genetically engineered mutants belonging to fundamental DNA type 467-989. By most accounts they were originally from the planet Skaro. The mutants were encased inside an armoured travel machine built from polycarbide and the metal Dalekanium. Intensely xenophobic and bent on universal domination, the Daleks were hated and feared throughout time and space. Their goal was to eradicate all non-Dalek life, as programmed by their creator, Davros. The type IX was a newer model built from Dalek remnants that managed to escape the Time Lock around the Last Great Time War and were later used by the New Paradigm, but later fell in disuse, with its predecessor becoming more common."


if menuGroup:           Foundation.ShipDef.DalekNewParadigmBlue.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekNewParadigmBlue.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
