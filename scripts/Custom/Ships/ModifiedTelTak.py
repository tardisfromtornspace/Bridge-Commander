#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 01/06/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'ModifiedTelTak'
iconName = 'TelTak'
longName = 'Modified Tel`Tak'
shipFile = 'ModifiedTelTak' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 793
SubMenu = ["Goa'uld Ships/Bases", "Cargo Ships"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'ModifiedTelTak',
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
Foundation.ShipDef.ModifiedTelTak = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.ModifiedTelTak.dTechs = {
	'SG Shields': { "RaceShieldTech": "Uprated Goa'uld" }
}
Foundation.ShipDef.ModifiedTelTak.fMaxWarp = 3.25
Foundation.ShipDef.ModifiedTelTak.fCruiseWarp = 3.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.ModifiedTelTak.hasTGLName = 1
Foundation.ShipDef.ModifiedTelTak.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.ModifiedTelTak.desc = 'No Description Available'
#                                                                                                                                              #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.ModifiedTelTak.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ModifiedTelTak.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
