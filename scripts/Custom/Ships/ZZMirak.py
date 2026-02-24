from bcdebug import debug
import Foundation
import App

abbrev = 'ZZMirak'
iconName = 'ZZMirak'
longName = 'CC Mirak Assassin'
shipFile = 'ZZMirak'
menuGroup = 'Kzinti Ships'
playerMenuGroup = 'Kzinti Ships'
species = App.SPECIES_GALAXY

# Credits and mod information.
credits = {
	'modName': 'ZZMirak',
	'author': 'Zambie Zan alexmarques400@hotmail.com',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'Tested in KM'
}

import F_ZZAttackDef

Foundation.ShipDef.ZZMirak = F_ZZAttackDef.ZZAttackDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})

# Set the ship's description.
Foundation.ShipDef.ZZMirak.desc = "KZINTI / MIRAK WARSHIP DOSSIER\n\nDESIGNATION: Assassin Class\nHULL IDENTIFIER: IKV Killer\nEMPIRE: Kzinti Patriarchy / Mirak Clans\nTACTICAL TYPE: Predator Strike Cruiser\n\nThe Assassin Class exists for a single function: the sanctioned killing of enemy warships.\nKzinti naval doctrine rejects prolonged engagements, defensive maneuvering, and mercy. Victory is achieved by identifying the strongest prey, closing the distance with maximum aggression, and delivering lethal force before the enemy can adapt.\nCrew survivability beyond mission completion is considered irrelevant.\nThe Assassin Class operates at the front of Kzinti strike formations or alone as a hunter-killer.\n\nStandard engagement sequence:\n1. High-velocity approach.\n2. Immediate missile saturation.\n3. Phaser fire to exploit shield failure.\n4. Super weapon deployment if prey survives.\n5. Disengage or advance to next target.\n\nRetreat is doctrinally discouraged unless it enables future kills."

if menuGroup:
	Foundation.ShipDef.ZZMirak.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:
	Foundation.ShipDef.ZZMirak.RegisterQBPlayerShipMenu(playerMenuGroup)

# Handle potential conflicts if the ship already exists in the list.
if Foundation.shipList._keyList.has_key(longName):
	Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
	Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def PreLoadAssets():
    pass
