#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Vorchan"
iconName = "Vorchan"
longName = "Vorchan"
shipFile = "Vorchan"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Centauri Republic"
Foundation.ShipDef.Vorchan = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubMenu": SubMenu })


Foundation.ShipDef.Vorchan.desc = "The Vorchan class medium warship is one of the newer starships in the Centauri fleet. Ships of this class were built by House Tavari Armaments at the Hevaria Orbital Shipyards over Tolonius VII. Usually its primarily use is as an escort for carrier fleets and as a fast interceptor. Though often operating in small squadrons, they are sometimes sent out alone to carry out hit-and-run tactical strikes. This warship is also configured for atmospheric flight. The warships´ weaponry consists of 2 twin plasma acceletors, missiles for planetary bombardment and guided mines. The plasma accelerators are used by Centauri forces mainly in a configuration which causes explosive damage to the target rather than slicing through its hull."


if menuGroup:           Foundation.ShipDef.Vorchan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Vorchan.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
