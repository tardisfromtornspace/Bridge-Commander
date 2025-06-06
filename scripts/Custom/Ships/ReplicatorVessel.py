#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 05/02/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'ReplicatorVessel'
iconName = 'ReplicatorVessel'
longName = 'Stolen Cruiser'
shipFile = 'ReplicatorVessel' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 781
SubMenu = "Replicator Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'ReplicatorVessel',
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
Foundation.ShipDef.ReplicatorVessel = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.ReplicatorVessel.dTechs = {
	"SGReplicator Adaptation": 1,
	'SG Shields': { "RaceShieldTech": "Replicator", "RaceHullTech": "Unknown" },
	'Simulated Point Defence' : { "Distance": 70.0, "InnerDistance": 26.0, "Effectiveness": 0.99, "LimitTurn": 8.5, "LimitSpeed": 250, "LimitDamage": "-600", "Period": 8.0, "MaxNumberTorps": 1, "Phaser": {"Priority": 1}},
}

Foundation.ShipDef.ReplicatorVessel.fMaxWarp = 9.0
Foundation.ShipDef.ReplicatorVessel.fCruiseWarp = 9.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.ReplicatorVessel.hasTGLName = 1
Foundation.ShipDef.ReplicatorVessel.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.ReplicatorVessel.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.ReplicatorVessel.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ReplicatorVessel.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
