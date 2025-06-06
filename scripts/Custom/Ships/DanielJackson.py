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
abbrev = 'DanielJackson'
iconName = 'DanielJackson'
longName = 'Science Vessel'
shipFile = 'DanielJackson' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 769
SubMenu = "Asgard Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'DanielJackson',
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
Foundation.ShipDef.DanielJackson = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.DanielJackson.dTechs = {
	'SG Shields': { "RaceShieldTech": "Asgard", "FacetFactor" : 3 },
	"TachyonBeam": { "Immune": -1 }
}

Foundation.ShipDef.DanielJackson.fMaxWarp = 9.2
Foundation.ShipDef.DanielJackson.fCruiseWarp = 9.2
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.DanielJackson.hasTGLName = 1
Foundation.ShipDef.DanielJackson.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.DanielJackson.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.DanielJackson.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DanielJackson.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
