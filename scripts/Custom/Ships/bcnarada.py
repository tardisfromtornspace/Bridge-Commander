##### Created by:
##### Bridge Commander Ship Menu Creator v5.6



import App
import Foundation
import BaznaradaShipDef


abbrev = 'bcnarada'
iconName = 'bcnarada'
longName = 'Baz1701 Narada'
shipFile = 'bcnarada'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Romulan Ships'
playerMenuGroup = 'Romulan Ships'


Foundation.ShipDef.bcnarada = BaznaradaShipDef.BaznaradaShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


# Foundation.ShipDef.bcnarada.fMaxWarp
# Foundation.ShipDef.bcnarada.fCruiseWarp
Foundation.ShipDef.bcnarada.desc = "Patroling the outer rim of the Federation near the Romulan border the U.S.S. Kelvin had a deadly ecounter with this 25th Century Mining Ship modified with Borg technology"

Foundation.ShipDef.bcnarada.SubMenu = "Baz1701 ships"

if menuGroup:           Foundation.ShipDef.bcnarada.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.bcnarada.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

