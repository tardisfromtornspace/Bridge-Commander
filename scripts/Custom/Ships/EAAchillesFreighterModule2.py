#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 18/04/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'EAAchillesFreighterModule2'
iconName = 'EAAchillesFreighterAModule'
longName = 'Achilles Module 2'
shipFile = 'EAAchillesFreighterModule2' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_SHUTTLE
SubMenu = "Earth Alliance"
SubSubMenu = "Non-military craft"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'EAAchillesFreighterModule2',
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
Foundation.ShipDef.EAAchillesFreighterModule2 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.EAAchillesFreighterModule2.hasTGLName = 1
# Foundation.ShipDef.EAAchillesFreighterModule2.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.EAAchillesFreighterModule2.desc = "The Achilles Type Freighter is a space vessel manufactered by Luigi Mendoza et Cle at Zanzibar Station orbiting Deneb IV. Designed primarily for moving cargo between stations, this freighter has no atmospheric capability and generally stays outside a station while its cargo modules are transferred by tender to and from the station's cargo bays."
Foundation.ShipDef.EAAchillesFreighterModule2.dTechs = {
	'Defense Grid': 6,
	"Tachyon Sensors": 2.5
}

#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.EAAchillesFreighterModule2.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EAAchillesFreighterModule2.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
