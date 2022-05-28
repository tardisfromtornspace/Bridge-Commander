##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation



abbrev = 'WCID4alienattacker'
iconName = 'WCID4alienattacker'
longName = 'Alien Attacker'
shipFile = 'WCID4alienattacker'
species = App.SPECIES_GALAXY
SubMenu = 'Alien Attacker'
menuGroup = 'Independence Day Ships'
playerMenuGroup = 'Independence Day Ships'


Foundation.ShipDef.WCID4alienattacker = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCID4alienattacker.fMaxWarp
# Foundation.ShipDef.WCID4alienattacker.fCruiseWarp
Foundation.ShipDef.WCID4alienattacker.desc = "Alien Attacker"

if menuGroup:           Foundation.ShipDef.WCID4alienattacker.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCID4alienattacker.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]