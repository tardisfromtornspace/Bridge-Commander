#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 5/27/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'aaMaurauderCorvette'
iconName = 'aaMarauderCorvette'
longName = 'Maurauder Corvette'
shipFile = 'aaMaurauderCorvette' 
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
	'modName': 'aaMaurauderCorvette',
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
Foundation.ShipDef.aaMaurauderCorvette = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaMaurauderCorvette.hasTGLName = 1
# Foundation.ShipDef.aaMaurauderCorvette.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaMaurauderCorvette.desc = 'Marauder-class corvettes were equipped with eight double turbolasers and three tractor beam projectors, and could optionally support four more turbolasers if a larger power generator was installed. They had space for 12 starfighters, and capacity for 80 troops for use in boarding actions or planetary landings. Their very accurate tractor beams allowed them to capture ships with little collateral damage, and they were sometimes paired with ships equipped with gravity well projectors for this purpose. Some Marauder-class ships were equipped with four diamond-boron missile launchers in place of their heavy turbolasers. Sometimes called a "Pocket cruiser," the Marauder´s sublight speed was faster than a Victory I-class Star Destroyer. Although not powerful enough for engagements against warships such as those used by the Imperial Navy, they were excellent as patrol and interdiction vessels. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaMaurauderCorvette.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaMaurauderCorvette.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
