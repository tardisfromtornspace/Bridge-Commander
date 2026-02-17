from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 13.12.2003                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App

from Custom.Autoload.RaceMixedGalaxyQuest import *
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'joke31stOberth'
iconName = 'joke31stOberth'
longName = 'U.S.S. Imahara'
shipFile = 'joke31stOberth' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Oberth V',
	'author': 'Alex SL Gato',
	'version': '1.0',
	'sources': [ '' ],
	'comments': 'Ship Concept By Alex SL Gato'
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.joke31stOberth = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "race": MixedGalaxyQuest })
Foundation.ShipDef.joke31stOberth.sBridge = 'novabridge'
Foundation.ShipDef.joke31stOberth.dTechs = {
#	"AutoTargeting": {"Phaser": [2, 1], "Torpedo": [2, 1]},
	'Breen Drainer Immune': 1,
	'Drainer Immune': 1,
	'Regenerative Shields': 40,
	'Multivectral Shields': 20,
	'ChronitonTorpe Immune': 1,
	"Phased Torpedo Immune": 1,
	"Phase Cloak": 10,
	"Transphasic Torpedo Immune": 1,
	"Reflux Weapon": 1,
	"Inversion Beam": [0.5, 0, 0.5, 1500],
	"Power Drain Beam": [0.5, 0, 0.5, 1500],
	'Fed Ablative Armor': { "Plates": ["Ablative Armour"]}
}
Foundation.ShipDef.joke31stOberth.SubMenu = "31st Century"
Foundation.ShipDef.joke31stOberth.CloakingSFX   = "FutureBattleCloak"
Foundation.ShipDef.joke31stOberth.DeCloakingSFX = "FutureBattleDecloak"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.joke31stOberth.hasTGLName = 1
#Foundation.ShipDef.joke31stOberth.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.joke31stOberth.desc = "The Imahara class is an alternate timeline, small Federation starship class heavily inspired by the Oberth class, used primarily by Starfleet and civilian scientists alike, as a scout and science vessel, from the late 30th to the late 32nd century; and produced on Nivar."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.joke31stOberth.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.joke31stOberth.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
