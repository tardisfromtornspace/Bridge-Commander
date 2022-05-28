#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 7/21/2004                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'DeathStarII'
iconName = 'DeathStarII'
longName = 'Death Star II'
shipFile = 'DeathStarII' 
menuGroup = 'Star Wars Fleet'                  # Menu to appear under in Quick Battle
playerMenuGroup = 'Star Wars Fleet'
SubMenu = "Galactic Empire"
SubSubMenu = "Planetkillers"	
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'DeathStarII',
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
Foundation.ShipDef.DeathStarII = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.DeathStarII.bPlanetKiller = 1
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.DeathStarII.hasTGLName = 1
# Foundation.ShipDef.DeathStarII.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.DeathStarII.desc = "The second Death Star, also known as the Death Star II, was a partially-completed moon-sized battle station constructed by the Galactic Empire as the successor to the Death Star. Like the first Death Star, the Death Star II's long-term purpose was to terrorize planets and star systems in league with the Rebel Alliance through the use of its planet-destroying superlaser. However, the Death Star II also served another purpose: luring the Rebels into a battle that would, the Empire hoped, destroy them once and for all. Though designed to be very similar in appearance and function to the first Death Star, the second Death Star improved on its predecessor's design by incorporating millions of millimeter-sized heat-dispersion tubes in place of the two-meter-wide thermal exhaust port exploited by the Rebel Alliance at the Battle of Yavin."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.DeathStarII.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DeathStarII.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
