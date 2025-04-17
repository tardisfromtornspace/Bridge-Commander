#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Andromeda"
iconName = "Andromeda"
longName = "Andromeda"
shipFile = "Andromeda"
species = App.SPECIES_GALAXY
menuGroup = "Andromeda"
playerMenuGroup = "Andromeda"
SubMenu = "System´s Commonwealth"
Foundation.ShipDef.Andromeda = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Andromeda.dTechs = {
	"AutoTargeting": { "Torpedo": [8, 1] },
	'Breen Drainer Immune': 1,
	'Multivectral Shields': 10,
        "Reflector Shields": 40,

	'Simulated Point Defence' : { "Distance": 120.0, "InnerDistance": 15.0, "Effectiveness": 0.8, "LimitTurn": 5.0, "LimitSpeed": 300, "Period": 0.2, "MaxNumberTorps": 12, "Torpedo": {"Priority": 1}},
	'Fed Ablative Armor': { "Plates": ["Armour"]
},
#'Alternate-Warp-FTL': {
'SubModel': {
        "Setup":        {
                "Body":                 shipFile,
                "NormalModel":          shipFile,
                #"WarpModel":            shipFile,
                "AttackModel":          "AndromedaBattleForm",
		"WarpIgnoreCall": 1,
		"SlipstreamIgnoreCall": 1,
                "Hardpoints":       {
                        "Battle Blades 1":  [-1.700000, 0.950000, 0.950000],
                        "Battle Blades 2":  [1.700000, 0.950000, 0.950000],
                },
                "AttackHardpoints":       {
                        "Battle Blades 1":  [-2.700000, 0.980000, 0.850000],
                        "Battle Blades 2":  [2.700000, 0.980000, 0.850000],
                },
        },
                
        "Port Wing":     ["andromedaBattleBladeLeft", {
                "Position":             [0, 0, 0.0],
                "Rotation":             [0, -0.1, 0.4], # normal Rotation used if not Red Alert and if not Warp
                "AttackRotation":         [0, 0.1, -0.4],
                "AttackDuration":         150.0, # Value 200 is 1/100 of a second
                "AttackPosition":         [0, 0, 0.0],
                #"WarpRotation":       [0, 0, 0],
                #"WarpPosition":       [0, 0, 0],
                #"WarpDuration":       150.0,
                }
        ],
        
        "Starboard Wing":     ["andromedaBattleBladeRight", {
                "Position":             [0, 0, 0.0],
                "Rotation":             [0, 0.1, -0.4],
                "AttackRotation":         [0, -0.1, 0.4],
                "AttackDuration":         150.0, # Value is 1/100 of a second
                "AttackPosition":         [0, 0, 0.0],
                #"WarpRotation":       [0, 0, 0],
                #"WarpPosition":       [0, 0, 0],
                #"WarpDuration":       150.0,
                }
        ],

        "PortLow Wing":     ["andromedaBattleBladeRightDown", {
                "Position":             [-3, 1, 0.0],
                "Rotation":             [0, 0.1, -0.4], # normal Rotation used if not Red Alert and if not Warp
                "AttackRotation":         [0, -0.1, 0.2],
                "AttackDuration":         150.0, # Value 200 is 1/100 of a second
                "AttackPosition":         [-3, 1, 0.0],
                #"WarpRotation":       [0, 0, 0],
                #"WarpPosition":       [-3, 1, 0.0],
                #"WarpDuration":       150.0,
                }
        ],

        "StarboardLow Wing":     ["andromedaBattleBladeLeftDown", {
                "Position":             [3, 1, 0.0],
                "Rotation":             [0, -0.1, 0.4],
                "AttackRotation":         [0, 0.1, -0.2],
                "AttackDuration":         150.0, # Value is 1/100 of a second
                "AttackPosition":         [3, 1, 0.0],
                #"WarpRotation":       [0, 0, 0],
                #"WarpPosition":       [3, 1, 0.0],
                #"WarpDuration":       150.0,
                }
        ],
}
}
Foundation.ShipDef.Andromeda.bPlanetKiller = 1

Foundation.ShipDef.Andromeda.desc = "The Andromeda Ascendant (Registry Designation: Shining Path to Truth and Knowledge Artificial Intelligence model GRA 112, serial number XMC-10-284) was a warship of both the Systems Commonwealth and the New Systems Commonwealth, and one of the last surviving Glorious Heritage Class ships after the First Systems Commonwealth Civil War and the Long Night of the Commonwealth. Regarded as one of the most powerful ships in the known galaxies, she is one of the most recognizable ships, achieving a near mythic status. The Andromeda Ascendant is the tenth Glorious Heritage Class heavy cruiser, built in the days of the old Systems Commonwealth. She began her life and career in the Newport News Orbital Shipyards above Earth, where her keel was laid in CY 9768. Construction proceeded for a period of 4 years, through to the delivery and installation of the Headwaters of Invention Mark VIII Slipstream drive in CY 9772, which was the last piece of physical equipment installed. After her construction was completed, she was sent on her shakedown cruise to Tarn-Vedra, where a custom designed and created Andromeda Ascendant Artificial Intelligence was installed in a Sentience ceremony. Her Gravity Field Generator reduces the effective mass of the Andromeda to just less than one kilogram. Its design, maneuverability, Valiant offensive missiles, Nova Bomb Torpedoes, Point Defense Lasers, Anti-Gravity Fields, Fullerene-Ablative-Reactive Armor and self-repair nanobots makes her a deadly enemy, specially at great distances."


if menuGroup:           Foundation.ShipDef.Andromeda.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Andromeda.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
