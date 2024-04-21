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
abbrev = 'B5RaiderBattlewagon'
iconName = 'B5RaiderBattlewagon'
longName = 'Empty Battlewagon'
shipFile = 'B5RaiderBattlewagon' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_SHUTTLE
SubMenu = "Raiders"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'B5RaiderBattlewagon',
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
Foundation.ShipDef.B5RaiderBattlewagon = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.B5RaiderBattlewagon.dTechs = {
	"Tachyon Sensors": 2.9
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.B5RaiderBattlewagon.hasTGLName = 1
# Foundation.ShipDef.B5RaiderBattlewagon.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.B5RaiderBattlewagon.desc = "This makeshift 'battle wagon' built by the Raiders was a very small vessel, using a series of rotating wheels to carry and support up to 21 Belt Alliance Z-109 Zephyr class multi-environment fighters."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.B5RaiderBattlewagon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5RaiderBattlewagon.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
