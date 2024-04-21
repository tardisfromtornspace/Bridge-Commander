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
abbrev = 'B5SoulHunterVessel'
iconName = 'B5SoulHunterVessel'
longName = 'Soul Hunter Vessel'
shipFile = 'B5SoulHunterVessel' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_SHUTTLE
SubMenu = "Soul Hunters"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'B5SoulHunterVessel',
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
Foundation.ShipDef.B5SoulHunterVessel = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.B5SoulHunterVessel.dTechs = {
	"Tachyon Sensors": 1.0
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.B5SoulHunterVessel.hasTGLName = 1
# Foundation.ShipDef.B5SoulHunterVessel.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                    #
Foundation.ShipDef.B5SoulHunterVessel.desc = "Soul Hunters have been using this type of ship for millennia. Little is known of its capabilities."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.B5SoulHunterVessel.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5SoulHunterVessel.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
