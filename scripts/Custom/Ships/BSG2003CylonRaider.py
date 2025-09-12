#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 08/09/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG2003CylonRaider'
iconName = 'CylonRaider'
longName = 'Raider Type III'
shipFile = 'BSG2003CylonRaider' 
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
	'modName': 'BSG2003CylonRaider',
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
Foundation.ShipDef.BSG2003CylonRaider = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG2003CylonRaider.dTechs = {
	'Simulated Point Defence' : { "Distance": 15.0, "InnerDistance": 2.0, "Effectiveness": 0.45, "LimitTurn": -0.8, "LimitSpeed": 35, "LimitDamage": "-90", "Period": 2.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Drive 1"], "Core": ["Tylium Reactor"], "Cooldown Time": 13 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003CylonRaider.fMaxWarp = 6.5
Foundation.ShipDef.BSG2003CylonRaider.fCruiseWarp = 6.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003CylonRaider.hasTGLName = 1
# Foundation.ShipDef.BSG2003CylonRaider.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003CylonRaider.desc = "The Cylon Raider is the basic Strike Interceptor of the Cylon fleet. Type III's sleek design means it can speed past nearly all enemy ships and hunt down slower ships as well as dodge bullets in firefights. The Raider's purpose is anti-strike, anti-missile and, in some cases, anti-escort. In small groups, Raiders can take down some Line Ships or do massive damage. This Raiders are cybernetic in nature: the ship is actually a living creature, with a complex system of organs, veins and biological fluids inside the main body. Just like the humanoid Cylons, these Raiders are also capable of being reborn into new Raiders after having been destroyed."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003CylonRaider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003CylonRaider.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
