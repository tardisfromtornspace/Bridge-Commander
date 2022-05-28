#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 6/19/02                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BorgDiamond'
iconName = 'BorgDiamond'
longName = 'BorgDiamond'
shipFile = 'BorgDiamond' 
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BorgDiamond',
	'author': 'Lord Delekhan',
	'version': '1.0',
	'sources': [ 'http://www.ldrealms.org/bc' ],
	'comments': 'The Diamond is one of my favorite Borg ships, and it has been fairly well neglected till now.'
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.BorgDiamond = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.BorgDiamond.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.BorgDiamond.fMaxWarp = 9.999
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.BorgDiamond.hasTGLName = 1
Foundation.ShipDef.BorgDiamond.hasTGLDesc = 1
Foundation.ShipDef.BorgDiamond.fMaxWarp = 9.999

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.BorgDiamond.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BorgDiamond.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BorgDiamond.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
