from bcdebug import debug
import Foundation
import App

abbrev = 'WZVindi'
iconName = 'Vindicator'
longName = 'CX Vindicator'
shipFile = 'WZVindi'
menuGroup = 'ZZ Ships'
playerMenuGroup = 'ZZ Ships'
SubMenu = "Andromedans WZ"
SubSubMenu = "X Era"
species = App.SPECIES_GALAXY

import K_ZZAndromedanAttackDef

Foundation.ShipDef.WZVindi = K_ZZAndromedanAttackDef.ZZAndromedanShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.WZVindi.desc = 'Vindicator Class Cruiser X-Era'

Foundation.ShipDef.WZVindi.dTechs = {"AutoTargeting": { "Phaser": [6, 1] },
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
	"Andromedan Tractor-Repulsor Beams Weapon": [{"HullDmgMultiplier": 900.0, "ShieldDmgMultiplier": 5.0, "TorpLifetime": 0}, ["Andromedan Tractor-Repulsor Beam"]],
}



if menuGroup:
    Foundation.ShipDef.WZVindi.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.WZVindi.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]