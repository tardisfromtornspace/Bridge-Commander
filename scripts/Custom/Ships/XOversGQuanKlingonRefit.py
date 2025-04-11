#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "GQuanKlingonRefit"
iconName = "GQuan"
longName = "G´Quan Refit"
shipFile = "GQuanKlingonRefit"
species = App.SPECIES_GALAXY
menuGroup = "Non canon X-Overs"
playerMenuGroup = "Non canon X-Overs"
SubMenu = "Narn-Klingon Alliance"
Foundation.ShipDef.GQuanKlingonRefit = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.GQuanKlingonRefit.dTechs = {
	"Tachyon Sensors": 1.4
}

Foundation.ShipDef.GQuanKlingonRefit.desc = "In a parallel multiverse where the Centauri attacked a paralel under-developed Quo'nos, enslaving and hunting the paralel Klingons, when a lost ST 24th century Klingon fleet discovered that because of a space rift they were enraged and started to attack the Centauri on skirmishes. During one of them they offered assistance to a damaged G'Quan. Knowing that the Narns had their own similar history, they decided to help them in repairs and some minor upgrades in order to give the new ally a decent advantage in a 1 vs 1 skirmish"


if menuGroup:           Foundation.ShipDef.GQuanKlingonRefit.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GQuanKlingonRefit.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
