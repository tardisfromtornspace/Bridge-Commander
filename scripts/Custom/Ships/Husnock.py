#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Husnock"
iconName = "Husnock"
longName = "Husnock Warship"
shipFile = "Husnock"
species = App.SPECIES_GALAXY
menuGroup = "Forgotten Ships"
playerMenuGroup = "Forgotten Ships"
Foundation.ShipDef.Husnock = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Husnock.desc = "This original Husnock ships belonged to a race that does not exist anymore, it was a feared race with hideous technology, and they believed in conquest and destruction, they were all eradicated by the thoughts of a Douwd. Later on, this amped-up version appeared as part of a Douwd plan to make the Enterprise leave orbit."
Foundation.ShipDef.Husnock.dTechs = {'Drainer Immune': 1, 'ChronitonTorpe Immune': 1}

if menuGroup:           Foundation.ShipDef.Husnock.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Husnock.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
