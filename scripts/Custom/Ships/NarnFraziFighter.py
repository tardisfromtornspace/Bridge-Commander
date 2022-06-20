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
Foundation.ShipDef.NarnFraziFighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.NarnFraziFighter.desc = "The Frazi class heavy fighter was the predominant class of fighter spacecraft utilized by the Narn Regime and was manufactured by Ma'Kan Industries at the Wings of G'Lan Orbital facility over Narn."


if menuGroup:           Foundation.ShipDef.NarnFraziFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NarnFraziFighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
