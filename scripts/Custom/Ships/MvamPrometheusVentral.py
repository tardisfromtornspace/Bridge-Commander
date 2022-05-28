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
abbrev = 'MvamPrometheusVentral'
iconName = 'MvamPrometheusVentral'
longName = 'Prometheus Ventral'
shipFile = 'MvamPrometheusVentral' 
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
	'modName': 'MvamPrometheusVentral',
	'author': 'Nixon, Gtea',
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
Foundation.ShipDef.MvamPrometheusVentral = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.MvamPrometheusVentral.sBridge = 'prometheusbridge'
Foundation.ShipDef.MvamPrometheusVentral.fMaxWarp = 9.9
Foundation.ShipDef.MvamPrometheusVentral.dTechs = {
	'Breen Drainer Immune': 1,
	'Multivectral Shields': 20,
	'Fed Ablative Armor': { "Plates": ["Ventral Aft Ablative Armor", "Ventral Forward Ablative Armor"]
}}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.MvamPrometheusVentral.hasTGLName = 1
Foundation.ShipDef.MvamPrometheusVentral.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.MvamPrometheusVentral.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.MvamPrometheusVentral.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MvamPrometheusVentral.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
