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
abbrev = 'EAExplorer'
iconName = 'EAExplorer'
longName = 'EA Explorer'
shipFile = 'EAExplorer' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_SHUTTLE
SubMenu = "Earth Alliance"
SubSubMenu = "Non-military craft"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'EAExplorer',
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
Foundation.ShipDef.EAExplorer = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.EAExplorer.dTechs = {
	'Defense Grid': 100,
	"Tachyon Sensors": 1.0
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.EAExplorer.hasTGLName = 1
# Foundation.ShipDef.EAExplorer.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.EAExplorer.desc = "Explorer class ships are used by Earthforce to explore new regions of space, map star systems and planets, make and maintain diplomatic relations with other races, and build new jumpgates. Vessels of this class were not built for combat and were unlikely to be called upon for fleet action support. Explorers are the largest ships in service of the Earth Alliance, at over six kilometers in length (for comparison, the Babylon 5 space station is just over eight kilometers long). Like many contemporary Earthforce vessels, Explorers were designed with a large rotational section for simulated gravity, and a forward-facing launch bay. In addition to their complement of fighters, Explorer-class ships have an array of smaller support vessels and shuttles for short range exploration and planetary surveying. The bulk of the ship's length is taken up by equipment mounting spars – forward and aft of the rotating habitation section – used to carry jumpgate construction equipment and pre-fabricated parts."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.EAExplorer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EAExplorer.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
