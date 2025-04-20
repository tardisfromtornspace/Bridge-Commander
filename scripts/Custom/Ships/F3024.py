#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 6/18/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'F3024'
iconName = 'F302'
shipFile = 'F3024' 
species = 750
#                                                                                     #
# Com-man's note: I removed the menugroup and playermenu group so that u wont         #
# be flooded with a list of F-302's                                                   #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'F3024',
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
Foundation.ShipDef.F3024 = Foundation.FedShipDef(abbrev, species, { 'iconName': iconName, 'shipFile': shipFile })
# F302 don't have shields, but we are adding this just in case
Foundation.ShipDef.F3024.dTechs = {
	'SG Shields': { "RaceShieldTech": "None" }
}

Foundation.ShipDef.F3024.fMaxWarp = 1.8
Foundation.ShipDef.F3024.fCruiseWarp = 1.0
#                                                                                     #
# Com-man's note: Of course you need to remove the 'name': longname here too for it   #
# to work.              						                          #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
Foundation.ShipDef.F3024.hasTGLName = 1
Foundation.ShipDef.F3024.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
#Foundation.ShipDef.F3024.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#   Com-man's note: Removing these lines was nesecary to prevent BC giving the        #
#   black screen yellow cursor error.                                                 #
#                                                                                     #
#######################################################################################
