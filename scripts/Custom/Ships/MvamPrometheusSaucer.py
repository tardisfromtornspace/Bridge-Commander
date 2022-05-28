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
abbrev = 'MvamPrometheusSaucer'
iconName = 'MvamPrometheusSaucer'
longName = 'Prometheus Saucer'
shipFile = 'MvamPrometheusSaucer' 
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
	'modName': 'MvamPrometheusSaucer',
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
Foundation.ShipDef.MvamPrometheusSaucer = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.MvamPrometheusSaucer.sBridge = 'prometheusbridge'
Foundation.ShipDef.MvamPrometheusSaucer.fMaxWarp = 9.9
Foundation.ShipDef.MvamPrometheusSaucer.dTechs = {
	'Breen Drainer Immune': 1,
	'Fed Ablative Armor': { "Plates": ["Saucer Left Ablative Armor", "Saucer Right Ablative Armor", "Saucer Forward Ablative Armor"]
}}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.MvamPrometheusSaucer.hasTGLName = 1
Foundation.ShipDef.MvamPrometheusSaucer.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.MvamPrometheusSaucer.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.MvamPrometheusSaucer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MvamPrometheusSaucer.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
