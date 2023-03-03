import Foundation
import App


### Integrated Ship ###


abbrev = 'ArsenalIntegrated'
iconName = 'Arsenal'
longName = 'Arsenal Class'
shipFile = 'ArsenalIntegrated' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY

Foundation.ShipDef.ArsenalIntegrated = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.ArsenalIntegrated.fMaxWarp = 9.997
Foundation.ShipDef.ArsenalIntegrated.fCruiseWarp = 9.0
Foundation.ShipDef.ArsenalIntegrated.dTechs = {
	'Breen Drainer Immune': 1, 'Multivectral Shields': 80, 
	'Fed Ablative Armor': { "Plates": [ "Saucer Ablative Armor", 
							"Engineering Ablative Armor", 
							"Port Dorsal Nacelle Armor", 
							"Star Dorsal Nacelle Armor", 
							"Port Ventral Nacelle Armor", 
							"Star Ventral Nacelle Armor"] }}

Foundation.ShipDef.ArsenalIntegrated.desc = "Arsenal Class Borg Hunter"

if menuGroup:           Foundation.ShipDef.ArsenalIntegrated.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ArsenalIntegrated.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


### Seperated Ship ###


abbrev = 'ArsenalSeperated'
iconName = 'Arsenal'
longName = 'Arsenal Seperated'
shipFile = 'ArsenalSeperated' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY

Foundation.ShipDef.ArsenalSeperated = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.ArsenalSeperated.fMaxWarp = 9.997
Foundation.ShipDef.ArsenalSeperated.fCruiseWarp = 9.0
Foundation.ShipDef.ArsenalSeperated.dTechs = {
	'Breen Drainer Immune': 1, 'Multivectral Shields': 80, 
	'Fed Ablative Armor': { "Plates": [ "Saucer Ablative Armor", 
							"Engineering Ablative Armor", 
							"Port Dorsal Nacelle Armor", 
							"Star Dorsal Nacelle Armor", 
							"Port Ventral Nacelle Armor", 
							"Star Ventral Nacelle Armor"] }}

Foundation.ShipDef.ArsenalSeperated.desc = "Arsenal Class Borg Hunter"

if menuGroup:           Foundation.ShipDef.ArsenalSeperated.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ArsenalSeperated.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]


### Auxillary Ship ###


abbrev = 'Gladiator'
iconName = 'Gladiator'
longName = 'Gladiator Class'
shipFile = 'Gladiator' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY

Foundation.ShipDef.Gladiator = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.Gladiator.fMaxWarp = 9.75
Foundation.ShipDef.Gladiator.fCruiseWarp = 8.5
Foundation.ShipDef.Gladiator.dTechs = { 'Breen Drainer Immune': 1, 'Multivectral Shields': 80, 
                                        'Fed Ablative Armor': { "Plates": [ "Fwd Ablative Armor", 
							                                  "Aft Ablative Armor", 
							                                  "Port Ablative Armor", 
							                                  "Star Ablative Armor" ] }}


Foundation.ShipDef.Gladiator.desc = "Gladiator Class Arsenal Auxillary Attack Ship"

if menuGroup:           Foundation.ShipDef.Gladiator.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Gladiator.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]