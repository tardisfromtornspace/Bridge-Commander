#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 14/03/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'HaririrDeathGlider1'
iconName = 'DeathGlider'
shipFile = 'HaririrDeathGlider1' 
species = 787
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'HaririrDeathGlider1',
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
Foundation.ShipDef.HaririrDeathGlider1 = Foundation.ShipDef(abbrev, species, { 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.HaririrDeathGlider1.hasTGLName = 1
#Foundation.ShipDef.HaririrDeathGlider1.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.HaririrDeathGlider1.desc = 'This Death Gliders have been updated by Lord Haririr to possess shielding, in order to have more efficiendy in battle and to reduce military losses'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
#                                                                                     #
#######################################################################################
