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
abbrev = 'D6AxanarBoom'
iconName = 'D6AxanarBoom'
longName = 'D6 Axanar Boom Section'
shipFile = 'D6AxanarBoom' 
menuGroup = 'Klingon Ships'
playerMenuGroup = 'Klingon Ships'
species = App.SPECIES_GALAXY
SubMenu = "Axanar"
SubSubMenu = "D6 Axanar"
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
Foundation.ShipDef.D6AxanarBoom = Foundation.KlingonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#Foundation.ShipDef.KTinga.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.D6AxanarBoom.fMaxWarp = 7.9
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.KTinga.hasTGLName = 1
#Foundation.ShipDef.KTinga.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.D6AxanarBoom.desc = 'The boom section of the D6, separated in the event of a warp core breach. A little homage to Star Fleet Battles and Klingon Honour Guard. Afterall, no Klingon Warrior wishes to end up at Grethor, do they?'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.D6AxanarBoom.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.D6AxanarBoom.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
	Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
	Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
