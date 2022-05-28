#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 23/10/2003                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Battlestar'
iconName = 'Battlestar'
longName = 'Battlestar Galactica'
shipFile = 'Battlestar' 
menuGroup = 'BSG (TOS) Ships'
playerMenuGroup = 'BSG (TOS) Ships'
SubMenu = "Twelve Colonies of Man"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Battlestar',
	'author': 'MadJohn',
	'version': '0.9',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.Battlestar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Battlestar.dTechs = {
	'Fed Ablative Armor': { "Plates": ["Ablative Armour"]
}}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Battlestar.hasTGLName = 1
# Foundation.ShipDef.Battlestar.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Battlestar.desc = 'Columbia-Class Battlestars represented the heart of the Colonial defense against the armies of the Cylon Empire. They served a three prong role in the defense of humanity, operating as aircraft carrier, battleship and a mobile base of operations. Standard Battlestars carried 75 Starhound class Vipers, 12 Landram ground-troop transports and twelve shuttlecrafts. Following the destruction of the twelve colonies, the Galactica was forced to dramatically increase the number of crew she carried, as well as the number of fighters she could bring onto the battlefield. Galactica now carries a crew of roughly 1000 military personnel, 168 of which are Viper fighter pilots. Galactica, in addition to her original Viper squadrons, Red and Blue, now has two additional Viper squadrons, Silver Spar and Bronze Spar of the Battlestar Pegasus. Galactica is still armed with her standard weapon system, consisting of 32 known Turbo-Lasers, which were powerful enough to destroy fighters, asteroids and their combined power was capable of destroying another vessel; and Fusion Missiles. Main power aboard Colonial Battlestars was provided by a combination of Tylium energizers and advanced Fusion reactors. Its megatron shield uses electromagnetic radiation to disrupt incoming energy weapons, and, by the inverse square law, reduces the weapon´s intensity spreading the energy beam over a wide area.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Battlestar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Battlestar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
