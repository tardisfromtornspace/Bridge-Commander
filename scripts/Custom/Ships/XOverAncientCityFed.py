#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 22.02.2009                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'XOverAncientCityFed'
iconName = 'AncientCity'
longName = 'UEC Atlantis'
shipFile = 'XOverAncientCityFed' 
menuGroup = "Non canon X-Overs"
playerMenuGroup = "Non canon X-Overs"
species = App.SPECIES_GALAXY
SubMenu = "SG-ST UEC"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'AncientCityFed',
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
Foundation.ShipDef.XOverAncientCityFed = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.XOverAncientCityFed.dTechs = {
	'Breen Drainer Immune': 0
}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.XOverAncientCityFed.hasTGLName = 1
# Foundation.ShipDef.XOverAncientCityFed.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.XOverAncientCityFed.desc = "This is an slightly refitted version of Atlantis by a collaboration between Ayiana and the United Earth Alliance, incorporating some Federation and Tollan technology, adding several phased torpedo launchers and upgrading the drones to be phased too, allowing an even better protection for the ship. Later the ZPM modules were replaced by the new 100-more-powerful-than-ZPMs Arcturus Zero Point Modules (AZPM for short), increasing considerably the power and shield output."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.XOverAncientCityFed.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.XOverAncientCityFed.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
