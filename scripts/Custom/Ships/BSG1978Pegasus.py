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
abbrev = 'BSG1978Pegasus'
iconName = 'BS_Pegasus'
longName = 'Battlestar Pegasus'
shipFile = 'BSG1978Pegasus' 
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
	'modName': 'BSG1978Pegasus',
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
Foundation.ShipDef.BSG1978Pegasus = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG1978Pegasus.dTechs = {
	"AutoTargeting": { "Pulse": [3, 0] },
	'Partially Distributed Shields': {"Shield Transfer Ratio": 1.25, "Max Percentage Damage": 2, "Collapse Threshold": 0.25, "Max Radians": 2.094395},
	"Alternate-Warp-FTL": {
		"Setup": {
			"BSG 1978 Ultra-Light-Drive": {	"Nacelles": ["Gravimetric Initiator"], "Core": ["Tylium Energizer"]},
		},
	},
}

Foundation.ShipDef.BSG1978Pegasus.fMaxWarp = 3.0
Foundation.ShipDef.BSG1978Pegasus.fCruiseWarp = 2.0

#                                                                                     #
#######################################################################################
#                                                                                     #
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG1978Pegasus.desc = "The battlestar Pegasus, in the years prior to the fall of the Colonies, was assigned to patrol the edges of Colonial space under the leadership of Commander Cain. Cain was a noteworthy military leader, and was in fact known as a 'living legend.'\n\nTwo yahren before the destruction of the Colonies, Pegasus was involved in the Battle of Molecay with the Cylons. The battle was a complete disaster for the Colonials and the entire fifth fleet, except Pegasus, was destroyed. Pegasus managed to slip away from the battle and, aware that the route back home would be crawling with Cylons, Cain ordered the battlestar out into deep space.\n\nAs a result, Pegasus is the second of only two battlestars known to have survived the Cylon attack."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG1978Pegasus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG1978Pegasus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
