#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 20.07.2003                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Ferengishuttle'
iconName = 'Ferengishuttle'
longName = 'Ferengi shuttle'
shipFile = 'Ferengishuttle' 
menuGroup = 'Ferengi Ships'
playerMenuGroup = 'Ferengi Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Ferengishuttle',
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
Foundation.ShipDef.Ferengishuttle = Foundation.FerengiShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Ferengishuttle.hasTGLName = 1
# Foundation.ShipDef.Ferengishuttle.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Ferengishuttle.desc = 'The Ferengi shuttle, also sometimes referred to as a Ferengi pod, was a fast warp-capable shuttlecraft used as an auxiliary vehicle and utilized by prominent businessmen in the Ferengi Alliance during the 24th century. Introduced prior to 2366, these vessels were the standard shuttle-type found aboard D´Kora-class Marauders.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Ferengishuttle.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Ferengishuttle.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
