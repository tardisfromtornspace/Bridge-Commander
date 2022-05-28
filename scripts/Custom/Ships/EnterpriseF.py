#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "EnterpriseF"
iconName = "Century"
longName = "Enterprise F"
shipFile = "EnterpriseF"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.EnterpriseF = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.EnterpriseF.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 30,
	'Multivectral Shields': 20,
	'Fed Ablative Armor': { "Plates": ["Aft Ablative Armor", "Engineering Ablative Armor", "Top Ablative Armor", "Forward Ablative Armor"]
}}

Foundation.ShipDef.EnterpriseF.desc = "The USS Enterprise (NCC-1701-F) was an Odyssey-class starship in service during the 25th century. The second ship of her class, she was launched in 2409."


if menuGroup:           Foundation.ShipDef.EnterpriseF.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseF.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
