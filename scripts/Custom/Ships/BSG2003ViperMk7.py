#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 08/09/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG2003ViperMk7'
iconName = 'ViperMk7'
longName = 'Mark 7'
shipFile = 'BSG2003ViperMk7' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Colonial Ships", "Fighters", "Vipers"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003ViperMk7',
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
Foundation.ShipDef.BSG2003ViperMk7 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG2003ViperMk7.dTechs = {
	"AutoTargeting": { "Torpedo": [2, 1] },
	'Simulated Point Defence' : { "Distance": 15.0, "InnerDistance": 2.0, "Effectiveness": 0.45, "LimitTurn": -0.8, "LimitSpeed": 35, "LimitDamage": "-90", "Period": 2.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	#"Alternate-Warp-FTL": {
	#	"Setup": {
	#		"nBSGDimensionalJump": {	"Nacelles": ["FTL Coil"], "Core": ["Tylium Reactor"], "Cooldown Time": 15 * 60},
	#	},
	#},
}

Foundation.ShipDef.BSG2003ViperMk7.fMaxWarp = 5.25
Foundation.ShipDef.BSG2003ViperMk7.fCruiseWarp = 5.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003ViperMk7.hasTGLName = 1
# Foundation.ShipDef.BSG2003ViperMk7.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003ViperMk7.desc = "The Mark II was superseded by newer models after the end of the Cylon War, with the Mark VII serving in front-line duties. The Mark VII incorporated software-based controls and fully networked systems, providing superior agility, battle management, and flight information for the pilot."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003ViperMk7.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003ViperMk7.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
