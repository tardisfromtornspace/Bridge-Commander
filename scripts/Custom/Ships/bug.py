from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 20.02.2003                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
import F_DomRamAI
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'bug'
iconName = 'Bug'
longName = 'Attack Ship'
shipFile = 'bug' 
menuGroup = 'Dominion Ships'
playerMenuGroup = 'Dominion Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'bugship',
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
Foundation.ShipDef.bugship = F_DomRamAI.DomRamAI(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.bugship.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.bugship.fMaxWarp = 8.77
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.bugship.hasTGLName = 1
Foundation.ShipDef.bugship.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.bug.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.bugship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.bugship.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
