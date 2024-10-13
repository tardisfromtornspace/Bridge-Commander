#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "AndSlipFighterMK1"
iconName = "AndSlipFighter"
longName = "Slipfighter MK-I"
shipFile = "AndSlipFighterMK1"
species = App.SPECIES_GALAXY
menuGroup = "Andromeda"
playerMenuGroup = "Andromeda"
SubMenu = "System´s Commonwealth"
SubSubMenu = "Slipfighters"
Foundation.ShipDef.AndSlipFighterMK1 = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.AndSlipFighterMK1.dTechs = {
	'Simulated Point Defence' : { "Distance": 120.0, "InnerDistance": 15.0, "Effectiveness": 0.3, "LimitTurn": 5.2, "LimitSpeed": 300, "Period": 1.0, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}}
}

Foundation.ShipDef.AndSlipFighterMK1.desc = "The RF-42 Centaur Tactical Fighter red variant"


if menuGroup:           Foundation.ShipDef.AndSlipFighterMK1.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AndSlipFighterMK1.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
