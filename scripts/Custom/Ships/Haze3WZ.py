import Foundation
import App

abbrev = 'Haze3WZ'
iconName = 'Haze3KWZ'
longName = 'FT Haze-3'
shipFile = 'Haze3WZ'
menuGroup = 'Orion Pirates Ships'
playerMenuGroup = 'Orion Pirates Ships'
SubMenu = "ZZ Orions"
species = App.SPECIES_GALAXY

credits = {'modName': 'Haze3WZ', 'author': '', 'version': '1.0', 'sources': ['http://'], 'comments': ''}

import K_ZZAndromedanAttackDef

Foundation.ShipDef.Haze3WZ = K_ZZAndromedanAttackDef.ZZAndromedanShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.Haze3WZ.desc = """Haze III Starfighter - Pirate Version\n\n1x Photon Launcher (1f)\n2x Pulse Disruptor Cannons (2f)"""

if menuGroup:
    Foundation.ShipDef.Haze3WZ.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.Haze3WZ.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]