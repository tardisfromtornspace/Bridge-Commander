#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DRA_Cruiser"
iconName = "DRA_Cruiser"
longName = "Drakh Cruiser"
shipFile = "DRA_Cruiser"
species = App.SPECIES_WARBIRD
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Drakh Horde"
SubSubMenu = "Carriers"
Foundation.ShipDef.DRA_Cruiser = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.DRA_Cruiser.dTechs = {
	'Simulated Point Defence' : { "Distance": 50.0, "InnerDistance": 3.0, "Effectiveness": 0.6, "LimitTurn": 0.85, "LimitSpeed": 76, "LimitDamage": "350", "Period": 1.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	"Tachyon Sensors": 0.9
}

Foundation.ShipDef.DRA_Cruiser.desc = "The Drakh cruiser was a vessel of unknown class used by the Drakh. The overall design of the vessel is essentially identical to the Drakh carrier, though on a much smaller scale. As with the carriers, the cruisers are typically accompanied by a number of Drakh fighters."


if menuGroup:           Foundation.ShipDef.DRA_Cruiser.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DRA_Cruiser.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
