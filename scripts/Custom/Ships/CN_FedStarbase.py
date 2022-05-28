from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 29.10.2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CN_FedStarbase'
iconName = 'FedStarbase'
longName = 'CN_FedStarbase'
shipFile = 'CN_FedStarbase' 
menuGroup = 'Bases'
playerMenuGroup = ''
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'CN_FedStarbase',
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
Foundation.ShipDef.CN_FedStarbase = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.CN_FedStarbase.dTechs = { 'Breen Drainer Immune': 1 }
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
#Foundation.ShipDef.CN_FedStarbase.hasTGLName = 1
#Foundation.ShipDef.CN_FedStarbase.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.CN_FedStarbase.desc = 'Earth Spacedock or Starbase 1 was a Federation space station facility in Earth orbit, built sometime prior to the year 2285. The station was built with a vast interior, in which numerous starships could be berthed for service and repairs, and was part of the Sol system´s Starbase 1 complex of facilities. In the late 24th century, several classes of Starfleet starships were commonly built at Spacedock 1, including the Saber-class and the Norway-class. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.CN_FedStarbase.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CN_FedStarbase.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
