# File: Z (Python 1.5)

import Foundation
import App
abbrev = 'ZZBNihidrone'
iconName = 'ZZBNihidrone'
longName = 'ZZ Borg Nihidrone'
shipFile = 'ZZBNihidrone'
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'
species = App.SPECIES_GALAXY
credits = {
    'modName': 'ZZBNihidrone',
    'author': '',
    'version': '1.0',
    'sources': [
        'http://'],
    'comments': '' }

import F_BorgAttackDef
Foundation.ShipDef.ZZBNihidrone = F_BorgAttackDef.BorgAttackDef(abbrev, species, {
    'name': longName,
    'iconName': iconName,
    'shipFile': shipFile })

Foundation.ShipDef.ZZBNihidrone.dTechs = {
	'Breen Drainer Immune': 1,
	'Borg Adaptation': 1,
	'Automated Destroyed System Repair': {"Time": 120.0},
	'Multivectral Shields': 5,
}

Foundation.ShipDef.ZZBNihidrone.fMaxWarp = 9.999

Foundation.ShipDef.ZZBNihidrone.desc = 'Borg Nihidrone'
if menuGroup:
    Foundation.ShipDef.ZZBNihidrone.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.ZZBNihidrone.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

