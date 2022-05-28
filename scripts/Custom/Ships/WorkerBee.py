from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 25.01.2004                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'WorkerBee'
iconName = 'WorkerBee'
longName = 'WorkerBee'
shipFile = 'WorkerBee' 
menuGroup = 'Other Ships'
playerMenuGroup = 'Other Ships'
species = App.SPECIES_GALAXY

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'WorkerBee',
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
import F_ShipRepairDef
Foundation.ShipDef.WorkerBee = F_ShipRepairDef.ShipRepairDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#Foundation.ShipDef.WorkerBee = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.WorkerBee.hasTGLName = 1
Foundation.ShipDef.WorkerBee.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.WorkerBee.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.WorkerBee.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WorkerBee.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
