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
abbrev = 'aaBulkFreighter'
iconName = 'aaBulkFreighter'
longName = 'Bulk Freighter'
shipFile = 'aaBulkFreighter' 
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
	'modName': 'aaBulkFreighter',
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
Foundation.ShipDef.aaBulkFreighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile,"SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaBulkFreighter.hasTGLName = 1
# Foundation.ShipDef.aaBulkFreighter.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaBulkFreighter.desc = 'The BFF-1 Bulk Freighter is all and nothing more than what its name states with a design that amounts to a decent hyperdrive engine surrounded by lots of cargo containers. One advantage of this type of transport is that despite its significant size, the BFF-1 has the ability to land. However, it flies rather sluggishly while travelling at sublight speeds, requiring a pilot with a steady, yet gentle hand. Besides cargo of all sorts, the manufacturers managed to make later versions acceptable for passenger transport, making room for about a hundred people. Another important attribute is the BFF-1´s tractor beam. This is very handy if there is even more to haul, but it also helps multiple ships to stay in formation which is very important because these ships tend to travel in convoy. A significant flaw in the BFF-1 Bulk Freighter is the fact that it has no armament, which makes it an easy target for pirates. Its thick hull, boasting good deflectors and ionic shielding as well as the safety in numbers, are the only things that can make sure this ship gets the goods where they are needed.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaBulkFreighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaBulkFreighter.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
