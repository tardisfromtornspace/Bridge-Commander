#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 5/11/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'ZetaWing'
iconName = 'Thunderbolt'
longName = 'ZetaWing'
shipFile = 'ZetaWing' 
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
	'modName': 'ZetaWing',
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
Foundation.ShipDef.ZetaWing = Foundation.FerengiShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.ZetaWing.dTechs = {
	'Simulated Point Defence' : { "Distance": 10.0, "InnerDistance": 3.0, "Effectiveness": 0.6, "LimitTurn": 8.5, "LimitSpeed": 70, "LimitDamage": "-150", "Period": 0.3, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	"Tachyon Sensors": 2.2
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.ZetaWing.hasTGLName = 1
# Foundation.ShipDef.ZetaWing.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.ZetaWing.desc = 'Zeta Wing of Babylon 5.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.ZetaWing.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ZetaWing.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
