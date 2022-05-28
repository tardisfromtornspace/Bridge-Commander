#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 24.11.2003                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'PlanetExpress'
iconName = 'PlanetExpress'
longName = 'PlanetExpress'
shipFile = 'PlanetExpress' 
menuGroup = 'Futurama Ships'
playerMenuGroup = 'Futurama Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'PlanetExpress',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.PlanetExpress = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.PlanetExpress.hasTGLName = 1
# Foundation.ShipDef.PlanetExpress.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.PlanetExpress.desc = 'The Planet Express ship, named Old Bessie by the Professor, is a bright green (actual name electric mucus) delivery spacecraft owned by Planet Express. It is used by Bender, Fry and Leela to take various packages all over the galaxy. It has windshield wipers, a coffee maker, cup holders, an elephant detector, a microwave, game room, cargo hold and a laundry room. The ship runs on dark matter, mostly supplied by Nibbler. After the dark matter incident in Bender´s Game where dark matter was rendered worthless, it used whale oil. The ship does not actually move itself, but, using the Dark Matter Accelerator, it moves the universe around it. It´s shielding has held up against a torrent of missiles, yet the ship falls victim to such things as rocks while parked.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.PlanetExpress.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.PlanetExpress.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
