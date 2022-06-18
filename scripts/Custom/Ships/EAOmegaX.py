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
abbrev = 'EAOmegaX'
iconName = 'EAOmegaX'
longName = "Shadow Omega-X"
shipFile = 'EAOmegaX' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_GALAXY
SubMenu = "Earth Alliance"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'EAOmegaX',
	'author': 'Madjohn',
	'version': '0.1beta',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.EAOmegaX = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.EAOmegaX.dTechs = {
	'Defense Grid': 150,
        'Shadow Dispersive Hull': 1
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.EAOmegaX.hasTGLName = 1
# Foundation.ShipDef.EAOmegaX.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.EAOmegaX.desc = "The Advanced Omega-X class destroyer was an experimental class of Earthforce starship incorporating Shadow technology adapted from vessels previously excavated on Mars and Ganymede. Based on the existing Omega-class destroyer, the Advanced Destroyers retained much of the Omega's basic configuration including the aft engines, rotating section and forward launch/docking bay. In addition to an upgraded weapons system, there was augmented semi-organic hull technology, in the shape of a number of spine-like structures on both the forward and aft hull and an organic skin characteristic of Shadow Vessels. Developed in secret, a small fleet of Advanced Destroyers, with at least six units, was deployed in late 2261 toward the end of the Earth Alliance Civil War. Under the command of Captain J. Thompson, the fleet was sent to ambush the renegade fleet with the intent of wiping out the Earth ships that had defected to the Resistance. With the fleet crippled and Sheridan captured on Mars, this would have left the advancing fleet made up of mostly alien ships and enabled EA President Clark to claim the campaign was an alien driven invasion and not an Earthforce insurrection."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.EAOmegaX.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EAOmegaX.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
