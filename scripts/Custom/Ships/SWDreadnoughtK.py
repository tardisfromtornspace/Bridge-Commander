from bcdebug import debug
import Foundation
import App

abbrev = 'SWDreadnoughtK'
iconName = 'SWDreadnoughtK'
longName = 'Katana'
shipFile = 'SWDreadnoughtK'
menuGroup = 'ZZ Ships'
playerMenuGroup = 'ZZ Ships'
SubMenu = "Star Wars"
SubSubMenu = "Dreadnought Class Heavy Cruiser"
species = App.SPECIES_GALAXY

import K_ZZAndromedanAttackDef

Foundation.ShipDef.SWDreadnoughtK = K_ZZAndromedanAttackDef.ZZAndromedanShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.SWDreadnoughtK.desc = """The Dreadnought Heavy Cruiser was one of the mainstays of the Old Republic fleet, outclassed only by the Star Destroyers of later years. Equipped with dozens of turbolaser, laser, ion cannon, missile, and torpedo weapons systems, the Dreadnoughts are tough and potent ships.

Even after the Old Republic's fall and the rise of the Empire, the Dreadnoughts were still sought after by all of the major warring factions. The most notable of which was the search for the long lost Katana Fleet (aka the Dark Force) of nearly two hundred Dreadnoughts, which was eventually found and taken by the Imperial forces then under command of Grand Admiral Thrawn. The Dreadnoughts proved vital to Thrawn's campaign against the New Republic, bolstering the weakened Imperial navy and providing support to the larger Star Destroyers.

Despite the defeat of the Empire and the death of the top leaders, including Thrawn himself, the Dreadnoughts nonetheless were proven to be an important aspect of any navy."""


Foundation.ShipDef.SWDreadnoughtK.dTechs = {
	"AutoTargeting": {"Pulse": [10, 1]},
	'Partially Distributed Shields': {"Shield Transfer Ratio": 1.25 * 0.3, "Max Percentage Damage": 0.3, "Collapse Threshold": 0.38, "Always Heal Closest": 1.1, "Max Radians": 1.994395},
	"SW Shields": {"Thingy": 1}
}

Foundation.ShipDef.SWDreadnoughtK.fMaxWarp = 2.25
Foundation.ShipDef.SWDreadnoughtK.fCruiseWarp = 2.2

Foundation.ShipDef.SWDreadnoughtK.shutLauncherShields = -2

if menuGroup:
    Foundation.ShipDef.SWDreadnoughtK.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.SWDreadnoughtK.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]