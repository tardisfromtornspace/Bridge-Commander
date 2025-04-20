#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 03/06/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'XOverAlteranWarship'
iconName = 'AncientWarship'
longName = 'UEC Aurora Class'
shipFile = 'XOverAlteranWarship' 
menuGroup = 'Non canon X-Overs'
playerMenuGroup = 'Non canon X-Overs'
species = 773
SubMenu = "SG-ST UEC"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'AncientWarship',
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
Foundation.ShipDef.XOverAlteranWarship = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.XOverAlteranWarship.dTechs = {
	'Breen Drainer Immune': 1,
	'Simulated Point Defence' : { "Distance": 120.0, "InnerDistance": 15.0, "Effectiveness": 1.0, "LimitTurn": 18.0, "LimitSpeed": 50, "LimitDamage": "-48", "Period": 0.2, "MaxNumberTorps": 1, "Torpedo": {"Priority": 1}},
	'SG Shields': { "RaceShieldTech": "Lantian" }
}

Foundation.ShipDef.XOverAlteranWarship.fMaxWarp = 9.5
Foundation.ShipDef.XOverAlteranWarship.fCruiseWarp = 7.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.XOverAlteranWarship.hasTGLName = 1
#Foundation.ShipDef.XOverAlteranWarship.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.XOverAlteranWarship.desc = "Seeing the apparent lack of sense for not installing real offensive pulse weapons, the Aurora-class battleships were refitted to include Destiny Battleship Main Cannons, even if the tech was a bit outdated."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.XOverAlteranWarship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.XOverAlteranWarship.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
