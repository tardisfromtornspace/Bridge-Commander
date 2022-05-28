from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 16.3.2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'PsExcelsiorRefitTNG1'
iconName = 'PsExcelsiorRefit'
longName = 'USS Lakota'
shipFile = 'PsExcelsiorRefitTNG1' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
#SubMenu = "Excelsior Class"
#SubSubMenu = "TNG"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'PsExcelsiorRefitTNG1',
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
Foundation.ShipDef.PsExcelsiorRefitTNG1 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
Foundation.ShipDef.PsExcelsiorRefitTNG1.sBridge = 'FCExcelsiorbridge'
Foundation.ShipDef.PsExcelsiorRefitTNG1.fMaxWarp = 8.6
Foundation.ShipDef.PsExcelsiorRefitTNG1.dTechs = { 'Fed Ablative Armor': {
	"Plates": ["Aft Ablative Armor", "Engineering Ablative Armor", "Saucer Ablative Armor"]
}}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.PsExcelsiorRefitTNG1.hasTGLName = 1
Foundation.ShipDef.PsExcelsiorRefitTNG1.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.PsExcelsiorRefitTNG1.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.PsExcelsiorRefitTNG1.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.PsExcelsiorRefitTNG1.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
