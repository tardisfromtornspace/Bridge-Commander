from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 3/9/03                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Reman Scimitar'
iconName = 'Reman Scimitar'
longName = 'Reman Scimitar'
shipFile = 'Reman Scimitar' 
menuGroup = 'Romulan Ships'
playerMenuGroup = 'Romulan Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'RemanScimitar',
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
#Foundation.ShipDef.RemanScimitar = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Cloak Fireing AI
import F_CloakAttackDef
Foundation.ShipDef.RemanScimitar = F_CloakAttackDef.CloakAttackDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.RemanScimitar.fMaxWarp = 9.86
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.RemanScimitar.hasTGLName = 1
Foundation.ShipDef.RemanScimitar.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.Reman Scimitar.desc = 'Produced by the Remans but technically operating under the flag of the Romulan Empire, the Scimitar was first encountered by the USS Enterprise-E, which travelled to Romulus in 2378 at the invite of the new Praetor, Shinzon. The ship is a large vessel, roughly the size of the D\'Deridex in terms of volume. It was classified by Captain Picard as a predator, and this is certainly an apt description. The ship carried very heavy armament and shielding, enabling it to remain in a battle for prolonged periods under heavy fire.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.RemanScimitar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.RemanScimitar.RegisterQBPlayerShipMenu(playerMenuGroup)

#                                                                                     #
#######################################################################################
