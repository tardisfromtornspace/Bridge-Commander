#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 18/04/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'AlphaWing'
iconName = 'EAStarfury'
longName = 'AlphaWing'
shipFile = 'AlphaWing'
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5' 
SubMenu = "B-5 starfuries wings"
species = App.SPECIES_GALAXY

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'AlphaWing',
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
Foundation.ShipDef.AlphaWing = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.AlphaWing.dTechs = {
	'Simulated Point Defence' : { "Distance": 10.0, "InnerDistance": 3.0, "Effectiveness": 0.6, "LimitTurn": 8.5, "LimitSpeed": 70, "LimitDamage": "-150", "Period": 0.3, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	"Tachyon Sensors": 2.2
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.AlphaWing.hasTGLName = 1
# Foundation.ShipDef.AlphaWing.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.AlphaWing.desc = 'Alpha Wing of Babylon 5.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.AlphaWing.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AlphaWing.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
