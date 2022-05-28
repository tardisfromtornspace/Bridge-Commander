from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 04.07.2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CloakFireBirdOfPrey'
iconName = 'BirdOfPrey'
longName = 'ST6 BirdOfPrey'
shipFile = 'CloakFireBirdOfPrey' 
menuGroup = 'Klingon Ships'
playerMenuGroup = 'Klingon Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'CloakFireBirdOfPrey',
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
import F_CloakAttackDef
Foundation.ShipDef.CloakFireBirdOfPrey = F_CloakAttackDef.CloakAttackDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.CloakFireBirdOfPrey.fMaxWarp = 8.4
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.CloakFireBirdOfPrey.hasTGLName = 1
Foundation.ShipDef.CloakFireBirdOfPrey.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.CloakFireBirdOfPrey.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.CloakFireBirdOfPrey.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CloakFireBirdOfPrey.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
