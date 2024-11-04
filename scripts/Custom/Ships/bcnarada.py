##### Created by:
##### Bridge Commander Ship Menu Creator v5.6



import App
import Foundation
import traceback


abbrev = 'bcnarada'
iconName = 'bcnarada'
longName = 'Baz1701 Narada'
shipFile = 'bcnarada'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Romulan Ships'
playerMenuGroup = 'Romulan Ships'

worked = 0
try:
	import Custom.Autoload.RaceBaznarada
	Foundation.ShipDef.bcnarada = Foundation.BaznaradaShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
	worked = 1
except:
	worked = 0
	print "Error while loading a race"
	Foundation.ShipDef.bcnarada = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()

if worked == 1:
	Foundation.ShipDef.bcnarada.OverrideWarpFXColor = Foundation.ShipDef.bcnarada.OverrideWarpFXColor
	Foundation.ShipDef.bcnarada.OverridePlasmaFXColor = Foundation.ShipDef.bcnarada.OverridePlasmaFXColor

Foundation.ShipDef.bcnarada.dTechs = {
	'Breen Drainer Immune': 1,
	'Borg Adaptation': 0.1,
	'Automated Destroyed System Repair': {"Time": 300.0}
}

# Foundation.ShipDef.bcnarada.fMaxWarp
# Foundation.ShipDef.bcnarada.fCruiseWarp
Foundation.ShipDef.bcnarada.desc = "Patroling the outer rim of the Federation near the Romulan border the U.S.S. Kelvin had a deadly ecounter with this 25th Century Mining Ship modified with Borg technology"

Foundation.ShipDef.bcnarada.SubMenu = "Baz1701 ships"

if menuGroup:           Foundation.ShipDef.bcnarada.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.bcnarada.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

