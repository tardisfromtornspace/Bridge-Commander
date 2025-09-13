import Foundation
import App

abbrev = 'StarcraftIIMinotaurDominion'
iconName = 'StarcraftIIDominionMinotaur'
longName = 'Minotaur Battlecruiser'
shipFile = 'StarcraftIIMinotaurDominion'
menuGroup = 'Starcraft Ships'
playerMenuGroup = 'Starcraft Ships'
species = App.SPECIES_GALAXY
SubMenu = "Human ships"
SubSubMenu = "Terran Dominion"
Foundation.ShipDef.StarcraftIIMinotaurDominion = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# TO-DO ADJUST + ADD SOMETHIGN FOR TEH YAMATO CANNON... ACTUALLY add a tech that replenishes torps and make the yamato cannon a torp
Foundation.ShipDef.StarcraftIIMinotaurDominion.dTechs = {
	"Starcraft Defensive Matrix": {
		"MatrixScale": 0.1,
		"PowerDrain": 100,
		"Duration": 20,
		"Cooldown": 20,
		"Smartcast": 1.6
	},
	"AutoTargeting": { "Pulse": [12, 0] },
        'Turret': {
        "Setup":        {
                #"Body":                 shipFile,
                #"NormalModel":          shipFile,
                #"WarpModel":          shipFile,
                #"AttackModel":          shipFile,
                #"Hardpoints":       {
                #},
                #"AttackHardpoints":       {
                #},
        },
                
        "Left TriCannon 1":     ["StarcraftIIMinotaurDominionTurretLeft1", {
                "Position":             [0.5720000, 0.5850000, -0.042000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0.8520000, 0.5850000, -0.042000],
                "WarpPosition":       [0.5720000, 0.5850000, -0.042000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": "Right",
                }
        ],
        "Left TriCannon 2":     ["StarcraftIIMinotaurDominionTurretLeft2", {
                "Position":             [0.5720000, -0.0250000, -0.042000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0.8520000, -0.0250000, -0.042000],
                "WarpPosition":       [0.5720000, -0.0250000, -0.042000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": "Right",
                }
        ],
        "Right TriCannon 1":     ["StarcraftIIMinotaurDominionTurretRight1", {
                "Position":             [-0.5720000, 0.5850000, -0.042000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [-0.8520000, 0.5850000, -0.042000],
                "WarpPosition":       [-0.5720000, 0.5850000, -0.042000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": "Left",
                }
        ],
        "Right TriCannon 2":     ["StarcraftIIMinotaurDominionTurretRight2", {
                "Position":             [-0.5720000, -0.0250000, -0.042000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [-0.8520000, -0.0250000, -0.042000],
                "WarpPosition":       [-0.5720000, -0.0250000, -0.042000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": "Left",
                }
        ],
        "LeftWing TriCannon":     ["StarcraftIIMinotaurDominionTurretDown2", {
                "Position":             [-1.400000, -0.620000, -0.150000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [-1.400000, -0.620000, -0.450000],
                "WarpPosition":       [-1.400000, -0.620000, -0.150000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": "Down",
                }
        ],
        "RightWing TriCannon":     ["StarcraftIIMinotaurDominionTurretDown1", {
                "Position":             [1.400000, -0.620000, -0.150000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [1.400000, -0.620000, -0.450000],
                "WarpPosition":       [1.400000, -0.620000, -0.150000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": "Down",
                }
        ],
        "FrontLeft TriCannon":     ["StarcraftIIMinotaurDominionTurretFrontLeft", {
                "Position":             [-0.240000, -0.160000, 0.520000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [-0.300000, -0.160000, 0.820000],
                "WarpPosition":       [-0.240000, -0.160000, 0.520000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": "Up",
                }
        ],
        "FrontRight TriCannon":     ["StarcraftIIMinotaurDominionTurretFrontRight", {
                "Position":             [0.240000, -0.160000, 0.520000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0.300000, -0.160000, 0.820000],
                "WarpPosition":       [0.240000, -0.160000, 0.520000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": "Up",
                }
        ],
        "BackLeft TriCannon":     ["StarcraftIIMinotaurDominionTurretBackLeft", {
                "Position":             [-0.410000, -1.100000, 0.420000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [-0.510000, -1.100000, 0.720000],
                "WarpPosition":       [-0.410000, -1.100000, 0.420000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": [-0.1, 0, 1],
                }
        ],
        "BackRight TriCannon":     ["StarcraftIIMinotaurDominionTurretBackRight", {
                "Position":             [0.410000, -1.100000, 0.420000],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0.510000, -1.100000, 0.720000],
                "WarpPosition":       [0.410000, -1.100000, 0.420000],
                "WarpDuration":       10.0,
                "SyncTorpType": 1,
                "SetScale": 0.6,
                "Orientation": [0.1, 0, 1],
                }
        ],
        
}
}

Foundation.ShipDef.StarcraftIIMinotaurDominion.desc = "The battlecruiser is the primary Terran capital ship. Battlecruisers fire rapid low damage shots from laser batteries.\nBattlecruisers are heavily armored and can withstand a single nuclear missile strike, making them better able at handling groups of weaker, low armor, units.\nThis particular version of the battlecruiser is additionally equipped with a Yamato Cannon (with enough energy to be fired from the start), Tactical Jump and Defense Matrix"

if menuGroup:           Foundation.ShipDef.StarcraftIIMinotaurDominion.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.StarcraftIIMinotaurDominion.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]