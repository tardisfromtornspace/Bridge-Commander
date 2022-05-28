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
abbrev = 'Millenium'
iconName = 'Millenium'
longName = 'Millennium Falcon'
shipFile = 'Millenium' 
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
	'modName': 'Millenium',
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
Foundation.ShipDef.Millenium = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Millenium.hasTGLName = 1
# Foundation.ShipDef.Millenium.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Millenium.desc = 'The Millennium Falcon, originally known as YT-1300 492727ZED, was a Corellian YT-1300f light freighter used by the smugglers Han Solo and Chewbacca during the Galactic Civil War. It was previously owned by Lando Calrissian, who lost it to Solo in a game of sabacc. Its aged appearance belied numerous advanced modifications to boost the ship´s speed, weapons and shield, including a hyperdrive engine among the fastest in the entire galaxy, enabling it to outrun Imperial Star Destroyers. It included sensor-proof smuggling compartments, which were used during the rescue of Princess Leia Organa to evade Imperial stormtroopers. Afterwards, the Millennium Falcon saw further action when Solo chose to join the Rebels during the Battle of Yavin, where it was able to sneak up on Darth Vader´s TIE Advanced.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Millenium.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Millenium.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
