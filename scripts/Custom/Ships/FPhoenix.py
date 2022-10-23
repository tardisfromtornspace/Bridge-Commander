#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 05/25/2013                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'phoenix'
iconName = 'phoenix'
longName = 'Phoenix Warp Ship'
shipFile = 'FPhoenix' 
menuGroup = 'Pre-Fed ships'
playerMenuGroup = 'Pre-Fed ships'
species = App.SPECIES_GALOR
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Phoenix',
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
Foundation.ShipDef.Phoenix = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.Phoenix.fMaxWarp = 1.0
Foundation.ShipDef.Phoenix.fCruiseWarp = 1.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.Phoenix.hasTGLName = 1
#Foundation.ShipDef.Phoenix.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.Phoenix.desc = "The Phoenix warp ship was the first man-made, manned spacecraft to achieve light speed using warp drive that was constructed during the mid-21st century. The Phoenix was remembered as the ship that instigated Earth's First Contact with Vulcans. Built from a missile, it had no defenses or weaponry. It didn't use a dilithium-regulated reaction to propel itself, but a far more inefficient fission reactor that didn't allow any warp factor beyond lightspeed."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Phoenix.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Phoenix.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
