#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 05.09.2002                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Primus'
iconName = 'Primus'
longName = 'Primus Warship'
shipFile = 'Primus' 
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Centauri Republic"
species = App.SPECIES_GALAXY
SubSubMenu = "Capital ships"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Primus',
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
Foundation.ShipDef.Primus = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.Primus.hasTGLName = 1
#Foundation.ShipDef.Primus.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.Primus.desc = 'The Primus class battle cruiser was a mainstay of the Centauri Republic fleet. The Primus was built by House Tavari Armaments at the Hevaria Orbital Shipyards at Tolonius VII. A very powerful warship compared to its contemporaries, the only real weakness of the Primus is its lack of fighter bay facilities. During the last days of the Narn-Centauri War, several Primus class battle cruisers were outfitted with highly illegal mass drivers and were used in the planetary bombardment of Narn. The Primus´ standard armament of two twin barrell heavy pulse cannons allow it equal ability to deal with capital ships and fighters. Despite this, without fighter support the Primus can be quickly overwhelmed by intense barrages from enemy fighters and a powerful Defense Grid.'
Foundation.ShipDef.Primus.dTechs = {
	'Gravimetric Defense': 150,
	"Tachyon Sensors": 1.2
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Primus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Primus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
