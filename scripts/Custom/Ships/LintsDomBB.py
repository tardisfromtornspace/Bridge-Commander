##### Created by:
##### Bridge Commander Ship Menu Creator v4.0



import App
import Foundation



abbrev = 'LintsDomBB'
iconName = 'LintsDomBB'
longName = 'Upgraded Dominion Battleship'
shipFile = 'LintsDomBB'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Dominion Ships'
playerMenuGroup = 'Dominion Ships'


Foundation.ShipDef.LintsDomBB = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


# Foundation.ShipDef.LintsDomBB.fMaxWarp
# Foundation.ShipDef.LintsDomBB.fCruiseWarp
Foundation.ShipDef.LintsDomBB.desc = 'An upgraded variant of the original Dominion Battleship'


if menuGroup:           Foundation.ShipDef.LintsDomBB.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.LintsDomBB.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
