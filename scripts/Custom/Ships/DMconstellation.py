##### Created by:
##### Bridge Commander Ship Menu Creator v2.1



import App
import Foundation



abbrev = 'DMconstellation'
iconName = 'DMconstellation'
longName = 'Constellation USS Stargazer'
shipFile = 'DMconstellation'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'


Foundation.ShipDef.DMconstellation = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


# Foundation.ShipDef.DMconstellation.fMaxWarp
# Foundation.ShipDef.DMconstellation.fCruiseWarp
Foundation.ShipDef.DMconstellation.desc = "The USS Stargazer (NCC-2893) was a 24th century Federation Constellation-class starship operated by Starfleet. In 2333, lieutenant Commander Jean-Luc Picard served as a bridge officer on this vessel. He later described the Stargazer as an overworked, underpowered vessel, always on the verge of flying apart at the seams. When the ship's captain was killed and the first officer injured on the bridge, Picard took command of the situation, and the vessel. In 2355, the Stargazer was attacked and severely damaged by an unknown vessel in the Maxia Zeta system. Picard was able to destroy the attacking vessel, using what would later be named the Picard Maneuver. The Stargazer was overcome by fire and severe damage during the battle and had to be abandoned. The event was called the Battle of Maxia by the Ferengi. "


if menuGroup:           Foundation.ShipDef.DMconstellation.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DMconstellation.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
