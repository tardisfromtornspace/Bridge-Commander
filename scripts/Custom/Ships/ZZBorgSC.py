# File: Z (Python 1.5)

import Foundation
import App
abbrev = 'ZZBorgSC'
iconName = 'ZZBorgSC'
longName = 'ZZ Borg War C-Sphere'
shipFile = 'ZZBorgSC'
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'
species = App.SPECIES_GALAXY
credits = {
    'modName': 'ZZBorgSC',
    'author': '',
    'version': '1.0',
    'sources': [
        'http://'],
    'comments': '' }

import F_BorgAttackDef
Foundation.ShipDef.ZZBorgSC = F_BorgAttackDef.BorgAttackDef(abbrev, species, {
    'name': longName,
    'iconName': iconName,
    'shipFile': shipFile })

Foundation.ShipDef.ZZBorgSC.dTechs = {
	'Ablative Armour': 45000,
	'Breen Drainer Immune': 1,
	'Borg Adaptation': 1,
	'Automated Destroyed System Repair': {"Time": 120.0},
	"Fool Targeting": {
		"Accurate": 0.1,
	},
	'Multivectral Shields': 5,
}

Foundation.ShipDef.ZZBorgSC.fMaxWarp = 9.999

Foundation.ShipDef.ZZBorgSC.desc = "In the year 2378, following Captain Janeway's intervention from the future, where she infected the Borg with a neurolytic pathogen and Voyager destroyed one of the Unicomplex transwarp hubs, severely crippling the Borg's ability to rapidly deploy ships across the Milky Way, the few remaining Borg were forced to adapt.\n\nWith their resources now limited, they focused on producing smaller, more heavily armored and heavily armed vessels.\n\nThe first of these new designs was the C-Sphere: a hybrid of a cube and a sphere, approximately 900 meters in diameter. Unlike traditional Borg ships, the C-Sphere was not built to assimilate, but to annihilate any threat it encountered.\n\n900m\nAblative Armour (Nothing will be damaged until the armor is gone)\nMultivectral Shields (Damaged shield automatically compensates draining from all other shields)\n6x Shield Drainer Torpedo Launchers (each hit drains 20% of ALL shields)\n6x Cutting Beams\n40x Rapid fire Pulse Phasers\n8x Super Particle Cannons (semi-assimilated from species 8472)\n4x Spatial Charges (each hit creates a focused shockwave that rotates the target randomly)\n8x Heavy Pulse Disruptors\nMVAM capable (Separates into Cube and Sphere)\n1x Scout Drone (launches from hangar)"
if menuGroup:
    Foundation.ShipDef.ZZBorgSC.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.ZZBorgSC.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

