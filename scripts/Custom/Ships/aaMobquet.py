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
abbrev = 'aaMobquet'
iconName = 'aaMobquet'
longName = 'Mobquet Transport'
shipFile = 'aaMobquet' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
species = App.SPECIES_GALAXY
SubMenu = "Civilian Craft"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'aaMobquet',
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
Foundation.ShipDef.aaMobquet = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaMobquet.hasTGLName = 1
# Foundation.ShipDef.aaMobquet.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaMobquet.desc = 'The Mobquet Medium Transport, also known as the Mobquet Medium Cargo Hauler, was a transport ship produced by Mobquet Swoops and Speeders. Although one of the slower transports, its slightly reinforced hull and extra space helped increase its popularity. The ship consisted of three modular nodes, that could be modified to serve the need of the owner. The standard design included crew quarters, storage, defensive weapons in front node, speeder racks in the second node and computer units in the third node. It wasn´t hard to install new weapons, increase the passenger capacity or modify the cargo space. Common installed weapons were two fire-linked twin medium laser cannons (which were also retractable) and a concussion missile launcher that was dorsal mounted.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaMobquet.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaMobquet.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
