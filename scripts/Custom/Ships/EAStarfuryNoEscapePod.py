#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 18/04/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'EAStarfuryNoEscapePod'
iconName = 'EAStarfuryNoEscapePod'
longName = 'Starfury (no pod)'
shipFile = 'EAStarfuryNoEscapePod' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_SHUTTLE
SubMenu = "Earth Alliance"
SubSubMenu = "Fighters"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'EAStarfuryNoEscapePod',
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
Foundation.ShipDef.EAStarfuryNoEscapePod = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.EAStarfuryNoEscapePod.hasTGLName = 1
# Foundation.ShipDef.EAStarfuryNoEscapePod.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.EAStarfuryNoEscapePod.desc = 'The Mk2 SA-23E Mitchell-Hyundyne Starfury is the Earthforce standard non-atmospheric deep space interdiction and recon fighter. It first entered service in the 2240s. By 2260 Earthforce began to supplement this model with the atmospheric capable Mk3 Thunderbolt, though the Mk2s would remain in active service for at least the next four decades. Mk2 Starfuries are highly maneuverable, unmatched among the younger races (even the Minbari acknowledging that in this area they are outclassed), with the ability to spin 180 degrees in under a second. They are also the only fighter craft capable of flying backward at nearly the same speed they can fly forward.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.EAStarfuryNoEscapePod.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EAStarfuryNoEscapePod.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
