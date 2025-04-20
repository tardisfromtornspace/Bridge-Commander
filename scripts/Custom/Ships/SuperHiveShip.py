#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 20/02/2008                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'SuperHiveShip'
iconName = 'SuperHiveShip'
longName = 'SuperHive Ship'
shipFile = 'SuperHiveShip' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
species = App.SPECIES_SOVEREIGN
SubMenu = "Wraith Ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'SuperHiveShip',
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
Foundation.ShipDef.SuperHiveShip = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.SuperHiveShip.fTorpedoID = "Not-Target"
# Wraith do not have shields used as actual shields. At most only used for forcefields to keep things in. This serves as an addendum to possibly add a tech later to prevent transporting.
Foundation.ShipDef.SuperHiveShip.dTechs = {
	'Automated Destroyed System Repair': {"Time": 120.0},
	'Breen Drainer Immune': 1,
	'Fed Ablative Armor': { "Plates": ["Regenerative Armor"]},
	"Multivectral Shields": 100,
	'SG Shields': { "RaceShieldTech": "Wraith", "Wraith Dampening" : 0.5 }
}

Foundation.ShipDef.SuperHiveShip.fMaxWarp = 7.9
Foundation.ShipDef.SuperHiveShip.fCruiseWarp = 7.9
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.SuperHiveShip.hasTGLName = 1
# Foundation.ShipDef.SuperHiveShip.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.SuperHiveShip.desc = 'The Super-Hive is a Wraith hive ship that was modified to draw energy from Zero Point Modules. With the abundance of new energy, the Hive had increased incredibly in size and power: their weapons are orders of magnitude stronger (enough to deplete an Ancient-City shield in minutes), the hyperdrive is much more efficient and the hull of the Hive both heals itself much faster and can absorb punishment on the same order as the most advanced shield technology used by the Tau´ri, making the hull nearly impenetrable even to Asgard plasma beams. Also it could withstand Ancient Drone weapons.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.SuperHiveShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SuperHiveShip.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
