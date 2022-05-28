##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation



abbrev = 'WCcitydestclosed'
iconName = 'WCcitydest'
longName = 'Flight Mode'
shipFile = 'WCcitydestclosed'
species = App.SPECIES_GALAXY
SubMenu = 'City Destroyer'
menuGroup = 'Independence Day Ships'
playerMenuGroup = 'Independence Day Ships'


Foundation.ShipDef.WCcitydestclosed = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCcitydestclosed.fMaxWarp
# Foundation.ShipDef.WCcitydestclosed.fCruiseWarp
Foundation.ShipDef.WCcitydestclosed.desc = "Alien City Destroyer Flight Mode"

if menuGroup:           Foundation.ShipDef.WCcitydestclosed.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCcitydestclosed.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]