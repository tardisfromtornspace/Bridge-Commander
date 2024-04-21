#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 9/3/2002                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'Victory'
iconName = 'Victory'
longName = 'Victory'
shipFile = 'Victory' 
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Interestellar Alliance"
species = App.SPECIES_GALAXY
SubSubMenu = "Destroyers"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'Victory',
	'author': 'DamoclesX',
	'version': '1.1',
	'sources': [ 'DamoclesX@hotmail.com' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.Victory = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.Victory.dTechs = {
	'Regenerative Shields': 30,
	"AutoTargeting": { "Phaser": [3, 1] },
	'Polarized Hull Plating': { "Plates": ["PlastiCrystalline Armour"]},
	'Simulated Point Defence' : { "Distance": 75.0, "InnerDistance": 12.0, "Effectiveness": 0.9, "LimitTurn": 0.9, "LimitSpeed": 76, "LimitDamage": "-450", "Period": 2.0, "MaxNumberTorps": 4, "Phaser": {"Priority": 2}, "Pulse": {"Priority": 1}},
	"Fool Targeting": {
		"Minbari Stealth": {
			"Miss": 500.0,
			"Sensor": 500,
        	}  
	},
	"Tachyon Sensors": 0.7,
        'Turret': {
        "Setup":        {
                "Body":                 shipFile,
                "NormalModel":          shipFile,
                "WarpModel":          shipFile,
                "AttackModel":          shipFile,
                #"ShieldOption": 1,
                "Hardpoints":       {
                #        "Port Cannon":  [-0.677745, 0.514529, -0.229285],
                #        "Star Cannon":  [0.663027, 0.511252, -0.240265],
                #        "Port Cannon 1":  [-0.323324, 0.240263, -0.115398],
                #        "Star Cannon 1":  [0.319566, 0.242142, -0.11861],
                },
                "AttackHardpoints":       {
                #        "Port Cannon":  [-0.503543, 0.524792, -0.47761],
                #        "Star Cannon":  [0.486256, 0.527008, -0.483889],
                #        "Port Cannon 1":  [-0.244469, 0.228191, -0.19762],
                #        "Star Cannon 1":  [0.243789, 0.243208, -0.201933],
                },
        },
                
        "Frontal TriCannon":     ["VictoryTurret", {
                "Position":             [0, 7.5, -0.1],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0, 7.5, 0.44],
                "WarpPosition":       [0, 1.5, 0.44],
                "WarpDuration":       150.0,
                "SyncTorpType": 1,
                "SimulatedPhaser": 1,
                "SetScale": 0.5,
                }
        ],

        "Central BiCannon":     ["VictoryTurretTwo", {
                "Position":             [0, 1.0, 0.1],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0, 1.0, 0.8],
                "WarpPosition":       [0, 1.0, 0.4],
                "WarpDuration":       150.0,
                "SyncTorpType": 1,
                "SimulatedPhaser": 1,
                "SetScale": 0.5,
                }
        ],
        
}
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.Victory.hasTGLName = 1
#Foundation.ShipDef.Victory.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.Victory.desc = "The Destroyer class White Star project was a joint Earth/Minbar venture to create a larger, more-powerful warship for use by the Interstellar Alliance to complement the White Star fleet. The resulting ship class is sometimes referred to as a Victory-class destroyer after the first ship of the line. The destroyer is based on technology from the White Star fleet - being a combination of Minbari and Vorlon technology - combined with Earth tech in function and aesthetic. The two greatest applications of alien technology with human is in the artificial gravity and associated gravimetric engines of Minbari design, coupled with the powerful weapon system derived from Vorlon tech. As opposed to the Warlock class destroyer used by Earthforce - which used conventional ion drives and weak artificial gravity - the destroyer would have a full-gravity environment in which the crew could move freely as well as full gravimetric propulsion. This made the ship as maneuverable and as jump capable as a Minbari capital vessel, able to jump into and out of hyperspace repeatedly. "
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.Victory.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Victory.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
