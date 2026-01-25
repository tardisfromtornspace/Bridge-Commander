import Foundation
import App

abbrev = 'ZZMirakWeap'
iconName = 'ZZMirakWeap'
longName = 'Mirak Super Weapon'
shipFile = 'ZZMirakWeap' 
menuGroup = 'Kzinti Ships'
playerMenuGroup = 'Kzinti Ships'
species = App.SPECIES_GALAXY

credits = {
	'modName': 'ZZMirakWeap',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}


#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.ZZMirakWeap = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.ZZMirakWeap.hasTGLName = 1
# Foundation.ShipDef.ZZMirakWeap.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.ZZMirakWeap.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
#if menuGroup:           Foundation.ShipDef.ZZMirakWeap.RegisterQBShipMenu(menuGroup)
#if playerMenuGroup:     Foundation.ShipDef.ZZMirakWeap.RegisterQBPlayerShipMenu(playerMenuGroup)

#if Foundation.shipList._keyList.has_key(longName):
#     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
#     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
