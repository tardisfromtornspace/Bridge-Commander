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
abbrev = 'B5ZephyrRaider'
iconName = 'B5ZephyrRaider'
longName = 'Zephyr Raider'
shipFile = 'B5ZephyrRaider' 
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
	'modName': 'B5ZephyrRaider',
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
Foundation.ShipDef.B5ZephyrRaider = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.B5ZephyrRaider.dTechs = {
	'Simulated Point Defence' : { "Distance": 10.0, "InnerDistance": 3.0, "Effectiveness": 0.6, "LimitTurn": 0.85, "LimitSpeed": 55, "LimitDamage": "350", "Period": 1.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}}
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.B5ZephyrRaider.hasTGLName = 1
# Foundation.ShipDef.B5ZephyrRaider.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.B5ZephyrRaider.desc = "This delta-winged atmospheric capable space fighter was once in the service of the Belt Alliance, an obsolete colonial defense force supported by the Earth colonies in the Orion system. Created simply for defensive purposes, the Belt Alliances Zephyr class fighter was originally only to be used to capture suspected smugglers, raiders, and starships that tried to avoid paying jumpgate fees. Unfortunately this versatile little fighter became the weapon of choice for those pirates it was designed to combat. Cheap to build and easy to maintain, the Zephyr is an effective light fighter that is used constantly by all forms of galactic criminals, to prey upon the weak and defenseless. Fortunately, compared to real fighters used by the Narn, Centauri, Earth Alliance and Minbari, the Zephyr is little more than an annoyance, her light armor and simple weapons no match for any of the fighters used by aforementioned races. As the Zephyr was designed to fly in atmosphere, her wings are its most vulnerable target. One solid hit to either of the fuel filled wings, gives the pilot a very low chance of survival."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.B5ZephyrRaider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5ZephyrRaider.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
