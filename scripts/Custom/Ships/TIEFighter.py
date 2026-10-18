from bcdebug import debug
import Foundation
import App

abbrev = 'TIEFighter'
iconName = 'Tiefighter'
longName = 'TIE Fighter'
shipFile = 'TIEFighter'
menuGroup = 'ZZ Ships'
playerMenuGroup = 'ZZ Ships'
SubMenu = "Star Wars"
species = App.SPECIES_GALAXY

import K_ZZAndromedanAttackDef

Foundation.ShipDef.TIEFighter = K_ZZAndromedanAttackDef.ZZAndromedanShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu})

Foundation.ShipDef.TIEFighter.desc = """Sienar Fleet Systems Twin Ion Engine (TIE) Starfighter"""


Foundation.ShipDef.TIEFighter.dTechs = {"AutoTargeting": {"Pulse": [2, 1]}, "SW Shields": {"Thingy": 1}}

Foundation.ShipDef.TIEFighter.fMaxWarp = 1
Foundation.ShipDef.TIEFighter.fCruiseWarp = 1

if menuGroup:
    Foundation.ShipDef.TIEFighter.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.TIEFighter.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]