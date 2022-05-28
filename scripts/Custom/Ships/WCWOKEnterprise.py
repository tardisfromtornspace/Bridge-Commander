#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by WileyCoyote                                                       #
#  Date: 7/15/09                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'WCWOKEnterprise'
iconName = 'WCWOKEnterprise'
longName = 'WOK Enterprise'
shipFile = 'WCWOKEnterprise' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "WC TMP Pack"
SubSubMenu = "WC Enterprise Refit"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'WCWOKEnterprise',
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
Foundation.ShipDef.WCWOKEnterprise = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.WCWOKEnterprise.hasTGLName = 1
# Foundation.ShipDef.WCWOKEnterprise.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.WCWOKEnterprise.desc = "USS Enterprise NCC-1701"
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.WCWOKEnterprise.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCWOKEnterprise.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
