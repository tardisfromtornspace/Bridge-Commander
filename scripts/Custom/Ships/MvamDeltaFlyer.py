#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "MvamDeltaFlyer"
iconName = "MvamDeltaFlyer"
longName = "Delta Flyer"
shipFile = "MvamDeltaFlyer"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
SubMenu = "USS Voyager"
Foundation.ShipDef.MvamDeltaFlyer = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.MvamDeltaFlyer.dTechs = {
	'Breen Drainer Immune': 1,
	'Regenerative Shields': 30,
}

Foundation.ShipDef.MvamDeltaFlyer.desc = "The Delta Flyer was a specially designed Starfleet shuttlecraft constructed by the crew of the USS Voyager in the Delta Quadrant in 2375.  It featured a warp-streamlined tetraburnium alloy hull, retractable warp nacelles, parametallic hull plating, unimatrix shielding, and a Borg-inspired weapon system."
Foundation.ShipDef.MvamDeltaFlyer.SubMenu = "USS Voyager"

if menuGroup:           Foundation.ShipDef.MvamDeltaFlyer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MvamDeltaFlyer.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
