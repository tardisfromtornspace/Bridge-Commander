#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'LCIntrepid_Warp'
iconName = 'LCIntrepid_Warp'
longName = 'USS Intrepid'
shipFile = 'LCIntrepid_Warp' 
menuGroup = None
playerMenuGroup = None
#SubMenu = 'Intrepid Class'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'LCIntrepid_Warp',
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
Foundation.ShipDef.LCIntrepid_Warp = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.LCIntrepid_Warp.hasTGLName = 1
# Foundation.ShipDef.LCIntrepid_Warp.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.LCIntrepid_Warp.desc = 'No Description Available'
#                                                                                     #
#######################################################################################


#Foundation.ShipDef.LCIntrepid_Warp.SDTEntry = {
#	"Textures": [["voyager04_glow", "data/Models/Ships/LCIntrepid/High/intrepid04_glow.tga"]]
#}

