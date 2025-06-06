#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 14/06/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Valhalla'
iconName = 'Valhalla'
longName = 'Warship (Standard)'
shipFile = 'Valhalla' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 770
SubMenu = "Asgard Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Valhalla',
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
Foundation.ShipDef.Valhalla = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Valhalla.dTechs = {
	'SG Shields': { "RaceShieldTech": "Asgard", "FacetFactor" : 3 },
	"TachyonBeam": { "Immune": -1 }
}

Foundation.ShipDef.Valhalla.fMaxWarp = 9.35
Foundation.ShipDef.Valhalla.fCruiseWarp = 9.2
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.Valhalla.hasTGLName = 1
Foundation.ShipDef.Valhalla.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.Valhalla.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Valhalla.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Valhalla.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
