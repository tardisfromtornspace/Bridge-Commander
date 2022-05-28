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
abbrev = 'TelTak'
iconName = 'TelTak'
longName = 'Tel`Tak'
shipFile = 'TelTak' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 793
SubMenu = ["Goa'uld Ships/Bases", "Cargo Ships"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'TelTak',
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
Foundation.ShipDef.TelTak = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                                                                              #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
# Foundation.ShipDef.TelTak.hasTGLName = 1
# Foundation.ShipDef.TelTak.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.TelTak.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.TelTak.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TelTak.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
