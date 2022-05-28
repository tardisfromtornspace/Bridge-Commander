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
abbrev = 'HaririrDeathGlider3'
iconName = 'DeathGlider'
longName = 'Haririr Death Glider 3'
shipFile = 'HaririrDeathGlider3' 
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'DeathGlider',
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
Foundation.ShipDef.HaririrDeathGlider3 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.HaririrDeathGlider3.hasTGLName = 1
#Foundation.ShipDef.HaririrDeathGlider3.hasTGLDesc = 1
#
# Otherwise, uncomment this and type something in:
Foundation.ShipDef.HaririrDeathGlider3.desc = 'This Death Gliders have been updated by Lord Haririr to possess shielding, in order to have more efficiendy in battle and to reduce military losses'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#######################################################################################
