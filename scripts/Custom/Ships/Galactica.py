#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 08/10/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Galactica'
iconName = 'Galactica'
longName = 'Galactica'
shipFile = 'Galactica' 
menuGroup = 'BSG Ships'
playerMenuGroup = 'BSG Ships'
species = App.SPECIES_GALAXY
SubMenu = ["Colonial Ships", "Battlestars"]
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Galactica',
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
Foundation.ShipDef.Galactica = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Galactica.dTechs = {
	'Fed Ablative Armor': { "Plates": ["Armour"]
}}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Galactica.hasTGLName = 1
# Foundation.ShipDef.Galactica.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Galactica.desc = 'The Galactica Class Battlestar was the first class of battlestar ever to be constructed by the Twelve Colonies. Twelve were initially constructed for the First Cylon War, each representing one of the Twelve Colonies of Kobol. Several were destroyed during the war; the rest were being retired from active service slowly at the time of the Fall, presumably either to be scrapped or converted into museums. Designed and constructed during the First Cylon War, ships of this class lack the advanced computer technology and networking of more modern battlestars for fear of Cylon infiltration of their computer systems. It is due to this resistance to infiltration that one ship was able to escape the Fall of the Colonies, going on to lead a group of survivors to Earth.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Galactica.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Galactica.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
