from bcdebug import debug
import Foundation
import App

abbrev = 'SWOutrider'
iconName = 'SWOutrider'
longName = 'Outrider YT-2400'
shipFile = 'SWOutrider'
menuGroup = 'ZZ Ships'
playerMenuGroup = 'ZZ Ships'
SubMenu = "Star Wars"
species = App.SPECIES_GALAXY

import K_ZZAndromedanAttackDef

Foundation.ShipDef.SWOutrider = K_ZZAndromedanAttackDef.ZZAndromedanShipDef(abbrev, species, {'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu})

Foundation.ShipDef.SWOutrider.desc = """-INITIATING DATA RETRIEVAL: SUBJECT "Correllian Engineering Corporation YT-2400 Freighter"
-BEGIN INFORMATION SUMMARY:

The YT-2400 sports the trademark saucer and cockpit configuration of the Correllian Engineering Corporation's series of freighters. Like the older YT-1300, the 2400 is a highly modifiable craft which caters to not only the legitimate transportation and cargo services, but also the not so lawful world of smuggling and piracy.

Being one of the latter, the Outrider is a veritable hotrod, sporting highly powerful engines, shields, sensor stealth packages, missile launchers, and a pair of heavy laser turrets. Captained by Dash Rendar, the Outrider is always running at peak performance and kept at the ready should the need for a fast escape or risky smuggling run arise.

-END DATA TRANSMISSION-"""


Foundation.ShipDef.SWOutrider.dTechs = {
	"AutoTargeting": {"Pulse": [4, 1]},
	'Partially Distributed Shields': {"Shield Transfer Ratio": 1.25 * 0.3, "Max Percentage Damage": 0.3, "Collapse Threshold": 0.45, "Always Heal Closest": 1.1, "Max Radians": 1.994395},
	"SW Shields": {"Thingy": 1}
}

Foundation.ShipDef.SWOutrider.fMaxWarp = 2.25
Foundation.ShipDef.SWOutrider.fCruiseWarp = 2.2

Foundation.ShipDef.SWOutrider.shutLauncherShields = -2

if menuGroup:
    Foundation.ShipDef.SWOutrider.RegisterQBShipMenu(menuGroup)

if playerMenuGroup:
    Foundation.ShipDef.SWOutrider.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
    Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
    Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]