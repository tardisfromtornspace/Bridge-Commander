#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 11/09/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG2003CylonBasestar'
iconName = 'CylonBasestar'
longName = 'Type-D Basestar'
shipFile = 'BSG2003CylonBasestar' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Cylon Ships", "Basestars"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003CylonBasestar',
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
Foundation.ShipDef.BSG2003CylonBasestar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.BSG2003CylonBasestar.dTechs = {
	'Automated Destroyed System Repair': {"Time": 3600.0 },
	"AutoTargeting": { "Pulse": [6, 1] },
	'Simulated Point Defence' : { "Distance": 35.0, "InnerDistance": 5.0, "Effectiveness": 0.95, "LimitTurn": 0.27, "LimitSpeed": 56, "Period": 0.1, "MaxNumberTorps": 10, },
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Drive 1", "FTL Drive 2", "FTL Drive 3", "FTL Drive 4"], "Core": ["Reactor Module"], "Cooldown Time": 13 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003CylonBasestar.fMaxWarp = 6.5
Foundation.ShipDef.BSG2003CylonBasestar.fCruiseWarp = 6.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003CylonBasestar.hasTGLName = 1
# Foundation.ShipDef.BSG2003CylonBasestar.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003CylonBasestar.desc = "Type-D Basestars, also known as Modern Basestars or Baseships, physically resemble two Y-shaped sections joined at an axis and pointing in opposite directions, although those sections can swivel to direct alignment for atmospheric flight. They are designed to make FTL jumps and are equipped to deploy large-scale strikes with nuclear and conventional ordnance. These basestars are biomechanical entities which could heal itself of battle damage, with fleshy hangars to house Raiders. The Basestar´s internal functions are controlled by a part-biological, part-machine central computer system known as the Hybrid. The biological part of the Hybrid is a female humanoid Cylon-like being. Basestars are capable of carrying other Cylon models as crew within them."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003CylonBasestar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003CylonBasestar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
