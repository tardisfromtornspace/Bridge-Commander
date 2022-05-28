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
abbrev = 'HadesBasestar'
iconName = 'HadesBasestar'
longName = 'HadesBasestar'
shipFile = 'HadesBasestar' 
menuGroup = 'BSG (TOS) Ships'
playerMenuGroup = 'BSG (TOS) Ships'
SubMenu = "Cylon Empire"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'HadesBasestar',
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
Foundation.ShipDef.HadesBasestar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.HadesBasestar.hasTGLName = 1
# Foundation.ShipDef.HadesBasestar.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.HadesBasestar.desc = "Backbone of the Cylon Empire is the infamous 'BASESTAR'. A fully armed Basestar has three times the fighters, troop and weapons capability of a Colonial Battlestar, making this space born killer the most deadly ship in the known galaxy. This massive, double saucer vessels measured some 1768 meters in diameter and carried a Legion of Cylon troops and 300 Raider type fighter craft. They are armed with over one-hundred defensive Turbo Laser turrets and two, long range, Mega-Pulsar guns. So formidable is a lone Basestar, it is considered to be more than a match for a single Battlestar, or even the defenses of an entire planet."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.HadesBasestar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HadesBasestar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
