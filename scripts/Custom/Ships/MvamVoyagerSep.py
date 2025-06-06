#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "MvamVoyagerSep"
iconName = "MvamVoyagerSep"
longName = "USS Voyager Separated"
shipFile = "MvamVoyagerSep"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
SubMenu = "USS Voyager"
Foundation.ShipDef.MvamVoyagerSep = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.MvamVoyagerSep.dTechs = {
	'Breen Drainer Immune': 1,
	'Regenerative Shields': 5,
	'Multivectral Shields': 5,
	'Fed Ablative Armor': { "Plates": ["Ablative Armor"]
}}

Foundation.ShipDef.MvamVoyagerSep.desc = "The USS Voyager (NCC-74656) was a 24th century Federation Intrepid-class starship operated by Starfleet. The vessel was famous for completing a non-scheduled seven-year journey across the Delta Quadrant between 2371 and 2378, which was the first successful exploration of that quadrant by the Federation. "

if menuGroup:           Foundation.ShipDef.MvamVoyagerSep.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MvamVoyagerSep.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
