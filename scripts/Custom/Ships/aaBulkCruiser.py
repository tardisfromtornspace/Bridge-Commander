#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 3/10/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'aaBulkCruiser'
iconName = 'aaBulkCruiser'
longName = 'Bulk Cruiser'
shipFile = 'aaBulkCruiser' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
species = App.SPECIES_GALAXY
SubMenu = "Galactic Empire"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'aaBulkCruiser',
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
Foundation.ShipDef.aaBulkCruiser = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile,"SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaBulkCruiser.hasTGLName = 1
# Foundation.ShipDef.aaBulkCruiser.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaBulkCruiser.desc = 'A bulk cruiser was a capital ship design that combined attributes of both warships and cargo haulers. They saw service in both the Sith Empire of the Great Galactic War, as well as the Galactic Empire and Alliance navies of the Galactic Civil War. Several different models existed, like the Neutron Star and Battle Horn classes, but the overall design was relatively the same, with an armament of thirty quad laser cannons (ten forward, ten to port, and ten to starboard) and two forward tractor beam projectors. The bulk cruiser´s large and bulbous forward section contained a medium sized hangar for up to one squadron of starfighters. The Empire and various corporations kept bulk cruisers as patrol vessels, guarding systems where important corporate assets were to be found. In addition, these ships were used to track down Rebel ships and combat pirate attacks on convoys.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaBulkCruiser.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaBulkCruiser.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
