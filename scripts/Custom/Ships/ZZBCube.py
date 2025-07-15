# File: Z (Python 1.5)

import Foundation
import App
abbrev = 'ZZBCube'
iconName = 'ZZBCube'
longName = 'ZZ Borg War Cube'
shipFile = 'ZZBCube'
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'
species = App.SPECIES_GALAXY
credits = {
    'modName': 'ZZBCube',
    'author': '',
    'version': '1.0',
    'sources': [
        'http://'],
    'comments': '' }
import F_BorgAttackDef
Foundation.ShipDef.ZZBCube = F_BorgAttackDef.BorgAttackDef(abbrev, species, {
    'name': longName,
    'iconName': iconName,
    'shipFile': shipFile })

Foundation.ShipDef.ZZBCube.dTechs = {
	'Ablative Armour': 45000,
	'Breen Drainer Immune': 1,
	'Borg Adaptation': 1,
	'Automated Destroyed System Repair': {"Time": 120.0},
	'Multivectral Shields': 5,
}

Foundation.ShipDef.ZZBCube.fMaxWarp = 9.999

Foundation.ShipDef.ZZBCube.desc = "In the year 2378, following Captain Janeway's intervention from the future — where she infected the Borg with a neurolytic pathogen and Voyager destroyed one of the Unicomplex transwarp hubs, severely crippling the Borg's ability to rapidly deploy ships across the Milky Way — the few remaining Borg were forced to adapt.\nWith their resources now limited, they focused on producing smaller, more heavily armored and heavily armed vessels.\nThe first of these new designs was the C-Sphere: a hybrid of a cube and a sphere, approximately 900 meters in diameter. Unlike traditional Borg ships, the C-Sphere was not built to assimilate, but to annihilate any threat it encountered."

if menuGroup:
    Foundation.ShipDef.ZZBCube.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.ZZBCube.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

