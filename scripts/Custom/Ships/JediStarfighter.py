#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 9/20/2004                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'JediStarfighter'
iconName = 'JediStarfighter'
longName = 'Jedi Starfighter'
shipFile = 'JediStarfighter' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
SubMenu = "Old Republic"
SubSubMenu = "Jedi ships"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'JediStarfighter',
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
Foundation.ShipDef.JediStarfighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.JediStarfighter.hasTGLName = 1
# Foundation.ShipDef.JediStarfighter.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.JediStarfighter.desc = 'The Jedi Starfighter (or Delta-7 Aethersprite Interceptor) is a small, sleek interceptor used by the Jedi Knights for reconnaissance missions. However, the starfighter was fitted with two twin-barrel laser cannons allowing the pilot to fight when necessary. As part of the Republic Judicial Department, the starfighters owned by the Jedi Order were colored in the maroon-and-white hues that represented diplomatic immunity in the Galactic Republic. It only has enough room for the head of an astromech droid, and required to dock a ship or a hyperspace ring to travel faster than light'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.JediStarfighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JediStarfighter.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
