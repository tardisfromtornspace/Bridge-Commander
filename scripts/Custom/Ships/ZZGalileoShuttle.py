# File: Z (Python 1.5)

import Foundation
import App
abbrev = 'ZZGalileoShuttle'
iconName = 'ZZGalileoShuttle'
longName = 'ZZ Galileo Shuttle'
shipFile = 'ZZGalileoShuttle'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
SubMenu = "Shuttles"

credits = {
    'modName': 'ZZGalileoShuttle',
    'author': '',
    'version': '1.0',
    'sources': [
        'http://'],
    'comments': '' }

Foundation.ShipDef.ZZGalileoShuttle = Foundation.FedShipDef(abbrev, species, {
    'name': longName,
    'iconName': iconName,
    'shipFile': shipFile,
    "SubMenu": SubMenu
})
Foundation.ShipDef.ZZGalileoShuttle.desc = 'Starfleet Galileo 7 Shuttle\n\n1x phaser emitter (f)\n\n'

if menuGroup:
    Foundation.ShipDef.ZZGalileoShuttle.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.ZZGalileoShuttle.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

