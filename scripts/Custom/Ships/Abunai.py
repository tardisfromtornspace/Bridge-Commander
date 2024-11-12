##### Created by:
##### Bridge Commander Ship Menu Creator v3.0



import App
import Foundation



abbrev = 'Abunai'
iconName = 'Abunai'
longName = 'Abunai Class'
shipFile = 'Abunai'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.Abunai = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


# Foundation.ShipDef.Abunai.fMaxWarp
# Foundation.ShipDef.Abunai.fCruiseWarp
Foundation.ShipDef.Abunai.desc = 'This is The Abunai (Dangerous) Class. She is a GOD ship that can finish big fleets in seconds.'


if menuGroup:           Foundation.ShipDef.Abunai.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Abunai.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
