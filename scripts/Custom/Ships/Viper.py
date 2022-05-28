#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 23/10/2003                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Viper'
iconName = 'Viper'
longName = 'Viper'
shipFile = 'Viper' 
menuGroup = 'BSG (TOS) Ships'
playerMenuGroup = 'BSG (TOS) Ships'
SubMenu = "Twelve Colonies of Man"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Viper',
	'author': 'MadJohn',
	'version': '0.9',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.Viper = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.Viper.hasTGLName = 1
# Foundation.ShipDef.Viper.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.Viper.desc = 'Vipers are capable of atmospheric as well as space flight, and can land and take off from a planetary surface. Viper engines are designed to collect commonly occurring gases in planetary atmospheres and in space to power the ship´s fusion reactor. Vipers are also capable of supporting the pilot for up to two weeks in a form of suspended animation for extremely long missions. Armament consist of two directed energy weapons that are linked together to fire simultaneously. They can also be modified to carry fire suppression equipment. In the event of a crash landing, a Viper´s cockpit can also be used as an escape pod, separating from the ship and parachuting to the ground. This system does not provide a soft landing—in fact, it can knock the pilot unconscious—but it is effective.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Viper.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Viper.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
