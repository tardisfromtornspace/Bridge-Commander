from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 16.08.2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import F_KlingonBaseDef
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'KlingonImperialStarbase'
iconName = 'KlingonImperialStarbase'
longName = 'Klingon Imperial Starbase'
shipFile = 'KlingonImperialStarbase' 
menuGroup = 'Bases'
playerMenuGroup = ''
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'KlingonImperialStarbase',
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
Foundation.ShipDef.KlingonImperialStarbase = Foundation.KlingonStarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.KlingonImperialStarbase.hasTGLName = 1
Foundation.ShipDef.KlingonImperialStarbase.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.KlingonImperialStarbase.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.KlingonImperialStarbase.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.KlingonImperialStarbase.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
