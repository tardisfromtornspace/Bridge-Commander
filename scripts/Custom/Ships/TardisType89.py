##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
# thank you Mario
from Custom.Autoload.RaceTimeLord import *


abbrev = 'TardisType89'
iconName = 'GenericTardis'
longName = 'Type 89 TARDIS'
shipFile = 'TardisType89'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Gallifreyan"


Foundation.ShipDef.TardisType89 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": TimeLord })
Foundation.ShipDef.TardisType89.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'ChronitonTorpe Immune': 1,
	'Drainer Immune': 1,
	"Multivectral Shields": 15,
	"Phased Torpedo Immune": 1,
	'Reflux Weapon': 100,
	'Regenerative Shields': 100,
	'TimeVortex Torpedo Immune': 1,
	"Inversion Beam": [0.2, 0, 0.5, 4200],
	"Power Drain Beam": [0.5, 0, 0.5, 900]
}
Foundation.ShipDef.TardisType89.bPlanetKiller = 1

Foundation.ShipDef.TardisType89.fMaxWarp = 8.0 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.TardisType89.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.TardisType89.desc = "Type 89 TARDIS was the classification used for the many types of Homeworld timeships that became popular between the Type 88 and Type 90 generations. To resolve the unorganised expansion of type classifications, the High Council stepped in and reclassified all timeships from this period as 89-forms, regardless of their cross-bred elements, leaving the type 90 and its successors, which were the first generations bred specifically for war."


if menuGroup:           Foundation.ShipDef.TardisType89.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TardisType89.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
