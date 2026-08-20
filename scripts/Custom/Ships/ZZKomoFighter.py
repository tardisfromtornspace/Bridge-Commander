import Foundation
import App
from bcdebug import debug

abbrev = 'ZZKomoFighter'
iconName = 'ZZKomoFighter'
longName = "ZZ K'Vok Fighter"
shipFile = 'ZZKomoFighter'
menuGroup = 'Klingon Ships'
playerMenuGroup = 'Klingon Ships'
species = App.SPECIES_GALAXY
SubMenu = 'BCH L-24 Komo Val refit'

credits = {'modName': 'ZZKomoFighter', 'author': 'Zambie Zan', 'version': '1.0', 'sources': ['http://'], 'comments': 'Jul/2026'}

import F_ZZAttackDef

Foundation.ShipDef.ZZKomoFighter = F_ZZAttackDef.ZZAttackDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.ZZKomoFighter.desc = """The most powerful Klingon fighter to date, fit to be a part of the Komo Val fleet\n\n4x Pulse Disruptors (4f)\n2x Mini Photon Launchers (1f/1a)\nBy ZambieZan."""

if menuGroup:
    Foundation.ShipDef.ZZKomoFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:
    Foundation.ShipDef.ZZKomoFighter.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]