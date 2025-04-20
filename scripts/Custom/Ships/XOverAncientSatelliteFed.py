#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 06/04/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'XOverAncientSatelliteFed'
iconName = 'AncientSatellite'
longName = 'UEC LGPS'
shipFile = 'XOverAncientSatelliteFed' 
menuGroup = 'Non canon X-Overs'
playerMenuGroup = 'Non canon X-Overs'
species = 772
SubMenu = "SG-ST UEC"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'AncientSatellite',
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
Foundation.ShipDef.XOverAncientSatelliteFed = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.XOverAncientSatelliteFed.fMaxWarp = 2.03
Foundation.ShipDef.XOverAncientSatelliteFed.fCruiseWarp = 1.1
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.XOverAncientSatelliteFed.hasTGLName = 1
#Foundation.ShipDef.XOverAncientSatelliteFed.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.XOverAncientSatelliteFed.desc = "The United Earth Alliance deemed necessary a repair and upgrade of the original Lantean Defence Sateelites over Lantea, equpping them with Federation shielding and Romulan cloaking devices. Later thousands of those were deployed in the Wraith and Ori wars."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.XOverAncientSatelliteFed.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.XOverAncientSatelliteFed.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
