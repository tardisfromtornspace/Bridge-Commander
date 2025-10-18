from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 3/9/03                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'D6Axanar'
iconName = 'D6Axanar'
longName = 'D6 Axanar'
shipFile = 'D6Axanar' 
menuGroup = 'Klingon Ships'
playerMenuGroup = 'Klingon Ships'
SubMenu = "Axanar"
SubSubMenu = "D6 Axanar"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'D6Axanar',
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
Foundation.ShipDef.D6Axanar = Foundation.KlingonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#Foundation.ShipDef.KTinga.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.D6Axanar.fMaxWarp = 7.9
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.KTinga.hasTGLName = 1
#Foundation.ShipDef.KTinga.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.D6Axanar.desc = 'The D6 was the most common Klingon Battlecruiser during the Four Years War against the Federation in 2241-2245. \nUntil the emergence of the Ares-class, no Federation ship was any match against the D6. \nTowards the end of the war, the D6 was succeeded by the D7.\n\nTactics: \nIf possible, focus your fire on a single shield or two. Empty your forward weapons then come around to use your aft torpedoes.\nWhen fighting the D6, focus your fire on the dorsal or ventral shield to stay out of its weapons arcs.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.D6Axanar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.D6Axanar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
