#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DRA_Shuttle"
iconName = "DRA_Shuttle"
longName = "Drakh Shuttle"
shipFile = "DRA_Shuttle"
species = App.SPECIES_SHUTTLE
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Drakh Horde"
SubSubMenu = "Shuttles"
Foundation.ShipDef.DRA_Shuttle = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.DRA_Shuttle.dTechs = {
	'Simulated Point Defence' : { "Distance": 25.0, "InnerDistance": 5.0, "Effectiveness": 0.6, "LimitTurn": 2.5, "LimitSpeed": 65, "LimitDamage": "-150", "Period": 0.5, "MaxNumberTorps": 1, "Phaser": {"Priority": 1}},
	"Tachyon Sensors": 0.9
}

Foundation.ShipDef.DRA_Shuttle.desc = "The Drakh shuttle (also refereed to as a life-pod) was a type of vessel used by the Drakh to transport personnel between larger ships. In 2261, a Drakh emissary took a shuttle to board Delenn's White Star to parley following a series of attacks on League ships."


if menuGroup:           Foundation.ShipDef.DRA_Shuttle.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DRA_Shuttle.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
