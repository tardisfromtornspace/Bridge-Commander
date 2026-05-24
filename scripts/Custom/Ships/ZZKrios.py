import Foundation
import App
from bcdebug import debug

abbrev = 'ZZKrios'
iconName = 'ZZKrios'
longName = 'ZZ IRW Krilos Bird-of-Prey'
shipFile = 'ZZKrios'
menuGroup = 'Romulan Ships'
playerMenuGroup = 'Romulan Ships'
species = App.SPECIES_GALAXY

credits = {'modName': 'ZZKrios', 'author': 'Zambie Zan', 'version': '1.0', 'sources': ['http://'], 'comments': 'May/2025'}

import F_ZZAttackDef

Foundation.ShipDef.ZZKrios = F_ZZAttackDef.ZZAttackDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.ZZKrios.desc = """Lost Era (2293-2369) IRW Krilos Bird-of-Prey\n\n4x disruptors (f)\n2x heavy disruptors (f)\n\n6x disruptor beams (3p/s 2a)\n\n1x plasma torpedo (f)"""

if menuGroup:
    Foundation.ShipDef.ZZKrios.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:
    Foundation.ShipDef.ZZKrios.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]