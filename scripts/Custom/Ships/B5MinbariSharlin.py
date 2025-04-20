#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "B5MinbariSharlin"
iconName = "MinbariSharlin"
longName = "Minbari Sharlin"
shipFile = "B5MinbariSharlin"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Minbari Federation"
SubSubMenu = "Capital Ships"

Foundation.ShipDef.B5MinbariSharlin = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })


Foundation.ShipDef.B5MinbariSharlin.desc = "The Sharlin class warcruiser was in its time the largest and most powerful ship in the Minbari fleet. They were manufactured at the Valeria-On-High Orbital Shipyards orbiting Minbar. The main capital ship of the Minbari fleet, the Sharlin's stealth systems give it an advantage over the scanning and tracking systems that when active it would prevent some of the races from achieving a positive weapons lock. The Sharlin is also equipped with advanced scanners so powerful that when set to maximum have been known to interfere with the electronics aboard less advanced starships, effectively jamming their systems. The Valen'tha, the cruiser used by the Grey Council, is a Sharlin class war cruiser."
Foundation.ShipDef.B5MinbariSharlin.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.B5MinbariSharlin.fCruiseWarp = 6 + 0.0001
Foundation.ShipDef.B5MinbariSharlin.dTechs = {
	'Regenerative Shields': 20,
	'Fed Ablative Armor': { "Plates": ["PolyCrystalline Armour"]},
	"Fool Targeting": {
		"Minbari Stealth": {
			"Miss": 1500.0,
			"Sensor": 600,
        	}  
	},
	"Tachyon Sensors": 0.5
}
#TO-DO set sensor range to 600, but for tests set it to 1200

if menuGroup:           Foundation.ShipDef.B5MinbariSharlin.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5MinbariSharlin.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
