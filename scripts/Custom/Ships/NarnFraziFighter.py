#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "NarnFraziFighter"
iconName = "NarnFraziFighter"
longName = "Frazi Fighter"
shipFile = "NarnFraziFighter"
species = App.SPECIES_SHUTTLE
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Narn Regime"
SubSubMenu = "Fighters"

Foundation.ShipDef.NarnFraziFighter = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.NarnFraziFighter.dTechs = {
	'Simulated Point Defence' : { "Distance": 10.0, "InnerDistance": 3.0, "Effectiveness": 0.7, "LimitTurn": 4.4, "LimitSpeed": 70, "LimitDamage": "-120", "Period": 0.5, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}},
	"Tachyon Sensors": 2.4
}
Foundation.ShipDef.NarnFraziFighter.desc = "The Frazi class heavy fighter was the predominant class of fighter spacecraft utilized by the Narn Regime and was manufactured by Ma'Kan Industries at the Wings of G'Lan Orbital facility over Narn."

if menuGroup:           Foundation.ShipDef.NarnFraziFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NarnFraziFighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
