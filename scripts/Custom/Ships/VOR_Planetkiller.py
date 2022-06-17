#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "VOR_Planetkiller"
iconName = "Vorlon_Planetkiller"
longName = "Vorlon Planetkiller"
shipFile = "VOR_Planetkiller"
species = App.SPECIES_SOVEREIGN
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Vorlon Empire"
Foundation.ShipDef.VOR_Planetkiller = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.VOR_Planetkiller.dTechs = {'Breen Drainer Immune': 1}
Foundation.ShipDef.VOR_Planetkiller.bPlanetKiller = 1

Foundation.ShipDef.VOR_Planetkiller.desc = "The Vorlon planet killer was an enormous type of ship used by the Vorlon Empire to destroy entire planets. The planet killers were first discovered by the younger races in 2261 when White Star 2 detected a fleet of thousands of ships led by two planet killers in Hyperspace in Sector 70 by 10 by 53. Shortly afterwards the fleet moved in on Arcata VII and the planet was reduced to rubble."


if menuGroup:           Foundation.ShipDef.VOR_Planetkiller.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VOR_Planetkiller.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
