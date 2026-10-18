from bcdebug import debug
import Foundation
import App

abbrev = 'TIEInterceptor'
iconName = 'TieInterceptor'
longName = 'TIE Interceptor'
shipFile = 'TIEInterceptor'
menuGroup = 'ZZ Ships'
playerMenuGroup = 'ZZ Ships'
SubMenu = "Star Wars"
species = App.SPECIES_GALAXY

import K_ZZAndromedanAttackDef

Foundation.ShipDef.TIEInterceptor = K_ZZAndromedanAttackDef.ZZAndromedanShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu})

Foundation.ShipDef.TIEInterceptor.desc = """Sienar Fleet Systems Twin Ion Engine (TIE) Interceptor"""


Foundation.ShipDef.TIEInterceptor.dTechs = {"AutoTargeting": {"Pulse": [2, 1]}, "SW Shields": {"Thingy": 1}}

Foundation.ShipDef.TIEInterceptor.fMaxWarp = 0.25
Foundation.ShipDef.TIEInterceptor.fCruiseWarp = 0.2

if menuGroup:
    Foundation.ShipDef.TIEInterceptor.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.TIEInterceptor.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]