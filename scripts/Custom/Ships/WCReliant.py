##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation



abbrev = 'WCReliant'
iconName = 'WCReliant'
longName = 'USS Reliant'
shipFile = 'WCReliant'
species = App.SPECIES_GALAXY
SubMenu = 'WC TMP Pack'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.WCReliant = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.WCReliant.fMaxWarp
# Foundation.ShipDef.WCReliant.fCruiseWarp
Foundation.ShipDef.WCReliant.desc = "USS Reliant NCC-1864"


if menuGroup:           Foundation.ShipDef.WCReliant.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCReliant.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
