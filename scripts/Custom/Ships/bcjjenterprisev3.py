##### Created by:
##### Bridge Commander Ship Menu Creator v5.6



import App
import Foundation



abbrev = 'bcjjenterprisev3'
iconName = 'bcjjprisev3'
longName = 'JJ Enterprise'
shipFile = 'bcjjenterprisev3'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "JJverse"

Foundation.ShipDef.bcjjenterprisev3 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


# Foundation.ShipDef.bcjjenterprisev3.fMaxWarp
# Foundation.ShipDef.bcjjenterprisev3.fCruiseWarp
Foundation.ShipDef.bcjjenterprisev3.desc = 'The USS Enterprise from the new film Star trek XI. Coming from an alternate timeline where the Federation is threatened by a Romulan named Nero. Starfleets research teams stepped up all departments, which explains the differences between this Enterprise and the classic TOS ship.'


if menuGroup:           Foundation.ShipDef.bcjjenterprisev3.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.bcjjenterprisev3.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
