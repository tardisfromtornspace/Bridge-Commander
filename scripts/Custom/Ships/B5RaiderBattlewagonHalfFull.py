#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 18/04/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #

abbrev = 'B5RaiderBattlewagonHalfFull'
iconName = 'B5RaiderBattlewagonHalfFull'
longName = 'mk. I Battlewagon'
shipFile = 'B5RaiderBattlewagonHalfFull' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_SHUTTLE
SubMenu = "Raiders"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'B5RaiderBattlewagonHalfFull',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': "This is meant to be the full version with 21 raiders. Unfortunately, due to problems with the modelling SW and for recommendations to allow good performance this ship is only meant to throw 8 raiders at a time, which are the only raiders which show."
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.B5RaiderBattlewagonHalfFull = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.B5RaiderBattlewagonHalfFull.hasTGLName = 1
# Foundation.ShipDef.B5RaiderBattlewagonHalfFull.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.B5RaiderBattlewagonHalfFull.desc = "This makeshift 'battle wagon' built by the Raiders was a very small vessel, using a series of rotating wheels to carry and support up to 21 Belt Alliance Z-109 Zephyr class multi-environment fighters."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.B5RaiderBattlewagonHalfFull.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5RaiderBattlewagonHalfFull.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
