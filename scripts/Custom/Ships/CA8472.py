from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 1/26/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CA8472'
iconName = 'CA8472'
longName = 'Species 8472 Bioship'
shipFile = 'CA8472' 
menuGroup = '8472 Ships'
playerMenuGroup = '8472 Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'CA8472',
	'author': 'Collective Alliance',
	'version': '1.0',
	'sources': None,
	'comments': 'CA'
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.CA8472 = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.CA8472.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.CA8472.fMaxWarp = 9.99
Foundation.ShipDef.CA8472.bPlanetKiller = 1
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.CA8472.hasTGLName = 1
Foundation.ShipDef.CA8472.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.CA8472.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.CA8472.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CA8472.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
