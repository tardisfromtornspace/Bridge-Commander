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
abbrev = 'BSG2003MkXRaider'
iconName = 'Mk10Raider'
longName = 'Raider Type I'
shipFile = 'BSG2003MkXRaider' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
SubMenu = ["Cylon Ships", "Raiders"]
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003MkXRaider',
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
Foundation.ShipDef.BSG2003MkXRaider = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG2003MkXRaider.dTechs = {
	'Simulated Point Defence' : { "Distance": 15.0, "InnerDistance": 2.0, "Effectiveness": 0.45, "LimitTurn": -0.8, "LimitSpeed": 25, "LimitDamage": "-90", "Period": 2.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["Jump Sys"], "Core": ["Tylium Energizer"], "Cooldown Time": 15 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003MkXRaider.fMaxWarp = 6.25
Foundation.ShipDef.BSG2003MkXRaider.fCruiseWarp = 6.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003MkXRaider.hasTGLName = 1
# Foundation.ShipDef.BSG2003MkXRaider.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003MkXRaider.desc = "The Assault Fighter used by the Cylon Fleet in the First Cylon War."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003MkXRaider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003MkXRaider.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
