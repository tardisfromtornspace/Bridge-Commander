from bcdebug import debug
import Foundation
import App

abbrev = 'VandalWZ'
iconName = 'VandalWZ'
longName = 'DD Vandal Class'
shipFile = 'VandalWZ'
menuGroup = 'Orion Pirates Ships'
playerMenuGroup = 'Orion Pirates Ships'
SubMenu = "ZZ Orions"
species = App.SPECIES_GALAXY

# Credits and mod information.
credits = {
	'modName': 'VandalWZ',
	'author': 'Zambie Zan alexmarques400@hotmail.com',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'Tested in KM'
}


import K_ZZAndromedanAttackDef

Foundation.ShipDef.VandalWZ = K_ZZAndromedanAttackDef.ZZAndromedanShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })

Foundation.ShipDef.VandalWZ.desc = """The Vandal Class Destroyer fills the workhorse role of the Orion fleet. Equipped with the usual array of weaponry and systems as her larger sister, the Vagabond, the Vandal provides escort and raiding duties throughout the quadrant."""

Foundation.ShipDef.VandalWZ.dTechs = {
					"AutoTargeting": { "Phaser": [3, 1] },
					"Slow Start": {"Beams": [], "Pulses": [], "Torpedoes": [], "BeamsFactor": 0.0, "TorpedoesFactor": 0.8, "GlobalFactor": 0.6}
}


if menuGroup:
	Foundation.ShipDef.VandalWZ.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:
	Foundation.ShipDef.VandalWZ.RegisterQBPlayerShipMenu(playerMenuGroup)

# Handle potential conflicts if the ship already exists in the list.
if Foundation.shipList._keyList.has_key(longName):
	Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
	Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

#def PreLoadAssets():
#    pass
