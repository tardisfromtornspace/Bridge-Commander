#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 09.09.2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
import F_MineAI
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Nuke'
iconName = 'Nuke'
longName = 'Nuke'
shipFile = 'Nuke' 
menuGroup = 'Stargate Ships'
playerMenuGroup = ''
species = 766
SubMenu = "Other Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Nuke',
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
Foundation.ShipDef.Nuke = F_MineAI.MineDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
# Foundation.ShipDef.Nuke.hasTGLName = 1
# Foundation.ShipDef.Nuke.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.Nuke.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Nuke.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Nuke.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
