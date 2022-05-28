##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation



abbrev = 'WCcitydest'
iconName = 'WCcitydest'
longName = 'Attack Mode'
shipFile = 'WCcitydest'
species = App.SPECIES_GALAXY
SubMenu = 'City Destroyer'
menuGroup = 'Independence Day Ships'
playerMenuGroup = 'Independence Day Ships'


Foundation.ShipDef.WCcitydest = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCcitydest.fMaxWarp
# Foundation.ShipDef.WCcitydest.fCruiseWarp
Foundation.ShipDef.WCcitydest.desc = "Alien City Destroyer Attack Mode"

if menuGroup:           Foundation.ShipDef.WCcitydest.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCcitydest.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]