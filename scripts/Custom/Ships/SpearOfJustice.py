#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created manually by - CharaToLoki AKA Alex SL Gato                                 #
#  Date: 12.10.2024                                                                   #
#######################################################################################
#                                                                                     #
import Foundation
import App
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'SpearOfJustice',
	'author': 'Alex SL Gato',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#    
abbrev = "SpearOfJustice"
iconName = "SpearOfJustice"
longName = "Undyne's Spear of Justice"
shipFile = "SpearOfJustice"
species = App.SPECIES_SOVEREIGN
menuGroup = "Non canon X-Overs"
playerMenuGroup = "Non canon X-Overs"
SubMenu = "CharaToLokis"

#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#

Foundation.ShipDef.SpearOfJustice = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu }) 

Foundation.ShipDef.SpearOfJustice.fMaxWarp = 9.99 + 0.01
Foundation.ShipDef.SpearOfJustice.fWarpEntryDelayTime = 0.5
Foundation.ShipDef.SpearOfJustice.bPlanetKiller = 1

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL 
#Foundation.ShipDef.SpearOfJustice.hasTGLName = 1
#Foundation.ShipDef.SpearOfJustice.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:

Foundation.ShipDef.SpearOfJustice.desc = "She will throw a spear on your face!"

#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#
# Alex SL Gato: commenting these to avoid crashes when we don't want any ship to be added here  #
#if menuGroup:           Foundation.ShipDef.SpearOfJustice.RegisterQBShipMenu(menuGroup)
#if playerMenuGroup:     Foundation.ShipDef.SpearOfJustice.RegisterQBPlayerShipMenu(playerMenuGroup)
#
#
#if Foundation.shipList._keyList.has_key(longName):
#      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
#      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

#                                                                                     #
#######################################################################################