##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
from Custom.Autoload.RaceDalek import *


abbrev = 'DalekNewParadigmGrey'
iconName = 'DalekNewParadigmGrey'
longName = 'Type IX Dalek Drone (Grey)' # Previous versions were not capable of space flight. Type IX is new Paradigm Dalek.
shipFile = 'DalekNewParadigmGrey'
species = App.SPECIES_AKIRA
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"
SubSubMenu = "New Paradigm"


Foundation.ShipDef.DalekNewParadigmGrey = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu, "race": Dalek })
Foundation.ShipDef.DalekNewParadigmGrey.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	"Vree Shields": 100
}

Foundation.ShipDef.DalekNewParadigmGrey.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekNewParadigmGrey.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekNewParadigmGrey.desc = "Dalek drones were the original footsoldiers of the Dalek Paradigm, before relying on the type VIII bronze dalek again. The Daleks are a warrior race made up of genetically engineered mutants belonging to fundamental DNA type 467-989. By most accounts they were originally from the planet Skaro. The mutants were encased inside an armoured travel machine built from polycarbide and the metal Dalekanium. Intensely xenophobic and bent on universal domination, the Daleks were hated and feared throughout time and space. Their goal was to eradicate all non-Dalek life, as programmed by their creator, Davros."


if menuGroup:           Foundation.ShipDef.DalekNewParadigmGrey.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekNewParadigmGrey.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
