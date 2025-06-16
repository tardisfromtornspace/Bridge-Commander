#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "ThirdspaceCapitalShip"
iconName = "ThirdspaceCapitalShip"
longName = "Thirdspace Capital Ship"
shipFile = "ThirdspaceCapitalShip"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Thirdspace Aliens"
SubSubMenu = "Capital Ships"

Foundation.ShipDef.ThirdspaceCapitalShip = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Yeah I know thirdspace aliens don't have Vree tech, but on this case I made both of them work the same way
Foundation.ShipDef.ThirdspaceCapitalShip.dTechs = {
	"AutoTargeting": { "Pulse": [3, 0] },
	'Breen Drainer Immune': 1,
	"Vree Shields": 100,
	'No bleedthrough Shields': 100,
}

Foundation.ShipDef.ThirdspaceCapitalShip.desc = "The Thirdspace capital ships are large vessels used by the beings from Thirdspace, piloted by the Harbingers themselves. These ships are the primary spearheads of an extinction armada. Slow and relentless, these ships are capable enough to withstand assaults by entire fleets of lesser ships."


if menuGroup:           Foundation.ShipDef.ThirdspaceCapitalShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ThirdspaceCapitalShip.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
