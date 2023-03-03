#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Phenom"
iconName = "Phenom"
longName = "USS-Phenom"
shipFile = "Phenom"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.Phenom = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Phenom.desc = "USS-Phenom NCC-965 \nwas the next ship of it\'s class. Captain of USS Phenom was Cpt.Milen Petrov Phenom was the second ship of her class, fitted with stronger hull plating and better tactical/defense systems. The ship was built in April 2171 and came into service since July 2171 to February 2238. in 2180 Phenom has been recalled back to sector 001 for much needed refit."
Foundation.ShipDef.Phenom.SubMenu = "Yorktown Class"
Foundation.ShipDef.Phenom.fMaxWarp = 5.75 + 0.0001
Foundation.ShipDef.Phenom.fCruiseWarp = 3.8 + 0.0001
Foundation.ShipDef.Phenom.fCrew = 240
Foundation.ShipDef.Phenom.dTechs = {
	'Polarized Hull Plating': { "Plates": ["Hull"]
}}


if menuGroup:           Foundation.ShipDef.Phenom.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Phenom.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
