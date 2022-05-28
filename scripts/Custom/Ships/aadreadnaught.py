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
abbrev = 'aaDreadnaught'
iconName = 'aaDreadnaught'
longName = 'Dreadnaught'
shipFile = 'aaDreadnaught' 
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
	'modName': 'aaDreadnaught',
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
Foundation.ShipDef.aaDreadnaught = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaDreadnaught.hasTGLName = 1
# Foundation.ShipDef.aaDreadnaught.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaDreadnaught.desc = 'The Dreadnaught-class heavy cruiser, or simply the Dreadnaught, was a type of capital ship built for planetary occupation and space combat used by the Galactic Republic, Galactic Empire, New Republic, local governments, and various other organizations. It was one of the most ubiquitous ship designs in all of the galaxy. Weapon systems included twenty quad laser cannons (six bow, seven port, seven starboard), ten turbolaser cannons (five port, five starboard and mounted in blisters), and ten laser cannons (five bow, five stern). Some ships were later customized to feature a warhead launcher for anti-starfighter defense. Deflector shield projectors were also located inside some of the blisters flanking the hull, and the primary and secondary sensor transceivers were located towards the stern of the vessel, on the dorsal and ventral sides, similar to those on CR90 corvettes. While technologically advanced at the time of its construction, the Dreadnaught-class lacked in sublight and hyperspace speeds (a Class 4 rating), suffered computer failures, and could not compete with comparable designs in terms of firepower and shielding.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaDreadnaught.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaDreadnaught.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
