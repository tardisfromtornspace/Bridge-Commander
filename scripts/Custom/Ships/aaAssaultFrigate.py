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
abbrev = 'aaAssaultFrigate'
iconName = 'aaAssaultFrigate'
longName = 'Assault Frigate'
shipFile = 'aaAssaultFrigate' 
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
	'modName': 'aaAssaultFrigate',
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
Foundation.ShipDef.aaAssaultFrigate = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaAssaultFrigate.hasTGLName = 1
# Foundation.ShipDef.aaAssaultFrigate.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaAssaultFrigate.desc = 'As the Rebel Alliance began to acquire Galactic Republic era Rendili StarDrive Dreadnaught class starships, it found the required 16,000-being crew to be difficult to manage and procure, yet they were in desperate need of warships. After equipping Dreadnaughts with droids and automated systems to reduce the crew requirement to 5,000 beings, thus rendering the ships usable, Rebel engineers began modifying Dreadnaughts to allow for greater speeds and efficiency while retaining the original weapons systems. Most of the internal structure was exposed to space, while a dorsal and ventral fin provided added maneuverability. These modifications removed the internal docking capacity of the Dreadnaught-class, but the ships were equipped with 20 umbilical docking fixtures like those on the EF76 Nebulon-B escort frigate. Unlike the Nebulon escort frigate however, these docking fixtures could not carry other ships through hyperspace. In addition, the assault frigate carried a modified assault shuttle on its back, which was secured in a manner that allowed it to be carried in hyperspace. The assault frigate had a larger number of weapon emplacements than the original Dreadnaught, but the turbolasers had a shorter range and slower fire rate due to the increased demand on the main power system. The removal of large quantities of hull plating reduced the ship´s durability, but slightly stronger shields partially compensated for this. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaAssaultFrigate.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaAssaultFrigate.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
