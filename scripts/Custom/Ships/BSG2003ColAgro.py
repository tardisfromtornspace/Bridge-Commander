#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 22/10/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG2003ColAgro'
iconName = 'ColAgro'
longName = 'Botanical Cruiser'
shipFile = 'BSG2003ColAgro' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Colonial Ships", "Civilian craft"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003ColAgro',
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
Foundation.ShipDef.BSG2003ColAgro = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.BSG2003ColAgro.dTechs = {
	"AutoTargeting": { "Pulse": [6, 1] },
	'Simulated Point Defence' : { "Distance": 35.0, "InnerDistance": 4.0, "Effectiveness": 0.15, "LimitTurn": 0.26, "LimitSpeed": 51, "Period": 3.1, "MaxNumberTorps": 1, },
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Coil"], "Core": ["Power Core"], "Cooldown Time": 15 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003ColAgro.fMaxWarp = 5.25
Foundation.ShipDef.BSG2003ColAgro.fCruiseWarp = 5.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003ColAgro.hasTGLName = 1
# Foundation.ShipDef.BSG2003ColAgro.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003ColAgro.desc = "A Botanical Cruiser (or Agro Ship) is a smaller and slightly less luxurious cruise liner type than the Aerilon Star.  However, both pre-war and currently it serves much the same purpose. The Agro Ships were designed for long and leisurely trips through space and provided simulated environments for guests. Whereas the Aerilon Star has one large bio-dome, this class of ship has fifteen small domes. Generally most of the rest of the vessel is also of a slightly less grand scale. The Botanical Cruisers are among the best places to live in the Fleet but due to the Aerilon Star's dominance of politics, commerce, and recreation these ships have seemingly drifted out of focus. Actually they are used for agriculture."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003ColAgro.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003ColAgro.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
