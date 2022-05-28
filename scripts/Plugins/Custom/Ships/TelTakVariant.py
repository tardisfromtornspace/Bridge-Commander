#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 01/06/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'TelTakVariant'
iconName = 'TelTakVariant'
longName = 'Tel`Tak (Variant)'
shipFile = 'TelTakVariant' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 797
SubMenu = ["Goa'uld Ships/Bases", "Cargo Ships"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'TelTakVariant',
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
Foundation.ShipDef.TelTakVariant = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
# Foundation.ShipDef.TelTakVariant.hasTGLName = 1
# Foundation.ShipDef.TelTakVariant.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.TelTakVariant.desc = 'No Description Available'
#                                                                                                                                              #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.TelTakVariant.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TelTakVariant.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
