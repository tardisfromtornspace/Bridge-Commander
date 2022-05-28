from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 4/16/03                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'MvamPrometheus'
iconName = 'MvamPrometheus'
longName = 'Prometheus'
shipFile = 'MvamPrometheus' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_SOVEREIGN
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'MvamPrometheus',
	'author': 'Nixon and Gtea',
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
Foundation.ShipDef.MvamPrometheus = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.MvamPrometheus.sBridge = 'prometheusbridge'
Foundation.ShipDef.MvamPrometheus.fMaxWarp = 9.9
Foundation.ShipDef.MvamPrometheus.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 20,
	'Multivectral Shields': 20,
	'Fed Ablative Armor': { "Plates": ["Dorsal Aft Ablative Armor", "Dorsal Forward Ablative Armor", "Ventral Aft Ablative Armor", "Ventral Forward Ablative Armor", "Saucer Left Ablative Armor", "Saucer Right Ablative Armor", "Saucer Forward Ablative Armor"]
}}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.MvamPrometheus.hasTGLName = 1
Foundation.ShipDef.MvamPrometheus.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.MvamPrometheus.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.MvamPrometheus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MvamPrometheus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
