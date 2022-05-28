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
abbrev = 'naboofighter'
iconName = 'naboofighter'
longName = 'Naboo Fighter'
shipFile = 'naboofighter' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
SubMenu = "Old Republic"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'naboofighter',
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
Foundation.ShipDef.naboofighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.naboofighter.hasTGLName = 1
# Foundation.ShipDef.naboofighter.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.naboofighter.desc = "The Naboo N-1 starfighter, also called the Naboo starfighter, was a single-seat patrol craft developed by the Theed Palace Space Vessel Engineering Corps and used by the Royal Naboo Security Forces for duties such as defense, patrol, and escorting. The craft carried two J-type engines and a Nubian Monarc C-4 hyperdrive engine, and had a single on-board astromech droid which was mounted from the bottom of the craft. It featured an autopilot system and shielding, along with offensive weaponry that consisted of two blaster cannons and proton torpedo launchers. It could attain a maximum speed of 1,100 kph and was eleven meters in length. The ships central rat-tail acted as a power charger collector, and received energy from onboard generators when it was not in use. The ships two outer finials served as heat sinks for the engines. They were used during the Trade Federation invasion of the planet. During the invasion, the pilots of Bravo Flight flew the N-1 during the final assault against the Droid Control Ship the Saak'ak. Young Anakin Skywalker fired his torpedoes into its main reactor, effectively destroying it from within. They later joined in the celebration on the planet below, flying overhead Naboo's capital of Theed."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.naboofighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.naboofighter.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
