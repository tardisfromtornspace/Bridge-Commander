#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DJEnterpriseGSaucer"
iconName = "DJEnterpriseGSaucer"
longName = "Ent G Saucer"
shipFile = "DJEnterpriseGSaucer"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.DJEnterpriseGSaucer = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DJEnterpriseGSaucer.desc = "Saucer section of the Enterprise G."
Foundation.ShipDef.DJEnterpriseGSaucer.SubMenu = "Eclipse Class"
Foundation.ShipDef.DJEnterpriseGSaucer.SubSubMenu = "DJ Enterprise G"


Foundation.ShipDef.DJEnterpriseGSaucer.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 45,
	'Multivectral Shields': 20,
	"Transphasic Torpedo Immune": 1,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor", "Aft Ablative Armor", "Dorsal Ablative Armor", "Ventral Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.DJEnterpriseGSaucer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJEnterpriseGSaucer.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
