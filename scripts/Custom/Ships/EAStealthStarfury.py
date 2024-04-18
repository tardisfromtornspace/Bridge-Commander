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
abbrev = 'EAStealthStarfury'
iconName = 'EAStealthStarfury'
longName = 'Stealth Starfury'
shipFile = 'EAStealthStarfury' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_SHUTTLE
SubMenu = "Earth Alliance"
SubSubMenu = "Fighters"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'EAStealthStarfury',
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
Foundation.ShipDef.EAStealthStarfury = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.EAStealthStarfury.dTechs = {
	'Simulated Point Defence' : { "Distance": 10.0, "InnerDistance": 3.0, "Effectiveness": 0.9, "LimitTurn": 8.5, "LimitSpeed": 75, "LimitDamage": "-15", "Period": 0.3, "MaxNumberTorps": 2, "Pulse": {"Priority": 1}}
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.EAStealthStarfury.hasTGLName = 1
# Foundation.ShipDef.EAStealthStarfury.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.EAStealthStarfury.desc = "Derived mainly from the SA-23E Mitchell-Hyundyne Starfury, the Stealth Starfury is far more rare and very expensive to produce. Outfitted as a fast interceptor and featuring some of Earthforce's most advanced stealth components, information on this model of Starfury is not widely distributed by Earthforce. The Psi Corps maintained a squadron of these fighters called 'Black Omega' and was formed under the supervision of the Psi Cop Alfred Bester."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.EAStealthStarfury.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EAStealthStarfury.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
