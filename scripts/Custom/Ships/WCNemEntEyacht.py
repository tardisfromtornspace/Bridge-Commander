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
abbrev = 'WCNemEntEyacht'
iconName = 'sovereignyacht'
longName = 'Nem 1701-E Captains Yacht'
shipFile = 'WCNemEntEyacht' 
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
	'modName': 'WCNemEntEyacht',
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
Foundation.ShipDef.WCNemEntEyacht = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.WCNemEntEyacht.fMaxWarp = 9.0
Foundation.ShipDef.WCNemEntEyacht.sBridge = 'Type11Bridge'
Foundation.ShipDef.WCNemEntEyacht.dTechs = {
	'Breen Drainer Immune': 1,
	'Regenerative Shields': 10,
	'Fed Ablative Armor': { "Plates": ["Aft Ablative Armor", "Engineering Ablative Armor", "Top Ablative Armor", "Forward Ablative Armor"]
}}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.WCNemEntEyacht.hasTGLName = 1
Foundation.ShipDef.WCNemEntEyacht.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.WCNemEntEyacht.desc = 'WileyCoyote Nemesis Enterprise E Captains Yacht'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.WCNemEntEyacht.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCNemEntEyacht.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
