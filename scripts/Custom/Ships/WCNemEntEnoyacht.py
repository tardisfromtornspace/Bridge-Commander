from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 9/08/11                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'WCNemEntEnoyacht'
iconName = 'Sovereign'
longName = 'Nem 1701-E No Yacht'
shipFile = 'WCNemEntEnoyacht' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'WCNemEntEnoyacht',
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
Foundation.ShipDef.WCNemEntEnoyacht = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.WCNemEntEnoyacht.sBridge = 'SovereignBridge'
Foundation.ShipDef.WCNemEntEnoyacht.fMaxWarp = 9.99
Foundation.ShipDef.WCNemEntEnoyacht.dTechs = {
	'Breen Drainer Immune': 1,
	'Regenerative Shields': 100,
	'Multivectral Shields': 10,
	'Fed Ablative Armor': { "Plates": ["Aft Ablative Armor", "Engineering Ablative Armor", "Top Ablative Armor", "Forward Ablative Armor"]
}}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.WCNemEntEnoyacht.hasTGLName = 1
Foundation.ShipDef.WCNemEntEnoyacht.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.WCNemEntEnoyacht.desc = 'WileyCoyote Nemesis Enterprise E'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.WCNemEntEnoyacht.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCNemEntEnoyacht.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
