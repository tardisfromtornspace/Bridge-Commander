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
abbrev = 'aaCorgun'
iconName = 'aaCorgun'
longName = 'Corellian Gunship'
shipFile = 'aaCorgun' 
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
	'modName': 'aaCorgun',
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
Foundation.ShipDef.aaCorgun = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaCorgun.hasTGLName = 1
# Foundation.ShipDef.aaCorgun.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaCorgun.desc = 'The Corellian Gunship was one of the few dedicated warship designs produced by the Corellian Engineering Corporation. Unlike its cousin, the CR90 corvette, the gunship had minimal cargo space and almost no space for passengers or troops. These small ships were designed to be only fast and deadly. Engines consumed nearly half of the gunship´s interior space. What little room was left was used for shield generators and weapons. Armed with eight double turbolaser cannons, four concussion missile tubes, and six quad laser cannons, the Corellian gunship was effective against both larger capital ships as well as starfighters. These ships were 120 meters long. Each one carried a crew of 45, along with 46 gunners. They were equipped with Class 2 hyperdrives. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaCorgun.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaCorgun.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
