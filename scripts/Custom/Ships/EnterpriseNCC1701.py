from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 7/12/2002                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'EnterpriseNCC1701'
iconName = 'EnterpriseNCC1701'
longName = 'Constitution'
shipFile = 'EnterpriseNCC1701' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'EnterpriseNCC1701',
	'author': 'Rick Knox',
	'version': '1.0',
	'sources': [ 'http://www.startrekgaming.com/~rick/' ],
	'comments': 'Ship By Pneumonic81 * BC-Mod Compiled By NanoByte'
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.EnterpriseNCC1701 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.EnterpriseNCC1701.sBridge = 'EnterpriseAbridge'
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.EnterpriseNCC1701.hasTGLName = 1
Foundation.ShipDef.EnterpriseNCC1701.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.EnterpriseNCC1701.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.EnterpriseNCC1701.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseNCC1701.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
