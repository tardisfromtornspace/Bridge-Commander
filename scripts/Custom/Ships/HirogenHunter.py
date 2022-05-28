#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 16/04/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Hunter'
iconName = 'hunter'
longName = 'Hirogen Hunter'
shipFile = 'Hunter' 
menuGroup = 'Hirogen'
playerMenuGroup = 'Hirogen'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #

#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.Hunter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Hunter.hasTGLName = 1
# Foundation.ShipDef.Hunter.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Hunter.desc = 'The Hirogen warship, also known as a Hirogen hunting vessel, was a small, heavily-armed warship used by Hirogen hunters during the 2370s as they hunted throughout the Delta Quadrant. This class of vessel was usually piloted by two Hunters, an Alpha-Hirogen and a Beta-Hirogen. The vessels were equipped with monotanium armor plating, and had dicyclic warp signatures. Inside the vessel was a large room which included the control stations as well as walls of trophies and bladed weapons. Also included was a harness-like construction to hang their prey on while preparing an osteotomy.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Hunter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Hunter.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
