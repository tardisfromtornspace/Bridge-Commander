#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 22.02.2009                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'ancientshuttle'
iconName = 'AncientShuttle'
longName = 'Ancient Shuttle'
shipFile = 'ancientshuttle' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 773
SubMenu = "Ancient Ships/Bases"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'ancientshuttle',
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
Foundation.ShipDef.ancientshuttle = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })
Foundation.ShipDef.ancientshuttle.fCrew = 17
Foundation.ShipDef.ancientshuttle.dTechs = {
	'SG Shields': { "RaceShieldTech": "Ancient Alteran" }
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.ancientshuttle.hasTGLName = 1
# Foundation.ShipDef.ancientshuttle.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.ancientshuttle.desc = "The Ancient shuttle is a short-range exploration vessel employed on the Ancient starship Destiny, bigger than a Puddle Jumper. The ship is capable of sublight speeds but not faster-than-light travel. Its sublight speed is also inferior to that of Destiny itself. It has two forward-firing energy weapons mounted in the wings, which appear to be of equivalent power to Destiny's anti-fighter turrets. It has energy shielding for defense, and a stealth mode."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.ancientshuttle.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ancientshuttle.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
