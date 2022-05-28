#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 10/09/2004                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'HadesBasestar2003'
iconName = 'HadesBasestar'
longName = 'Hades Basestar 2003'
shipFile = 'HadesBasestar2003' 
menuGroup = 'BSG Ships'
playerMenuGroup = 'BSG Ships'
SubMenu = ["Cylon Ships", "Basestars"]
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'HadesBasestar2003',
	'author': 'MadJohn',
	'version': '2.0.5',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.HadesBasestar2003 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.HadesBasestar2003.hasTGLName = 1
# Foundation.ShipDef.HadesBasestar2003.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.HadesBasestar2003.desc = "Backbone of the Cylon Rebellion during the First Cylon War and originally designed by Colonial scientists as a combat vessel is the infamous 'Basestar'. A fully armed Basestar is the most deadly ship in the known space. This massive, double saucer vessels measured some 1768 meters in diameter and carried a Legion of Cylon troops and 300 Raider type fighter craft. They are armed with over one-hundred defensive  RailGun turrets and nukes. So formidable is a lone Basestar, it is considered to be more powerful than a Battlestar."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.HadesBasestar2003.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HadesBasestar2003.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
