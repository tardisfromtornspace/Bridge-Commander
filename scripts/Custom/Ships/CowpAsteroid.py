from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 03.01.2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CowpAsteroid'
iconName = 'Asteroid'
longName = 'Cowp Asteroid'
shipFile = 'CowpAsteroid' 
menuGroup = 'Card Ships'
playerMenuGroup = 'Card Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'CowpAsteroid',
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
Foundation.ShipDef.CowpAsteroid = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.CowpAsteroid.hasTGLName = 1
Foundation.ShipDef.CowpAsteroid.hasTGLDesc = 1
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.CowpAsteroid.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.CowpAsteroid.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CowpAsteroid.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
