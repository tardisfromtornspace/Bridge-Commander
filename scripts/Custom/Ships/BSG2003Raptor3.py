#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created manually                                                                   #
#  Date: 19/09/2025                                                                   #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG2003Raptor3'
iconName = 'Raptor3'
longName = 'Assault Raptor'
shipFile = 'BSG2003Raptor3' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Colonial Ships", "Raptors"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003Raptor3',
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
Foundation.ShipDef.BSG2003Raptor3 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG2003Raptor3.dTechs = {
	"AutoTargeting": { "Torpedo": [4, 1] },
	'Simulated Point Defence' : { "Distance": 15.0, "InnerDistance": 2.0, "Effectiveness": 0.45, "LimitTurn": -0.8, "LimitSpeed": 35, "LimitDamage": "-90", "Period": 5.0, "MaxNumberTorps": 1},
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Coil"], "Core": ["Tylium Reactor"], "Cooldown Time": 15 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003Raptor3.fMaxWarp = 5.25
Foundation.ShipDef.BSG2003Raptor3.fCruiseWarp = 5.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003Raptor3.hasTGLName = 1
# Foundation.ShipDef.BSG2003Raptor3.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003Raptor3.desc = "The Raptor is a multipurpose military spacecraft. Normally, Raptors accompany Viper squadrons and provides targeting information as well as electronic counter measures. Raptors can also carry external munitions to assist Vipers against large targets. The Raptor's non-combat roles include SAR (search and rescue) operations and transport of military personnel in hostile areas. Raptors, like Vipers are capable of atmospheric operations. Unlike Vipers, however, Raptors are also capable of short-range FTL jumps. Its standard crew includes a pilot and electronics countermeasure officer."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003Raptor3.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003Raptor3.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
