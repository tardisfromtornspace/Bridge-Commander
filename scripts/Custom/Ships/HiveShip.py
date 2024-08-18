#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 20/02/2008                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'HiveShip'
iconName = 'HiveShip'
longName = 'Hive Ship'
shipFile = 'HiveShip' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = App.SPECIES_SHUTTLE
SubMenu = "Wraith Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'HiveShip',
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
Foundation.ShipDef.HiveShip = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     # 
Foundation.ShipDef.HiveShip.fTorpedoID = "Not-Target"                               # 
# Wraith do not have shields used as actual shields. At most only used for forcefields to keep things in. This serves as an addendum to possibly add a tech later to prevent transporting.
Foundation.ShipDef.HiveShip.dTechs = {
	'SG Shields': { "RaceShieldTech": "Wraith" }
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.HiveShip.hasTGLName = 1
# Foundation.ShipDef.HiveShip.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.HiveShip.desc = 'Hive ships are the main component of the Wraith fleet and the centerpiece of their entire society. Hive ships function in a role similar to that of Ancient City-ships and Traveler generational ships. A Hive ship is a massive Wraith mothership capable of carrying thousands of Wraith along with their Wraith Dart fighters. Large parts of their internal structure are used to house organic cocoons in which Humans may be stored for later feeding. There are a number of corridors within the large vessel with a fine mist covering the floor. Despite their size, Hive ships are capable of entering a planet´s atmosphere and landing. They are even capable of surviving for countless centuries in such conditions to the point where vegetation and the planet´s environment can grow around them. This did not affect the ship as it was capable of achieving space flight and combat, suffering little, if any, adverse affects. Hive ships are also capable of surviving uncontrolled reentry into a planet´s atmosphere, suffering no visible damage from the friction. The hulls of Hive ships are composed of living, and growing, organic matter through the use of a unique type of biotechnology capable of growing at a rapid rate. This has afforded the Wraith Hive ship a number of advantages such as hull regeneration, providing them considerable protection in battles despite the fact that they lack any true energy shielding system. However, these organic hulls have an effect on their capacity to enter into hyperspace for extended periods of time as the Hive requires moments of rest to heal the hull damage caused by hyperspace radiation. As Hive ships posses no true energy shield, weapons are considerably more effective against them. This is particularly the case with Asgard plasma beam weapons, which are able to completely destroy a Hive ship in just a handful of shots. Drone weapons are also capable of inflicting mass amounts of damage, being able to destroy a Hive in a single, massive, salvo.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.HiveShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HiveShip.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
