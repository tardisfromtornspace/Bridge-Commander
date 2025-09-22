#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created manually                                                                   #
#  Date: 21/09/2025                                                                   #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG1978Olympia'
iconName = 'BS_Olympia'
longName = 'Battlestar Olympia'
shipFile = 'BSG1978Olympia' 
menuGroup = 'BSG (1978) Ships'
playerMenuGroup = 'BSG (1978) Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Twelve Colonies of Man", "Battlestars"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG1978Olympia',
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
Foundation.ShipDef.BSG1978Olympia = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG1978Olympia.dTechs = {
	"AutoTargeting": { "Pulse": [3, 0] },
	'Partially Distributed Shields': {"Shield Transfer Ratio": 1.25, "Max Percentage Damage": 2, "Collapse Threshold": 0.25, "Max Radians": 2.094395},
	"Alternate-Warp-FTL": {
		"Setup": {
			"BSG 1978 Ultra-Light-Drive": {	"Nacelles": ["Gravimetric Initiator"], "Core": ["Tylium Energizer"]},
		},
	},
}

Foundation.ShipDef.BSG1978Olympia.fMaxWarp = 3.0
Foundation.ShipDef.BSG1978Olympia.fCruiseWarp = 2.0

#                                                                                     #
#######################################################################################
#                                                                                     #
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG1978Olympia.desc = "The Olympia is the name of a Colonial battlestar."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG1978Olympia.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG1978Olympia.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
