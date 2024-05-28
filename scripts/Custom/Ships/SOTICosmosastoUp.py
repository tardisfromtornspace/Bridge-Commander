#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 6/23/2004                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
from Custom.Autoload.RaceCosmosASTO import *

#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'SOTICosmosastoUp'
iconName = 'SOTICosmosasto'
longName = 'S.O.T.I. (2014) View Mode'
shipFile = 'SOTICosmosastoUp' 
menuGroup = 'Cosmos a Spacetime Odyssey'
playerMenuGroup = 'Cosmos a Spacetime Odyssey'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'S.O.T.I. (2014)',
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
Foundation.ShipDef.SOTICosmosastoUp = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "race": CosmosASTO })
Foundation.ShipDef.SOTICosmosastoUp.dTechs = {
	"SOTI Inexistance": 1,
	"SOTI Size Change": {"Scale": 1.0, "Power": 3, "Types": [App.CT_WEAPON_SYSTEM]} 
}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.SOTICosmosastoUp.hasTGLName = 1
# Foundation.ShipDef.SOTICosmosastoUp.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.SOTICosmosastoUp.desc = "The Ship of the Imagination (or S.O.T.I. for short) is a spacecraft used by astrophysicist Neil deGrasse Tyson in 'Cosmos: A Spacetime Odyssey' to explore the universe in search of answers to key questions of science and philosophy."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.SOTICosmosastoUp.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SOTICosmosastoUp.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
