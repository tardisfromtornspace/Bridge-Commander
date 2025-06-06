#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 14/01/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'UpgradedHatak'
iconName = 'HatakRefit'
longName = 'Ha`tak (Upgrade)'
shipFile = 'UpgradedHatak' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 780
SubMenu = ["Goa'uld Ships/Bases", "Motherships"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'UpgradedHatak',
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
Foundation.ShipDef.UpgradedHatak = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.UpgradedHatak.dTechs = {
	'SG Shields': { "RaceShieldTech": "Anubis Go'auld" }
}

Foundation.ShipDef.UpgradedHatak.fMaxWarp = 2.35
Foundation.ShipDef.UpgradedHatak.fCruiseWarp = 2.25
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.UpgradedHatak.hasTGLName = 1
Foundation.ShipDef.UpgradedHatak.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.UpgradedHatak.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.UpgradedHatak.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.UpgradedHatak.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
