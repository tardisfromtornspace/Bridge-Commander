#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 09/03/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'HaririrHatak'
iconName = 'HaririrHatak'
longName = 'Haririr Ha`tak'
shipFile = 'HaririrHatak' 
menuGroup = "Non canon X-Overs"
playerMenuGroup = "Non canon X-Overs"
species = App.SPECIES_GALAXY
SubMenu = "Goa'uld Ships/Bases"
SubSubMenu = "Motherships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'HaririrHatak',
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
Foundation.ShipDef.HaririrHatak = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.HaririrHatak.hasTGLName = 1
#Foundation.ShipDef.HaririrHatak.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.HaririrHatak.desc = "This Ha'tak was the heavily upgraded version done by the Goa'uld System Lord controlled by Harry Potter, Pelops, also known as Lord Haririr. This ship possess several upgrades and redundant systems, as well as a cloaking device, and it's capable of destroying 3 enemy standard Ha'taks at once before exploding. Lately, Lord Haririr added magical defenses and other techno-magic upgrades, making this ship very hard to kill, powerful enough to even theoretically give an Asgard Beliskner problems in a 1vs1 engagement."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.HaririrHatak.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HaririrHatak.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
