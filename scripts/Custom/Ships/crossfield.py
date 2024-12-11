#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "crossfield"
iconName = "Crossfield"
longName = "Crossfield"
shipFile = "crossfield"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.crossfield = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.crossfield.desc = "The Crossfield class was a type of Federation starship in service during the mid-23rd century. Consisting of a modular saucer section, a wide secondary hull, and two elongated nacelles, these odd design choices were put into place to facilitate an experimental method of travel involving mycelial spores."

Foundation.ShipDef.crossfield.dTechs = {
	"Alternate-Warp-FTL": {
		"Setup": {
			"Spore-Drive": {	"Nacelles": [], "Core": ["Spore-Drive Chamber"], "NormalRotation": [0, 0, 0], "EndRotation" : [0, 4.19, 0], "Time": 200, "ExitDirection": "Down",  "UncloakDistance": 25, "UncloakChance": 20,},
			"Body": shipFile,
			"NormalModel":          shipFile,
			"Spore-DriveModel":          shipFile,
			"BodySetScale": 1.0,
			"NormalSetScale": 1.0,
			"Spore-DriveSetScale": 1.0,
		},

		"copy1":     ["crossfieldSporeCopy", {
			"Experimental": 1,
			"SetScale": 1.0,
			"ResetToPrevious": 1,
			"IgnoreSpore-DriveExit": 1,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"Spore-DriveRotation":       [0, App.PI * 2 / 1.5 * 253.0/256, 0],
			"Spore-DrivePosition":       [0, 0, 0],
			"Spore-DriveDuration":       15.0,
			},
		],
		"copy2":     ["crossfieldSporeCopy", {
			"Experimental": 1,
			"SetScale": 1.0,
			"ResetToPrevious": 1,
			"IgnoreSpore-DriveExit": 1,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"Spore-DriveRotation":       [0, App.PI * 2 / 1.5 * 252.0/256, 0],
			"Spore-DrivePosition":       [0, 0, 0],
			"Spore-DriveDuration":       20.0,
			},
		],
		"copy3":     ["crossfieldSporeCopy", {
			"Experimental": 1,
			"SetScale": 1.0,
			"ResetToPrevious": 1,
			"IgnoreSpore-DriveExit": 1,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"Spore-DriveRotation":       [0, App.PI * 2 / 1.5 * 241.0/256, 0],
			"Spore-DrivePosition":       [0, 0, 0],
			"Spore-DriveDuration":       25.0,
			},
		],
		"copy4":     ["crossfieldSporeCopy", {
			"Experimental": 1,
			"SetScale": 1.0,
			"ResetToPrevious": 1,
			"IgnoreSpore-DriveExit": 1,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"Spore-DriveRotation":       [0, App.PI * 2 / 1.5 * 121.0/128, 0],
			"Spore-DrivePosition":       [0, 0, 0],
			"Spore-DriveDuration":       30.0,
			},
		],
	},
}

if menuGroup:           Foundation.ShipDef.crossfield.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.crossfield.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
