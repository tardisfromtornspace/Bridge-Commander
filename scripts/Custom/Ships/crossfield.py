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
			"Spore-Drive": {	"Nacelles": [], "Core": ["Spore-Drive Chamber"], },
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
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"Spore-DriveRotation":       [0, -4, 0],
			"Spore-DrivePosition":       [0, 0, 0],
			"Spore-DriveDuration":       150.0,
			},
		],
		"copy2":     ["crossfieldSporeCopy", {
			"Experimental": 1,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"Spore-DriveRotation":       [0, -8, 0],
			"Spore-DrivePosition":       [0, 0, 0],
			"Spore-DriveDuration":       200.0,
			},
		],
		"copy3":     ["crossfieldSporeCopy", {
			"Experimental": 1,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"Spore-DriveRotation":       [0, -12, 0],
			"Spore-DrivePosition":       [0, 0, 0],
			"Spore-DriveDuration":       250.0,
			},
		],
		"copy4":     ["crossfieldSporeCopy", {
			"Experimental": 1,
			"SetScale": 1.0,
			"Position":             [0, 0, 0],
			"Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
			"Spore-DriveRotation":       [0, -16, 0],
			"Spore-DrivePosition":       [0, 0, 0],
			"Spore-DriveDuration":       300.0,
			},
		],
	},
}

if menuGroup:           Foundation.ShipDef.crossfield.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.crossfield.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
