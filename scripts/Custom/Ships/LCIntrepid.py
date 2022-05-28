#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'LCIntrepid'
iconName = 'Intrepid'
longName = 'Intrepid'
shipFile = 'LCIntrepid' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
#SubMenu = 'Intrepid Class'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'LCIntrepid',
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
Foundation.ShipDef.LCIntrepid = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
Foundation.ShipDef.LCIntrepid.sBridge = 'intrepidbridge'
Foundation.ShipDef.LCIntrepid.fMaxWarp = 9.975

Foundation.ShipDef.LCIntrepid.dTechs = { 'SubModel': {
        "Setup":        {
                "Body":                 "LCIntrepid_no_nacelle",
                "NormalModel":          "LCIntrepid",
                "WarpModel":          "LCIntrepid_Warp",
                "Hardpoints":       {
			"Port Warp":  [-0.63, -1.15223, -0.15],
			"Star Warp":  [0.63, -1.15223, -0.15],
                },
                "WarpHardpoints":       {
			"Port Warp":  [-0.6, -1.15223, 0],
			"Star Warp":  [0.6, -1.15223, 0],
                },
        },
                
        "Port Nacelle":     ["LCIntrepid_n_left", {
                "Position":             [-0.32, -1.07, -0.144],
                "Rotation":             [0, 0, 0], # normal Rotation used if not Warp
                "WarpRotation":       [0, -0.45, 0],
                "WarpPosition":       [-0.32, -1.07, -0.144],
                "WarpDuration":       150.0,
                }
        ],
        
        "Starboard Nacelle":     ["LCIntrepid_n_right", {
                "Position":             [0.32, -1.07, -0.144],
                "Rotation":             [0, 0, 0],
                "WarpRotation":       [0, 0.45, 0],
                "WarpPosition":       [0.32, -1.07, -0.144],
                "WarpDuration":       150.0,
                }
        ],
}}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.LCIntrepid.hasTGLName = 1
Foundation.ShipDef.LCIntrepid.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.LCIntrepid.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.LCIntrepid.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.LCIntrepid.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################

#Foundation.ShipDef.LCIntrepid.SDTEntry = {
#	"Textures": [["voyager04_glow", "data/Models/Ships/LCIntrepid/High/intrepid04_glow.tga"]]
#}
