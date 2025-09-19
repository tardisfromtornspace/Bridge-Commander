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
abbrev = 'BSG2003Artemis'
iconName = 'BS_Acropolis'
longName = 'Artemis class'
shipFile = 'BSG2003Artemis' 
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
	'modName': 'BSG2003Artemis',
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
Foundation.ShipDef.BSG2003Artemis = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.BSG2003Artemis.dTechs = {
	'Fed Ablative Armor': { "Plates": ["Armour"]},
	"AutoTargeting": { "Pulse": [3, 1] },
	'Simulated Point Defence' : { "Distance": 35.0, "InnerDistance": 5.0, "Effectiveness": 0.75, "LimitTurn": 0.26, "LimitSpeed": 55, "Period": 0.1, "MaxNumberTorps": 8, },
	"Alternate-Warp-FTL": {
		"Setup": {
			"nBSGDimensionalJump": {	"Nacelles": ["FTL Drive 1", "FTL Drive 2"], "Core": ["Reactor Module"], "Cooldown Time": 15 * 60},
		},
	},
}

Foundation.ShipDef.BSG2003Artemis.fMaxWarp = 5.25
Foundation.ShipDef.BSG2003Artemis.fCruiseWarp = 5.0

def BSGArtemisIDSwap(self):
       retval = {"Textures": [["galact1.tga", "Data/Models/Ships/Battlestar/battlestar_names/Acropolis/galact1.tga"]]}
       return retval

Foundation.ShipDef.BSG2003Artemis.__dict__['SDT Entry'] = BSGArtemisIDSwap

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.BSG2003Artemis.hasTGLName = 1
# Foundation.ShipDef.BSG2003Artemis.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.BSG2003Artemis.desc = "The Artemis-class was a type of battlestar used in the First Cylon War. Before the unification of the Twelve Colonies and the development of the Jupiter-class, the Artemis was the heaviest warship fielded by the Colonies of the Cyrannus System."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.BSG2003Artemis.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BSG2003Artemis.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
