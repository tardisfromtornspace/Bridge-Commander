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
abbrev = 'DSC304ApolloRefit'
iconName = 'DSC304'
longName = 'Apollo (Refit)'
shipFile = 'DSC304ApolloRefit' 
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
	'modName': 'DSC304ApolloRefit',
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
Foundation.ShipDef.DSC304ApolloRefit = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.DSC304ApolloRefit.dTechs = {
	"AutoTargeting": { "Pulse": [3, 1] },
	"SG Asgard Beams Weapon": {"HullDmgMultiplier": 1.0, "ShieldDmgMultiplier": 1.0},
	'SG Shields': { "RaceShieldTech": "Asgard", "RaceHullTech": "Tau'ri" }
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.DSC304ApolloRefit.hasTGLName = 1
#Foundation.ShipDef.DSC304ApolloRefit.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.DSC304ApolloRefit.desc = "Description: The Apollo, as well as the other BC-304s, received a small refit to equip better shields and Asgard Beam weapons before the time of the Battle of Asuras. After the Asurans started attacking human worlds as a tactic in their war with the Wraith, the Daedalus and the Apollo are both sent to Atlantis to use the tracking system Atlantis has recently received capable of tracking all of the Asuran Aurora-class battleships and their new Asgard plasma beam weapons to stop the Asurans once and for all.\n\nWeapons: 32 Rail Guns, 22 Missile Batteries (carrying 100 Mark 8 nuclear warheads)), 12 Energy Beam Weapons.\n\nShield Rating: 35,000 Asgard Shielding\n\nHull Rating: 17,500\n\nTactics:"
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.DSC304ApolloRefit.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DSC304ApolloRefit.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
