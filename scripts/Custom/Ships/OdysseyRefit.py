#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 21/06/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'OdysseyRefit'
iconName = 'DSC304'
shipFile = 'OdysseyRefit' 
species = 754
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'OdysseyRefit',
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
Foundation.ShipDef.OdysseyRefit = Foundation.FedShipDef(abbrev, species, { 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.OdysseyRefit.dTechs = {
	"AutoTargeting": { "Pulse": [3, 1] },
	"Fool Targeting": {
		"Slow Beam Simulation": {
			"Distance Threshold": 40.0,
			"Speed Threshold": 2,
			"Distance Multiplier": 6.0,
			"Speed Multiplier": 8.0,
		}  
	},
	"SG Asgard Beams Weapon": {"HullDmgMultiplier": 1.0, "ShieldDmgMultiplier": 1.0, "FacetFactor": 2.0},
	'SG Shields': { "RaceShieldTech": "Asgard", "RaceHullTech": "Tau'ri" }
}

Foundation.ShipDef.OdysseyRefit.fMaxWarp = 9.4
Foundation.ShipDef.OdysseyRefit.fCruiseWarp = 6.8
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
Foundation.ShipDef.OdysseyRefit.hasTGLName = 1
Foundation.ShipDef.OdysseyRefit.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
#Foundation.ShipDef.OdysseyRefit.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#   Com-man's note: Removing these lines was nesecary to prevent BC giving the        #
#   black screen yellow cursor error.                                                 #
#                                                                                     #
#######################################################################################
