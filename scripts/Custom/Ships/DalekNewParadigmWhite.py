##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation



abbrev = 'DalekNewParadigmWhite'
iconName = 'DalekNewParadigmWhite'
longName = 'Type IX Supreme Dalek' # Previous versions were not capable of space flight. Type IX is new Paradigm Dalek.
shipFile = 'DalekNewParadigmWhite'
species = App.SPECIES_AKIRA
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"


Foundation.ShipDef.DalekNewParadigmWhite = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.DalekNewParadigmWhite.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	"Vree Shields": 100,
	'Reflux Weapon': 100,
	'Regenerative Shields': 25,
	"Inversion Beam": [0.5, 0, 0.5, 15],
	"Power Drain Beam": [0.5, 0, 0.5, 15]
}

Foundation.ShipDef.DalekNewParadigmWhite.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekNewParadigmWhite.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekNewParadigmWhite.desc = "The Daleks are a warrior race made up of genetically engineered mutants belonging to fundamental DNA type 467-989. By most accounts they were originally from the planet Skaro. The mutants were encased inside an armoured travel machine built from polycarbide and the metal Dalekanium. Intensely xenophobic and bent on universal domination, the Daleks were hated and feared throughout time and space. Their goal was to eradicate all non-Dalek life, as programmed by their creator, Davros. The Supreme Dalek was a white-coloured type IX Dalek specialised for leadership in the New Dalek Paradigm."


if menuGroup:           Foundation.ShipDef.DalekNewParadigmWhite.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekNewParadigmWhite.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
