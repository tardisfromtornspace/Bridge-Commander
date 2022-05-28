#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 22.02.2009                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'AncientCity'
iconName = 'AncientCity'
longName = 'AncientCity'
shipFile = 'AncientCity' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = App.SPECIES_GALAXY
SubMenu = "Ancient Ships/Bases"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'AncientCity',
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
Foundation.ShipDef.AncientCity = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.AncientCity.dTechs = {
	'Breen Drainer Immune': 0
}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.AncientCity.hasTGLName = 1
# Foundation.ShipDef.AncientCity.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.AncientCity.desc = 'A City-ship is a mobile city developed by the Ancients several million years ago toward the end of their original habitation of the Milky Way galaxy, being the most famous Atlantis. With roughly the same internal space as is found on Manhattan island on Earth, city-ships are among the largest vessels ever developed. All known City-ships are capable of planetary landing. Their hulls are not airtight, requiring the use of a shield to maintain atmosphere. As they are typically powered by three Zero Point Modules, the shields are exceptionally powerful, withstanding years of constant enemy fire, though probably as a result of this, the hull itself is quite fragile. City-ships are inherently buoyant, capable of floating on the surface of a large body of water without any apparent technological aid; they can also rest on the bottom of an ocean, though again the shield is needed to prevent flooding. Some City-ships, such as Atlantis, contain their own Stargates, located near the top of the central tower so that it may be easily accessed by Puddle Jumpers. On some City-ships, however, this location instead houses the Control chair, which in Atlantis is located in another tower altogether. City-ships carry a large number of Drone weapons, which are apparently their only armament. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.AncientCity.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AncientCity.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
