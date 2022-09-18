#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 1/3/03                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Surrok'
iconName = 'Surrok'
longName = 'Suurok Class'
shipFile = 'Surrok' 
menuGroup = 'Pre-Fed ships'
playerMenuGroup = 'Pre-Fed ships'
SubMenu = "Vulcan High Command"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Surrok',
	'author': 'NinjaDriver',
	'version': '1.0',
	'sources': [ 'http://home.attbi.com/~mattwhite' ],
	'comments': 'This is my first ship with all custom textures.  Designed to complement NX-01 era ships.'
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.Surrok = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.Surrok.fMaxWarp = 7.0
Foundation.ShipDef.Surrok.fCruiseWarp = 6.5
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Surrok.hasTGLName = 1
# Foundation.ShipDef.Surrok.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Surrok.desc = "The Suurok-class was a type of Vulcan starship designated by the High Command as a science vessel and combat cruiser during the mid-22nd century. During the 2150s, this design was among the fastest and most powerful starships operating in the Vulcan fleet."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Surrok.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Surrok.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
