#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 09/09/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'GalacticaClosed'
iconName = 'GalacticaClosed'
shipFile = 'GalacticaClosed' 
species = App.SPECIES_GALAXY
#                                                                                     #
# Com-man's note: I removed the menugroup and playermenu group so that u wont         #
# be flooded with a list of F-302's                                                   #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'GalacticaClosed',
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
Foundation.ShipDef.GalacticaClosed = Foundation.FedShipDef(abbrev, species, { 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.GalacticaClosed.dTechs = {
	'Fed Ablative Armor': { "Plates": ["Armour"]
}}
#                                                                                     #
# Com-man's note: Of course you need to remove the 'name': longname here too for it   #
# to work.              						                          #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.GalacticaClosed.hasTGLName = 1
# Foundation.ShipDef.GalacticaClosed.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.GalacticaClosed.desc = 'The Galactica Class Battlestar was the first class of battlestar ever to be constructed by the Twelve Colonies. Twelve were initially constructed for the First Cylon War, each representing one of the Twelve Colonies of Kobol. Several were destroyed during the war; the rest were being retired from active service slowly at the time of the Fall, presumably either to be scrapped or converted into museums. Designed and constructed during the First Cylon War, ships of this class lack the advanced computer technology and networking of more modern battlestars for fear of Cylon infiltration of their computer systems. It is due to this resistance to infiltration that one ship was able to escape the Fall of the Colonies, going on to lead a group of survivors to Earth.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#   Com-man's note: Removing these lines was nesecary to prevent BC giving the        #
#   black screen yellow cursor error.                                                 #
#                                                                                     #
#######################################################################################
