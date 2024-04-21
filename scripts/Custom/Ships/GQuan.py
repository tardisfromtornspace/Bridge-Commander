#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "GQuan"
iconName = "GQuan"
longName = "G´Quan"
shipFile = "GQuan"
species = App.SPECIES_GALAXY
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "Narn Regime"
SubSubMenu = "Capital ships"

Foundation.ShipDef.GQuan = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.EAPsiCorpCrewShuttle.dTechs = {
	"Tachyon Sensors": 2.4
}

Foundation.ShipDef.GQuan.desc = "G'Quan class heavy cruisers are the backbone of the Narn Regime's naval forces. Ma'Kan Industries located at Wings of G'Lan facility over Narn is responsible for manufactoring this class of vessel."

if menuGroup:           Foundation.ShipDef.GQuan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GQuan.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
