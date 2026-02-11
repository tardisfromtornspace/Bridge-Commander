from bcdebug import debug
import Foundation
import App

abbrev = 'WZDetec'
iconName = 'Detector'
longName = 'FF Detector'
shipFile = 'WZDetec'
menuGroup = 'ZZ Ships'
playerMenuGroup = 'ZZ Ships'
SubMenu = "Andromedans WZ"
SubSubMenu = "TMP"
species = App.SPECIES_GALAXY

Foundation.ShipDef.WZDetec = Foundation.FedShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.WZDetec.desc = """Andromedan Detector Frigate/Satship"""

Foundation.ShipDef.WZDetec.dTechs = {
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
	"Andromedan Tractor-Repulsor Beams Weapon": [{"HullDmgMultiplier": 400.0, "ShieldDmgMultiplier": 1.0}, ["Andromedan Tractor-Repulsor Beam"]],
}



if menuGroup:
    Foundation.ShipDef.WZDetec.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.WZDetec.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]