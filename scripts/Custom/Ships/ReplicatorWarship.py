#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 19/01/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'ReplicatorWarship'
iconName = 'ReplicatorWarship'
longName = 'Command Cruiser'
shipFile = 'ReplicatorWarship' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 782
SubMenu = "Replicator Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'ReplicatorWarship',
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
Foundation.ShipDef.ReplicatorWarship = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.ReplicatorWarship.dTechs = {
	'Automated Destroyed System Repair': {"Time": 60.0},
	"SGReplicator Adaptation": 1,
	'SG Shields': { "RaceShieldTech": "Replicator" }
}

Foundation.ShipDef.ReplicatorWarship.fMaxWarp = 9.0
Foundation.ShipDef.ReplicatorWarship.fCruiseWarp = 9.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.ReplicatorWarship.hasTGLName = 1
Foundation.ShipDef.ReplicatorWarship.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.ReplicatorWarship.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.ReplicatorWarship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ReplicatorWarship.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
