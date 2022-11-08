#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'DLCIntrepid_no_nacelle'
iconName = 'AMVoyager'
longName = 'USS Intrepid'
shipFile = 'DLCIntrepid_no_nacelle' 
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
	'modName': 'DLCIntrepid_no_nacelle',
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
Foundation.ShipDef.DLCIntrepid_no_nacelle = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.DLCIntrepid_no_nacelle.hasTGLName = 1
# Foundation.ShipDef.DLCIntrepid_no_nacelle.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.DLCIntrepid_no_nacelle.desc = 'No Description Available'
#                                                                                     #
#######################################################################################

#Foundation.ShipDef.DLCIntrepid_no_nacelle.SDTEntry = {
#	"Textures": [["voyager04_glow", "data/Models/Ships/DLCIntrepid/High/intrepid04_glow.tga"]]
#}

