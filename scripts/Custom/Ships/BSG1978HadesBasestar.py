#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created manually                                                                   #
#  Date: 22/09/2025                                                                   #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG1978HadesBasestar'
iconName = 'HadesBasestar'
longName = 'Hades Basestar'
shipFile = 'BSG1978HadesBasestar' 
menuGroup = 'BSG (1978) Ships'
playerMenuGroup = 'BSG (1978) Ships'
SubMenu = ["Cylon Empire", "Basestars"]
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG1978HadesBasestar',
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
Foundation.ShipDef.BSG1978HadesBasestar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.BSG1978HadesBasestar.dTechs = {
	"AutoTargeting": { "Pulse": [3, 1] },
	'Partially Distributed Shields': {"Shield Transfer Ratio": 1.25, "Max Percentage Damage": 2, "Collapse Threshold": 0.23, "Max Radians": 2.094395},
	"Alternate-Warp-FTL": {
		"Setup": {
			"BSG 1978 Ultra-Light-Drive": {	"Nacelles": ["Gravimetric Initiator"], "Core": ["Tylium Energizer"]},
		},
	},
}

Foundation.ShipDef.BSG1978HadesBasestar.fMaxWarp = 4.0
Foundation.ShipDef.BSG1978HadesBasestar.fCruiseWarp = 3.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG1978HadesBasestar.hasTGLName = 1
# Foundation.ShipDef.BSG1978HadesBasestar.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG1978HadesBasestar.desc = "Backbone of the Cylon Empire is the infamous 'Basestar'. A fully armed Basestar has three times the fighters, troop and weapons capability of a Colonial Battlestar, making this space born killer the most deadly ship in the known galaxy. This massive, double saucer vessels measured some 1768 meters in diameter and carried a Legion of Cylon troops and 300 Raider type fighter craft. They are armed with over one-hundred defensive Turbo Laser turrets and two, long range, Mega-Pulsar guns. So formidable is a lone Basestar, it is considered to be more than a match for a single Battlestar, or even the defenses of an entire planet."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG1978HadesBasestar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG1978HadesBasestar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
