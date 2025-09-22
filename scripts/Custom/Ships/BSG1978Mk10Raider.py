#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created manually                                                                   #
#  Date: 22/09/2025                                                                   #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG1978Mk10Raider'
iconName = 'Mk10Raider'
longName = 'Mk. 10 Raider'
shipFile = 'BSG1978Mk10Raider' 
menuGroup = 'BSG (1978) Ships'
playerMenuGroup = 'BSG (1978) Ships'
SubMenu = ["Cylon Empire", "Raiders"]
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG1978Mk10Raider',
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
Foundation.ShipDef.BSG1978Mk10Raider = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.BSG1978Mk10Raider.dTechs = {
	'Partially Distributed Shields': {"Shield Transfer Ratio": 1.25, "Max Percentage Damage": 2, "Collapse Threshold": 0.23, "Max Radians": 2.094395},
	"Alternate-Warp-FTL": {
		"Setup": {
			"BSG 1978 Ultra-Light-Drive": {	"Nacelles": ["Gravimetric Initiator"], "Core": ["Tylium Energizer"]},
		},
	},
}

Foundation.ShipDef.BSG1978Mk10Raider.fMaxWarp = 4.0
Foundation.ShipDef.BSG1978Mk10Raider.fCruiseWarp = 3.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG1978Mk10Raider.hasTGLName = 1
# Foundation.ShipDef.BSG1978Mk10Raider.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG1978Mk10Raider.desc = "The Raider is the primary fighter attack craft of the Cylons. and is the craft most often encountered by Colonial Warriors in engagements.\n\nIt is capable of both atmospheric and space flight, and capable of being used in both a defensive and offensive campaign. Raiders tend to swarm in phalanxes using superior numbers to overwhelm their adversaries and, while lacking in originality, are devastatingly effective in engagements.\n\nThey are a primary workhorse of the Cylon Empire's military campaigns, and are versatile in their use as platforms for numerous types of engagements, from their use as bomber craft on planetary targets to using their crafts as weapons themselves in suicide runs. They are also used in transportation of cargo and personnel.\n\nRaiders are not only part of a basestar's standard complement (numbering 300 units), but also part of the complement of various outposts and listening posts."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG1978Mk10Raider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG1978Mk10Raider.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
