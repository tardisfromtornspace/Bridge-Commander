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
abbrev = 'EAStealthStarfuryNoEscapePod'
iconName = 'EAStealthStarfuryNoEscapePod'
longName = 'Stealth Starfury (no pod)'
shipFile = 'EAStealthStarfuryNoEscapePod' 
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
	'modName': 'EAStealthStarfuryNoEscapePod',
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
Foundation.ShipDef.EAStealthStarfuryNoEscapePod = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.EAStealthStarfuryNoEscapePod.hasTGLName = 1
# Foundation.ShipDef.EAStealthStarfuryNoEscapePod.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.EAStealthStarfuryNoEscapePod.desc = "Derived mainly from the SA-23E Mitchell-Hyundyne Starfury, the Stealth Starfury is far more rare and very expensive to produce. Outfitted as a fast interceptor and featuring some of Earthforce's most advanced stealth components, information on this model of Starfury is not widely distributed by Earthforce. The Psi Corps maintained a squadron of these fighters called 'Black Omega' and was formed under the supervision of the Psi Cop Alfred Bester."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.EAStealthStarfuryNoEscapePod.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EAStealthStarfuryNoEscapePod.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
