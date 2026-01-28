from bcdebug import debug
import Foundation
import App

abbrev = 'WZAggravS'
iconName = 'WZAggrav'
longName = 'DD Aggravator'
shipFile = 'WZAggravS'
menuGroup = 'ZZ Ships'
playerMenuGroup = 'ZZ Ships'
SubMenu = "Andromedans WZ"
species = App.SPECIES_GALAXY

Foundation.ShipDef.WZAggravS = Foundation.FedShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.WZAggravS.desc = 'Pray to the Omnissiah it works'

Foundation.ShipDef.WZAggravS.dTechs = {
	"Andromedan absorption Armor": [50000, "Ablative Armor", {
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
}


if menuGroup:
    Foundation.ShipDef.WZAggravS.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.WZAggravS.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]