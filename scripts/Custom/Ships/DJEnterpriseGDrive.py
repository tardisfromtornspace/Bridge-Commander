#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DJEnterpriseGDrive"
iconName = "DJEnterpriseGDrive"
longName = "Ent G Drive"
shipFile = "DJEnterpriseGDrive"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.DJEnterpriseGDrive = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DJEnterpriseGDrive.desc = "Drive section of the Enterprise G."
Foundation.ShipDef.DJEnterpriseGDrive.SubMenu = "Eclipse Class"
Foundation.ShipDef.DJEnterpriseGDrive.SubSubMenu = "DJ Enterprise G"
Foundation.ShipDef.DJEnterpriseGDrive.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.DJEnterpriseGDrive.fCruiseWarp = 8.5 + 0.0001


Foundation.ShipDef.DJEnterpriseGDrive.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 20,
	'Multivectral Shields': 20,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor", "Aft Ablative Armor", "Dorsal Ablative Armor", "Ventral Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.DJEnterpriseGDrive.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJEnterpriseGDrive.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
