##### Created by:
##### Bridge Commander Ship Menu Creator v3.0



import App
import Foundation



abbrev = 'lintsktinga'
iconName = 'lintsktinga'
longName = 'DS9 K´tinga'
shipFile = 'lintsktinga'
species = App.SPECIES_GALAXY
# SubMenu
menuGroup = 'Klingon Ships'
playerMenuGroup = 'Klingon Ships'


Foundation.ShipDef.lintsktinga = Foundation.KlingonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


# Foundation.ShipDef.lintsktinga.fMaxWarp
# Foundation.ShipDef.lintsktinga.fCruiseWarp
Foundation.ShipDef.lintsktinga.desc = 'For nearly a century, the K´tinga-class cruiser proved to be a rugged, sturdy design that saw continuous use. In that aspect they were much like their Federation counterparts the Excelsior-class and Miranda-class starships, whose usefulness outlived contemporaries such as the Constitution-class cruiser. With marked improvements, these warships saw continuous use as front-line and border patrol ships throughout the Second Klingon-Federation War and the Dominion War of the early-2370s.'


if menuGroup:           Foundation.ShipDef.lintsktinga.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.lintsktinga.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
