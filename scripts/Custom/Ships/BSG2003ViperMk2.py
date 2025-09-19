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
abbrev = 'BSG2003ViperMk2'
iconName = 'ViperMk2'
longName = 'Mark 2'
shipFile = 'BSG2003ViperMk2' 
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
	'modName': 'BSG2003ViperMk2',
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
Foundation.ShipDef.BSG2003ViperMk2 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG2003ViperMk2.dTechs = {
	"AutoTargeting": { "Torpedo": [2, 1] },
	'Simulated Point Defence' : { "Distance": 15.0, "InnerDistance": 2.0, "Effectiveness": 0.45, "LimitTurn": -0.8, "LimitSpeed": 35, "LimitDamage": "-90", "Period": 2.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	#"Alternate-Warp-FTL": {
	#	"Setup": {
	#		"nBSGDimensionalJump": {	"Nacelles": ["FTL Coil"], "Core": ["Tylium Reactor"], "Cooldown Time": 15 * 60},
	#	},
	#},
}

Foundation.ShipDef.BSG2003ViperMk2.fMaxWarp = 5.25
Foundation.ShipDef.BSG2003ViperMk2.fCruiseWarp = 5.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003ViperMk2.hasTGLName = 1
# Foundation.ShipDef.BSG2003ViperMk2.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003ViperMk2.desc = "Capable of atmospheric flight, the Viper is a single-seat sub-light speed craft mounting two kinetic energy weapons (3 on at least one later design), as well as having hardpoints beneath the wings for mounting missiles, munitions pods and other ordnance. The Mark II was used during the Cylon War, proving a capable fighting vehicle. It is regarded as one of the reasons the Twelve Colonies did not suffer defeat at the hands of the Cylons. The Mark II remained in service after the end of the war."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003ViperMk2.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003ViperMk2.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
