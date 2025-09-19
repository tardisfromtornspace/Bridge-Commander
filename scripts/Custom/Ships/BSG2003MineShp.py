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
abbrev = 'BSG2003MineShp'
iconName = 'MineShp'
longName = 'Mining Ship'
shipFile = 'BSG2003MineShp' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Colonial Ships", "Civilian craft"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003MineShp',
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
Foundation.ShipDef.BSG2003MineShp = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG2003MineShp.dTechs = {
	'Simulated Point Defence' : { "Distance": 35.0, "InnerDistance": 4.0, "Effectiveness": 0.15, "LimitTurn": 0.26, "LimitSpeed": 51, "Period": 3.1, "MaxNumberTorps": 1, },
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Coil"], "Core": ["Power Core"], "Cooldown Time": 15 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003MineShp.fMaxWarp = 5.25
Foundation.ShipDef.BSG2003MineShp.fCruiseWarp = 5.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003MineShp.hasTGLName = 1
# Foundation.ShipDef.BSG2003MineShp.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003MineShp.desc = "A Mining ship was a vehicle of the Fleet. The designation is the Majahul. Her design was unusual, but it worked all the same."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003MineShp.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003MineShp.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
