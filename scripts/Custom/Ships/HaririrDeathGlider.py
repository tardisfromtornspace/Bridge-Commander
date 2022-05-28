#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 14/03/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'HaririrDeathGlider'
iconName = 'DeathGlider'
longName = 'Haririr Death Glider'
shipFile = 'HaririrDeathGlider' 
menuGroup = "Non canon X-Overs"
playerMenuGroup = "Non canon X-Overs"
species = App.SPECIES_GALAXY
SubMenu = "Goa'uld Ships/Bases"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'DeathGlider',
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
Foundation.ShipDef.HaririrDeathGlider = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.HaririrDeathGlider.hasTGLName = 1
#Foundation.ShipDef.HaririrDeathGlider.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.HaririrDeathGlider.desc = "This Death Gliders have been updated by Lord Haririr to possess shielding, in order to have more efficiendy in battle and to reduce military losses"
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.HaririrDeathGlider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.HaririrDeathGlider.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
