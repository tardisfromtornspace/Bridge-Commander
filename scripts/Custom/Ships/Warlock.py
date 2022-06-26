#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 9/3/2002                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Warlock'
iconName = 'Warlock'
longName = 'Warlock'
shipFile = 'Warlock' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
SubMenu = "Earth Alliance"
species = App.SPECIES_GALAXY
SubSubMenu = "Capital Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Warlock',
	'author': 'DamoclesX',
	'version': '1.2',
	'sources': [ 'DamoclesX@hotmail.com' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.Warlock = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.Warlock.dTechs = {
	'Defense Grid': 195
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.Warlock.hasTGLName = 1
#Foundation.ShipDef.Warlock.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.Warlock.desc = "The Warlock-class destroyer is an advanced warship design produced by the Earth Alliance. Rushed into production immediately after the Earth Alliance Civil War, the Warlock-class destroyer incorporates some of the most advanced technology available. It was the first Earth Alliance ship to feature artificial gravity without rotating sections thanks to the technology the Minbari delivered. This allowed designers to greatly improve the Warlock's design. Among these improvements was the Warlock having greater speed and maneuverability compared to the older Omega-class destroyers. The Warlock's conventional particle thrust engines are supplemented by a pair of hybrid gravitic engines that, like the artificial gravity systems, are based on Minbari technology and propulsion theory but are designed and manufactured using Earth-based materials. The weapons systems aboard the Warlock feature a wide variety of offensive and defensive emplacements that include standard plasma cannons, railguns, and missiles. Perhaps the most notable armament is a pair of particle beam cannons originally designed for use on the Aegis orbital defense platforms that formed Earth's planetary defense grid. Prior to the development of the Warlock, the power requirements of these weapons were so high that only dedicated stationary platforms could accommodate them, and then only one unit per platform. Installing the cannons aboard the Warlock enabled a ship of the class to destroy multiple Drakh vessels with one shot each at the start of the Drakh War, and another to destroy a Centauri Vorchan-class with a single shot in a possible future battle. The ability to use such powerful weapons allows the Warlock to take ships from advanced races like Minbari with ease. In addition to human technology, an unknown Shadow device is buried somewhere in the Warlock's control systems. The exact purpose and function of this device is unclear. "
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Warlock.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Warlock.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
