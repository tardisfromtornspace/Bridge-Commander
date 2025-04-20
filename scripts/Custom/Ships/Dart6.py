#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 12/03/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Dart6'
iconName = 'WraithDart'
longName = 'Dart'
shipFile = 'Dart6' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 761
SubMenu = "Wraith Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Dart6',
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
Foundation.ShipDef.Dart6 = Foundation.FedShipDef(abbrev, species, { 'iconName': iconName, 'shipFile': shipFile })
# Wraith do not have shields used as actual shields. At most only used for forcefields to keep things in. This serves as an addendum to possibly add a tech later to prevent transporting.
Foundation.ShipDef.Dart6.dTechs = {
	'SG Shields': { "RaceShieldTech": "Wraith" }
}

Foundation.ShipDef.Dart6.fMaxWarp = 2.03
Foundation.ShipDef.Dart6.fCruiseWarp = 1.2
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.Dart6.hasTGLName = 1
Foundation.ShipDef.Dart6.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.Dart6.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
#if menuGroup:           Foundation.ShipDef.Dart6.RegisterQBShipMenu(menuGroup)
#if playerMenuGroup:     Foundation.ShipDef.Dart6.RegisterQBPlayerShipMenu(playerMenuGroup)
#
#if Foundation.shipList._keyList.has_key(longName):
#     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
#     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
