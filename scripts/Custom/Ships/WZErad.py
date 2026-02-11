from bcdebug import debug
import Foundation
import App

abbrev = 'WZErad'
iconName = 'Eradicator'
longName = 'CB Eradicator'
shipFile = 'WZErad'
menuGroup = 'ZZ Ships'
playerMenuGroup = 'ZZ Ships'
SubMenu = "Andromedans WZ"
SubSubMenu = "TMP"
species = App.SPECIES_GALAXY

Foundation.ShipDef.WZErad = Foundation.FedShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.WZErad.desc = 'Pray to the Omnissiah it works'

Foundation.ShipDef.WZErad.dTechs = {"AutoTargeting": { "Phaser": [4, 1] },
	"Andromedan absorption Armor": [0.0001, "Power Absorber", {
			"Torpedoes": [],
			"Tractors": [],
			"BeamsFactor": 1.0,
			"PulsesFactor": 1.0,
			"GlobalFactor": 1.0,
			"HealDepletes": 0,
			"DmgStrMod": 0.0,
			"DmgRadMod": 0.0,
		}
	],
	"Andromedan Tractor-Repulsor Beams Weapon": [{"HullDmgMultiplier": 800.0, "ShieldDmgMultiplier": 4.0}, ["Andromedan Tractor-Repulsor Beam"]],
}



if menuGroup:
    Foundation.ShipDef.WZErad.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.WZErad.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]