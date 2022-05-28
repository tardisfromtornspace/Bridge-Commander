#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "TENeptune"
iconName = "TENeptune"
longName = "Terran Neptune"
shipFile = "TENeptune"
species = App.SPECIES_GALAXY
menuGroup = "Terran Empire ships"
playerMenuGroup = "Terran Empire ships"
Foundation.ShipDef.TENeptune = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.TENeptune.desc = "Use the four forward phasers and 2 torpedo tubes to soften up the opponents forward shielding because the ships limited sensor range prohibits subsystem targeting until 30 kilometers distance. Watch your flank, there is no aft waepons and your enemy can exploit that weakness. Once your shields go down on any point, the opponent will make quick work of your ships systems and hull so turn that part AWAY from the firing line. To go againt this ship, target the Hull Polarizer and destroy it then go for the impulse engines. The ship will be easier to hit with the Photonic torpedos of the era becasue the ship will be less manuverable"


if menuGroup:           Foundation.ShipDef.TENeptune.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TENeptune.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
