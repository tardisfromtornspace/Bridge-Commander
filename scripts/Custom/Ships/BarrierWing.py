import Foundation
import App

abbrev = 'BarrierWing'
iconName = 'BarrierWing'
longName = 'Barrier Attack Wing'
shipFile = 'BarrierWing' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY

Foundation.ShipDef.BarrierWing = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.BarrierWing.dTechs = { 'Breen Drainer Immune': 1, 'Ablative Armour': 3500 }

Foundation.ShipDef.BarrierWing.desc = "Barrier Class Attack Wing"

if menuGroup:           Foundation.ShipDef.BarrierWing.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BarrierWing.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
