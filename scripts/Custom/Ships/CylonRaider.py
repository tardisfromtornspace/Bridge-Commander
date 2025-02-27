#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 08/09/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CylonRaider'
iconName = 'CylonRaider'
longName = 'Raider'
shipFile = 'CylonRaider' 
menuGroup = 'BSG Ships'
playerMenuGroup = 'BSG Ships'
SubMenu = ["Cylon Ships", "Raiders"]
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'CylonRaider',
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
Foundation.ShipDef.CylonRaider = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.CylonRaider.hasTGLName = 1
# Foundation.ShipDef.CylonRaider.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.CylonRaider.desc = 'The Cylon Raider is the basic Strike Interceptor of the Cylon fleet. Its sleek design means it can speed past nearly all enemy ships and hunt down slower ships as well as dodge bullets in firefights. The Raider�s purpose is anti-strike, anti-missile and, in some cases, anti-escort. In small groups, Raiders can take down some Line Ships or do massive damage. This Raiders are cybernetic in nature: the ship is actually a living creature, with a complex system of organs, veins and biological fluids inside the main body. Just like the humanoid Cylons, the Raiders are also capable of being reborn into new Raiders after having been destroyed.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.CylonRaider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CylonRaider.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
