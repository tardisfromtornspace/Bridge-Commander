#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "WCDoomMachine"
iconName = "WCDoomMachine"
longName = "Doomsday Machine"
shipFile = "WCDoomMachine"
species = App.SPECIES_GALAXY
menuGroup = "Other Ships"
playerMenuGroup = "Other Ships"
Foundation.ShipDef.WCDoomMachine = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.WCDoomMachine.desc = "The 'planet killer' was an automated, self-propelled doomsday machine capable of destroying entire planets. This robot was encountered in 2267 by the Federation starships USS Constellation and USS Enterprise. Its origins were unknown, but based on its apparent trajectory, it was believed to have come from a galaxy other than the Milky Way. "
Foundation.ShipDef.WCDoomMachine.fMaxWarp = 9 + 0.0001
Foundation.ShipDef.WCDoomMachine.fCruiseWarp = 6 + 0.0001
Foundation.ShipDef.WCDoomMachine.bPlanetKiller = 1
Foundation.ShipDef.WCDoomMachine.dTechs = {
	'Fed Ablative Armor': { "Plates": ["Ablative Armour"]
}}


if menuGroup:           Foundation.ShipDef.WCDoomMachine.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCDoomMachine.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
