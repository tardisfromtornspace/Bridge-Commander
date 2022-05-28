#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DCMPDefiant"
iconName = "DCMPDefiantClass"
longName = "Defiant Refit"
shipFile = "DCMPDefiant"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.DCMPDefiant = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DCMPDefiant.desc = "The Defiant class refitted after the second Borg attack in sector 001."
Foundation.ShipDef.DCMPDefiant.dTechs = {
	'Multivectral Shields': 30,
	'Fed Ablative Armor': { "Plates": ["Aft Ablative Armor", "Right Ablative Armor", "Left Ablative Armor", "Forward Ablative Armor"]
}}

if menuGroup:           Foundation.ShipDef.DCMPDefiant.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DCMPDefiant.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
