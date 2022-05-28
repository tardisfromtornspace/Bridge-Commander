#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 30/10/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Blackbird'
iconName = 'Blackbird'
longName = 'Blackbird'
shipFile = 'Blackbird' 
menuGroup = 'BSG Ships'
playerMenuGroup = 'BSG Ships'
species = App.SPECIES_GALAXY
SubMenu = "Colonial Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Blackbird',
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
Foundation.ShipDef.Blackbird = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Blackbird.hasTGLName = 1
# Foundation.ShipDef.Blackbird.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Blackbird.desc = 'The Blackbird is a prototype Colonial stealth fighter craft constructed by Chief Galen Tyrol, his deck crews, and other members of Galactica. This craft was meant to supplement the Viper, given the issues in maintaining the remaining craft aboard the battlestar, however they ended up building a ship that was of more value to Galactica than another Viper. It is designed to use the Viper launch tubes, and therefore shares the same general shape. It is built more for speed than for maneuverability. The Blackbird is not equipped with any guns, but is equipped with a single missile. It does not use metal for its exterior. Instead, it uses a carbon composite material, which makes it largely invisible to DRADIS scanning. The Blackbird is also FTL-capable, but is not equipped with a Colonial transponder. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Blackbird.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Blackbird.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
