#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 6/23/2004                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'DiamondsAMVoyager'
iconName = 'AMVoyager'
longName = 'AM Voyager'
shipFile = 'DiamondsAMVoyager' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'DiamondsAMVoyager',
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
Foundation.ShipDef.DiamondsAMVoyager = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DiamondsAMVoyager.dTechs = {
'Multivectral Shields': 30,
"Phase Cloak": 10,
'SubModel': {
        "Setup":        {
                "Body":                 "DLCIntrepid_no_nacelle",
                "NormalModel":          shipFile,
                "WarpModel":          "DLCIntrepid_Warp",
                "Hardpoints":       {
			"Port Warp":  [-0.63, -1.15223, -0.15],
			"Star Warp":  [0.63, -1.15223, -0.15],
                },
                "WarpHardpoints":       {
			"Port Warp":  [-0.6, -1.15223, 0],
			"Star Warp":  [0.6, -1.15223, 0],
                },
        },
                
        "Port Nacelle":     ["DLCIntrepid_n_left", {
                "Position":             [-0.32, -1.07, -0.144],
                "Rotation":             [0, 0, 0], # normal Rotation used if not Warp
                "WarpRotation":       [0, -0.45, 0],
                "WarpPosition":       [-0.32, -1.07, -0.144],
                "WarpDuration":       150.0,
                }
        ],
        
        "Starboard Nacelle":     ["DLCIntrepid_n_right", {
                "Position":             [0.32, -1.07, -0.144],
                "Rotation":             [0, 0, 0],
                "WarpRotation":       [0, 0.45, 0],
                "WarpPosition":       [0.32, -1.07, -0.144],
                "WarpDuration":       150.0,
                }
        ],
},
"Transphasic Torpedo Immune": 1,
"Adv Armor Tech": 1  # Please notice that this is only here to allow the non-players to have this special armor and for the armor to apply after Mvam
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.DiamondsAMVoyager.hasTGLName = 1
# Foundation.ShipDef.DiamondsAMVoyager.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.DiamondsAMVoyager.desc = "The Armoured Voyager without an specific armour - but still equipped with Transphasic Torpedoes."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.DiamondsAMVoyager.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DiamondsAMVoyager.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
