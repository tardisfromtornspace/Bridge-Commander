#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 8/7/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'DiamondsArmoredSC4'
iconName = 'ArmoredSC4'
longName = 'Endgame Armored SC4'
shipFile = 'DiamondsArmoredSC4' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
SubMenu = "Shuttles"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'ArmoredSC4',
	'author': 'MRJOHN',
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
Foundation.ShipDef.DiamondsArmoredSC4 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.DiamondsArmoredSC4.dTechs = {
#'Ablative Armour': 295000,
'Adv Armor Tech': 1,
'Breen Drainer Immune': 1,
'Multivectral Shields': 12,
"Phase Cloak": 10,
"Regenerative Shields": 40,
"Transphasic Torpedo Immune": 1
}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.DiamondsArmoredSC4.hasTGLName = 1
# Foundation.ShipDef.DiamondsArmoredSC4.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.DiamondsArmoredSC4.desc = "SC-4 was the designation of a Starfleet Command shuttlecraft during the early 25th century.\nThe shuttle was capable of achieving a speed of at least warp 6 and was equipped with deflector shields. It was also equipped with several advanced anti-Borg technologies developed by the crew of USS Voyager between 2394 and 2404, including stealth technology, an ablative armor generator, transphasic torpedoes, as well as a neural interface and synaptic transceiver.\nThis shuttle was prepped at Oakland Shipyard and arranged for use by Reginald Barclay for Admiral Kathryn Janeway in an alternate 2404 in order to alter history.\nAlong with the anti-Borg technology, she equipped the shuttle with a chrono deflector stolen from Korath in 2404. The shuttle was chased and fired on by his forces, but escaped only to be intercepted by the USS Rhode Island. Its captain, Harry Kim, allowed Janeway to leave and rescued her from Korath's forces when they caught up with them."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.DiamondsArmoredSC4.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DiamondsArmoredSC4.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
