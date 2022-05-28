#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 20.08.2002                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = "TIEd"
iconName = 'tiedrone'
longName = 'TIE Drone'
shipFile = "TIEd" 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
SubMenu = "Galactic Empire"
SubSubMenu = "Fighters"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'TIEd',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'Automated Starfighter, Unplayable.'
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.TIEd = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.TIEd.hasTGLName = 1
# Foundation.ShipDef.TIEd.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.TIEd.desc = "SFS TIE/d Automated Drone Fighter. Manufactured by World Devastaors, a pilotless TIE Fighter that can be updated to new tactics, but still gets outwitted by normal pilots. 6.1 M"
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.TIEd.RegisterQBShipMenu(menuGroup)
#if playerMenuGroup:     Foundation.ShipDef.TIEd.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
