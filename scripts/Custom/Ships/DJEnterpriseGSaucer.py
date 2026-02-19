#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
import traceback


abbrev = "DJEnterpriseGSaucer"
iconName = "DJEnterpriseGSaucer"
longName = "Ent G Saucer"
shipFile = "DJEnterpriseGSaucer"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"

try:
	import Custom.Autoload.RaceFutureFed25c
	Foundation.ShipDef.DJEnterpriseGSaucer = Foundation.FutureFed25cShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
except:
	print "Error while loading a race"
	Foundation.ShipDef.DJEnterpriseGSaucer = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
	traceback.print_exc()


Foundation.ShipDef.DJEnterpriseGSaucer.desc = "Saucer section of the Enterprise G."

Foundation.ShipDef.DJEnterpriseGSaucer.SubMenu = "2400s"
Foundation.ShipDef.DJEnterpriseGSaucer.SubSubMenu = "Eclipse Class"
Foundation.ShipDef.DJEnterpriseGSaucer.SubSubSubMenu = "DJ Enterprise G"

Foundation.ShipDef.DJEnterpriseGSaucer.OverrideWarpFXColor = Foundation.ShipDef.DJEnterpriseGSaucer.OverrideWarpFXColor
Foundation.ShipDef.DJEnterpriseGSaucer.OverridePlasmaFXColor = Foundation.ShipDef.DJEnterpriseGSaucer.OverridePlasmaFXColor

Foundation.ShipDef.DJEnterpriseGSaucer.dTechs = {
	"Borg Attack Resistance": 35,
	'Transphasic Torpedo Immune': 1,
	'Drainer Immune': 1,
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 55,
	'Multivectral Shields': 8,
	'Partially Distributed Shields': {"Shield Transfer Ratio": 0.1, "Max Percentage Damage": 2, "Collapse Threshold": 0.5, "Emergency Redistribute Threshold": 0.32, "Emergency Redistribute Chance": 10, "Max Radians": 0.5 * 3.141592, "ModX": 2.735 * 1.16, "ModY": 1.0, "ModZ": 9.0},
	"Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.DJEnterpriseGSaucer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJEnterpriseGSaucer.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
