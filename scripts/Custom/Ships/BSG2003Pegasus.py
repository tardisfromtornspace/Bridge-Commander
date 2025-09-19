#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created manually                                                                   #
#  Date: 19/09/2025                                                                   #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'BSG2003Pegasus'
iconName = 'Pegasus'
longName = 'Pegasus'
shipFile = 'BSG2003Pegasus' 
menuGroup = 'BSG (2003) Ships'
playerMenuGroup = 'BSG (2003) Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Colonial Ships", "Battlestars"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'BSG2003Pegasus',
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
Foundation.ShipDef.BSG2003Pegasus = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.BSG2003Pegasus.dTechs = {
	'Fed Ablative Armor': { "Plates": ["Armour"]},
	"AutoTargeting": { "Pulse": [6, 1] },
	'Simulated Point Defence' : { "Distance": 35.0, "InnerDistance": 5.0, "Effectiveness": 0.75, "LimitTurn": 0.26, "LimitSpeed": 56, "Period": 0.1, "MaxNumberTorps": 14, },
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Drive 1", "FTL Drive 2"], "Core": ["Reactor Module"], "Cooldown Time": 14.30 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003Pegasus.fMaxWarp = 5.25
Foundation.ShipDef.BSG2003Pegasus.fCruiseWarp = 5.0
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003Pegasus.hasTGLName = 1
# Foundation.ShipDef.BSG2003Pegasus.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003Pegasus.desc = "Battlestar Pegasus is a Mercury Class Battlestar, assigned to Battlestar Group 62 of the Colonial Fleet, and commanded by Admiral Helena Cain at the time of the Cylon attack on the Twelve Colonies. Thought to have been destroyed during the attack, Pegasus escaped, and encounters Battlestar Galactica and the last survivors of the Twelve Colonies around six months after their escape from Ragnar Anchorage."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003Pegasus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003Pegasus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
