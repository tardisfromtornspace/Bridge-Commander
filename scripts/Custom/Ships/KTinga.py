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
abbrev = 'KTinga'
iconName = 'KTinga'
longName = 'KTinga'
shipFile = 'KTinga' 
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
	'modName': 'KTinga',
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
Foundation.ShipDef.KTinga = Foundation.KlingonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.KTinga.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.KTinga.fMaxWarp = 7.9
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.KTinga.hasTGLName = 1
Foundation.ShipDef.KTinga.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.KTinga.desc = 'Perhaps the most successful design of vessel in history, the Bird of Prey has been in service in larger numbers over more subtypes for a longer time than any other class in known space. First fielded as the D11 class in the late 2270s, the ship was built from the start to fill a variety of roles. As a special operations ship she could use her cloak to penetrate Federation border defences and attack lightly defended targets such as sensor outposts, communications relays and cargo craft, creating confusion in advance of a Klingon fleet attack. She was also a natural scout ship, ideal for locating and tracking Federation fleets from under cloak. During the long period of tensions between the Federation and Klingon Empire, many D11s operated as raiders, cruising deep inside Federation space to pick off occasional lone vessels or outposts.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.KTinga.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.KTinga.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
