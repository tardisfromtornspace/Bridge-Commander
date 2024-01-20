import Foundation
import App

abbrev = 'BarrierMain'
iconName = 'BarrierMain'
longName = 'Barrier Main Hull'
shipFile = 'BarrierMain'
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY

Foundation.ShipDef.BarrierMain = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.BarrierMain.fMaxWarp = 9.976
Foundation.ShipDef.BarrierMain.fCruiseWarp = 8.7
Foundation.ShipDef.BarrierMain.dTechs = { 'Breen Drainer Immune': 1, 'Ablative Armour': 9250 }

Foundation.ShipDef.BarrierMain.desc = "Barrier Class Main Hull"

if menuGroup:           Foundation.ShipDef.BarrierMain.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BarrierMain.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

