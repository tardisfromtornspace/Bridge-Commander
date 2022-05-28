#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 11/09/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CylonBasestar'
iconName = 'CylonBasestar'
longName = 'Basestar'
shipFile = 'CylonBasestar' 
menuGroup = 'BSG Ships'
playerMenuGroup = 'BSG Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Cylon Ships", "Basestars"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'CylonBasestar',
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
Foundation.ShipDef.CylonBasestar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.CylonBasestar.hasTGLName = 1
# Foundation.ShipDef.CylonBasestar.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.CylonBasestar.desc = 'Basestars physically resemble two Y-shaped sections joined at an axis and pointing in opposite directions, although those sections can swivel to direct alignment for atmospheric flight. They are designed to make FTL jumps and are equipped to deploy large-scale strikes with nuclear and conventional ordnance. Basestars are biomechanical entities which could heal itself of battle damage, with fleshy hangars to house Raiders. The Basestar´s internal functions are controlled by a part-biological, part-machine central computer system known as the Hybrid. The biological part of the Hybrid is a female humanoid Cylon-like being. Basestars are capable of carrying other Cylon models as crew within them.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.CylonBasestar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CylonBasestar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
