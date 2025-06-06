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
abbrev = 'WraithDart'
iconName = 'WraithDart'
longName = 'Dart'
shipFile = 'WraithDart' 
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
	'modName': 'WraithDart',
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
Foundation.ShipDef.WraithDart = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
# Wraith do not have shields used as actual shields. At most only used for forcefields to keep things in. This serves as an addendum to possibly add a tech later to prevent transporting.
Foundation.ShipDef.WraithDart.dTechs = {
	'SG Shields': { "RaceShieldTech": "Wraith" }
}

Foundation.ShipDef.WraithDart.fMaxWarp = 2.03
Foundation.ShipDef.WraithDart.fCruiseWarp = 1.2
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.WraithDart.hasTGLName = 1
Foundation.ShipDef.WraithDart.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.WraithDart.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.WraithDart.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WraithDart.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
