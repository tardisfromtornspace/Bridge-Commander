#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 26/06/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BelisknerRefit'
iconName = 'BelisknerRefit'
longName = 'Mothership (Refit)'
shipFile = 'BelisknerRefit' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = 768
SubMenu = "Asgard Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BelisknerRefit',
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
Foundation.ShipDef.BelisknerRefit = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.BelisknerRefit.dTechs = {
	'SG Shields': { "RaceShieldTech": "Asgard", "FacetFactor" : 2 },
	"TachyonBeam": { "Immune": -1 }
}

Foundation.ShipDef.BelisknerRefit.fMaxWarp = 9.0
Foundation.ShipDef.BelisknerRefit.fCruiseWarp = 8.0

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.BelisknerRefit.hasTGLName = 1
Foundation.ShipDef.BelisknerRefit.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.BelisknerRefit.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BelisknerRefit.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BelisknerRefit.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
