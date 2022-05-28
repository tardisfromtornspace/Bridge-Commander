##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation



abbrev = 'WCID4captfighter'
iconName = 'WCID4captfighter'
longName = 'Captured Alien Fighter'
shipFile = 'WCID4captfighter'
species = App.SPECIES_GALAXY
SubMenu = 'Alien Attacker'
menuGroup = 'Independence Day Ships'
playerMenuGroup = 'Independence Day Ships'


Foundation.ShipDef.WCID4captfighter = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCID4captfighter.fMaxWarp
# Foundation.ShipDef.WCID4captfighter.fCruiseWarp
Foundation.ShipDef.WCID4captfighter.desc = "Captured Alien Fighter"

if menuGroup:           Foundation.ShipDef.WCID4captfighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCID4captfighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]