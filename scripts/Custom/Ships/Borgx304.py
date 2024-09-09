#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 30/03/2008                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Borgx304'
iconName = 'Borgx304'
longName = 'Assimilated BC-304'
shipFile = 'Borgx304' 
menuGroup = 'Non canon X-Overs'
playerMenuGroup = 'Non canon X-Overs'
species = App.SPECIES_GALAXY
SubMenu = "Borg"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Borgx304',
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
Foundation.ShipDef.Borgx304 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Borgx304.dTechs = {
	'SG Shields': { "RaceShieldTech": "Asgard", "RaceHullTech": "Tau'ri" },
	"SG Asgard Beams Weapon": {"HullDmgMultiplier": 1.0, "ShieldDmgMultiplier": 1.0},
	'Automated Destroyed System Repair': {"Time": 120.0},
	"AutoTargeting": { "Pulse": [3, 1] },
	'Borg Adaptation': 2,
	'Breen Drainer Immune': 1,
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Borgx304.hasTGLName = 1
# Foundation.ShipDef.Borgx304.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Borgx304.desc = 'Assimilated BC-304'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Borgx304.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Borgx304.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
