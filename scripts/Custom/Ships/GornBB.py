import Foundation
import App

menuGroup = 'Gorn Ships'
playerMenuGroup = 'Gorn Ships'

abbrev = 'GornBB'
iconName = 'GornBB'
longName = 'Gorn Battleship'
shipFile = 'GornBB' 
species = App.SPECIES_GALAXY

Foundation.ShipDef.GornBB = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.GornBB.desc = "Gorn Battleship.\n2424m\n\nThis is the largest warship ever constructed by the Gorn, yet has seldom seen active service.  Sight of this behemoth vessel has been more than enough to send most attackers fleeing for cover; while those that have stayed to face her down have soon come to regret the decision.\n\nLike the Gorn themselves, the ship is massive, powerful and resilient. It is capable of taking multiple hits from enemy capital ships, but it lacks speed and maneuverability."

if menuGroup:           Foundation.ShipDef.GornBB.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GornBB.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]