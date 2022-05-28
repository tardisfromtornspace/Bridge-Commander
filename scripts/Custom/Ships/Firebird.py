#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Firebird"
iconName = "Firebird"
longName = "Firebird"
shipFile = "Firebird"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.Firebird = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.Firebird.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 40,
	'Multivectral Shields': 20,
	'Fed Ablative Armor': { "Plates": ["Ablative Armour"]
}}

Foundation.ShipDef.Firebird.desc = "The Prometheus class (but without Mvam)."


if menuGroup:           Foundation.ShipDef.Firebird.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Firebird.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
