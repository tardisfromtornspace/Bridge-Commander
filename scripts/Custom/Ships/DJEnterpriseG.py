#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DJEnterpriseG"
iconName = "DJEnterpriseG"
longName = "DJEnterpriseG"
shipFile = "DJEnterpriseG"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.DJEnterpriseG = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DJEnterpriseG.desc = "This is the eigth Federation Starship called Enterprise."
Foundation.ShipDef.DJEnterpriseG.SubMenu = "Eclipse Class"
Foundation.ShipDef.DJEnterpriseG.SubSubMenu = "DJ Enterprise G"
Foundation.ShipDef.DJEnterpriseG.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.DJEnterpriseG.fCruiseWarp = 8.5 + 0.0001

Foundation.ShipDef.DJEnterpriseG.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 20,
	'Multivectral Shields': 20,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor", "Aft Ablative Armor", "Dorsal Ablative Armor", "Ventral Ablative Armor"]}
}

if menuGroup:           Foundation.ShipDef.DJEnterpriseG.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJEnterpriseG.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
