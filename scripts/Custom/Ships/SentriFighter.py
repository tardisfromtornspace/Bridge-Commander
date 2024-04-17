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
abbrev = 'SentriFighter'
iconName = 'Sentri'
longName = 'Sentri Fighter'
shipFile = 'SentriFighter' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = 787
SubMenu = "Centauri Republic"
SubSubMenu = "Fighters"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Sentri Fighter',
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
Foundation.ShipDef.SentriFighter = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
# Foundation.ShipDef.SentriFighter.hasTGLName = 1
# Foundation.ShipDef.SentriFighter.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.SentriFighter.desc = 'The Sentri class medium fighter is a fast but lightly armed aerospace fighter deployed by the Centauri military. House Tavari Armaments located at Hevaria Orbital Shipyards over Tolonius VII is responsible for manufacturing this class of vessel. Possessing greater maneuverability and acceleration than comparable craft such as the Earthforce Starfury, Centauri pilots have been known to perform drastic and stressful maneuvers that will cause them to pass out, passing control over to the autopilot to complete the maneuver and bring the fighter around to a superior tactical position.'

Foundation.ShipDef.SentriFighter.dTechs = {
	'Simulated Point Defence' : { "Distance": 14.0, "InnerDistance": 3.0, "Effectiveness": 0.69, "LimitTurn": 4.6, "LimitSpeed": 67, "LimitDamage": "-120", "Period": 0.5, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}}
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.SentriFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SentriFighter.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
