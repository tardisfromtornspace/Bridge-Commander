from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 12/29/2011                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'WCSonaBattleship'
iconName = 'WCSonaBattleship'
longName = 'Sona Battleship'
shipFile = 'WCSonaBattleship' 
menuGroup = 'Son´a Ships'
playerMenuGroup = 'Son´a Ships'
species = App.SPECIES_MARAUDER
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'WCSonaBattleship',
	'author': '',
	'version': '',
	'sources': [ '' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.WCSonaBattleship = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.WCSonaBattleship.fMaxWarp = 7.0
Foundation.ShipDef.WCSonaBattleship.sBridge = 'Type11Bridge'
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.WCSonaBattleship.hasTGLName = 1
Foundation.ShipDef.WCSonaBattleship.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.WCSonaBattleship.desc = 'Sona Battleship.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.WCSonaBattleship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCSonaBattleship.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
