#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 13/01/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'DSC304Odyssey'
iconName = 'DSC304'
longName = 'Odyssey'
shipFile = 'DSC304Odyssey' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 754
SubMenu = ["Human (Tau'ri) Ships", "DSC-304"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'DSC304Odyssey',
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
Foundation.ShipDef.DSC304Odyssey = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.DSC304Odyssey.dTechs = {
	"AutoTargeting": { "Pulse": [3, 1] },
	'SG Shields': { "RaceShieldTech": "Asgard", "RaceHullTech": "Tau'ri" }
}

Foundation.ShipDef.DSC304Odyssey.fMaxWarp = 6.0
Foundation.ShipDef.DSC304Odyssey.fCruiseWarp = 5.9
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.DSC304Odyssey.hasTGLName = 1
Foundation.ShipDef.DSC304Odyssey.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.DSC304Odyssey.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.DSC304Odyssey.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DSC304Odyssey.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
