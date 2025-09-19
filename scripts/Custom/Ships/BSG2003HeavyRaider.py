#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created manually                                                                   #
#  Date: 19/09/2025                                                                   #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG2003HeavyRaider'
iconName = 'HeavyRaider'
longName = 'Heavy Raider'
shipFile = 'BSG2003HeavyRaider' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
SubMenu = ["Cylon Ships", "Raiders"]
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003HeavyRaider',
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
Foundation.ShipDef.BSG2003HeavyRaider = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG2003HeavyRaider.dTechs = {
	"AutoTargeting": { "Pulse": [2, 1] },
	'Simulated Point Defence' : { "Distance": 15.0, "InnerDistance": 2.0, "Effectiveness": 0.45, "LimitTurn": -0.8, "LimitSpeed": 35, "LimitDamage": "-90", "Period": 2.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Drive 1"], "Core": ["Tylium Reactor"], "Cooldown Time": 13 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003HeavyRaider.fMaxWarp = 6.5
Foundation.ShipDef.BSG2003HeavyRaider.fCruiseWarp = 6.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003HeavyRaider.hasTGLName = 1
# Foundation.ShipDef.BSG2003HeavyRaider.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003HeavyRaider.desc = "The Cylon Heavy Raider is roughly equivalent to the Colonial Raptor. However, the Heavy Raider is armed with six high caliber KEWs designed for close support roles. The reinforced hull of the Heavy Raider also makes it suited for ship boarding actions, as well as the deployment of Centurions and munitions planetside. Certain variants may include a cockpit for a humanoid Cylon model to pilot the vessel. However, Heavy Raiders are primarily piloted by veteran Cylon Raider minds."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003HeavyRaider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003HeavyRaider.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
