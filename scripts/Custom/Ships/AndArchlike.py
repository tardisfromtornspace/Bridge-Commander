#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "AndArchlike"
iconName = "AndArchlike"
longName = "Andromeda Slipfighter"
shipFile = "AndArchlike"
species = App.SPECIES_GALAXY
menuGroup = "Andromeda"
playerMenuGroup = "Andromeda"
SubMenu = "System´s Commonwealth"
Foundation.ShipDef.AndArchlike = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

Foundation.ShipDef.AndArchlike.dTechs = {
	'Simulated Point Defence' : { "Distance": 120.0, "InnerDistance": 15.0, "Effectiveness": 0.3, "LimitTurn": 5.2, "LimitSpeed": 300, "Period": 1.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}}
}
Foundation.ShipDef.AndArchlike.desc = "The Type 2 Arc Light Slipfighter was a class of long-range strike fighter used by the High Guard of the Systems Commonwealth, capable of firing Nova Bombs."


if menuGroup:           Foundation.ShipDef.AndArchlike.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AndArchlike.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
