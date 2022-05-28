#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 12/01/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
import F_DomRamAI
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'TobanMine'
iconName = 'TobanMine'
longName = 'Toban Mine'
shipFile = 'TobanMine' 
menuGroup = 'Stargate Ships'
playerMenuGroup = ''
species = 765
SubMenu = "Other Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'TobanMine',
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
Foundation.ShipDef.TobanMine = F_DomRamAI.DomRamAI(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
# Foundation.ShipDef.TobanMine.hasTGLName = 1
# Foundation.ShipDef.TobanMine.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.TobanMine.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.TobanMine.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TobanMine.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
