#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 10/09/2004                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG2003HadesBasestar'
iconName = 'HadesBasestar'
longName = 'Type-A Basestar'
shipFile = 'BSG2003HadesBasestar' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
SubMenu = ["Cylon Ships", "Basestars"]
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003HadesBasestar',
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
Foundation.ShipDef.BSG2003HadesBasestar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG2003HadesBasestar.dTechs = {
	"AutoTargeting": { "Pulse": [3, 1] },
	'Simulated Point Defence' : { "Distance": 35.0, "InnerDistance": 5.0, "Effectiveness": 0.8, "LimitTurn": 0.25, "LimitSpeed": 56, "Period": 0.1, "MaxNumberTorps": 24, },
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Coils"], "Core": ["Tylium Energizer"], "Cooldown Time": 15 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003HadesBasestar.fMaxWarp = 6.1
Foundation.ShipDef.BSG2003HadesBasestar.fCruiseWarp = 6.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003HadesBasestar.hasTGLName = 1
# Foundation.ShipDef.BSG2003HadesBasestar.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003HadesBasestar.desc = "Backbone of the Cylon Rebellion during the First Cylon War and originally designed by Colonial scientists as a combat vessel is the infamous 'Type-A' Basestar, also known as 'Hades Basestar'. A fully armed Basestar is the most deadly ship in the known space. This massive, double saucer vessels measured some 1768 meters in diameter and carried a Legion of Cylon troops and 300 Raider type fighter craft. They are armed with over one-hundred defensive RailGun turrets and nukes. So formidable is a lone Basestar, it is considered to be more powerful than a Battlestar."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003HadesBasestar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003HadesBasestar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
