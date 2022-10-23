#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 05.09.2002                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Tholian'
iconName = 'Tholian'
longName = 'Tholian Ship'
shipFile = 'Tholian' 
menuGroup = 'Tholian Ships'
playerMenuGroup = 'Tholian Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Tholian',
	'author': 'Queball, Ignis',
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
Foundation.ShipDef.Tholian = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.Tholian.fMaxWarp = 7.0
Foundation.ShipDef.Tholian.fCruiseWarp = 6.5
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.Tholian.hasTGLName = 1
#Foundation.ShipDef.Tholian.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.Tholian.desc = 'The Tholian starship of the 22nd century was a relatively small starship employed by the Tholian Assembly. In 2152, making an unusual move, the Tholians traveled far beyond their territory, as they attempted to possess a 31st century time-travel pod discovered by the Earth starship Enterprise NX-01. Four Tholian starships intercepted and disabled the Vulcan cruiser Tal´Kir while it waited to rendezvous with Enterprise. They also attacked and defeated a fleet of Suliban vessels that were in pursuit of the arriving Earth ship. They then successfully removed the pod from Enterprise´s possession, only to have the pod return to its proper timeline moments later. THIS SHIP HAS BEEN MADE BY ROXORS!'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Tholian.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Tholian.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
