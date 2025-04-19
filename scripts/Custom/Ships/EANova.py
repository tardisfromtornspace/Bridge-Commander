#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 16/04/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'EANova'
iconName = 'EANova'
longName = 'Nova Class'
shipFile = 'EANova' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_GALAXY
SubMenu = "Earth Alliance"
SubSubMenu = "Capital Ships"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'EANova',
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
Foundation.ShipDef.EANova = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.EANova.dTechs = {
	'Defense Grid': 130,
	'Simulated Point Defence' : { "Distance": 38.0, "InnerDistance": 15.0, "Effectiveness": 0.7, "LimitTurn": 0.5, "LimitSpeed": 79, "LimitDamage": "650", "Period": 1.0, "MaxNumberTorps": 3, "Pulse": {"Priority": 1}},
	"Tachyon Sensors": 2.5
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.EANova.hasTGLName = 1
# Foundation.ShipDef.EANova.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.EANova.desc = "The Nova class dreadnought, sometimes referred to as a battleship, is an immense Earth Alliance warship designed to bring massive firepower against any target. This vessel is one of the older classes alongside the Hyperion-class heavy cruiser and shares a similar basic design as the much later Omega-class destroyer. This design fought in many engagements in the Earth-Minbari War but like the other capital ships of that time found itself unable to lock onto the Minbari ships, and many were destroyed during the conflict."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.EANova.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EANova.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
