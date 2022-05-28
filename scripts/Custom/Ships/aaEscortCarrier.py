#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 5/26/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'aaEscortCarrier'
iconName = 'aaEscortCarrier'
longName = 'Escort Carrier'
shipFile = 'aaEscortCarrier' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
species = App.SPECIES_GALAXY
SubMenu = "Galactic Empire"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'aaEscortCarrier',
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
Foundation.ShipDef.aaEscortCarrier = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaEscortCarrier.hasTGLName = 1
# Foundation.ShipDef.aaEscortCarrier.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaEscortCarrier.desc = 'The Ton-Falk-class escort carrier was a transport ship designed to carry Imperial starfighters. Though a capital ship, it was poorly armed and protected relative for its size, so it stayed to the rear of battle for its own safety while allowing its TIE fighters to engage the enemy. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaEscortCarrier.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaEscortCarrier.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
