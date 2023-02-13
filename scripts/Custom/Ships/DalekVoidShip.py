##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation
from Custom.Autoload.RaceDalek import *


abbrev = 'DalekVoidShip'
iconName = 'DalekVoidShip'
longName = 'Dalek Void Ship'
shipFile = 'DalekVoidShip'
species = App.SPECIES_AKIRA
# SubMenu
menuGroup = 'Doctor Who'
playerMenuGroup = 'Doctor Who'
SubMenu = "Dalek"


Foundation.ShipDef.DalekVoidShip = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "race": Dalek })

Foundation.ShipDef.DalekVoidShip.dTechs = {
	'Adv Armor Tech': 1,
	'Breen Drainer Immune': 0,
	'Drainer Immune': 1,
	'ChronitonTorpe Immune': 1,
	'Drainer Immune': 1,
	"Phased Torpedo Immune": 1,
	'Reflux Weapon': 1,
	'Regenerative Shields': 1,
	'TimeVortex Torpedo Immune': 1,
	"Void State": 0,
	"Vree Shields": 100,
	"Inversion Beam": [1, 0, 1, 1500],
	"Power Drain Beam": [1, 0, 1, 1500]
}

Foundation.ShipDef.DalekVoidShip.fMaxWarp = 9.99 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekVoidShip.fCruiseWarp = 9.999999999 + 0.0   # 0.0 makes sure that the number is a decimal number
Foundation.ShipDef.DalekVoidShip.desc = "A Void Ship was a vessel designed to exist outside Time and Space, thus being capable of traversing the Void that existed 'between' all parallel universes and dimensions. A Void Ship could protect its occupants from 'the Big Bang, the end of the universe and the start of the next', and, until it properly landed in its target dimension, could defy all forms of analysis, meaning it had no detectable mass, heat, quantifiable age or radiation. Due to these properties, people who looked upon a Void Ship found it deeply unsettling; foreboding. An invisible barrier prevented anything from the outside from having physical contact with the ship. In the Doctor's universe, Void Ships were considered by the Time Lords, including the Tenth Doctor, to be impossible to build and strictly theoretical, although TARDISes, and, through them, the Time Lords at the height of their power, were able to travel between parallel universes through different mechanisms."


if menuGroup:           Foundation.ShipDef.DalekVoidShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DalekVoidShip.RegisterQBPlayerShipMenu(playerMenuGroup)



if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
