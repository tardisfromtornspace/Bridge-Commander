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
abbrev = 'DSC304OdysseyRefit'
iconName = 'DSC304'
longName = 'Odyssey (Refit)'
shipFile = 'DSC304OdysseyRefit' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 754
SubMenu = ["Human (Tau'ri) Ships", "DSC-304"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'DSC304OdysseyRefit',
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
Foundation.ShipDef.DSC304OdysseyRefit = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
# Foundation.ShipDef.DSC304OdysseyRefit.hasTGLName = 1
# Foundation.ShipDef.DSC304OdysseyRefit.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.DSC304OdysseyRefit.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.DSC304OdysseyRefit.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DSC304OdysseyRefit.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
