#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 14/01/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'ReplicatorHatak'
iconName = 'HatakRefit'
longName = 'Goa`uld Ha`tak'
shipFile = 'ReplicatorHatak' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 780
SubMenu = "Replicator Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'ReplicatorHatak',
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
Foundation.ShipDef.ReplicatorHatak = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.ReplicatorHatak.dTechs = {
	"SGReplicator Adaptation": 1,
	'SG Shields': { "RaceShieldTech": "Replicator", "RaceHullTech": "Go'auld" }
}


Foundation.ShipDef.ReplicatorHatak.fMaxWarp = 9.0
Foundation.ShipDef.ReplicatorHatak.fCruiseWarp = 9.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.ReplicatorHatak.hasTGLName = 1
Foundation.ShipDef.ReplicatorHatak.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.ReplicatorHatak.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.ReplicatorHatak.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ReplicatorHatak.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
