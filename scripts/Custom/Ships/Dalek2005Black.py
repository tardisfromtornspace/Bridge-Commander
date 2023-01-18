##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
from Custom.Autoload.RaceDalek import *


abbrev = 'Dalek2005Black'
iconName = 'Dalek2005Black'
longName = 'Type VIII Black Dalek' # Previous versions were not capable of space flight. Type IX is new Paradigm Dalek.
shipFile = 'Dalek2005Black'
species = App.SPECIES_AKIRA
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"
SubSubMenu = "Leaders"


Foundation.ShipDef.Dalek2005Black = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu, "race": Dalek })
Foundation.ShipDef.Dalek2005Black.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	"Vree Shields": 100
}

Foundation.ShipDef.Dalek2005Black.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.Dalek2005Black.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.Dalek2005Black.desc = "Black Daleks were senior ranking Daleks within the Dalek hierarchy and the most common rank to take up the role of Supreme Dalek or Supreme Controller. The type VIII casing was based on the bronze design from the Imperial Daleks, and developed for the Last Great Time War. The Daleks are a warrior race made up of genetically engineered mutants belonging to fundamental DNA type 467-989. By most accounts they were originally from the planet Skaro. The mutants were encased inside an armoured travel machine built from polycarbide and the metal Dalekanium. Intensely xenophobic and bent on universal domination, the Daleks were hated and feared throughout time and space. Their goal was to eradicate all non-Dalek life, as programmed by their creator, Davros."


if menuGroup:           Foundation.ShipDef.Dalek2005Black.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Dalek2005Black.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
