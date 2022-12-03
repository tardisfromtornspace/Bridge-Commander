#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 12/16/2004                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'DiamondsArmorVoyager'
iconName = 'ArmoredVoyager'
longName = 'Voyager Armor'
shipFile = 'DiamondsArmorVoyager' 
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
	'modName': 'ArmoredVoyager',
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
Foundation.ShipDef.DiamondsArmorVoyager = Foundation.FedShipDef(abbrev, species, { 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DiamondsArmorVoyager.dTechs = {
'Ablative Armour': 295000,
'Breen Drainer Immune': 1,
'Multivectral Shields': 30,
"Phase Cloak": 10,
"Regenerative Shields": 30,
"Transphasic Torpedo Immune": 1
}
Foundation.ShipDef.DiamondsArmorVoyager.CloakingSFX   = "Phasing_Device"
Foundation.ShipDef.DiamondsArmorVoyager.DeCloakingSFX = "Unphasing_Device"
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.DiamondsArmoredVoyager.hasTGLName = 1
# Foundation.ShipDef.DiamondsArmoredVoyager.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.DiamondsArmorVoyager.desc = "Admiral Janeway from a different timeline went back in time 30 years to rescue USS Voyager's crew, she brought back Transphasic torpedoes, Energy Ablative Armour Generators, and a quantum phasing device."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#   Alex SL Gato note: Removing these lines was necessary to prevent BC giving the    #
#   black screen yellow cursor error.                                                 #
#                                                                                     #
#if menuGroup:           Foundation.ShipDef.DiamondsArmoredVoyager.RegisterQBShipMenu(menuGroup)
#if playerMenuGroup:     Foundation.ShipDef.DiamondsArmoredVoyager.RegisterQBPlayerShipMenu(playerMenuGroup)
#
#if Foundation.shipList._keyList.has_key(longName):
#     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
#     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
