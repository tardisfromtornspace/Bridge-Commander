#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 5/26/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'aaCorevette'
iconName = 'aacorvette'
longName = 'Corellian Corvette'
shipFile = 'aaCorevette' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
species = App.SPECIES_GALAXY
SubMenu = "Rebel Alliance"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'aaCorevette',
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
Foundation.ShipDef.aaCorevette = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaCorevette.hasTGLName = 1
# Foundation.ShipDef.aaCorevette.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaCorevette.desc = 'CR90 corvettes, also known as Alderaan cruisers, Corellian corvettes, or blockade runners, were consular vessels manufactured by the Corellian Engineering Corporation. While the CR90 would see initial use within the late Galactic Republic and Imperial Senate, many vessels would be appropriated by the early rebellion and Rebel Alliance against the First Galactic Empire, despite not being designed as a combat-oriented vessel. Measuring 126.68 meters in length, it featured two dual and four single turbolaser turrets, and had the ability to reach a maximum speed of 950 kph. Capable of carrying an entire diplomatic escort, it had a passenger capacity of hundreds. Although the ships were not built as carriers, three RZ-1 A-wing interceptors could be attached to the docking rings, allowing a small escort to be with it. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaCorevette.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaCorevette.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
