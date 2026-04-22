import Foundation
import App
from bcdebug import debug

abbrev = 'ZZPrimate'
iconName = 'ZZPrimate'
longName = 'ZZ Primate Cruiser'
shipFile = 'ZZPrimate'
menuGroup = 'Xindi Ships'
playerMenuGroup = 'Xindi Ships'
species = App.SPECIES_GALAXY

credits = {'modName': 'ZZPrimate', 'author': 'Zambie Zan', 'version': '1.0', 'sources': ['http://'], 'comments': 'May/2025'}

import F_ZZAttackDef

Foundation.ShipDef.ZZPrimate = F_ZZAttackDef.ZZAttackDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.ZZPrimate.dTechs = {
	"AutoTargeting": { "Phaser": [3, 1] },
	'Polarized Hull Plating': { "Plates": ["Hull Plating"], "mathFactor": 1.87}
}

Foundation.ShipDef.ZZPrimate.desc = """Xindi Primate Cruiser\n\n6x particle cannons (2f/1p/1s/2a)\n\n"""

if menuGroup:
    Foundation.ShipDef.ZZPrimate.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:
    Foundation.ShipDef.ZZPrimate.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]