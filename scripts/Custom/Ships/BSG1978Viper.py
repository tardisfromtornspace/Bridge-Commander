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
abbrev = 'BSG1978Viper'
iconName = 'ViperMk1'
longName = 'Viper'
shipFile = 'BSG1978Viper' 
menuGroup = 'BSG (1978) Ships'
playerMenuGroup = 'BSG (1978) Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Twelve Colonies of Man", "Fighters"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG1978Viper',
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
Foundation.ShipDef.BSG1978Viper = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG1978Viper.dTechs = {
	'Partially Distributed Shields': {"Shield Transfer Ratio": 1.25, "Max Percentage Damage": 2, "Collapse Threshold": 0.23, "Max Radians": 2.094395},
	"Alternate-Warp-FTL": {
		"Setup": {
			"BSG 1978 Ultra-Light-Drive": {	"Nacelles": ["Gravimetric Initiator"], "Core": ["Tylium Energizer"]},
		},
	},
}

Foundation.ShipDef.BSG1978Viper.fMaxWarp = 3.0
Foundation.ShipDef.BSG1978Viper.fCruiseWarp = 2.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG1978Viper.hasTGLName = 1
# Foundation.ShipDef.BSG1978Viper.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG1978Viper.desc = "Vipers are capable of atmospheric as well as space flight, and can land and take off from a planetary surface. Viper engines are designed to collect commonly occurring gases in planetary atmospheres and in space to power the ship´s fusion reactor. Vipers are also capable of supporting the pilot for up to two weeks in a form of suspended animation for extremely long missions. Armament consist of two directed energy weapons that are linked together to fire simultaneously. They can also be modified to carry fire suppression equipment. In the event of a crash landing, a Viper's cockpit can also be used as an escape pod, separating from the ship and parachuting to the ground. This system does not provide a soft landing—in fact, it can knock the pilot unconscious—but it is effective."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG1978Viper.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG1978Viper.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
