#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "DJEnterpriseGDrive"
iconName = "DJEnterpriseGDrive"
longName = "Ent G Drive"
shipFile = "DJEnterpriseGDrive"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.DJEnterpriseGDrive = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.DJEnterpriseGDrive = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.DJEnterpriseGDrive.desc = "Drive section of the Enterprise G."
Foundation.ShipDef.DJEnterpriseGDrive.SubMenu = "Eclipse Class"
Foundation.ShipDef.DJEnterpriseGDrive.SubSubMenu = "DJ Enterprise G"
Foundation.ShipDef.DJEnterpriseGDrive.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.DJEnterpriseGDrive.fCruiseWarp = 8.5 + 0.0001
Foundation.ShipDef.DJEnterpriseGDrive.OverrideWarpFXColor = Foundation.ShipDef.DJEnterpriseGDrive.OverrideWarpFXColor
Foundation.ShipDef.DJEnterpriseGDrive.OverridePlasmaFXColor = Foundation.ShipDef.DJEnterpriseGDrive.OverridePlasmaFXColor


Foundation.ShipDef.DJEnterpriseGDrive.dTechs = {
	"Borg Attack Resistance": 35,
	'Transphasic Torpedo Immune': 1,
	'Drainer Immune': 1,
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 45,
	'Multivectral Shields': 30,
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.DJEnterpriseGDrive.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJEnterpriseGDrive.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
