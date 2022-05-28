#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "AndSlipFighter"
iconName = "AndSlipFighter"
longName = "Slipfighter"
shipFile = "AndSlipFighter"
species = App.SPECIES_GALAXY
menuGroup = "Andromeda"
playerMenuGroup = "Andromeda"
SubMenu = "System´s Commonwealth"
Foundation.ShipDef.AndSlipFighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })


Foundation.ShipDef.AndSlipFighter.desc = "The RF-42 Centaur Tactical Fighter (in this case, red variant) is the premiere space superiority Slipfighter in the High Guard fleet. Designed to conduct high speed, fire-and-forget combat maneuvers, it is unmatched in its ability to engage multiple targets at short to medium distances. The primary mission of the Centaur is to provide combat patrol support for Glorious Heritage Class cruisers and Atmospheric Attack Craft Carriers. It also flies tactical escort for strike fighters and conducts suppression of enemy defense operations during interplanetary combat. "


if menuGroup:           Foundation.ShipDef.AndSlipFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AndSlipFighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
