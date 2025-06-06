#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 28/05/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'MidwayStation'
iconName = 'MidwayStation'
longName = 'Midway Station'
shipFile = 'MidwayStation' 
menuGroup = 'Stargate Ships'
playerMenuGroup = ''
species = 755
SubMenu = "Human (Tau'ri) Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'MidwayStation',
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
Foundation.ShipDef.MidwayStation = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.MidwayStation.dTechs = {
	'SG Shields': { "RaceShieldTech": "Asgard" }
}

Foundation.ShipDef.MidwayStation.fMaxWarp = 1.0
Foundation.ShipDef.MidwayStation.fCruiseWarp = 1.0
Foundation.ShipDef.MidwayStation.IsSGWorkingStargate = 3
Foundation.ShipDef.MidwayStation.SGWorkingStargateRad = 0.17
Foundation.ShipDef.MidwayStation.SGWorkingStargateFlashRad = 0.08
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.MidwayStation.hasTGLName = 1
Foundation.ShipDef.MidwayStation.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.MidwayStation.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.MidwayStation.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MidwayStation.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
