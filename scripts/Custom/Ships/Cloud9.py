#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 22/10/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Cloud9'
iconName = 'Cloud9'
longName = 'Cloud 9'
shipFile = 'Cloud9' 
menuGroup = 'BSG Ships'
playerMenuGroup = 'BSG Ships'
species = App.SPECIES_GALAXY
SubMenu = "Colonial Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Cloud9',
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
Foundation.ShipDef.Cloud9 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Cloud9.hasTGLName = 1
# Foundation.ShipDef.Cloud9.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Cloud9.desc = 'Cloud 9 was a massive vessel of unusual design that contained a five-star restaurant, theater, casino, several bars, and numerous hotel rooms and luxury suites. Its most notable feature was a huge biodome which contained a pressurized natural habitat nearly a quarter-mile in diameter, which simulated an outdoor park. The dome was mounted to the starboard side of the ship´s main hull by a V shaped pylon structure which supported a spoon-shaped bow that contained the hotel. Behind the hotel section was a separately attached crew module which also contained the ship´s hangar bay, command bridge, engineering, and sub-light/FTL drive engines. Directly under the saucer dome were another set of drive engines. Inside the dome, many varieties of trees and plants from the Twelve Colonies were grown on the grounds and were cared for by a dedicated gardening staff. The dome also contained an artificial lake used for swimming. At the center of the park was a large auditorium structure used for gatherings and festivals. This building was used by Laura Roslin as the meeting place for the new Quorum of Twelve after the Cylon attack on the Colonies. The dome used any natural sunlight that was available, in an attempt to replicate the atmospheric conditions of a planet´s sky. However, Cloud 9 was still a spaceship, and didn´t really live up to the quality of a real planet, as there were some flaws in the design—such as fake terrain used to disguise the machinery as well as the easily noticeable and massive support beams of the sky dome. Despite this, Cloud 9 was judged to be one of the nicer places to live in the colonial fleet. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Cloud9.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Cloud9.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
