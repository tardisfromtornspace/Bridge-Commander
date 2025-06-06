#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 02/05/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'GoauldStarbase'
iconName = 'GoauldStarbase'
longName = 'Starbase'
shipFile = 'GoauldStarbase' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 791
SubMenu = "Goa'uld Ships/Bases"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'GoauldStarbase',
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
Foundation.ShipDef.GoauldStarbase = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.GoauldStarbase.dTechs = {
	"AutoTargeting": { "Pulse": [6, 0] },
	'SG Shields': { "RaceShieldTech": "Starbase Go'auld" }
}

Foundation.ShipDef.GoauldStarbase.fMaxWarp = 2.25
Foundation.ShipDef.GoauldStarbase.fCruiseWarp = 2.25
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.GoauldStarbase.hasTGLName = 1
Foundation.ShipDef.GoauldStarbase.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.GoauldStarbase.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.GoauldStarbase.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GoauldStarbase.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
