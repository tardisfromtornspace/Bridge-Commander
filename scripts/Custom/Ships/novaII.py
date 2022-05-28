from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 13.12.2003                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'novaII'
iconName = 'novaII'
longName = 'Rhode Island'
shipFile = 'novaII' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'novaII',
	'author': 'Lord Vader',
	'version': '1.0',
	'sources': [ '' ],
	'comments': 'Ship By Lord Vader'
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.novaII = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.novaII.sBridge = 'novabridge'
Foundation.ShipDef.novaII.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 5,
	'Fed Ablative Armor': { "Plates": ["Forward Ablative Armor", "Dorsal Ablative Armor", "Aft Ablative Armor", "Ventral Ablative Armor"]
}}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.novaII.hasTGLName = 1
Foundation.ShipDef.novaII.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.novaII.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.novaII.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.novaII.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
