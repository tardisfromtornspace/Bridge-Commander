# File: Z (Python 1.5)

import Foundation
import App
abbrev = 'ZZRepShip'
iconName = 'ZZRepIcon'
longName = 'ZZ Reptilian Warship'
shipFile = 'ZZRepShip'
menuGroup = 'Xindi Ships'
playerMenuGroup = 'Xindi Ships'
species = App.SPECIES_GALAXY
credits = {
    'modName': 'ZZRepShip',
    'author': 'Zambie Zan',
    'version': '1.0',
    'sources': [
        'http://'],
    'comments': 'May 2025' }

Foundation.ShipDef.ZZRepShip = Foundation.FerengiShipDef(abbrev, species, {
    'name': longName,
    'iconName': iconName,
    'shipFile': shipFile })

Foundation.ShipDef.ZZRepShip.dTechs = {
	'Polarized Hull Plating': { "Plates": ["Hull Polarizer and Shields"]
}}

Foundation.ShipDef.ZZRepShip.desc = 'Xindi Reptilian Warship\n\n4x Torpedo launchers (3f/1a)\n5x particle weapons (3f/1d/1v)\n\n'

if menuGroup:
    Foundation.ShipDef.ZZRepShip.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.ZZRepShip.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

