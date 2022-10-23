#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 04/07/2003                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'jclasspod'
iconName = 'jclasspod'
longName = 'J Class pod'
shipFile = 'jclasspod' 
menuGroup = 'Pre-Fed ships'
playerMenuGroup = 'Pre-Fed ships'
SubMenu = "United Earth ships"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'jclasspod',
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
Foundation.ShipDef.jclasspod = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.jclasspod.dTechs = {
	'Polarized Hull Plating': { "Plates": ["Hull Polarizer"]
}}

Foundation.ShipDef.jclasspod.fMaxWarp = 2.0
Foundation.ShipDef.jclasspod.fCruiseWarp = 1.5
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.jclasspod.hasTGLName = 1
# Foundation.ShipDef.jclasspod.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.jclasspod.desc = "The J-class was a starship design of Earth origin utilized by the Earth Cargo Service as a freighter. They were operated by captains with an Earth Cargo Authority license. These vessels have a history dating back to the early 22nd century, with one of the ships of the class, the ECS Horizon, commissioned in 2102."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.jclasspod.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.jclasspod.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
