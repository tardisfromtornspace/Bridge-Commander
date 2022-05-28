from bcdebug import debug
#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 31.07.2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'VasKholhr'
iconName = 'VasKholhr'
longName = 'VasKholhr'
shipFile = 'VasKholhr' 
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
	'modName': 'VasKholhr',
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
Foundation.ShipDef.VasKholhr = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
        
Foundation.ShipDef.VasKholhr.dTechs = { 'SubModel': {
        "Setup":        {
                "Body":                 "VasKholhr_Body",
                "NormalModel":          shipFile,
                "WarpModel":          "VasKholhr_WingUp",
                "AttackModel":          "VasKholhr_WingDown",
                "Hardpoints":       {
                        "Port Cannon":  [-0.677745, 0.514529, -0.229285],
                        "Star Cannon":  [0.663027, 0.511252, -0.240265],
                        "Port Cannon 1":  [-0.323324, 0.240263, -0.115398],
                        "Star Cannon 1":  [0.319566, 0.242142, -0.11861],
                },
                "AttackHardpoints":       {
                        "Port Cannon":  [-0.503543, 0.524792, -0.47761],
                        "Star Cannon":  [0.486256, 0.527008, -0.483889],
                        "Port Cannon 1":  [-0.244469, 0.228191, -0.19762],
                        "Star Cannon 1":  [0.243789, 0.243208, -0.201933],
                },
        },
                
        "Port Wing":     ["VasKholhr_Portwing", {
                "Position":             [0, 0, 0],
                "Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
                "AttackRotation":         [0, -0.3, 0],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0, 0, 0.03],
                "WarpRotation":       [0, 0.149, 0],
                "WarpPosition":       [0, 0, 0.02],
                "WarpDuration":       150.0,
                }
        ],
        
        "Starboard Wing":     ["VasKholhr_Starboardwing", {
                "Position":             [0, 0, 0],
                "Rotation":             [0, 0, 0],
                "AttackRotation":         [0, 0.3, 0],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0, 0, 0.03],
                "WarpRotation":       [0, -0.149, 0],
                "WarpPosition":       [0, 0, 0.02],
                "WarpDuration":       150.0,
                }
        ],
}}


#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.VasKholhr.hasTGLName = 1
Foundation.ShipDef.VasKholhr.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.VasKholhr.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.VasKholhr.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VasKholhr.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
