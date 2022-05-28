from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 23/02/2003                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'LowCube'
iconName = 'LowCube'
longName = 'Cube'
shipFile = 'LowCube' 
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'LowCube',
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
#Foundation.ShipDef.LowCube = Foundation.CardStarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
import F_BorgAttackDef
Foundation.ShipDef.LowCube = F_BorgAttackDef.BorgAttackDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.LowCube.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.LowCube.fMaxWarp = 9.999
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.LowCube.hasTGLName = 1
Foundation.ShipDef.LowCube.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.LowCube.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.LowCube.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.LowCube.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
