from bcdebug import debug
import Foundation
import App

abbrev = 'ImpStarDest2'
iconName = 'ImpStarDest2'
longName = 'Imperator Star Destroyer MkII'
shipFile = 'ImpStarDest2'
menuGroup = 'ZZ Ships'
playerMenuGroup = 'ZZ Ships'
SubMenu = "Star Wars"
species = App.SPECIES_GALAXY

import K_ZZAndromedanAttackDef

Foundation.ShipDef.ImpStarDest2 = K_ZZAndromedanAttackDef.ZZAndromedanShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu})

Foundation.ShipDef.ImpStarDest2.desc = """-LONG RANGE SATELLITE INTERLINK ACTIVE-
-DATA TRANSMISSION INITIATED-
-OMEGA SECTOR Com.Sat.-045 RESPONDING-
-INITIATING DATA RETRIEVAL: SUBJECT "Imperator Class Star Destroyer"
-BEGIN INFORMATION SUMMARY:

Insufficient Data

-END DATA TRANSMISSION-"""


Foundation.ShipDef.ImpStarDest2.dTechs = {
	"AutoTargeting": {"Pulse": [10, 1]},
	'Partially Distributed Shields': {"Shield Transfer Ratio": 1.25 * 0.3, "Max Percentage Damage": 0.3, "Collapse Threshold": 0.38, "Always Heal Closest": 1.1, "Max Radians": 2.594395},
	"SW Shields": {"Thingy": 1}
}

Foundation.ShipDef.ImpStarDest2.fMaxWarp = 2.25
Foundation.ShipDef.ImpStarDest2.fCruiseWarp = 2.2

Foundation.ShipDef.ImpStarDest2.shutLauncherShields = -2


if menuGroup:
    Foundation.ShipDef.ImpStarDest2.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.ImpStarDest2.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]