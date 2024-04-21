#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "AshenShuumtian"
iconName = "AshenShuumtian"
longName = "Ashen Shuumtian"
shipFile = "AshenShuumtian"
species = App.SPECIES_GALAXY
menuGroup = "Non canon X-Overs"
playerMenuGroup = "Non canon X-Overs"
SubMenu = "Minbari-Ashen Minbari Alliance"
Foundation.ShipDef.AshenShuumtian = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.AshenShuumtian.desc = "The Ashen Shuumtian class warcruiser was a parallel evolution of the Sharlin, developed by an aggresive tribe of Minbari raised by the Vorlons in case the Minbari weren't powerful enough to defeat the Shadows or the circle was broken. Due to their more aggresive nature, they have been constantly at war to Shadow influenced races and in consequence their ships are more advanced in terms of weaponry and armor."
Foundation.ShipDef.AshenShuumtian.SubSubMenu = "Capital Ships"
Foundation.ShipDef.AshenShuumtian.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.AshenShuumtian.fCruiseWarp = 6 + 0.0001
Foundation.ShipDef.AshenShuumtian.dTechs = {
	'Regenerative Shields': 20,
	'Fed Ablative Armor': { "Plates": ["PolyCrystalline Armour"]},
	"Fool Targeting": {
		"Minbari Stealth": {
			"Miss": 2000.0,
			"Sensor": 1000,
		}  
	},
	"Tachyon Sensors": 0.5
}


if menuGroup:           Foundation.ShipDef.AshenShuumtian.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AshenShuumtian.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
